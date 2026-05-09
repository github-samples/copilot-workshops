# Scenarios

This directory contains **scenario packs** — self-contained bundles of configuration and content that let authors swap the sample application used in the "Agents in the SDLC" workshop without rewriting the core exercises.

## What is a scenario?

A scenario is a specific sample application (e.g. Tailspin Toys, a Java e-commerce store, a Node.js blog platform) that learners interact with as they work through the workshop exercises. The exercises themselves teach the same Copilot concepts regardless of the scenario; the scenario just provides the concrete codebase and context.

## Directory structure

```
scenarios/
  <scenario-id>/
    scenario.yml          # Required: metadata, variables, skip list
    steps/                # Optional: scenario-specific exercise sections
      <exercise>.md       # Injects sections into the named core exercise
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

### `steps/` — optional

The core exercises in `workshop-content/` are generic templates. When your scenario needs to inject application-specific content (company name, tech-stack details, feature descriptions), create a steps file in `steps/` with the same filename as the exercise. A steps file contains only the `## ` sections that differ from the core — each matching section replaces its counterpart in the core exercise when exercises are rendered for this scenario.

See [docs/authoring/new-scenario-guide.md](../docs/authoring/new-scenario-guide.md) for step-by-step instructions.

## Available scenarios

| Scenario ID | Application | Tech stack | Status |
|---|---|---|---|
| `tailspin-toys` | Tailspin Toys (crowdfunding for board games) | Python/Flask · Astro/Svelte | ✅ Default |
| `tailspin-toys-dotnet` | Tailspin Toys .NET (crowdfunding for board games) | ASP.NET Core · Astro/Svelte | ✅ Available |

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
