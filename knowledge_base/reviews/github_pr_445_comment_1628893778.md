# [src/renderer/chunk_meshing.zig] - PR #445 review diff

**Type:** review
**Keywords:** taskType, lighting, LightRefreshTask, LightMapLoadTask, .misc, performance impact
**Symbols:** ChunkMesh, isStillNeeded, run, clean, taskType
**Concepts:** architectural design, performance optimization

## Summary
The change adds a new task type 'lighting' to the ChunkMesh struct.

## Explanation
The reviewer suggests categorizing the LightRefreshTask and LightMapLoadTask under a '.misc' category, indicating that these tasks do not significantly impact performance. The addition of the 'taskType' field with the value '.lighting' is intended to clarify the purpose of the task within the ChunkMesh struct.

## Related Questions
- What is the purpose of adding 'taskType' to the ChunkMesh struct?
- Why are LightRefreshTask and LightMapLoadTask suggested for '.misc' category?
- How does this change affect performance optimization in chunk meshing?
- Can you explain the architectural reasoning behind categorizing tasks as '.misc'?
- What other task types might be considered for future implementations?
- How does this modification impact thread safety in the rendering pipeline?

*Source: unknown | chunk_id: github_pr_445_comment_1628893778*
