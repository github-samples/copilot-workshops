using TailspinToys.Api.Models;

namespace TailspinToys.Api.Data;

public static class DataSeeder
{
    public static void Seed(AppDbContext context)
    {
        if (context.Games.Any()) return;

        var devGames = new Publisher { Name = "DevGames Inc" };
        var scrumMasters = new Publisher { Name = "Scrum Masters" };
        var bitByBit = new Publisher { Name = "Bit By Bit Games" };
        var stackOverflow = new Publisher { Name = "Stack Overflow Studios" };
        context.Publishers.AddRange(devGames, scrumMasters, bitByBit, stackOverflow);

        var strategy = new Category { Name = "Strategy" };
        var cardGame = new Category { Name = "Card Game" };
        var cooperative = new Category { Name = "Cooperative" };
        var workerPlacement = new Category { Name = "Worker Placement" };
        context.Categories.AddRange(strategy, cardGame, cooperative, workerPlacement);

        context.SaveChanges();

        context.Games.AddRange(
            new Game
            {
                Title = "Pipeline Panic",
                Description = "Build your DevOps pipeline before chaos ensues. Race against other teams to ship features without breaking production.",
                Category = strategy,
                Publisher = devGames,
                StarRating = 4.5
            },
            new Game
            {
                Title = "Agile Adventures",
                Description = "Navigate your team through sprints and releases. Plan, execute, and adapt in this fast-paced card game about agile development.",
                Category = cardGame,
                Publisher = scrumMasters,
                StarRating = 4.2
            },
            new Game
            {
                Title = "Deploy or Die",
                Description = "A cooperative game where your team must deploy a legacy monolith before the deadline while keeping uptime above 99%.",
                Category = cooperative,
                Publisher = bitByBit,
                StarRating = 3.8
            },
            new Game
            {
                Title = "Merge Conflict",
                Description = "A strategy game about resolving code conflicts and shipping features on time. Collaboration and communication are key to victory.",
                Category = strategy,
                Publisher = stackOverflow,
                StarRating = 4.7
            },
            new Game
            {
                Title = "Bug Hunt",
                Description = "Find and squash bugs before they make it to production in this cooperative race through layers of code.",
                Category = cooperative,
                Publisher = devGames,
                StarRating = 4.0
            },
            new Game
            {
                Title = "Standup Shuffle",
                Description = "A card game where players take on developer roles and race to finish their backlog before the sprint ends.",
                Category = cardGame,
                Publisher = scrumMasters,
                StarRating = 3.9
            },
            new Game
            {
                Title = "Refactor Rally",
                Description = "A worker placement game where you clean up legacy code and add new features simultaneously. Balance is everything.",
                Category = workerPlacement,
                Publisher = bitByBit,
                StarRating = 4.3
            },
            new Game
            {
                Title = "Dependency Hell",
                Description = "A strategy game about managing a complex web of library dependencies. One wrong upgrade and everything breaks.",
                Category = strategy,
                Publisher = stackOverflow,
                StarRating = 4.1
            },
            new Game
            {
                Title = "Code Review Chronicles",
                Description = "A cooperative game where your team reviews each other's pull requests before merging. Catch bugs before they ship!",
                Category = cooperative,
                Publisher = devGames,
                StarRating = 4.6
            },
            new Game
            {
                Title = "Sprint Planning Shenanigans",
                Description = "A worker placement game where you estimate stories, assign tasks, and try to actually finish the sprint. Spoiler: you won't.",
                Category = workerPlacement,
                Publisher = scrumMasters,
                StarRating = 4.4
            }
        );

        context.SaveChanges();
    }
}
