---
description: Create or update a sample application to use as a workshop scenario
mode: agent
---

# Create or update a workshop scenario application

You are helping a workshop author create or update a sample application that will be used as the hands-on codebase for the "Agents in the SDLC" workshop. The workshop teaches learners how to use GitHub Copilot's agent capabilities across the software development lifecycle.

## Your task

${input:task:Choose one — (a) Create a brand-new sample application, or (b) Adapt an existing application to fit the workshop. Describe your choice and the application concept here.}

## Workshop exercise requirements

The sample application must support the following exercises. Review each requirement and confirm your application design meets it before generating code.

### Exercise 1 — MCP and issue creation
- No application requirements (learners create GitHub issues for their backlog).

### Exercise 2 — Custom instructions
- The application must have an API with unit tests.
- The application must have a UI (frontend).
- The codebase should lack docstrings/comment headers so learners can add them.
- A `.github/copilot-instructions.md` should NOT exist yet (learners create it).
- A `.github/instructions/` directory with one or more `*.instructions.md` files for specific languages or file types IS expected (learners reference these).

### Exercise 3 — Copilot agent mode (implement a new feature)
- The application must have an API endpoint that returns a list of the primary entities (e.g. `/api/games`).
- The primary entities must have at least two categorical attributes suitable for filtering (e.g. `category` and `publisher`).
- The application must have a frontend page that displays those entities.
- The existing filtering functionality must NOT be implemented yet — learners implement it.
- The API must have a test suite that Copilot can run as part of implementing the feature.

### Exercise 4 — Copilot coding agent (async tasks)
- The application must lack docstrings/comment headers (first async task: add them).
- The application must have a set of CRUD endpoints that are partially implemented — specifically, only the "read" (GET) endpoints exist. Learners assign the task of adding create/update/delete endpoints to Copilot coding agent.
- A `.github/workflows/copilot-setup-steps.yml` must exist that installs all dependencies and runs tests. This file is pre-created ahead of the workshop.

### Exercise 5 — Custom agents (accessibility)
- The application must have a UI with a dark colour scheme.
- The UI must not yet have a high-contrast or accessibility toggle — learners add it with a custom accessibility agent.
- A `.github/agents/accessibility.md` custom agent definition must exist that describes how to implement accessibility features for this UI.

### Exercise 6 — Managing agents
- No additional application requirements.

### Exercise 7 — Iterating on Copilot's work
- No additional application requirements beyond what exercises 4 and 5 created.

## Application structure requirements

- The application must be runnable inside a **GitHub Codespace** using a `.devcontainer/` configuration.
- A `scripts/` directory must contain:
  - `setup-env.sh` — installs all dependencies.
  - `run-server-tests.sh` — calls setup and runs backend tests.
  - `start-app.sh` — calls setup and starts both frontend and backend servers.
- The application must use a **database** (SQLite is fine) with seed data so it works out of the box.
- **Separate frontend and backend** processes are required (e.g. a Python/Node API on one port, a Svelte/React/Vue SPA on another).

## What to generate

1. **Describe the application concept** — company name, what the app does, primary entities, and tech stack.
2. **Review each exercise requirement** and confirm the application design satisfies it. Note any gaps.
3. **Generate the full application** including:
   - Backend API with seed data and tests (only GET endpoints for the primary entities).
   - Frontend displaying the primary entities (no filtering yet).
   - `.devcontainer/devcontainer.json` for Codespaces.
   - `scripts/setup-env.sh`, `scripts/run-server-tests.sh`, `scripts/start-app.sh`.
   - `.github/workflows/copilot-setup-steps.yml`.
   - `.github/agents/accessibility.md`.
   - `.github/instructions/` with relevant instruction files for the chosen stack.
   - A `README.md` describing the application and how to run it.
4. **Do NOT generate**:
   - `.github/copilot-instructions.md` (learners create this in exercise 2).
   - Filter endpoints or filter UI (learners build these in exercise 3).
   - Create/update/delete endpoints (learners assign these to coding agent in exercise 4).
   - Docstrings or comment headers (learners add these via coding agent in exercise 4).
   - High-contrast mode (learners build this with the custom agent in exercise 5).

## Validation checklist

Before finishing, confirm:

- [ ] Application runs in a fresh Codespace with `scripts/start-app.sh`.
- [ ] Backend tests pass with `scripts/run-server-tests.sh`.
- [ ] `copilot-setup-steps.yml` completes successfully when triggered via `workflow_dispatch`.
- [ ] Primary entities list endpoint returns at least 8–10 seed records.
- [ ] Each entity has at least two categorical attributes suitable for filtering.
- [ ] The UI renders the entity list with no errors.
- [ ] Dark colour scheme is present in the UI.
- [ ] `accessibility.md` custom agent exists in `.github/agents/`.
- [ ] No filtering, no CRUD-write endpoints, no docstrings in the initial state.
