# [issues/issue_1489.md] - Issue #1489 discussion

**Type:** review
**Keywords:** world type, testing, LOD update, map update, biome hash, seed consistency, loading times, structure generators
**Concepts:** LOD, biome changes, seed consistency

## Summary
Discussion about adding a special world type for testing that doesn't update LODs and maps on biome changes, with considerations for seed consistency.

## Explanation
The discussion revolves around adding a special world type for testing purposes that avoids updating Level of Detail (LOD) and map data when biomes change. The user suggests keeping the seed constant to improve testing of loading/startup times and new structure generators, noting that consistent terrain helps in these tests. However, the maintainer raises concerns about potential bugs related to biome hash differences across release modes, indicating that a different biome hash would mean inconsistent behavior between release modes. Additionally, the maintainer questions the importance of maintaining a constant seed for testing purposes.

## Related Questions
- What is the impact of biome hash differences in various release modes?
- How does keeping a consistent seed benefit testing loading/startup times and new structure generators?

*Source: unknown | chunk_id: github_issue_1489_discussion*
