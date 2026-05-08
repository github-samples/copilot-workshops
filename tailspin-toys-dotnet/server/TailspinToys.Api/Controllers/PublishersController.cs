using Microsoft.AspNetCore.Mvc;
using TailspinToys.Api.Data;

namespace TailspinToys.Api.Controllers;

[ApiController]
[Route("api/[controller]")]
public class PublishersController : ControllerBase
{
    private readonly AppDbContext _context;

    public PublishersController(AppDbContext context)
    {
        _context = context;
    }
}
