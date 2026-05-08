namespace TailspinToys.Api.DTOs;

public record CategorySummary(int Id, string Name);
public record PublisherSummary(int Id, string Name);
public record GameSummary(
    int Id,
    string Title,
    string Description,
    double? StarRating,
    CategorySummary? Category,
    PublisherSummary? Publisher);
