using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using TailspinToys.Api.Controllers;
using TailspinToys.Api.Data;
using TailspinToys.Api.DTOs;
using TailspinToys.Api.Models;
using Xunit;

namespace TailspinToys.Tests;

public class GamesControllerTests
{
    private const string GamesApiPath = "/api/games";

    private static readonly Publisher Publisher1 = new() { Name = "DevGames Inc" };
    private static readonly Publisher Publisher2 = new() { Name = "Scrum Masters" };
    private static readonly Category Category1 = new() { Name = "Strategy" };
    private static readonly Category Category2 = new() { Name = "Card Game" };

    private static AppDbContext CreateTestContext(string dbName)
    {
        var options = new DbContextOptionsBuilder<AppDbContext>()
            .UseInMemoryDatabase(dbName)
            .Options;
        var context = new AppDbContext(options);
        SeedTestData(context);
        return context;
    }

    private static void SeedTestData(AppDbContext context)
    {
        var publisher1 = new Publisher { Name = "DevGames Inc" };
        var publisher2 = new Publisher { Name = "Scrum Masters" };
        var category1 = new Category { Name = "Strategy" };
        var category2 = new Category { Name = "Card Game" };

        context.Publishers.AddRange(publisher1, publisher2);
        context.Categories.AddRange(category1, category2);
        context.SaveChanges();

        context.Games.AddRange(
            new Game
            {
                Title = "Pipeline Panic",
                Description = "Build your DevOps pipeline before chaos ensues.",
                Publisher = publisher1,
                Category = category1,
                StarRating = 4.5
            },
            new Game
            {
                Title = "Agile Adventures",
                Description = "Navigate your team through sprints and releases.",
                Publisher = publisher2,
                Category = category2,
                StarRating = 4.2
            });
        context.SaveChanges();
    }

    [Fact]
    public async Task GetGames_ReturnsOkWithAllGames()
    {
        using var context = CreateTestContext(nameof(GetGames_ReturnsOkWithAllGames));
        var controller = new GamesController(context);

        var result = await controller.GetGames();

        var ok = Assert.IsType<OkObjectResult>(result);
        var games = Assert.IsAssignableFrom<List<GameSummary>>(ok.Value);
        Assert.Equal(2, games.Count);
    }

    [Fact]
    public async Task GetGames_ReturnsCorrectStructure()
    {
        using var context = CreateTestContext(nameof(GetGames_ReturnsCorrectStructure));
        var controller = new GamesController(context);

        var result = await controller.GetGames();

        var ok = Assert.IsType<OkObjectResult>(result);
        var games = Assert.IsAssignableFrom<List<GameSummary>>(ok.Value);
        var first = games[0];

        Assert.NotEqual(0, first.Id);
        Assert.False(string.IsNullOrEmpty(first.Title));
        Assert.False(string.IsNullOrEmpty(first.Description));
        Assert.NotNull(first.Category);
        Assert.NotNull(first.Publisher);
    }

    [Fact]
    public async Task GetGames_ReturnsCorrectData()
    {
        using var context = CreateTestContext(nameof(GetGames_ReturnsCorrectData));
        var controller = new GamesController(context);

        var result = await controller.GetGames();

        var ok = Assert.IsType<OkObjectResult>(result);
        var games = Assert.IsAssignableFrom<List<GameSummary>>(ok.Value);

        Assert.Contains(games, g => g.Title == "Pipeline Panic" && g.Publisher!.Name == "DevGames Inc");
        Assert.Contains(games, g => g.Title == "Agile Adventures" && g.Category!.Name == "Card Game");
    }

    [Fact]
    public async Task GetGames_EmptyDatabase_ReturnsEmptyList()
    {
        var options = new DbContextOptionsBuilder<AppDbContext>()
            .UseInMemoryDatabase(nameof(GetGames_EmptyDatabase_ReturnsEmptyList))
            .Options;
        using var context = new AppDbContext(options);
        var controller = new GamesController(context);

        var result = await controller.GetGames();

        var ok = Assert.IsType<OkObjectResult>(result);
        var games = Assert.IsAssignableFrom<List<GameSummary>>(ok.Value);
        Assert.Empty(games);
    }

    [Fact]
    public async Task GetGame_ValidId_ReturnsGame()
    {
        using var context = CreateTestContext(nameof(GetGame_ValidId_ReturnsGame));
        var controller = new GamesController(context);

        var allResult = await controller.GetGames();
        var allOk = Assert.IsType<OkObjectResult>(allResult);
        var allGames = Assert.IsAssignableFrom<List<GameSummary>>(allOk.Value);
        var gameId = allGames[0].Id;

        var result = await controller.GetGame(gameId);

        var ok = Assert.IsType<OkObjectResult>(result);
        var game = Assert.IsType<GameSummary>(ok.Value);
        Assert.Equal(gameId, game.Id);
        Assert.Equal("Pipeline Panic", game.Title);
        Assert.Equal("DevGames Inc", game.Publisher!.Name);
        Assert.Equal("Strategy", game.Category!.Name);
    }

    [Fact]
    public async Task GetGame_InvalidId_ReturnsNotFound()
    {
        using var context = CreateTestContext(nameof(GetGame_InvalidId_ReturnsNotFound));
        var controller = new GamesController(context);

        var result = await controller.GetGame(999);

        Assert.IsType<NotFoundObjectResult>(result);
    }

    [Fact]
    public async Task GetGame_ReturnsStarRating()
    {
        using var context = CreateTestContext(nameof(GetGame_ReturnsStarRating));
        var controller = new GamesController(context);

        var allResult = await controller.GetGames();
        var allOk = Assert.IsType<OkObjectResult>(allResult);
        var allGames = Assert.IsAssignableFrom<List<GameSummary>>(allOk.Value);
        var gameId = allGames[0].Id;

        var result = await controller.GetGame(gameId);

        var ok = Assert.IsType<OkObjectResult>(result);
        var game = Assert.IsType<GameSummary>(ok.Value);
        Assert.Equal(4.5, game.StarRating);
    }
}
