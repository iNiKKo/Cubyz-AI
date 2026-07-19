# [issues/issue_770.md] - Issue #770 discussion

**Type:** review
**Keywords:** LOD chunks, region file cache size, multiple instances, chunk reload, investigation
**Concepts:** region file cache, thread safety, memory management

## Summary
Investigation into LOD chunk issues suggests a potential cause related to hitting the region file cache size, leading to multiple instances of the same region file.

## Explanation
The maintainer investigated an issue where LOD chunks were breaking sometimes. This happened after regenerating them last time, as shown in the screenshot below: ![Screenshot at 2024-11-07 16-31-54](https://github.com/user-attachments/assets/4df94da2-e014-41c7-9c3d-d08dad64fd38). The suspected cause is that the system might be hitting the region file cache size limit, which could result in multiple instances of the same region file being loaded. This explanation aligns with why the issue only started occurring after a significant number of chunks had been built since the last LOD chunk reload.

## Related Questions
- What is the current limit of the region file cache size?
- How does the system handle multiple instances of the same region file?
- Are there any logs or error messages related to region file caching when this issue occurs?
- Can increasing the region file cache size mitigate this problem?
- Is there a way to ensure that only one instance of each region file is loaded at a time?
- How does the LOD chunk generation process interact with the region file cache?
- Are there any known optimizations for managing region files in Cubyz?
- What are the potential performance implications of increasing the region file cache size?
- Is there a mechanism to detect and handle conflicts when multiple instances of the same region file are loaded?
- How does this issue affect backwards compatibility with older LOD chunk data?

*Source: unknown | chunk_id: github_issue_770_discussion*
