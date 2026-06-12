"""Shared parsing helpers for partials lint + sync scripts.

A "partial" is an MDX file under docs/src/content/docs/_partials/. Every
partial begins with a metadata block:

    {/*
    @summary One-sentence description.
    @sections
      - H2 First heading
      - H2 Second heading
    */}

This module locates and parses that block, plus extracts the partial's
actual headings and consumer-page imports. See
.github/instructions/partials.instructions.md for the format.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs" / "src" / "content" / "docs"
PARTIALS_DIR = DOCS_DIR / "_partials"
TYPES_DIR = REPO_ROOT / "docs" / "src" / "types" / "_partials"
PARTIAL_ALIAS = "@partials/"

SUMMARY_MAX_LEN = 200

_METADATA_RE = re.compile(r"\A\s*\{/\*(.*?)\*/\}", re.DOTALL)
_SECTION_LINE_RE = re.compile(r"^\s*-\s+(H[1-6])\s+(.+?)\s*$")
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_FENCE_RE = re.compile(r"^(\s*)```")
_IMPORT_DEFAULT_RE = re.compile(
    r"^([ \t]*)import\s+(\w+)\s+from\s+['\"]([^'\"]+)['\"];?\s*$",
    re.MULTILINE,
)


@dataclass
class PartialMetadata:
    path: Path
    summary: str
    sections: list[str]  # entries like "H2 Custom instructions"
    block_text: str  # raw text of the comment block (incl. {/* */})
    block_end: int  # offset just after the closing */} in the file text


@dataclass
class ImportRef:
    """A single `import Var from '../_partials/foo.mdx';` line in a consumer."""

    var: str
    partial_path: Path  # resolved absolute path to the partial
    line_start: int  # offset of the start of the import line
    line_end: int  # offset just after the trailing newline of the import line
    indent: str


def list_partials() -> list[Path]:
    return sorted(p for p in PARTIALS_DIR.glob("*.mdx"))


def list_consumer_pages() -> list[Path]:
    """All MDX pages under docs/src/content/docs/ EXCEPT files in _partials/."""
    out: list[Path] = []
    for p in DOCS_DIR.rglob("*.mdx"):
        if PARTIALS_DIR in p.parents:
            continue
        out.append(p)
    return sorted(out)


def parse_metadata(partial_path: Path) -> PartialMetadata | None:
    """Parse the leading metadata block. Returns None if missing/malformed
    enough that we can't produce a PartialMetadata. Lint will raise its own
    errors on top of this."""
    text = partial_path.read_text(encoding="utf-8")
    m = _METADATA_RE.match(text)
    if not m:
        return None
    inner = m.group(1)
    summary = _extract_summary(inner)
    sections = _extract_sections(inner)
    return PartialMetadata(
        path=partial_path,
        summary=summary,
        sections=sections,
        block_text=text[: m.end()],
        block_end=m.end(),
    )


def _extract_summary(inner: str) -> str:
    """@summary spans from its own line until the next @key or end-of-block."""
    lines = inner.splitlines()
    collecting = False
    parts: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("@summary"):
            collecting = True
            tail = stripped[len("@summary") :].strip()
            if tail:
                parts.append(tail)
            continue
        if collecting and stripped.startswith("@"):
            break
        if collecting:
            if stripped:
                parts.append(stripped)
    return " ".join(parts).strip()


def _extract_sections(inner: str) -> list[str]:
    lines = inner.splitlines()
    out: list[str] = []
    collecting = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("@sections"):
            collecting = True
            continue
        if collecting and stripped.startswith("@"):
            break
        if not collecting:
            continue
        if not stripped:
            continue
        m = _SECTION_LINE_RE.match(line)
        if m:
            out.append(f"{m.group(1)} {m.group(2)}")
    return out


def extract_body_headings(partial_path: Path) -> list[str]:
    """Return list of "H<n> <text>" for every Markdown heading in the
    partial body (excluding inside fenced code blocks). The metadata block
    is not part of the body."""
    text = partial_path.read_text(encoding="utf-8")
    md = _METADATA_RE.match(text)
    body = text[md.end() :] if md else text
    out: list[str] = []
    in_fence = False
    fence_marker: str | None = None
    for line in body.splitlines():
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
        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            text_part = m.group(2).strip()
            out.append(f"H{level} {text_part}")
    return out


def find_partial_imports(consumer_path: Path) -> list[ImportRef]:
    """Find every `import X from '@partials/foo.mdx';` line (alias) and,
    for backward compatibility during migration, `'../_partials/foo.mdx'`
    (relative)."""
    text = consumer_path.read_text(encoding="utf-8")
    refs: list[ImportRef] = []
    for m in _IMPORT_DEFAULT_RE.finditer(text):
        rel = m.group(3)
        if not rel.endswith(".mdx"):
            continue
        target = _resolve_partial_specifier(rel, consumer_path)
        if target is None:
            continue
        try:
            target.relative_to(PARTIALS_DIR)
        except ValueError:
            continue
        if not target.exists():
            continue
        end = m.end()
        if end < len(text) and text[end] == "\n":
            end += 1
        refs.append(
            ImportRef(
                var=m.group(2),
                partial_path=target,
                line_start=m.start(),
                line_end=end,
                indent=m.group(1),
            )
        )
    return refs


def _resolve_partial_specifier(specifier: str, consumer_path: Path) -> Path | None:
    """Resolve either an alias (`@partials/foo.mdx`) or a relative
    (`../_partials/foo.mdx`) import specifier to an absolute partial path."""
    if specifier.startswith(PARTIAL_ALIAS):
        rest = specifier[len(PARTIAL_ALIAS):]
        return (PARTIALS_DIR / rest).resolve()
    return (consumer_path.parent / specifier).resolve()


def build_metadata_block(summary: str, sections: list[str]) -> str:
    """Render a canonical metadata block."""
    lines = ["{/*", f"@summary {summary}", "@sections"]
    for s in sections:
        lines.append(f"  - {s}")
    lines.append("*/}")
    return "\n".join(lines) + "\n"


def render_dts(meta: PartialMetadata) -> str:
    """Render a sibling `<name>.mdx.d.ts` file. TypeScript uses this
    declaration file as the type for the actual `<name>.mdx` next to it,
    overriding Astro's generic ambient `*.mdx` declaration. JSDoc on the
    default export surfaces as a hover tooltip at every `<Component />`
    use site (with the unifiedjs.vscode-mdx extension and/or the MDX TS
    plugin) and on the imported identifier."""
    out: list[str] = [
        "// GENERATED FILE — do not edit. Regenerate with:",
        "//   python scripts/sync_partial_metadata.py",
        "/**",
    ]
    for line in _wrap_for_jsdoc(meta.summary, width=72):
        out.append(f" * {line}".rstrip())
    if meta.sections:
        out.append(" *")
        out.append(" * **Sections:**")
        for section in meta.sections:
            out.append(f" * - {section}")
    out.append(" */")
    out.append(
        "declare const Component: import('astro').MDXInstance<Record<string, never>>['default'];"
    )
    out.append("export default Component;")
    out.append("")
    return "\n".join(out)


def _wrap_for_jsdoc(text: str, width: int) -> list[str]:
    if not text:
        return [""]
    words = text.split()
    out: list[list[str]] = [[]]
    cur = 0
    for w in words:
        add = (1 if out[-1] else 0) + len(w)
        if out[-1] and cur + add > width:
            out.append([w])
            cur = len(w)
        else:
            out[-1].append(w)
            cur += add
    return [" ".join(parts) for parts in out]


def filename_to_var(partial_path: Path) -> str:
    """Derive a default PascalCase identifier from the partial filename.
    `section-instructions-overview.mdx` -> `SectionInstructionsOverview`.
    Used when no consumer page imports the partial yet."""
    stem = partial_path.stem
    return "".join(part.capitalize() for part in re.split(r"[-_]", stem) if part)


PARTIAL_PREFIXES = ("section", "exercise", "callout")


def partial_prefix(partial_path: Path) -> str | None:
    """Return the leading filename prefix (`section`/`exercise`/`callout`)
    for a partial, or None if the filename doesn't follow the convention."""
    stem = partial_path.stem
    for p in PARTIAL_PREFIXES:
        if stem == p or stem.startswith(f"{p}-"):
            return p
    return None
