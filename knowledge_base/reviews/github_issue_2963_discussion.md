# [issues/issue_2963.md] - Issue #2963 discussion

**Type:** review
**Keywords:** tags field, biomes, conflicts, PRs, git merge, order of tags
**Concepts:** merge conflicts, pull requests, version control

## Summary
Discussion on adding a tags field to biomes to prevent conflicts in pull requests.

## Explanation
The issue revolves around the potential for merge conflicts when multiple pull requests add new tags to biome definitions. The maintainer explains that simply adding a `.tags` field does not resolve the conflict if two PRs attempt to modify the same line by adding different tags. Git cannot automatically determine which order to merge these changes, leading to a conflict.

## Related Questions
- How can conflicts be resolved when multiple PRs add different tags to the same biome?
- What is the impact of adding a `.tags` field on preventing merge conflicts in biome definitions?
- Can git automatically resolve conflicts when two PRs modify the same line in different ways?
- What are some strategies to prevent merge conflicts in pull requests that involve modifying shared data structures like biome tags?
- How does the order of tags affect the resolution of merge conflicts in biome definitions?
- What are the potential drawbacks of adding a `.tags` field to every biome?

*Source: unknown | chunk_id: github_issue_2963_discussion*
