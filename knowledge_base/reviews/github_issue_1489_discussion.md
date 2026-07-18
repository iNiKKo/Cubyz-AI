# [issues/issue_1489.md] - Issue #1489 discussion

**Type:** review
**Keywords:** world type, testing, LOD update, map update, biome hash, seed consistency, loading times, structure generators
**Concepts:** LOD, biome changes, seed consistency

## Summary
Discussion about adding a special world type for testing that doesn't update LODs and maps on biome changes, with considerations for seed consistency.

## Explanation
The discussion revolves around the need for a test world type that avoids updating Level of Detail (LOD) and map data when biomes change. The user suggests also keeping the seed constant to improve testing of loading/startup times and new structure generators. The maintainer raises concerns about potential bugs related to biome hash differences across release modes and questions the importance of maintaining a consistent seed for testing purposes.

## Related Questions
- What is the potential impact of different biome hashes in release modes?
- How could maintaining a constant seed improve testing of structure generators?
- Are there any existing world types that address LOD and map update issues?
- What are the benefits of not saving anything in a test world type?
- How might this new world type affect performance during gameplay?
- Is there a risk of introducing bugs by not updating LODs and maps on biome changes?

*Source: unknown | chunk_id: github_issue_1489_discussion*
