---
description: 'ASP.NET Core Web API controller and endpoint development guidelines'
applyTo: 'server/TailspinToys.Api/Controllers/*.cs'
---

# ASP.NET Core API Controller Guidelines

## Controller Structure

- Inherit from `ControllerBase` (not `Controller` — no views needed)
- Decorate with `[ApiController]` and `[Route("api/[controller]")]`
- Inject `AppDbContext` via constructor
- Return `IActionResult` from all action methods

## Data Access Patterns

- Use `AppDbContext` directly — no separate repository layer
- Always use `.Include()` for eager loading of navigation properties
- Use `.Select()` to project to DTOs — never return EF entities directly
- Use `async`/`await` throughout: `ToListAsync()`, `FirstOrDefaultAsync()`

## Route Definitions

- GET list: `[HttpGet]` on action returning `IActionResult`
- GET single: `[HttpGet("{id}")]` with `int id` parameter
- RESTful conventions: GET (retrieve), POST (create), PUT/PATCH (update), DELETE (remove)

## Response Handling

- Use `Ok(data)` for 200 responses
- Use `NotFound(new { error = "Resource not found" })` for 404
- Use `BadRequest(new { error = "..." })` for 400
- Return DTOs, not EF model objects

## DTO Pattern

```csharp
// DTOs/GameDtos.cs
public record CategorySummary(int Id, string Name);
public record PublisherSummary(int Id, string Name);
public record GameSummary(int Id, string Title, string Description, double? StarRating,
    CategorySummary? Category, PublisherSummary? Publisher);
```

## Example Controller Action

```csharp
[HttpGet]
public async Task<IActionResult> GetGames()
{
    var games = await _context.Games
        .Include(g => g.Category)
        .Include(g => g.Publisher)
        .Select(g => new GameSummary(
            g.Id, g.Title, g.Description, g.StarRating,
            g.Category != null ? new CategorySummary(g.Category.Id, g.Category.Name) : null,
            g.Publisher != null ? new PublisherSummary(g.Publisher.Id, g.Publisher.Name) : null))
        .ToListAsync();

    return Ok(games);
}
```

## Required Testing

- All controllers need xUnit tests per [csharp-tests.instructions.md](./csharp-tests.instructions.md)
- Run: [scripts/run-server-tests.sh](../../scripts/run-server-tests.sh)
- All tests must pass before committing

## Registration & References

- Controllers are auto-discovered via `app.MapControllers()` in `Program.cs`
- Example: [server/TailspinToys.Api/Controllers/GamesController.cs](../../server/TailspinToys.Api/Controllers/GamesController.cs)
- Tests: [server/TailspinToys.Tests/GamesControllerTests.cs](../../server/TailspinToys.Tests/GamesControllerTests.cs)
