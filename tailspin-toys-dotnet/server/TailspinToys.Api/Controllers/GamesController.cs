using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using TailspinToys.Api.Data;
using TailspinToys.Api.DTOs;

namespace TailspinToys.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class GamesController : ControllerBase
{
    private readonly AppDbContext _context;

    public GamesController(AppDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<IActionResult> GetGames()
    {
        var games = await _context.Games
            .Include(g => g.Category)
            .Include(g => g.Publisher)
            .OrderBy(g => g.Id)
            .Select(g => new GameSummary(
                g.Id,
                g.Title,
                g.Description,
                g.StarRating,
                g.Category != null ? new CategorySummary(g.Category.Id, g.Category.Name) : null,
                g.Publisher != null ? new PublisherSummary(g.Publisher.Id, g.Publisher.Name) : null))
            .ToListAsync();

        return Ok(games);
    }

    [HttpGet("{id}")]
    public async Task<IActionResult> GetGame(int id)
    {
        var game = await _context.Games
            .Include(g => g.Category)
            .Include(g => g.Publisher)
            .Where(g => g.Id == id)
            .Select(g => new GameSummary(
                g.Id,
                g.Title,
                g.Description,
                g.StarRating,
                g.Category != null ? new CategorySummary(g.Category.Id, g.Category.Name) : null,
                g.Publisher != null ? new PublisherSummary(g.Publisher.Id, g.Publisher.Name) : null))
            .FirstOrDefaultAsync();

        if (game is null)
            return NotFound(new { error = "Game not found" });

        return Ok(game);
    }
}
