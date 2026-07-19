# [src/renderer/chunk_meshing.zig] - PR #445 review diff

**Type:** review
**Keywords:** chunk_meshing.zig, taskType, .lighting, performance problems, classification
**Symbols:** ChunkMesh, isStillNeeded, run, clean, taskType
**Concepts:** architectural review, task classification

## Summary
Added a 'taskType' field to the ChunkMesh struct with the value '.lighting'.

## Explanation
The reviewer added a 'taskType' field to the ChunkMesh struct and classified it as '.lighting'. They suggest that this change is straightforward but raise a question about whether there might be a better classification method for task types. The current classification is based on the reviewer's impressions of performance problems in the chunk meshing process.

The addition of 'taskType' impacts the performance of chunk meshing tasks by providing a clearer categorization of tasks, which could lead to more efficient management and optimization. However, there may be potential memory implications from adding this new field to ChunkMesh, as it increases the size of the struct.

The reviewer indicates that future improvements in task classification are possible based on their feedback, suggesting a plan to refactor task classification if necessary. This change does not affect backwards compatibility with existing chunk meshing logic, as it is an additive modification.

## Related Questions
- What other task types are currently being considered for classification?
- How does the addition of 'taskType' impact the performance of chunk meshing tasks?
- Are there any potential memory implications from adding this new field to ChunkMesh?
- Can you provide more details on the performance issues that led to this change?
- Is there a plan to refactor task classification in the future based on reviewer feedback?
- How does this change affect backwards compatibility with existing chunk meshing logic?

*Source: unknown | chunk_id: github_pr_445_comment_1628890561*
