namespace TailspinToys.Api.Models;

public class Publisher
{
    public int Id { get; set; }
    public string Name { get; set; } = string.Empty;
    public ICollection<Game> Games { get; set; } = [];
}
