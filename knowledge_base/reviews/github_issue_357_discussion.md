# [issues/issue_357.md] - Issue #357 discussion

**Type:** review
**Keywords:** rotation mode, wood blocks, cacti blocks, textured logs, multi-block logs, directional textures
**Concepts:** block design, texture mapping, directional rendering

## Summary
Discussion about using a rotation mode for wood and cacti blocks instead of separate top and log blocks.

## Explanation
The discussion revolves around whether to implement a rotation mode for wood and cacti blocks to allow for directional textures. The maintainer suggests that this could complicate the system with too many variations and would require additional textures for multi-block logs, potentially making it unnecessary. They also suggest handling such cases with separate blocks or considering if it is even worth implementing, referencing Thaumcraft's large trees as an example where normal logs are used without issues. The user argues in favor of directional textures specifically for the ends of the logs.

## Related Questions
- What are the potential performance implications of implementing a rotation mode for wood and cacti blocks?
- How would the addition of directional textures affect the rendering pipeline?
- Are there any existing examples in other games that handle similar block designs effectively?
- What are the maintenance challenges associated with supporting multiple texture orientations for each log type?
- Could this change introduce compatibility issues with existing world files or mods?
- How might this feature impact the overall visual consistency of the game environment?
- Are there any memory usage considerations when implementing additional textures for logs?
- What is the expected user feedback on this proposed block design change?
- How would this change affect the modding API and plugin development?
- Is there a way to implement this feature without significantly increasing the complexity of the block system?

*Source: unknown | chunk_id: github_issue_357_discussion*
