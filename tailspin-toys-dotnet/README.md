# Tailspin Toys (.NET)

A crowdfunding platform for board games with a developer theme — built with **ASP.NET Core Web API** and **Astro + Svelte**.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | ASP.NET Core 8 Web API |
| ORM / Database | Entity Framework Core + SQLite |
| Frontend | Astro + Svelte 5 + Tailwind CSS |

## Project Structure

```
tailspin-toys-dotnet/
├── .devcontainer/          # Codespace / devcontainer configuration
├── .github/
│   ├── agents/             # Custom Copilot agents
│   ├── instructions/       # Copilot instruction files
│   └── workflows/          # GitHub Actions (Copilot setup steps)
├── client/                 # Astro + Svelte frontend (port 4321)
├── scripts/                # Helper scripts
│   ├── setup-env.sh        # Install all dependencies
│   ├── run-server-tests.sh # Run backend xUnit tests
│   └── start-app.sh        # Start both servers
└── server/                 # ASP.NET Core solution
    ├── TailspinToys.Api/   # Main Web API project
    └── TailspinToys.Tests/ # xUnit test project
```

## Getting Started

### Prerequisites

- [.NET 8 SDK](https://dotnet.microsoft.com/download)
- [Node.js 22+](https://nodejs.org/)

### Running the Application

```bash
./scripts/start-app.sh
```

Once started:
- **API** → http://localhost:5100
- **Frontend** → http://localhost:4321

### Running Backend Tests

```bash
./scripts/run-server-tests.sh
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/games` | List all games |
| GET | `/api/games/{id}` | Get a single game by ID |

## Workshop Context

This application is designed for use in the **Agents in the SDLC** workshop. Learners work through exercises using GitHub Copilot agent capabilities:

- **Exercise 1**: Use GitHub MCP server to create issues for the backlog
- **Exercise 2**: Add custom instructions for C# and the project coding standards
- **Exercise 3**: Use Copilot agent mode to add game filtering (category + publisher)
- **Exercise 4**: Assign Copilot to add XML documentation and CRUD endpoints
- **Exercise 5**: Use the custom accessibility agent to add a high-contrast mode toggle
- **Exercises 6–7**: Review, iterate, and manage Copilot's work
