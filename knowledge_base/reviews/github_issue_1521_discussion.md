# [issues/issue_1521.md] - Issue #1521 discussion

**Type:** review
**Keywords:** sparkle animation, multiple textures, color overrides, particle system, flexibility, redundancy
**Concepts:** particle system, animation, texture support, color customization

## Summary
Discussion about adding a sparkle particle with small animations that immediately disappear without velocity, having slightly randomized animation speed, texture, and size. The current implementation does not support multiple textures per particle and lacks color customization options.

## Explanation
The discussion revolves around implementing a sparkle particle in the Cubyz game engine. This particle will play a small sparkle animation and then immediately disappear without velocity. The animation's speed, texture, and size are slightly randomized. The current implementation does not support multiple textures per particle, which could complicate adding different visual effects. Additionally, there is a suggestion to include color overrides for the particles to avoid creating new particle types just for different colors. This would enhance flexibility and reduce redundancy in particle management.

## Related Questions
- What are the characteristics of the sparkle animation?
- Why does the current implementation not support multiple textures per particle?
- How can color customization be implemented without creating new particle types?

*Source: unknown | chunk_id: github_issue_1521_discussion*
