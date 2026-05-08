# Scenarios

This directory contains **scenario packs** — self-contained bundles of configuration and content that let authors swap the sample application used in the "Agents in the SDLC" workshop without rewriting the core exercises.

## What is a scenario?

A scenario is a specific sample application (e.g. Tailspin Toys, a Java e-commerce store, a Node.js blog platform) that learners interact with as they work through the workshop exercises. The exercises themselves teach the same Copilot concepts regardless of the scenario; the scenario just provides the concrete codebase and context.

## Directory structure

```
scenarios/
  <scenario-id>/
    scenario.yml          # Required: metadata, variables, skip list
    overrides/            # Optional: exercise content overrides
      <exercise>.md       # Replaces or supplements the named exercise
    README.md             # Optional: notes for maintainers
```

### `scenario.yml` — required fields

| Field | Type | Description |
|---|---|---|
| `name` | string | Human-readable scenario name |
| `description` | string | Short description of the sample app |
| `repository` | string | GitHub repo in `org/repo` format |
| `tech_stack` | map | Frontend, backend, and database details |
| `variables` | map | Content variables (company name, features, etc.) |
| `skip` | list | Exercise filenames (without `.md`) to omit from this scenario |

### `overrides/` — optional

When the core workshop exercises contain scenario-specific wording (company name, feature descriptions, etc.) that does not match your application, create a replacement Markdown file in `overrides/` with the same filename as the exercise. The replacement file should contain a `## Scenario` section that describes what learners are building in the context of your application, plus any other section-level rewrites needed.

See [docs/authoring/new-scenario-guide.md](../docs/authoring/new-scenario-guide.md) for step-by-step instructions.

## Available scenarios

| Scenario ID | Application | Tech stack | Status |
|---|---|---|---|
| `tailspin-toys` | Tailspin Toys (crowdfunding for board games) | Python/Flask · Astro/Svelte | ✅ Default |

## Adding a new scenario

Use the scaffolding script to get started:

```bash
python scripts/new-scenario.py <scenario-id>
```

This creates the directory structure, a pre-filled `scenario.yml`, and placeholder override files. See the [authoring guide](../docs/authoring/new-scenario-guide.md) for full instructions.

## Validating a scenario

Before submitting a new scenario, run the validation script to catch common issues:

```bash
python scripts/validate-scenario.py <scenario-id>
```
