# [issues/issue_2647.md] - Issue #2647 discussion

**Type:** review
**Keywords:** transitionBiomes, ocean tag, land tag, biome behavior, error handling, climate zones
**Symbols:** .transitionBiomes, .ocean, .land
**Concepts:** biome mechanics, tag requirements, climate zones

## Summary
The issue discusses the behavior of the `.transitionBiomes` method, which requires both interior and transition biomes to have specific tags for proper functionality.

## Explanation
The issue discusses the behavior of the `.transitionBiomes` method, which requires both interior and transition biomes to have specific tags for proper functionality. The user encountered a problem where the `.transitionBiomes` method did not work as expected unless both the interior and transition biomes had the `.ocean` tag, and the entry in `.transitionBiomes` had the `.land` tag. Additionally, the maintainer confirmed that the method only works if the host biome does not already have the same climate zones. They suggested adding an error to handle this scenario better.

## Related Questions
- What are the requirements for using .transitionBiomes?
- Why does .transitionBiomes only work with specific tags?
- How can I ensure proper biome transitions in Cubyz?
- What is the purpose of the .ocean and .land tags in biomes?
- How does climate zone overlap affect .transitionBiomes?
- Is there a way to debug issues with .transitionBiomes?

*Source: unknown | chunk_id: github_issue_2647_discussion*
