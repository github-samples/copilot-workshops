# Tailspin Toys — Scenario Overrides

This directory holds exercise-specific content overrides for the **Tailspin Toys** scenario.

## About overrides

Tailspin Toys is the **default scenario** — the core exercises in `workshop-content/` were originally authored against it. However, as the base workshop content has been generalized to support any language or framework, overrides are used here to restore the Python/Flask-specific and Tailspin Toys-specific details where needed.

## Files in this directory

| File | Purpose |
|------|---------|
| `2-custom-instructions.md` | Restores Python/Flask-specific file references (`publishers.py`, `flask-endpoint.instructions.md`, `python-tests.instructions.md`) and Python docstring code examples removed from the generic base |
| `5-custom-agents.md` | Restores the Tailspin Toys high-contrast mode accessibility scenario |
| `6-managing-agents.md` | Restores the Tailspin Toys light-mode steering scenario and the Tailspin-specific task list |

## When to add an override

If you fork the workshop to use a different sample application you may need to replace the *Scenario* section of one or more exercises with text that matches your application. For a new scenario, place the replacement file here with the **same filename** as the exercise it overrides:

```
overrides/
  1-mcp.md               ← replaces the Scenario section of exercise 1
  3-copilot-agent-mode-vscode.md
```

See [scenarios/README.md](../../../scenarios/README.md) and the [authoring guide](../../../docs/authoring/new-scenario-guide.md) for full details.
