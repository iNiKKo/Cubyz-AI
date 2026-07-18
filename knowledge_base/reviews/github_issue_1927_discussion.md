# [issues/issue_1927.md] - Issue #1927 discussion

**Type:** review
**Keywords:** multiple terrain generators, generation dimensions, stacking, regional split, legacy code, engine design
**Concepts:** terrain generation, biome system, world design

## Summary
The user suggests adding multiple terrain generators per world with configurable generation dimensions, while the maintainer discusses existing limitations and potential conflicts.

## Explanation
The user suggests allowing multiple terrain generators in a single world with configurable generation dimensions (X, Y, Z) to enable stacking different types of terrains vertically or regionally. The maintainer clarifies that new versions of the generator will overwrite previous ones and emphasizes the importance of avoiding harsh borders by storing heightmaps and interpolating them. They also mention that current biome systems can achieve similar effects but are less fine-grained, specifically referencing caves biomes as an example. The maintainer expresses concern about adding too many legacy systems to the engine, suggesting that features should be useful for the core game rather than just addons.

## Related Questions
- How does Cubyz handle heightmap interpolation to avoid harsh terrain transitions?
- What are the limitations of using biome systems for stacking different terrains?
- Can existing generation methods accommodate multiple surface maps without significant overhead?

*Source: unknown | chunk_id: github_issue_1927_discussion*
