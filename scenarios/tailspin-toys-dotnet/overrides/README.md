# Tailspin Toys .NET — Exercise Overrides

This directory contains exercise-specific content overrides for the **Tailspin Toys .NET** scenario.

## How overrides work

Place a Markdown file here with the **same filename** as an exercise in `workshop-content/` to replace
its contents for this scenario. Typically you only need to rewrite the `## Scenario` section of each
exercise to match your application — copy the original exercise file and replace every Tailspin-specific
reference with your application's equivalent.

Overrides must NOT be created for exercises listed in the `skip` field of `scenario.yml`.

See [docs/authoring/new-scenario-guide.md](../../../docs/authoring/new-scenario-guide.md) for full instructions.

## Files in this directory

| File | Purpose |
|------|---------|
| `2-custom-instructions.md` | Replaces Python/Flask references with C#/ASP.NET Core equivalents (`PublishersController.cs`, `csharp-api.instructions.md`, `csharp-tests.instructions.md`, XML doc comment examples) |
| `3-copilot-agent-mode-vscode.md` | Replaces "backend written in Python" and Flask startup output with C#/ASP.NET Core equivalents |
| `4-copilot-coding-agent.md` | Replaces the Python `copilot-setup-steps.yml` snippet with the .NET (`setup-dotnet@v4`, `dotnet restore/build`) equivalent |
| `5-custom-agents.md` | Provides the Tailspin Toys high-contrast mode accessibility scenario (identical to the `tailspin-toys` scenario since the frontend is shared) |
| `6-managing-agents.md` | Provides the Tailspin Toys light-mode steering scenario (identical to `tailspin-toys` since the frontend is shared) |
| `7-iterating-copilot-work.md` | Replaces "Flask API" references with "ASP.NET Core API" |

