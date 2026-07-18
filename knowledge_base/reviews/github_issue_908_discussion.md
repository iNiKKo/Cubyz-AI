# [issues/issue_908.md] - Issue #908 discussion

**Type:** review
**Keywords:** biome interpolation, NoiseBasedVoronoi, natural neighbor interpolation, variable size voronoi grid, edge cases, smaller biomes, interpolation rewrite
**Symbols:** NoiseBasedVoronoi, Natural-neighbor Interpolation
**Concepts:** interpolation, biome generation, voronoi grid

## Summary
Discussion about improving biome interpolation in the NoiseBasedVoronoi generator for better performance with smaller biomes and edge cases.

## Explanation
The issue report highlights that the current implementation of biome interpolation in the NoiseBasedVoronoi generator does not perform well, especially for smaller biomes. The maintainer suggests that this problem might have been addressed in a previous rewrite (#1783) focused on interpolation improvements.

## Related Questions
- What was the specific change made in #1783 that might have fixed this issue?
- How does natural neighbor interpolation differ from other interpolation methods?
- Can you explain how the variable size voronoi grid affects biome interpolation?
- Are there any known limitations of natural neighbor interpolation in this context?
- What are the potential performance implications of implementing natural neighbor interpolation?
- How might edge cases be handled with the new interpolation method?

*Source: unknown | chunk_id: github_issue_908_discussion*
