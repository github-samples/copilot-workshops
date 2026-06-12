#!/usr/bin/env python3
"""Render docs/src/content/docs/ MDX into workshop/ Markdown for GitHub.com.

This script is the single source of truth for the workshop/ folder.
workshop/ is generated output and should never be hand-edited.

Pipeline:
1. Walk docs/src/content/docs/, build slug map: source mdx -> (slug, output rel path).
2. For each non-stub lesson page, render it: strip frontmatter, prepend H1,
   strip imports, inline partials, convert <Aside> -> GitHub admonitions,
   rewrite internal slug-style links to .md paths, copy images.
3. For each stub lesson page (per-path pointer at shared/), inline the
   referenced shared content with link/image resolution rebased to the stub
   location, strip the shared file's "Return to your path" tail, and synthesize
   a Next lesson footer from the stub's [next-lesson] ref.
4. Copy docs/src/content/docs/images/ -> workshop/images/.
5. Validate: every component invocation, partial path, internal link, and
   image reference must resolve. Otherwise exit non-zero.

Usage:
    python scripts/render-markdown.py [--check]

--check exits non-zero if regenerating would change workshop/.
"""

from __future__ import annotations

import argparse
import os
import posixpath
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = REPO_ROOT / "docs" / "src" / "content" / "docs"
OUTPUT_DIR = REPO_ROOT / "workshop"
PARTIALS_DIR = SOURCE_DIR / "_partials"
IMAGES_DIR_NAME = "images"

# Starlight Aside type -> GitHub admonition keyword.
ADMONITION_MAP = {
    "note": "NOTE",
    "tip": "TIP",
    "caution": "WARNING",
    "danger": "CAUTION",
}

# Components the renderer knows how to handle natively (everything else
# must be a partial import or it's a fatal error).
BUILTIN_COMPONENTS = {"Aside"}


class RenderError(Exception):
    """Fatal rendering problem. Surfaces as a non-zero exit."""


# ---------------------------------------------------------------------------
# Slug / URL helpers
# ---------------------------------------------------------------------------


def source_to_slug(rel: Path) -> str:
    """Convert a content-collection-relative .mdx path to its Starlight slug.

    cli/1-install-copilot-cli.mdx -> "cli/1-install-copilot-cli"
    cli/index.mdx                 -> "cli"
    index.mdx                     -> ""
    shared/cloud-agent/cloud-agent.mdx -> "shared/cloud-agent/cloud-agent"
    """
    parts = list(rel.with_suffix("").parts)
    if parts and parts[-1] == "index":
        parts.pop()
    return "/".join(parts)


def source_to_output(rel: Path) -> Path:
    """Convert a content-collection-relative .mdx path to its workshop/ output path.

    cli/index.mdx                 -> cli/README.md
    cli/1-install-copilot-cli.mdx -> cli/1-install-copilot-cli.md
    """
    if rel.name == "index.mdx":
        return rel.with_name("README.md")
    return rel.with_suffix(".md")


def slug_to_url(slug: str) -> str:
    """Slug -> URL with leading and trailing slash. "" -> "/"."""
    if not slug:
        return "/"
    return "/" + slug + "/"


def resolve_link(target: str, page_slug: str) -> tuple[str | None, str, str, str]:
    """Resolve a link's path component relative to page_slug.

    Returns (resolved_slug, fragment, query, original_target_kind).
    resolved_slug is None for external/protocol/anchor-only links.
    original_target_kind is one of: "external", "anchor", "image", "internal".
    """
    if not target:
        return (None, "", "", "external")
    if target.startswith(("http://", "https://", "mailto:", "tel:")):
        return (None, "", "", "external")
    path, _, query_and_frag = target.partition("?")
    if not _:
        path, _, frag = target.partition("#")
        query = ""
    else:
        query, _, frag = query_and_frag.partition("#")
    if not path:
        # bare "#anchor" -> same page
        return (None, frag, query, "anchor")
    base = slug_to_url(page_slug)
    resolved = posixpath.normpath(posixpath.join(base, path))
    if resolved == "/":
        slug = ""
    else:
        slug = resolved.lstrip("/")
    return (slug, frag, query, "internal")


def relative_output_link(from_output: Path, to_output: Path) -> str:
    """Compute a relative POSIX link from one output file to another."""
    rel = os.path.relpath(to_output, from_output.parent).replace(os.sep, "/")
    return rel


# ---------------------------------------------------------------------------
# Frontmatter
# ---------------------------------------------------------------------------


_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return ({}, text)
    body = text[m.end():]
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        val = val.strip()
        # strip surrounding quotes
        if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
            val = val[1:-1]
        fm[key.strip()] = val
    return (fm, body)


# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------


_IMPORT_RE = re.compile(
    # An import statement, optionally preceded by one or more JS line-comment
    # lines (the `// Var: summary` blocks generated by sync_partial_metadata.py).
    r"^import\s+(?:\{[^}]*\}|\w+)\s+from\s+['\"]([^'\"]+)['\"];?\s*$",
    re.MULTILINE,
)
_IMPORT_NAMED_RE = re.compile(
    r"^import\s+\{([^}]*)\}\s+from\s+['\"]([^'\"]+)['\"];?\s*$",
    re.MULTILINE,
)
_IMPORT_DEFAULT_RE = re.compile(
    r"^import\s+(\w+)\s+from\s+['\"]([^'\"]+)['\"];?\s*$",
    re.MULTILINE,
)


def extract_imports(body: str, source_path: Path) -> tuple[dict[str, Path], str]:
    """Extract default-imports of MDX partials, return (component_name -> partial path) map and body with import lines removed."""
    partial_map: dict[str, Path] = {}

    for m in _IMPORT_DEFAULT_RE.finditer(body):
        name = m.group(1).strip()
        rel = m.group(2)
        if not rel.endswith(".mdx"):
            continue  # not a partial; skip
        if rel.startswith("@partials/"):
            partial_path = (PARTIALS_DIR / rel[len("@partials/"):]).resolve()
        else:
            partial_path = (source_path.parent / rel).resolve()
        if not partial_path.exists():
            raise RenderError(
                f"{source_path}: import {name!r} from {rel!r} not found at {partial_path}"
            )
        partial_map[name] = partial_path

    # Strip ALL import lines (named imports of components like { Aside } AND default imports).
    body = _IMPORT_RE.sub("", body)
    return partial_map, body


def strip_mdx_comments(body: str) -> str:
    """Remove MDX comment blocks ({/* ... */}) from the body.

    Handles both single-line and multi-line comments. Skips contents of
    fenced code blocks so that an MDX comment shown as code is preserved.
    Lines that contained ONLY a comment block are removed entirely;
    inline comments leave the surrounding text in place. Final blank-line
    collapsing happens later in _final_cleanup.
    """
    lines = body.split("\n")
    out: list[str] = []
    in_fence = False
    fence_marker: str | None = None
    in_comment = False

    for raw_line in lines:
        stripped = raw_line.lstrip(" ")
        # Track code-fence state (mirrors transform_asides logic).
        if not in_comment and stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_marker = stripped[: len(stripped) - len(stripped.lstrip("`"))]
            elif fence_marker and stripped.startswith(fence_marker):
                in_fence = False
                fence_marker = None
            out.append(raw_line)
            continue

        if in_fence:
            out.append(raw_line)
            continue

        if in_comment:
            # Inside a multi-line comment: drop lines until we find */}
            end = raw_line.find("*/}")
            if end == -1:
                continue
            in_comment = False
            tail = raw_line[end + 3 :]
            # Re-scan the tail for further comments on the same line.
            remainder = tail
            cleaned = ""
            while True:
                start = remainder.find("{/*")
                if start == -1:
                    cleaned += remainder
                    break
                cleaned += remainder[:start]
                rest = remainder[start + 3 :]
                end2 = rest.find("*/}")
                if end2 == -1:
                    in_comment = True
                    break
                remainder = rest[end2 + 3 :]
            if cleaned.strip() or not in_comment:
                if cleaned.strip():
                    out.append(cleaned.rstrip())
            continue

        # Not in a comment: scan the line for {/* ... */} occurrences.
        remainder = raw_line
        cleaned = ""
        while True:
            start = remainder.find("{/*")
            if start == -1:
                cleaned += remainder
                break
            cleaned += remainder[:start]
            rest = remainder[start + 3 :]
            end = rest.find("*/}")
            if end == -1:
                in_comment = True
                break
            remainder = rest[end + 3 :]
        if in_comment:
            # Comment opened mid-line; keep any preceding content, drop the rest.
            if cleaned.strip():
                out.append(cleaned.rstrip())
        elif cleaned == raw_line:
            out.append(raw_line)
        else:
            # Comment fully consumed; emit cleaned text only if it has content,
            # otherwise drop the line entirely (avoid stranded blank lines).
            if cleaned.strip():
                out.append(cleaned.rstrip())

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Aside parsing (stack-based, code-fence-aware)
# ---------------------------------------------------------------------------


_ASIDE_OPEN_RE = re.compile(
    r"<Aside\b([^>]*)>",
)
_ASIDE_CLOSE_RE = re.compile(r"</Aside>")
_ATTR_RE = re.compile(r"""(\w+)=(?:"([^"]*)"|'([^']*)')""")
_FENCE_RE = re.compile(r"^(\s*)```")


def _parse_attrs(attr_text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for m in _ATTR_RE.finditer(attr_text):
        out[m.group(1)] = m.group(2) if m.group(2) is not None else m.group(3)
    return out


def _strip_common_indent(text: str) -> str:
    """Strip the smallest common leading-space indent from non-blank lines.

    Done BEFORE recursing into nested asides so nested results are not
    confused by surrounding indentation.
    """
    lines = text.splitlines()
    indents = [len(line) - len(line.lstrip(" ")) for line in lines if line.strip()]
    common = min(indents) if indents else 0
    if not common:
        return text
    return "\n".join((line[common:] if len(line) >= common else line) for line in lines)


def _wrap_admonition(kind: str, title: str, body_text: str) -> str:
    """Wrap body_text into a GitHub admonition block. Every body line including
    fence delimiters and code lines gets a leading `> `.

    body_text MUST already have common indentation stripped and nested asides
    already converted (so `> [!...]` blocks present here are nested admonitions
    and just need an additional `> ` prefix).
    """
    keyword = ADMONITION_MAP.get(kind)
    if keyword is None:
        raise RenderError(f"Unknown <Aside type=\"{kind}\">; expected one of {sorted(ADMONITION_MAP)}")

    lines = body_text.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    out_lines: list[str] = [f"> [!{keyword}]"]
    if title:
        out_lines.append(f"> **{title}**")
        out_lines.append(">")
    for line in lines:
        if line.strip() == "":
            out_lines.append(">")
        else:
            out_lines.append(f"> {line}")
    return "\n".join(out_lines)


def transform_asides(body: str) -> str:
    """Walk body, finding <Aside ...>...</Aside> blocks (possibly nested),
    converting them to GitHub admonitions. Code fences inside an <Aside> body
    are wrapped along with the rest of the body content.

    Important: outside <Aside> blocks, code fences are skipped (no Aside parsing
    inside code that happens to contain an "<Aside>" string).
    """
    out_chunks: list[str] = []
    i = 0
    in_fence = False
    fence_marker = ""
    n = len(body)

    # Use line-by-line scan to track fences correctly.
    lines = body.split("\n")
    j = 0
    buffer_lines: list[str] = []
    aside_stack: list[tuple[int, dict[str, str]]] = []  # (start_line_index_in_buffer, attrs)

    while j < len(lines):
        line = lines[j]
        # Track code fences only when we are NOT currently inside an aside
        # (asides may legitimately contain code fences as part of the body).
        if not aside_stack:
            stripped = line.lstrip(" ")
            if stripped.startswith("```"):
                if not in_fence:
                    in_fence = True
                    fence_marker = stripped[: len(stripped) - len(stripped.lstrip("`"))]
                else:
                    if stripped.startswith(fence_marker):
                        in_fence = False
                        fence_marker = ""
                buffer_lines.append(line)
                j += 1
                continue
            if in_fence:
                buffer_lines.append(line)
                j += 1
                continue

        # Look for opens / closes on this line. We need to handle the
        # possibility of multiple opens/closes on a single line, though our
        # source only ever puts them on their own lines in practice.
        col = 0
        produced_for_line: list[str] = []
        consumed_to_eol = False
        while col < len(line):
            open_m = _ASIDE_OPEN_RE.search(line, col)
            close_m = _ASIDE_CLOSE_RE.search(line, col)
            if not open_m and not close_m:
                produced_for_line.append(line[col:])
                col = len(line)
                break
            if open_m and (not close_m or open_m.start() < close_m.start()):
                produced_for_line.append(line[col:open_m.start()])
                attrs = _parse_attrs(open_m.group(1))
                aside_stack.append((len(buffer_lines), attrs, produced_for_line.copy()))
                produced_for_line.clear()
                col = open_m.end()
                # If anything remains after the open tag on this same line,
                # treat it as the start of the body.
                continue
            else:
                # close tag
                if not aside_stack:
                    raise RenderError("Unmatched </Aside> tag")
                produced_for_line.append(line[col:close_m.start()])
                # Anything we've accumulated in produced_for_line is the
                # final-line body portion. Combine with buffered body lines.
                start_idx, attrs, _pre = aside_stack.pop()
                # Body lines = buffer_lines[start_idx:] + tail of produced_for_line
                inner_first_line_remainder = "".join(_pre)  # was content BEFORE the open tag, on the open line
                # Actually we need to handle this more carefully. Let's
                # reconstruct: pre-open content stays as a sibling line.
                # But for simplicity in our actual MDX (which puts <Aside>
                # and </Aside> on their own lines), we ignore pre/post
                # content on the same line.
                body_lines = buffer_lines[start_idx:]
                buffer_lines[start_idx:] = []  # consume
                # Trailing content on the closing line BEFORE </Aside>:
                inner_tail = "".join(produced_for_line).rstrip()
                produced_for_line.clear()
                if inner_tail:
                    body_lines.append(inner_tail)
                inner_text = "\n".join(body_lines)
                # Strip common indentation BEFORE recursing — otherwise the
                # nested aside's wrapped output (which has no indent) gets
                # mixed with still-indented surrounding lines and the indent
                # detection in _wrap_admonition would see 0.
                inner_text = _strip_common_indent(inner_text)
                # Recurse for nested asides.
                inner_text = transform_asides(inner_text)
                kind = attrs.get("type", "note")
                title = attrs.get("title", "")
                wrapped = _wrap_admonition(kind, title, inner_text)
                # Pre-open content (if any) on the open-tag line gets emitted
                # BEFORE the wrapped block. Capture the leading indent of the
                # open tag and re-apply it to every line of the wrapped output
                # so it sits at the correct indent within an enclosing aside.
                pre_text = inner_first_line_remainder
                stripped_pre = pre_text.rstrip()
                indent = pre_text[: len(pre_text) - len(pre_text.lstrip(" "))]
                if stripped_pre.strip():
                    buffer_lines.append(stripped_pre)
                if indent:
                    wrapped = "\n".join(indent + line for line in wrapped.split("\n"))
                buffer_lines.append(wrapped)
                col = close_m.end()
                continue

        # End of line processing. produced_for_line has any literal text not
        # inside an aside.
        if not aside_stack:
            buffer_lines.append("".join(produced_for_line))
        else:
            # We're inside an aside: append the literal content as a body line
            buffer_lines.append("".join(produced_for_line))
        j += 1

    if aside_stack:
        raise RenderError("Unclosed <Aside> tag")
    if in_fence:
        raise RenderError("Unclosed code fence")

    return "\n".join(buffer_lines)


# ---------------------------------------------------------------------------
# Component invocation (partial inlining)
# ---------------------------------------------------------------------------


_COMPONENT_RE = re.compile(r"<([A-Z]\w*)\s*/>")


def inline_partials(
    body: str,
    partial_map: dict[str, Path],
    source_path: Path,
    image_set: set[str],
) -> str:
    """Replace each <Component /> with the inlined body of its partial.

    Links and images inside the partial body are LEFT ALONE here — they are
    rewritten in the single top-level pass against the importing page's URL
    context. This matches Starlight's runtime behaviour where the partial's
    relative links are evaluated from the URL of the page that imports it.
    Image refs are canonicalized file-relative inside prepare_body before
    inlining, so they survive intact through partial inlining.
    """

    def replace(m: re.Match[str]) -> str:
        name = m.group(1)
        if name in BUILTIN_COMPONENTS:
            raise RenderError(
                f"{source_path}: encountered <{name} /> which should have been handled earlier"
            )
        if name not in partial_map:
            raise RenderError(
                f"{source_path}: <{name} /> used but no matching import"
            )
        partial_path = partial_map[name]
        partial_text = partial_path.read_text(encoding="utf-8")
        rendered = prepare_body(partial_text, source_path=partial_path, image_set=image_set)
        # Ensure a blank line follows the inlined block so trailing ref-defs
        # (or any other content) stay separated from the consumer's next line.
        return "\n" + rendered.strip("\n") + "\n"

    return _COMPONENT_RE.sub(replace, body)


# ---------------------------------------------------------------------------
# Link / image rewriting
# ---------------------------------------------------------------------------


_INLINE_LINK_RE = re.compile(
    # markdown link: [label](target)  (skip images: leading !)
    r"(?<!\!)\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)"
)
_REF_DEF_RE = re.compile(r"^\[([^\]]+)\]:[ \t]*(\S+)[ \t]*$", re.MULTILINE)
_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
# Sentinel form for an image ref already canonicalized against the source
# tree. Resolved to a real output-relative path in the top-level link pass.
_IMAGE_SENTINEL_PREFIX = "@@workshop-image:"


def canonicalize_images(body: str, source_path: Path, image_set: set[str]) -> str:
    """Rewrite every image target into a sentinel form '@@workshop-image:foo.png'.

    Image targets are FILE-relative (not URL-relative): `../images/x.png` from
    a partial in `_partials/` means `images/x.png` at the content root,
    regardless of which page later imports the partial. We do this resolution
    here, against source_path's directory.
    """
    def _rewrite(m: re.Match[str]) -> str:
        alt, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", _IMAGE_SENTINEL_PREFIX)):
            return m.group(0)
        # Resolve FILE-relative to source_path's parent.
        resolved = (source_path.parent / target).resolve()
        try:
            rel = resolved.relative_to(SOURCE_DIR)
        except ValueError:
            raise RenderError(
                f"{source_path}: image {target!r} resolves outside content root ({resolved})"
            )
        rel_posix = rel.as_posix()
        if not rel_posix.startswith(IMAGES_DIR_NAME + "/"):
            raise RenderError(
                f"{source_path}: image {target!r} resolved to {rel_posix!r}; expected to live under {IMAGES_DIR_NAME}/"
            )
        basename = rel_posix[len(IMAGES_DIR_NAME) + 1 :]
        if basename not in image_set:
            raise RenderError(
                f"{source_path}: image {target!r} -> {basename!r} not present in {IMAGES_DIR_NAME}/"
            )
        return f"![{alt}]({_IMAGE_SENTINEL_PREFIX}{basename})"

    return _IMAGE_RE.sub(_rewrite, body)


def rewrite_links(
    body: str,
    page_slug: str,
    page_output: Path,
    slug_map: dict[str, tuple[Path, Path]],
    source_path: Path,
) -> str:
    """Rewrite inline links, ref definitions, and image sentinels.

    Code-fence-aware: lines inside code fences are passed through untouched.
    """
    out_lines: list[str] = []
    in_fence = False
    fence_marker = ""
    for line in body.split("\n"):
        stripped = line.lstrip(" ")
        if stripped.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_marker = stripped[: len(stripped) - len(stripped.lstrip("`"))]
            else:
                if stripped.startswith(fence_marker):
                    in_fence = False
                    fence_marker = ""
            out_lines.append(line)
            continue
        if in_fence:
            out_lines.append(line)
            continue
        line = _IMAGE_RE.sub(lambda m: _rewrite_image_sentinel(m, page_output, source_path), line)
        line = _INLINE_LINK_RE.sub(lambda m: _rewrite_inline_link(m, page_slug, page_output, slug_map, source_path), line)
        out_lines.append(line)

    text = "\n".join(out_lines)
    text = _REF_DEF_RE.sub(lambda m: _rewrite_ref_def(m, page_slug, page_output, slug_map, source_path), text)
    return text


def _rewrite_inline_link(
    m: re.Match[str],
    page_slug: str,
    page_output: Path,
    slug_map: dict[str, tuple[Path, Path]],
    source_path: Path,
) -> str:
    label, target = m.group(1), m.group(2)
    new_target = _rewrite_url(target, page_slug, page_output, slug_map, source_path)
    return f"[{label}]({new_target})"


def _rewrite_ref_def(
    m: re.Match[str],
    page_slug: str,
    page_output: Path,
    slug_map: dict[str, tuple[Path, Path]],
    source_path: Path,
) -> str:
    label, target = m.group(1), m.group(2)
    new_target = _rewrite_url(target, page_slug, page_output, slug_map, source_path)
    return f"[{label}]: {new_target}"


def _rewrite_url(
    target: str,
    page_slug: str,
    page_output: Path,
    slug_map: dict[str, tuple[Path, Path]],
    source_path: Path,
) -> str:
    resolved_slug, frag, query, kind = resolve_link(target, page_slug)
    if kind in ("external", "anchor"):
        return target  # leave untouched
    if resolved_slug is None:
        return target
    if resolved_slug not in slug_map:
        raise RenderError(
            f"{source_path}: link target {target!r} resolved to slug {resolved_slug!r} but no such page exists"
        )
    _, target_output_rel = slug_map[resolved_slug]
    target_output_abs = OUTPUT_DIR / target_output_rel
    new_target = relative_output_link(page_output, target_output_abs)
    if query:
        new_target += "?" + query
    if frag:
        new_target += "#" + frag
    return new_target


def _rewrite_image_sentinel(
    m: re.Match[str],
    page_output: Path,
    source_path: Path,
) -> str:
    alt, target = m.group(1), m.group(2)
    if not target.startswith(_IMAGE_SENTINEL_PREFIX):
        # Not canonicalized — should never happen because canonicalize_images
        # runs before inlining, and authors only write image refs in source.
        raise RenderError(
            f"{source_path}: image target {target!r} was not canonicalized"
        )
    basename = target[len(_IMAGE_SENTINEL_PREFIX):]
    target_output = OUTPUT_DIR / IMAGES_DIR_NAME / basename
    new_target = relative_output_link(page_output, target_output)
    return f"![{alt}]({new_target})"


# ---------------------------------------------------------------------------
# Body rendering
# ---------------------------------------------------------------------------


def prepare_body(text: str, *, source_path: Path, image_set: set[str]) -> str:
    """Strip frontmatter (if present), remove imports, transform asides,
    canonicalize image refs (file-relative resolution), inline partials.
    Returns markdown with NO link rewriting and image refs in sentinel form.
    The caller does the link/image-output pass in the importing page's URL context.
    """
    _, body = parse_frontmatter(text)
    body = strip_mdx_comments(body)
    partial_map, body = extract_imports(body, source_path)
    body = transform_asides(body)
    body = canonicalize_images(body, source_path, image_set)
    body = inline_partials(body, partial_map, source_path, image_set)
    leftovers = _COMPONENT_RE.findall(body)
    if leftovers:
        raise RenderError(
            f"{source_path}: unresolved components {leftovers!r} after partial inlining"
        )
    return body


def render_body(
    text: str,
    *,
    source_path: Path,
    slug_map: dict[str, tuple[Path, Path]],
    image_set: set[str],
    link_context_slug: str,
    link_context_output: Path,
) -> str:
    """Render an MDX body fragment fully (prepare + link/image rewrite)."""
    body = prepare_body(text, source_path=source_path, image_set=image_set)
    body = rewrite_links(body, link_context_slug, link_context_output, slug_map, source_path)
    return body


# ---------------------------------------------------------------------------
# Stub detection & inlining
# ---------------------------------------------------------------------------


_STUB_ARROW_RE = re.compile(
    r"^➡️\s*\*\*Start the exercise:\*\*\s*\[[^\]]+\]\((\.\./\.\./shared/[^)]+)\)\s*$",
    re.MULTILINE,
)
_RETURN_TO_PATH_RE = re.compile(r"\n---\s*\n+##\s+Return to your path[\s\S]*\Z")


def detect_stub(body: str) -> str | None:
    """If body is a per-path redirect stub, return the relative shared link
    target (still in slug-style with trailing slash). Otherwise return None.
    """
    matches = _STUB_ARROW_RE.findall(body)
    if len(matches) != 1:
        return None
    return matches[0]


def strip_return_to_path(body: str) -> str:
    """Remove the trailing '## Return to your path' section from a shared
    module body."""
    return _RETURN_TO_PATH_RE.sub("", body).rstrip() + "\n"


def render_stub(
    text: str,
    *,
    source_path: Path,
    stub_output: Path,
    stub_slug: str,
    shared_link: str,
    slug_map: dict[str, tuple[Path, Path]],
    image_set: set[str],
) -> str:
    """Render a per-path stub by inlining the referenced shared content."""
    fm, body = parse_frontmatter(text)
    title = fm.get("title", "").strip()
    if not title:
        raise RenderError(f"{source_path}: stub missing frontmatter title")

    # Resolve the shared link to a source path.
    shared_slug, _, _, _ = resolve_link(shared_link, stub_slug)
    if shared_slug is None or shared_slug not in slug_map:
        raise RenderError(
            f"{source_path}: stub points at shared module {shared_link!r} which doesn't resolve"
        )
    shared_source, _ = slug_map[shared_slug]
    shared_text = shared_source.read_text(encoding="utf-8")
    shared_fm, shared_body = parse_frontmatter(shared_text)

    # Render the shared body in the STUB's link context (so internal links
    # resolve as if read from the stub's URL).
    rendered_shared = render_body(
        shared_body,
        source_path=shared_source,
        slug_map=slug_map,
        image_set=image_set,
        link_context_slug=stub_slug,
        link_context_output=stub_output,
    )
    rendered_shared = strip_return_to_path(rendered_shared)

    # Render the stub's intro (everything before the ➡️ line and the
    # "When you finish" line). We also strip the top "previous lesson" table
    # and re-emit it as part of the synthesized nav block at the bottom.
    intro_paragraph = _extract_stub_intro(body)
    intro_paragraph = render_body(
        intro_paragraph,
        source_path=source_path,
        slug_map=slug_map,
        image_set=image_set,
        link_context_slug=stub_slug,
        link_context_output=stub_output,
    ).strip()

    # Synthesize nav from refs.
    nav_top, nav_bottom = _stub_nav(body, stub_slug, stub_output, slug_map, source_path)

    parts = [f"# {title}", ""]
    if nav_top:
        parts.extend([nav_top, ""])
    if intro_paragraph:
        parts.extend([intro_paragraph, ""])
    parts.extend([rendered_shared.rstrip(), ""])
    if nav_bottom:
        parts.extend(["---", "", nav_bottom, ""])
    return "\n".join(parts).rstrip() + "\n"


def _extract_stub_intro(body: str) -> str:
    """Pull the 'You're in the X path...' paragraph out of a stub body, ignoring
    the top previous-lesson table, the ➡️ line, the 'When you finish' line, and
    the trailing ref definitions. Collapses runs of blank lines.
    """
    lines = body.splitlines()
    out: list[str] = []
    for line in lines:
        s = line.strip()
        if s.startswith("|"):  # nav table
            continue
        if s.startswith("➡️"):
            continue
        if s.startswith("When you finish"):
            continue
        if s.startswith("[next-lesson]:") or s.startswith("[previous-lesson]:"):
            continue
        out.append(line)
    text = "\n".join(out).strip()
    # Collapse 2+ consecutive blank lines down to one.
    return re.sub(r"\n{3,}", "\n\n", text)


def _stub_nav(
    body: str,
    stub_slug: str,
    stub_output: Path,
    slug_map: dict[str, tuple[Path, Path]],
    source_path: Path,
) -> tuple[str, str]:
    """Build top (Previous) and bottom (Previous + Next) nav blocks from
    the stub's [previous-lesson] / [next-lesson] refs."""
    refs: dict[str, str] = {}
    for m in _REF_DEF_RE.finditer(body):
        refs[m.group(1)] = m.group(2)
    prev = refs.get("previous-lesson")
    nxt = refs.get("next-lesson")

    def link(target: str) -> tuple[str, str]:
        resolved_slug, frag, query, kind = resolve_link(target, stub_slug)
        if resolved_slug is None or resolved_slug not in slug_map:
            raise RenderError(
                f"{source_path}: nav ref {target!r} doesn't resolve to a known page"
            )
        target_source, target_output_rel = slug_map[resolved_slug]
        target_output_abs = OUTPUT_DIR / target_output_rel
        # Title from frontmatter
        target_text = target_source.read_text(encoding="utf-8")
        target_fm, _ = parse_frontmatter(target_text)
        title = target_fm.get("title", resolved_slug)
        return (title, relative_output_link(stub_output, target_output_abs))

    top_lines: list[str] = []
    bottom_lines: list[str] = []
    if prev:
        prev_title, prev_url = link(prev)
        top_lines.append(f"⬅️ **Previous lesson:** [{prev_title}]({prev_url})")
        bottom_lines.append(f"⬅️ **Previous lesson:** [{prev_title}]({prev_url})")
    if nxt:
        nxt_title, nxt_url = link(nxt)
        bottom_lines.append(f"➡️ **Next lesson:** [{nxt_title}]({nxt_url})")
    return ("\n".join(top_lines), "\n".join(bottom_lines))


# ---------------------------------------------------------------------------
# Page rendering
# ---------------------------------------------------------------------------


GENERATED_BANNER = (
    "<!--\n"
    "  GENERATED FILE — do not edit.\n"
    "  Source: docs/src/content/docs/{src_rel}\n"
    "  Run `python scripts/render-markdown.py` to regenerate.\n"
    "-->\n\n"
)


def _final_cleanup(text: str) -> str:
    """Collapse runs of 3+ blank lines down to 2. Trim trailing whitespace per line."""
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def render_page(
    source_path: Path,
    output_path: Path,
    slug: str,
    slug_map: dict[str, tuple[Path, Path]],
    image_set: set[str],
) -> str:
    text = source_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    title = fm.get("title", "").strip()
    if not title:
        raise RenderError(f"{source_path}: missing frontmatter title")

    src_rel = source_path.relative_to(SOURCE_DIR).as_posix()

    # Detect stub.
    shared_link = detect_stub(body)
    if shared_link is not None:
        rendered = render_stub(
            text,
            source_path=source_path,
            stub_output=output_path,
            stub_slug=slug,
            shared_link=shared_link,
            slug_map=slug_map,
            image_set=image_set,
        )
    else:
        rendered_body = render_body(
            body,
            source_path=source_path,
            slug_map=slug_map,
            image_set=image_set,
            link_context_slug=slug,
            link_context_output=output_path,
        )
        rendered = f"# {title}\n\n{rendered_body.strip()}\n"

    return GENERATED_BANNER.format(src_rel=src_rel) + _final_cleanup(rendered).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def discover_pages() -> list[tuple[Path, Path, str]]:
    """Return a sorted list of (source_path, output_rel, slug) for every
    non-partial MDX page."""
    items: list[tuple[Path, Path, str]] = []
    for source in sorted(SOURCE_DIR.rglob("*.mdx")):
        rel = source.relative_to(SOURCE_DIR)
        if rel.parts[0] == "_partials":
            continue
        slug = source_to_slug(rel)
        output_rel = source_to_output(rel)
        items.append((source, output_rel, slug))
    return items


def discover_images() -> set[str]:
    images_dir = SOURCE_DIR / IMAGES_DIR_NAME
    if not images_dir.is_dir():
        return set()
    return {
        p.relative_to(images_dir).as_posix()
        for p in images_dir.rglob("*")
        if p.is_file()
    }


def render_all() -> None:
    if not SOURCE_DIR.is_dir():
        raise RenderError(f"Source directory not found: {SOURCE_DIR}")

    # Clean output.
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    pages = discover_pages()
    image_set = discover_images()

    slug_map: dict[str, tuple[Path, Path]] = {
        slug: (source, output_rel) for source, output_rel, slug in pages
    }

    for source, output_rel, slug in pages:
        rendered = render_page(source, OUTPUT_DIR / output_rel, slug, slug_map, image_set)
        out_path = OUTPUT_DIR / output_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered, encoding="utf-8")

    # Copy images.
    src_images = SOURCE_DIR / IMAGES_DIR_NAME
    if src_images.is_dir():
        dst_images = OUTPUT_DIR / IMAGES_DIR_NAME
        shutil.copytree(src_images, dst_images)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true",
                        help="Render and exit non-zero if workshop/ would change.")
    args = parser.parse_args()

    try:
        render_all()
    except RenderError as e:
        print(f"render-markdown: error: {e}", file=sys.stderr)
        return 2

    if args.check:
        result = subprocess.run(
            ["git", "status", "--porcelain", "--", "workshop"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if result.stdout.strip():
            print("render-markdown: workshop/ is out of date. Diff:", file=sys.stderr)
            sys.stderr.write(result.stdout)
            diff = subprocess.run(
                ["git", "--no-pager", "diff", "--", "workshop"],
                cwd=REPO_ROOT,
                capture_output=True,
                text=True,
            )
            sys.stderr.write(diff.stdout)
            return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
