#!/usr/bin/env python3
"""
render-scenario.py — Render workshop exercises for a specific scenario.

Usage:
    python scripts/render-scenario.py <scenario-id> [<output-dir>]
    python scripts/render-scenario.py --all [<output-dir>]

For each exercise in workshop-content/, the script:
  1. Reads the core exercise.
  2. If the scenario has a matching steps file in scenarios/<id>/steps/,
     injects its ## sections into the core exercise, replacing any section
     in the core that shares the same heading.
  3. Writes the rendered file to <output-dir>/<scenario-id>/ (default:
     rendered/<scenario-id>/).

The steps file need only contain the sections that differ from the core.
Sections not present in the steps file are kept verbatim from the core.

Exit codes:
    0  All exercises rendered successfully.
    1  One or more errors occurred.
"""

import sys
import textwrap
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def repo_root() -> Path:
    """Return the repository root (the directory containing scripts/)."""
    return Path(__file__).resolve().parent.parent


def parse_sections(content: str) -> "dict[str, str]":
    """
    Split markdown content into level-2 sections keyed by heading text.

    Each value includes the '## heading\\n' line plus all subsequent lines
    up to (but not including) the next level-2 heading.  Content that
    appears before the first '## ' heading is ignored for injection
    purposes (it is preserved verbatim from the core exercise).
    """
    sections: dict[str, str] = {}
    lines = content.splitlines(keepends=True)
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("## "):
            header = line[3:].rstrip("\n").rstrip()
            section_lines: list[str] = [line]
            i += 1
            while i < len(lines) and not lines[i].startswith("## "):
                section_lines.append(lines[i])
                i += 1
            sections[header] = "".join(section_lines)
        else:
            i += 1
    return sections


def inject_sections(core: str, steps: str) -> str:
    """
    Return a copy of *core* where each level-2 section whose heading
    matches a heading in *steps* has been replaced by the steps version.

    Content before the first '## ' heading and any sections not present
    in *steps* are kept exactly as they appear in *core*.
    """
    step_sections = parse_sections(steps)
    if not step_sections:
        return core

    lines = core.splitlines(keepends=True)
    result: list[str] = []
    in_replaced_section = False

    for line in lines:
        if line.startswith("## "):
            header = line[3:].rstrip("\n").rstrip()
            if header in step_sections:
                # Emit the replacement section (includes the ## heading line)
                result.append(step_sections[header])
                in_replaced_section = True
            else:
                in_replaced_section = False
                result.append(line)
        elif not in_replaced_section:
            result.append(line)

    return "".join(result)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_scenario(scenario_id: str, output_dir: Path) -> bool:
    """
    Render all exercises for *scenario_id* into *output_dir*/<scenario_id>/.
    Returns True if everything succeeded.
    """
    root = repo_root()
    workshop_dir = root / "workshop-content"
    steps_dir = root / "scenarios" / scenario_id / "steps"
    scenario_dir = root / "scenarios" / scenario_id
    out_dir = output_dir / scenario_id

    if not scenario_dir.is_dir():
        print(
            f"  ✗  scenarios/{scenario_id}/ does not exist.",
            file=sys.stderr,
        )
        return False

    out_dir.mkdir(parents=True, exist_ok=True)

    exercises = sorted(p for p in workshop_dir.glob("*.md") if p.name != "README.md")
    for ex_path in exercises:
        core = ex_path.read_text(encoding="utf-8")
        steps_path = steps_dir / ex_path.name
        if steps_path.exists():
            steps = steps_path.read_text(encoding="utf-8")
            rendered = inject_sections(core, steps)
            label = "(with scenario steps)"
        else:
            rendered = core
            label = ""
        out_path = out_dir / ex_path.name
        out_path.write_text(rendered, encoding="utf-8")
        print(f"  ✓  {ex_path.name} {label}".rstrip())

    return True


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    root = repo_root()
    scenarios_dir = root / "scenarios"
    default_output = root / "rendered"

    if len(sys.argv) < 2:
        print(
            textwrap.dedent(
                """\
                Usage:
                    python scripts/render-scenario.py <scenario-id> [<output-dir>]
                    python scripts/render-scenario.py --all [<output-dir>]

                Example:
                    python scripts/render-scenario.py tailspin-toys
                    python scripts/render-scenario.py --all rendered/
                """
            )
        )
        sys.exit(1)

    arg = sys.argv[1].strip()
    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else default_output

    if arg == "--all":
        if not scenarios_dir.is_dir():
            print("No scenarios/ directory found.", file=sys.stderr)
            sys.exit(1)
        scenario_ids = [
            d.name
            for d in sorted(scenarios_dir.iterdir())
            if d.is_dir() and not d.name.startswith(".")
        ]
        if not scenario_ids:
            print("No scenarios found in scenarios/.")
            sys.exit(0)
        all_ok = True
        for sid in scenario_ids:
            print(f"Rendering scenario: {sid}")
            if not render_scenario(sid, output_dir):
                all_ok = False
            print()
        sys.exit(0 if all_ok else 1)
    else:
        print(f"Rendering scenario: {arg}")
        ok = render_scenario(arg, output_dir)
        sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
