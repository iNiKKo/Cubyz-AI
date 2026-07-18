# [issues/issue_908.md] - Issue #908 discussion

**Type:** review
**Keywords:** biome interpolation, NoiseBasedVoronoi, natural neighbor interpolation, variable size voronoi grid, edge cases, smaller biomes, interpolation rewrite
**Symbols:** NoiseBasedVoronoi, Natural-neighbor Interpolation
**Concepts:** interpolation, biome generation, voronoi grid

## Summary
Discussion about improving biome interpolation in the NoiseBasedVoronoi generator for better performance with smaller biomes and edge cases.

## Explanation
The issue report highlights that the current implementation of biome interpolation in the NoiseBasedVoronoi generator does not perform well, especially for smaller biomes. The maintainer suggests using natural-neighbor interpolation and adjusting it to fit a variable size voronoi grid. This problem was addressed in a previous rewrite (#1783) focused on interpolation improvements.

## Related Questions
- What specific changes were made in #1783 to address the biome interpolation issue?
- How does natural-neighbor interpolation differ from other methods and how is it adjusted for a variable size voronoi grid?

*Source: unknown | chunk_id: github_issue_908_discussion*
