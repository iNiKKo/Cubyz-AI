# [src/renderer/chunk_meshing.zig] - PR #445 review diff

**Type:** review
**Keywords:** taskType, .lighting, LightRefreshTask, mesh generation, performance issues
**Symbols:** ChunkMesh, taskType
**Concepts:** thread safety, performance profiling

## Summary
Added a taskType field to ChunkMesh and assigned it to .lighting.

## Explanation
The change introduces a new field 'taskType' in the ChunkMesh struct and assigns it the value '.lighting'. The reviewer points out that there are multiple tasks with the same tag, which can obscure performance issues. Specifically, they mention that the LightRefreshTask is relatively fast, which might skew the average mesh generation time. Additionally, there are three .lighting tasks, but they do completely different things. This can hide performance problems because having multiple tasks with the same tag can make it difficult to identify and address specific issues related to each task. For example, if one of the .lighting tasks is significantly slower than others, it might not be noticed if all tasks are grouped under the same tag.

## Related Questions
- What are the other tasks with the .lighting tag?
- How does the addition of taskType affect performance profiling?
- Are there any potential thread safety concerns with multiple .lighting tasks?
- How does this change impact the overall mesh generation process?
- Is there a need to refactor the LightRefreshTask for better performance measurement?
- What are the implications of having multiple tasks with the same tag?

*Source: unknown | chunk_id: github_pr_445_comment_1628886190*
