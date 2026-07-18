# [issues/issue_1927.md] - Issue #1927 discussion

**Type:** review
**Keywords:** multiple terrain generators, generation dimensions, stacking, regional split, legacy code, engine design
**Concepts:** terrain generation, biome system, world design

## Summary
The user suggests adding multiple terrain generators per world with configurable generation dimensions, while the maintainer discusses existing limitations and potential conflicts.

## Explanation
The user proposes allowing multiple terrain generators in a single world by specifying generation dimensions (X, Y, Z). This would enable stacking different types of terrains vertically or regionally. The maintainer points out that current biome systems can already achieve similar effects but are less fine-grained. The maintainer also expresses concern about adding too many legacy systems to the engine, suggesting that features should be useful for the core game rather than just addons.

## Related Questions
- How can the current biome system be modified to support more fine-grained stacking of terrains?
- What are the potential performance implications of adding multiple terrain generators per world?
- How can conflicts between different terrain generators be prevented?
- What is the current mechanism for handling heightmap interpolation in Cubyz?
- Can the existing generation methods be adapted to accommodate multiple surface maps without significant overhead?
- What criteria should be used to determine if a feature is worth adding to the core engine?

*Source: unknown | chunk_id: github_issue_1927_discussion*
