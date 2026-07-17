# [src/renderer/chunk_meshing.zig] - PR #445 review diff

**Type:** review
**Keywords:** ChunkMesh, taskType, .lighting, classification, performance problems
**Symbols:** ChunkMesh, taskType
**Concepts:** architectural design, performance optimization

## Summary
Added 'taskType' field with value '.lighting' to ChunkMesh struct.

## Explanation
The reviewer added a 'taskType' field to the ChunkMesh struct, setting its value to '.lighting'. This change is intended to better classify tasks based on performance characteristics. The reviewer suggests that while this implementation is straightforward, there might be a more optimal classification method for task types.

## Related Questions
- What is the purpose of adding 'taskType' to ChunkMesh?
- How does the '.lighting' task type impact performance?
- Are there any potential regressions introduced by this change?
- Is there a more efficient way to classify tasks in ChunkMesh?
- What other task types could be added to improve classification?
- How does this change affect backwards compatibility with existing code?

*Source: unknown | chunk_id: github_pr_445_comment_1628890561*
