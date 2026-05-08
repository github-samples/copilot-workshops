# Tailspin Toys — Scenario Overrides

This directory holds exercise-specific content overrides for the **Tailspin Toys** scenario.

## About overrides

Because Tailspin Toys is the **default scenario** — meaning all of the exercises in `workshop-content/` were authored against it — this directory is intentionally empty. No overrides are needed.

## When to add an override

If you fork the workshop to use a different sample application you may need to replace the *Scenario* section of one or more exercises with text that matches your application. For a new scenario, place the replacement file here with the **same filename** as the exercise it overrides:

```
overrides/
  1-mcp.md               ← replaces the Scenario section of exercise 1
  3-copilot-agent-mode-vscode.md
```

See [scenarios/README.md](../../../scenarios/README.md) and the [authoring guide](../../../docs/authoring/new-scenario-guide.md) for full details.
