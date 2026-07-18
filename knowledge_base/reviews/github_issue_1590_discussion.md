# [issues/issue_1590.md] - Issue #1590 discussion

**Type:** review
**Keywords:** damage numbers, particles, UI element, DPS meter, tooltip, cosmetic feature, performance impact
**Concepts:** UI design, player experience, performance

## Summary
The discussion revolves around implementing visual damage numbers when hitting blocks, with concerns about UI clutter, performance, and practicality.

## Explanation
The discussion revolves around implementing visual damage numbers when hitting blocks in Cubyz. Users and maintainers debate whether this feature should be displayed as particles or as a UI element, considering its potential impact on performance and player experience. A user suggests using the command `/countdamage` to enable damage numbers in chat logs during testing, but maintainers argue that this feature is more useful alongside other random numbered damages or as an extended tooltip showing exact damage values when breaking blocks. They note that after issue #1656, the crafting grid DPS system is now accurate except for resistance, making the proposed damage number feature less necessary. The maintainers conclude that implementing visual damage numbers would be purely cosmetic and could clutter the UI without providing significant utility to players.

## Related Questions
- What are the potential performance impacts of implementing damage number particles?
- How can we ensure that damage numbers do not clutter the UI?
- Are there any existing systems in Cubyz that could be adapted for displaying damage numbers?
- What is the purpose of showing damage numbers to players?
- How does the current crafting grid DPS system compare to the proposed damage number feature?
- Can damage numbers be implemented without significantly affecting game performance?

*Source: unknown | chunk_id: github_issue_1590_discussion*
