# Tailspin Toys Dotnet — Exercise Overrides

This directory contains exercise-specific content overrides for the **Tailspin Toys Dotnet** scenario.

## How overrides work

Place a Markdown file here with the **same filename** as an exercise in `workshop-content/` to replace
its contents for this scenario. Typically you only need to rewrite the `## Scenario` section of each
exercise to match your application — copy the original exercise file and replace every Tailspin-specific
reference with your application's equivalent.

```
overrides/
  1-mcp.md                        ← replaces Scenario section for exercise 1
  3-copilot-agent-mode-vscode.md  ← replaces Scenario section for exercise 3
```

Overrides must NOT be created for exercises listed in the `skip` field of `scenario.yml`.

See [docs/authoring/new-scenario-guide.md](../../../docs/authoring/new-scenario-guide.md) for full instructions.

## Files in this directory

*(None yet — add override files as needed.)*
