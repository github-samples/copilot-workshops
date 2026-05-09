#!/usr/bin/env python3
"""
new-scenario.py — Scaffold a new workshop scenario.

Usage:
    python scripts/new-scenario.py <scenario-id>

Creates the directory structure and starter files for a new scenario under
scenarios/<scenario-id>/. After running this script, follow the instructions
in docs/authoring/new-scenario-guide.md to complete the scenario.
"""

import sys
import os
import re
import textwrap
from pathlib import Path


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def fail(message: str) -> None:
    """Print an error message and exit with a non-zero status."""
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)


def validate_scenario_id(scenario_id: str) -> None:
    """Enforce a simple naming convention: lowercase letters, digits, hyphens."""
    if not re.fullmatch(r"[a-z][a-z0-9-]*", scenario_id):
        fail(
            f"'{scenario_id}' is not a valid scenario ID. "
            "Use only lowercase letters, digits, and hyphens (must start with a letter)."
        )


def repo_root() -> Path:
    """Return the repository root (the directory that contains scripts/)."""
    scripts_dir = Path(__file__).resolve().parent
    return scripts_dir.parent


# ---------------------------------------------------------------------------
# File content templates
# ---------------------------------------------------------------------------

SCENARIO_YML_TEMPLATE = """\
# {scenario_id} — scenario configuration
# Edit every field below before opening a pull request.
# See docs/authoring/new-scenario-guide.md for full documentation.

# Human-readable name displayed in the workshop
name: {display_name}

# Short description of the application used in this scenario
description: >
  TODO: Describe the sample application in one or two sentences.
  What does it do? Who is the fictional company?

# GitHub repository for the sample application (org/repo)
repository: TODO/TODO

# Technology stack — used when generating scenario-specific content
tech_stack:
  frontend:
    name: TODO
    language: TODO
    notes: >
      TODO: Describe the frontend framework and any notes relevant to the exercises.
  backend:
    name: TODO
    language: TODO
    notes: >
      TODO: Describe the backend framework and any notes relevant to the exercises.
  database: TODO

# Content variables — substituted into workshop content and prompts
variables:
  company_name: TODO
  company_description: TODO  # one-line description, e.g. "a crowdfunding platform for board games"
  product_type: TODO          # e.g. "e-commerce store", "blog platform"
  primary_entities: TODO      # e.g. "products, orders, customers"
  filter_feature: TODO        # what learners build in exercise 3
  new_endpoints_feature: TODO # what the coding agent builds in exercise 4
  accessibility_feature: TODO # what the custom agent builds in exercise 5
  documentation_feature: TODO # what is documented in exercise 4's first task

# Exercises to skip for this scenario.
# List exercise filenames (without the .md extension) from workshop-content/
# that are NOT applicable to this scenario.
skip: []
  # Examples:
  # - 3-copilot-agent-mode-vscode  # skip if the app has no frontend
  # - 5-custom-agents              # skip if accessibility task doesn't apply

# Notes for workshop authors or maintainers (not shown to participants)
author_notes: >
  TODO: Add any notes for future maintainers about this scenario.
"""

STEPS_README_TEMPLATE = """\
# {display_name} — Exercise Steps

This directory contains scenario-specific step content for the **{display_name}** scenario.

## How steps work

Place a Markdown file here with the **same filename** as an exercise in `workshop-content/` to inject
scenario-specific sections into that exercise. A steps file contains only the `## ` sections that differ
from the generic core exercise — each matching section replaces the corresponding section in the core
file when exercises are rendered for this scenario.

For example, to customise only the `## Scenario` and `## Running the application` sections of exercise 3:

```markdown
## Scenario

Your application-specific scenario description here.

## Running the application

Your application-specific startup instructions here.
```

Steps files must NOT be created for exercises listed in the `skip` field of `scenario.yml`.

See [docs/authoring/new-scenario-guide.md](../../../docs/authoring/new-scenario-guide.md) for full instructions.

## Files in this directory

*(None yet — add steps files as needed.)*
"""


# ---------------------------------------------------------------------------
# Scaffolding logic
# ---------------------------------------------------------------------------

def scenario_id_to_display_name(scenario_id: str) -> str:
    """Convert 'my-scenario-id' to 'My Scenario Id' as a placeholder name."""
    return " ".join(word.capitalize() for word in scenario_id.split("-"))


def create_scenario(scenario_id: str) -> None:
    root = repo_root()
    scenario_dir = root / "scenarios" / scenario_id
    steps_dir = scenario_dir / "steps"

    # Guard against overwriting an existing scenario
    if scenario_dir.exists():
        fail(
            f"scenarios/{scenario_id}/ already exists. "
            "Remove it first or choose a different scenario ID."
        )

    display_name = scenario_id_to_display_name(scenario_id)

    # Create directories
    steps_dir.mkdir(parents=True)
    print(f"Created: scenarios/{scenario_id}/")
    print(f"Created: scenarios/{scenario_id}/steps/")

    # Write scenario.yml
    yml_content = SCENARIO_YML_TEMPLATE.format(
        scenario_id=scenario_id,
        display_name=display_name,
    )
    (scenario_dir / "scenario.yml").write_text(yml_content, encoding="utf-8")
    print(f"Created: scenarios/{scenario_id}/scenario.yml")

    # Write steps/README.md
    steps_readme = STEPS_README_TEMPLATE.format(display_name=display_name)
    (steps_dir / "README.md").write_text(steps_readme, encoding="utf-8")
    print(f"Created: scenarios/{scenario_id}/steps/README.md")

    # Summary
    print()
    print("Scaffolding complete!")
    print()
    print("Next steps:")
    print(f"  1. Edit scenarios/{scenario_id}/scenario.yml — fill in every TODO field.")
    print(f"  2. Add exercise steps files to scenarios/{scenario_id}/steps/ as needed.")
    print(f"  3. Run: python scripts/validate-scenario.py {scenario_id}")
    print(f"  4. Update the scenario table in scenarios/README.md.")
    print()
    print("Full instructions: docs/authoring/new-scenario-guide.md")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    if len(sys.argv) != 2:
        print(
            textwrap.dedent(
                """\
                Usage:
                    python scripts/new-scenario.py <scenario-id>

                Example:
                    python scripts/new-scenario.py java-bookstore

                The scenario ID must be lowercase letters, digits, and hyphens.
                """
            )
        )
        sys.exit(1)

    scenario_id = sys.argv[1].strip()
    validate_scenario_id(scenario_id)
    create_scenario(scenario_id)


if __name__ == "__main__":
    main()
