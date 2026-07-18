# [issues/issue_693.md] - Issue #693 discussion

**Type:** review
**Keywords:** lava caves, crystal caves, surface level, height variation, commit bc1c1d6
**Concepts:** terrain generation, biome generation

## Summary
Discussion about cave biome generation issues, specifically lava and crystal caves appearing above the surface.

## Explanation
The issue report indicates that lava and crystal caves are generating near and above the surface at specific coordinates. The maintainer notes that this is a different problem from #475, which only applies when the terrain itself has significant height variations. The maintainer suspects that the issue was introduced in a specific commit (bc1c1d6d922037afd1bdbf2c963c5689a4c19e7b).

## Related Questions
- What changes were made in commit bc1c1d6 that could have affected cave generation?
- Are there any other issues related to cave biome generation in Cubyz?
- How does the terrain height affect cave generation in Cubyz?
- Is there a known solution or workaround for caves generating above the surface?
- What is the relationship between this issue and #475?
- Can the cave generation algorithm be modified to prevent caves from appearing above the surface?

*Source: unknown | chunk_id: github_issue_693_discussion*
