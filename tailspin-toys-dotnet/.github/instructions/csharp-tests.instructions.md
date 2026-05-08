---
description: 'xUnit test guidelines for ASP.NET Core controller tests in C#'
applyTo: 'server/TailspinToys.Tests/**/*Tests.cs'
---

# C# xUnit Testing Guidelines

## Test Class Structure

- Each controller should have its own test class for proper grouping
- Name pattern: `<ControllerName>Tests` (e.g., `GamesControllerTests`)
- Include XML documentation comments describing what each test validates
- Use `public class` — no base class required for xUnit

## Test Data

- Define seed data as private static helpers or constants
- Keep data minimal but cover edge cases and relationships
- Use descriptive names indicating purpose

## Setup Pattern

- Create a `CreateTestContext(string dbName)` helper method
- Use `UseInMemoryDatabase` with a unique name per test to avoid shared state
- Seed data inside the helper
- Instantiate the controller directly: `new GamesController(context)`

```csharp
private static AppDbContext CreateTestContext(string dbName)
{
    var options = new DbContextOptionsBuilder<AppDbContext>()
        .UseInMemoryDatabase(dbName)
        .Options;
    var context = new AppDbContext(options);
    SeedTestData(context);
    return context;
}
```

## Required Test Coverage

- Success cases returning data (list and single item)
- Not-found cases (404 errors)
- Empty database scenarios
- Response structure validation (required fields present)
- Data correctness (correct values returned)

## Test Method Best Practices

- Follow Arrange-Act-Assert pattern
- Name: `<Action>_<Scenario>_<ExpectedResult>` (e.g., `GetGame_InvalidId_ReturnsNotFound`)
- Use `nameof(TestMethodName)` as the in-memory database name to ensure uniqueness
- Assert the result type with `Assert.IsType<OkObjectResult>(result)`
- Cast the value with `Assert.IsAssignableFrom<List<GameSummary>>(ok.Value)`
- Use `using var context = ...` to ensure proper disposal

## Example Test

```csharp
[Fact]
public async Task GetGames_ReturnsOkWithAllGames()
{
    // Arrange
    using var context = CreateTestContext(nameof(GetGames_ReturnsOkWithAllGames));
    var controller = new GamesController(context);

    // Act
    var result = await controller.GetGames();

    // Assert
    var ok = Assert.IsType<OkObjectResult>(result);
    var games = Assert.IsAssignableFrom<List<GameSummary>>(ok.Value);
    Assert.Equal(2, games.Count);
}
```

## Running Tests

```bash
scripts/run-server-tests.sh
# or directly:
dotnet test server/TailspinToys.Tests/TailspinToys.Tests.csproj --verbosity normal
```
