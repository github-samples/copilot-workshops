# Authoring Guide — Adding a New Workshop Scenario

This guide walks you through every step needed to introduce a new sample application into the "Agents in the SDLC" workshop. After following it, learners will be able to use your application as the concrete codebase they work with while exploring GitHub Copilot's agent capabilities.

## Prerequisites

- Python 3.9 or later (for the scaffolding and validation scripts).
- A sample application repository accessible on GitHub. If you don't have one yet, see [Using the AI prompt to create a sample app](#using-the-ai-prompt-to-create-a-sample-app).
- Familiarity with the workshop structure — skim through `workshop-content/README.md` and a couple of the exercise files before you begin.

---

## Step 1 — Understand what makes a good workshop scenario

A scenario application should:

- **Be small enough to navigate quickly.** Learners spend time in the codebase during exercises; a sprawling monorepo is hard to work with in a short workshop.
- **Have clear separation between frontend and backend** (even if it's a single-language stack). Exercises like 3 and 4 assume there is both a UI and an API to update.
- **Have a test suite** that Copilot can run and iterate against.
- **Tell a story.** Learners take on the role of a developer at a fictional company. Choose a company concept that is interesting and lends itself to obvious feature work.
- **Be deployable in a GitHub Codespace.** The `.devcontainer/` configuration in the main repo drives the learner environment.

Exercises you may want to **skip** for a particular scenario:

| Exercise | Common reason to skip |
|---|---|
| `3-copilot-agent-mode-vscode` | App has no frontend, or frontend is purely static |
| `5-custom-agents` | Scenario doesn't include an accessibility use case |

Skipped exercises are listed in `scenario.yml` and are omitted when the workshop is rendered for that scenario.

---

## Step 2 — Create the scaffolding

Run the scaffolding script from the repository root:

```bash
python scripts/new-scenario.py <scenario-id>
```

Replace `<scenario-id>` with a short, lowercase, hyphenated identifier (e.g. `java-bookstore`, `node-blog`).

The script creates:

```
scenarios/
  <scenario-id>/
    scenario.yml          ← pre-filled template; edit this next
    overrides/
      README.md           ← placeholder for exercise overrides
```

---

## Step 3 — Fill in `scenario.yml`

Open `scenarios/<scenario-id>/scenario.yml` and complete every field:

```yaml
name: <Human-readable name>
description: >
  One or two sentences describing the application.

repository: <org>/<repo>        # GitHub repo for your sample app

tech_stack:
  frontend:
    name: <Framework name>
    language: <Language>
    notes: >
      Any notes relevant to the exercises.
  backend:
    name: <Framework name>
    language: <Language>
    notes: >
      Any notes relevant to the exercises.
  database: <Database>

variables:
  company_name: <Company name>
  company_description: <one-line description>
  product_type: <e.g. e-commerce store, blog platform>
  primary_entities: <e.g. products, orders, customers>
  filter_feature: <what learners build in exercise 3>
  new_endpoints_feature: <what the coding agent builds in exercise 4>
  accessibility_feature: <what the custom agent builds in exercise 5>
  documentation_feature: <what is documented in exercise 4's first task>

skip:
  # List exercise filenames (without .md) that do NOT apply to your scenario
  # - 5-custom-agents
```

### Required variables

| Variable | Used in | Example |
|---|---|---|
| `company_name` | All exercises | `Tailspin Toys` |
| `company_description` | README, exercise intros | `a crowdfunding platform for board games` |
| `product_type` | README scenario section | `crowdfunding platform` |
| `primary_entities` | Exercises 3 & 4 | `games, publishers, categories` |
| `filter_feature` | Exercise 3 | `filter games by category and publisher` |
| `new_endpoints_feature` | Exercise 4 | `endpoints to create, update, and delete games` |
| `accessibility_feature` | Exercise 5 | `high-contrast mode toggle` |
| `documentation_feature` | Exercise 4 | `docstrings for all functions` |

---

## Step 4 — Identify which exercises to skip

Work through `workshop-content/` one exercise at a time and ask: *"Can a learner complete this exercise with my application?"*

Common mismatches:

- **Exercise 3** asks learners to add a filter feature that spans frontend and backend. If your app has no frontend, skip it.
- **Exercise 5** builds an accessibility agent for a dark-themed UI. If your app uses a different colour scheme or has no significant CSS layer, you may want to skip it or provide an alternative task in an override.

Add each exercise to be skipped to the `skip` list in `scenario.yml`.

---

## Step 5 — Write exercise overrides (as needed)

Each exercise in `workshop-content/` contains a `## Scenario` section that describes the task in the context of Tailspin Toys. You will need to override this section for any exercise where the Tailspin-specific context does not make sense for your application.

Create the override file at:

```
scenarios/<scenario-id>/overrides/<exercise-filename>.md
```

The override file should be a **complete exercise file** structured identically to the original in `workshop-content/`, with the `## Scenario` section rewritten for your application and any Tailspin-specific references replaced.

> [!TIP]
> Start by copying the original exercise file, then search for "Tailspin" and replace every occurrence with your scenario's equivalent. Update code snippets and prompts to match your tech stack.

### Minimal override example

If only the `## Scenario` section needs to change:

```markdown
<!-- scenarios/my-scenario/overrides/1-mcp.md -->

# Exercise 1 - Setting up the backlog with Copilot agent mode and GitHub's MCP Server

...same content as workshop-content/1-mcp.md, except:...

## Scenario

You are a developer for <Company Name> — <company_description>. You've been
assigned tasks to introduce new functionality. To file your backlog of issues
you'll enlist the help of Copilot Chat in agent mode and the GitHub MCP server.

...rest of file unchanged...
```

---

## Step 6 — Validate your scenario

Run the validation script to catch common problems:

```bash
python scripts/validate-scenario.py <scenario-id>
```

The script checks:

- All required fields are present in `scenario.yml`.
- Every exercise listed in `skip` exists in `workshop-content/`.
- Every override file in `overrides/` corresponds to an exercise in `workshop-content/`.
- No override exists for an exercise in the `skip` list (that would be a conflict).

Fix any issues reported before continuing.

---

## Step 7 — Update the scenarios table

Add your scenario to the table in `scenarios/README.md`:

```markdown
| `<scenario-id>` | <App name and description> | <Tech stack> | 🚧 In progress |
```

Change the status to ✅ once the scenario is complete and validated.

---

## Step 8 — Test the scenario end-to-end

Follow the workshop yourself from start to finish using your scenario:

1. Clone your sample app repository into a codespace.
2. Work through each exercise (skipping those listed in `skip`).
3. Verify that every prompt in the exercises produces reasonable output from Copilot for your tech stack.
4. Adjust `scenario.yml` variables and/or override files as needed based on your experience.

---

## Using the AI prompt to create a sample app

If you need to create or adapt a sample application for your scenario, use the prompt file at `.github/prompts/create-scenario-app.prompt.md`. Open it in VS Code with GitHub Copilot Chat in **agent mode** and follow the instructions embedded in the prompt.

The prompt guides Copilot to:

- Create a minimal but realistic application matching your tech stack.
- Include a working test suite.
- Structure the code in a way that maps cleanly to the workshop exercises.
- Add a `.devcontainer/` configuration for Codespaces.

---

## Checklist

Use this checklist to track your progress:

- [ ] Identified and evaluated a suitable sample application
- [ ] Created scaffolding with `scripts/new-scenario.py`
- [ ] Completed all fields in `scenario.yml`
- [ ] Identified exercises to skip
- [ ] Written overrides for exercises with Tailspin-specific content
- [ ] Validated with `scripts/validate-scenario.py` (zero errors)
- [ ] Updated `scenarios/README.md` table
- [ ] Tested the scenario end-to-end
