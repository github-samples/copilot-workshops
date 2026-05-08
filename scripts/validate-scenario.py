#!/usr/bin/env python3
"""
validate-scenario.py — Validate a workshop scenario's structure and configuration.

Usage:
    python scripts/validate-scenario.py <scenario-id>
    python scripts/validate-scenario.py --all          # validate every scenario

Exit codes:
    0  All checks passed.
    1  One or more errors found.
"""

import sys
from pathlib import Path
from typing import Any


# Sentinel used by the minimal YAML parser to indicate that a field was
# detected in the file but its value is a block scalar or nested map that
# the parser did not fully deserialise (e.g. `description: >`).
_PRESENT_MARKER = "__present__"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def repo_root() -> Path:
    """Return the repository root (the directory that contains scripts/)."""
    return Path(__file__).resolve().parent.parent


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file, returning a dict. Requires PyYAML."""
    try:
        import yaml  # type: ignore[import]
    except ImportError:
        # Fall back to a minimal parser for simple flat YAML structures
        # so the script works without installing extra dependencies.
        return _minimal_yaml_parse(path)

    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def _minimal_yaml_parse(path: Path) -> dict[str, Any]:
    """
    Minimal YAML parser that handles the subset of YAML used in scenario.yml:
    - Top-level key: value pairs (strings, empty, block scalars)
    - Nested maps at two levels of indentation
    - Lists (inline [] or block - items)
    Comments and blank lines are ignored.
    """
    lines = path.read_text(encoding="utf-8").splitlines()
    return _parse_block(lines, 0, 0)[0]


def _skip_to_next_indent(lines: list[str], start: int, base_indent: int) -> int:
    """Advance past all lines that are more indented than base_indent."""
    i = start
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        indent = len(raw) - len(raw.lstrip())
        if indent <= base_indent:
            break
        i += 1
    return i


def _parse_block(
    lines: list[str], start: int, base_indent: int
) -> "tuple[dict[str, Any], int]":
    """
    Parse a YAML mapping block starting at `start`, where all keys are
    indented exactly `base_indent` spaces.  Returns (mapping_dict, next_line_index).
    """
    result: dict[str, Any] = {}
    i = start

    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()

        # Skip blank lines and comments
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        indent = len(raw) - len(raw.lstrip())

        # If we've de-dented below our base, we're done with this block
        if indent < base_indent:
            break

        # If we're deeper than expected, skip (handled by recursive calls)
        if indent > base_indent:
            i += 1
            continue

        # Expect a mapping key at this indent level
        if ":" not in stripped:
            i += 1
            continue

        key, _, rest = stripped.partition(":")
        key = key.strip()
        rest = rest.strip()

        i += 1  # advance past this key line

        if rest in (">", "|"):
            # Block scalar: consume its content lines and mark as present
            i = _skip_to_next_indent(lines, i, base_indent)
            result[key] = _PRESENT_MARKER
        elif rest == "":
            # Could be a nested map or an empty value; peek ahead
            j = i
            while j < len(lines) and (not lines[j].strip() or lines[j].strip().startswith("#")):
                j += 1

            if j < len(lines):
                next_indent = len(lines[j]) - len(lines[j].lstrip())
                next_stripped = lines[j].strip()

                if next_indent > base_indent:
                    if next_stripped.startswith("- "):
                        items, i = _parse_list(lines, j, next_indent)
                        result[key] = items
                    else:
                        nested, i = _parse_block(lines, j, next_indent)
                        result[key] = nested
                else:
                    result[key] = _PRESENT_MARKER
            else:
                result[key] = _PRESENT_MARKER
        elif rest == "[]":
            result[key] = []
        else:
            result[key] = rest.strip("'\"")

    return result, i


def _parse_list(lines: list[str], start: int, base_indent: int) -> "tuple[list[str], int]":
    """Parse a YAML sequence (list of '- item' lines) at `base_indent`."""
    items: list[str] = []
    i = start

    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()

        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        indent = len(raw) - len(raw.lstrip())

        if indent < base_indent:
            break

        if stripped.startswith("- "):
            item = stripped[2:].strip().strip("'\"")
            # Skip commented-out items
            if not item.startswith("#"):
                items.append(item)

        i += 1

    return items, i


# ---------------------------------------------------------------------------
# Validation checks
# ---------------------------------------------------------------------------

REQUIRED_TOP_LEVEL_FIELDS = ["name", "description", "repository", "tech_stack", "variables", "skip"]
REQUIRED_VARIABLES = [
    "company_name",
    "company_description",
    "product_type",
    "primary_entities",
    "filter_feature",
    "new_endpoints_feature",
    "accessibility_feature",
    "documentation_feature",
]


class Validator:
    def __init__(self, scenario_id: str) -> None:
        self.scenario_id = scenario_id
        self.root = repo_root()
        self.scenario_dir = self.root / "scenarios" / scenario_id
        self.workshop_dir = self.root / "workshop-content"
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    def exercises(self) -> list[str]:
        """Return all exercise filenames (without .md) from workshop-content/."""
        if not self.workshop_dir.exists():
            return []
        return [
            p.stem
            for p in sorted(self.workshop_dir.glob("*.md"))
            if p.name != "README.md"
        ]

    def run(self) -> bool:
        """Run all checks. Return True if no errors were found."""
        self._check_directory_exists()
        if self.errors:
            return False  # Cannot continue without the directory

        config = self._check_scenario_yml()
        if config is not None:
            self._check_required_fields(config)
            self._check_variables(config)
            skip_list = self._check_skip_list(config)
            self._check_overrides(skip_list)
        else:
            # scenario.yml missing — overrides check may still be useful
            self._check_overrides([])

        return len(self.errors) == 0

    def _check_directory_exists(self) -> None:
        if not self.scenario_dir.is_dir():
            self.err(
                f"scenarios/{self.scenario_id}/ does not exist. "
                f"Run: python scripts/new-scenario.py {self.scenario_id}"
            )

    def _check_scenario_yml(self) -> "dict[str, Any] | None":
        yml_path = self.scenario_dir / "scenario.yml"
        if not yml_path.exists():
            self.err(f"scenarios/{self.scenario_id}/scenario.yml is missing.")
            return None
        try:
            config = load_yaml(yml_path)
        except Exception as exc:
            self.err(f"scenarios/{self.scenario_id}/scenario.yml cannot be parsed: {exc}")
            return None
        return config

    def _check_required_fields(self, config: dict[str, Any]) -> None:
        for field in REQUIRED_TOP_LEVEL_FIELDS:
            val = config.get(field)
            if val is None:
                self.err(f"scenario.yml: required field '{field}' is missing or empty.")
            # skip: [] is an empty list — that is valid (means "no exercises skipped")

    def _check_variables(self, config: dict[str, Any]) -> None:
        variables = config.get("variables") or {}
        if not isinstance(variables, dict):
            self.err("scenario.yml: 'variables' must be a mapping.")
            return
        for var in REQUIRED_VARIABLES:
            val = variables.get(var)
            if val is None:
                self.err(f"scenario.yml: variables.{var} is missing.")
            elif isinstance(val, str) and (val.upper().startswith("TODO") or val == _PRESENT_MARKER):
                self.warn(f"scenario.yml: variables.{var} still contains a TODO placeholder.")

        # Check top-level fields for TODOs
        for field in ["name", "description", "repository"]:
            val = config.get(field)
            if isinstance(val, str) and val.upper().startswith("TODO"):
                self.warn(f"scenario.yml: field '{field}' still contains a TODO placeholder.")

    def _check_skip_list(self, config: dict[str, Any]) -> list[str]:
        skip = config.get("skip") or []
        if not isinstance(skip, list):
            self.err("scenario.yml: 'skip' must be a list.")
            return []

        valid_exercises = self.exercises()
        for entry in skip:
            if not isinstance(entry, str):
                self.err(f"scenario.yml: skip entry {entry!r} is not a string.")
            elif entry not in valid_exercises:
                self.err(
                    f"scenario.yml: skip entry '{entry}' does not match any exercise "
                    f"in workshop-content/ (valid: {', '.join(valid_exercises)})."
                )
        return [s for s in skip if isinstance(s, str)]

    def _check_overrides(self, skip_list: list[str]) -> None:
        overrides_dir = self.scenario_dir / "overrides"
        if not overrides_dir.is_dir():
            self.warn(
                f"scenarios/{self.scenario_id}/overrides/ does not exist. "
                "Create it (even empty) to hold exercise overrides."
            )
            return

        valid_exercises = set(self.exercises())
        for override_file in overrides_dir.glob("*.md"):
            if override_file.name == "README.md":
                continue
            stem = override_file.stem
            if stem not in valid_exercises:
                self.err(
                    f"overrides/{override_file.name}: does not correspond to any exercise "
                    f"in workshop-content/."
                )
            elif stem in skip_list:
                self.err(
                    f"overrides/{override_file.name}: exercise '{stem}' is in the skip "
                    "list but also has an override — remove one or the other."
                )


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def validate_one(scenario_id: str) -> bool:
    print(f"Validating scenario: {scenario_id}")
    v = Validator(scenario_id)
    passed = v.run()

    for warning in v.warnings:
        print(f"  ⚠  {warning}")
    for error in v.errors:
        print(f"  ✗  {error}")

    if passed and not v.warnings:
        print(f"  ✓  All checks passed.")
    elif passed:
        print(f"  ✓  No errors (but see warnings above).")
    else:
        print(f"  ✗  {len(v.errors)} error(s) found.")

    print()
    return passed


def main() -> None:
    root = repo_root()
    scenarios_dir = root / "scenarios"

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    arg = sys.argv[1]

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
        all_passed = True
        for sid in scenario_ids:
            if not validate_one(sid):
                all_passed = False
        sys.exit(0 if all_passed else 1)
    else:
        passed = validate_one(arg)
        sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
