#!/usr/bin/env python3
"""Validate the @summary/@sections metadata block in every partial,
the corresponding `.mdx.d.ts` declaration, and consumer-page imports.

Checks (per partial):
1. The leading {/* ... */} metadata block exists.
2. Both @summary and @sections are present (sections may be empty if
   the partial introduces no headings).
3. @summary is a single line ≤ 200 chars (after joining).
4. Each @sections entry matches `H<n> <text>`.
5. The @sections list matches the actual ##/### headings in the body
   exactly (same entries, same order).
6. The corresponding `docs/src/types/_shared/<name>.mdx.d.ts` exists
   and is up to date with the metadata (run sync to refresh it).
7. The partial body contains no `^## ` (H2) headings — the host page
   owns every H2; partials use H3 and below only.

Checks (across consumers):
8. Every partial import uses the `@shared/` alias rather than a
   relative `../_shared/` path or a legacy `@partials/` alias.
9. The local binding for a partial import starts with the PascalCase
   form of the filename prefix (`Section`, `Exercise`, `Callout`).

Exit code is non-zero on any failure. Each error prints `path:line: message`.

Usage:
    python scripts/lint_partials.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from _partials_lib import (
    PARTIAL_ALIAS,
    PARTIALS_DIR,
    REPO_ROOT,
    SUMMARY_MAX_LEN,
    TYPES_DIR,
    extract_body_headings,
    find_partial_imports,
    list_consumer_pages,
    list_partials,
    parse_metadata,
    partial_prefix,
    render_dts,
)

_RELATIVE_PARTIAL_IMPORT = re.compile(
    r"""^[ \t]*import\s+\w+\s+from\s+['"](?:\.\./)+_shared/[^'"]+\.mdx['"];?\s*$""",
    re.MULTILINE,
)

_LEGACY_ALIAS_IMPORT = re.compile(
    r"""^[ \t]*import\s+\w+\s+from\s+['"]@partials/[^'"]+\.mdx['"];?\s*$""",
    re.MULTILINE,
)

_FENCE_RE = re.compile(r"^(\s*)```")
_H2_RE = re.compile(r"^##\s")


def _line_of(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def lint() -> int:
    errors: list[str] = []

    for partial in list_partials():
        meta = parse_metadata(partial)
        rel = partial.relative_to(REPO_ROOT)
        if meta is None:
            errors.append(
                f"{rel}:1: missing metadata block. Add a {{/* ... */}} block at the top with @summary and @sections."
            )
            continue
        if not meta.summary:
            errors.append(f"{rel}:1: @summary is empty.")
        if "\n" in meta.summary:
            errors.append(f"{rel}:1: @summary must be a single line.")
        if len(meta.summary) > SUMMARY_MAX_LEN:
            errors.append(
                f"{rel}:1: @summary is {len(meta.summary)} chars (max {SUMMARY_MAX_LEN})."
            )
        actual = extract_body_headings(partial)
        if not meta.sections and actual:
            errors.append(
                f"{rel}:1: @sections is empty but the body has headings. List every ### or deeper heading."
            )
        if meta.sections != actual:
            errors.append(
                f"{rel}:1: @sections does not match body headings.\n"
                f"  declared: {meta.sections}\n"
                f"  actual:   {actual}"
            )

        # Reject H2 headings inside the partial body — host page owns H2.
        text = partial.read_text(encoding="utf-8")
        body_offset = meta.block_end
        body = text[body_offset:]
        in_fence = False
        fence_marker: str | None = None
        for i, line in enumerate(body.splitlines(), start=1):
            stripped_left = line.lstrip(" ")
            if stripped_left.startswith("```"):
                if not in_fence:
                    in_fence = True
                    fence_marker = stripped_left[
                        : len(stripped_left) - len(stripped_left.lstrip("`"))
                    ]
                elif fence_marker and stripped_left.startswith(fence_marker):
                    in_fence = False
                    fence_marker = None
                continue
            if in_fence:
                continue
            if _H2_RE.match(line):
                # Compute absolute line number in the file.
                abs_line = text.count("\n", 0, body_offset) + i
                errors.append(
                    f"{rel}:{abs_line}: H2 not allowed in partials — host page owns the H2; use H3 or below inside the partial."
                )

        dts_path = TYPES_DIR / f"{partial.name}.d.ts"
        rel_dts = dts_path.relative_to(REPO_ROOT) if dts_path.exists() else dts_path
        expected = render_dts(meta)
        if not dts_path.exists():
            errors.append(
                f"{dts_path.relative_to(REPO_ROOT)}:1: missing declaration file. "
                f"Run `python scripts/sync_partial_metadata.py` to create it."
            )
        elif dts_path.read_text(encoding="utf-8") != expected:
            errors.append(
                f"{rel_dts}:1: stale declaration file. "
                f"Run `python scripts/sync_partial_metadata.py` to refresh it."
            )

    # Cross-page check: every partial import must use the @partials/ alias,
    # and the local binding must start with the PascalCase form of the
    # partial filename's prefix (Section/Exercise/Callout).
    for consumer in list_consumer_pages():
        text = consumer.read_text(encoding="utf-8")
        rel = consumer.relative_to(REPO_ROOT)
        for m in _RELATIVE_PARTIAL_IMPORT.finditer(text):
            line = _line_of(text, m.start())
            errors.append(
                f"{rel}:{line}: partial import uses a relative path; "
                f"use the `{PARTIAL_ALIAS}` alias instead. "
                f"Run `python scripts/sync_partial_metadata.py` to migrate."
            )
        for m in _LEGACY_ALIAS_IMPORT.finditer(text):
            line = _line_of(text, m.start())
            errors.append(
                f"{rel}:{line}: partial import uses the legacy `@partials/` alias; "
                f"rewrite to `{PARTIAL_ALIAS}`."
            )
        for ref in find_partial_imports(consumer):
            prefix = partial_prefix(ref.partial_path)
            if prefix is None:
                continue
            expected = prefix.capitalize()
            if not ref.var.startswith(expected):
                line = _line_of(text, ref.line_start)
                errors.append(
                    f"{rel}:{line}: import of {ref.partial_path.name} must be bound to a name starting with "
                    f'"{expected}" (got "{ref.var}").'
                )

    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        print(f"\n{len(errors)} partial-lint error(s).", file=sys.stderr)
        return 1
    print(
        f"OK: {len(list_partials())} partial(s), "
        f"{len(list_consumer_pages())} consumer page(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(lint())
