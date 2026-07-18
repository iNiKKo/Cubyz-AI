# [src/renderer/chunk_meshing.zig] - PR #445 review diff

**Type:** review
**Keywords:** chunk_meshing.zig, taskType, .lighting, performance problems, classification
**Symbols:** ChunkMesh, isStillNeeded, run, clean, taskType
**Concepts:** architectural review, task classification

## Summary
Added a 'taskType' field to the ChunkMesh struct with the value '.lighting'.

## Explanation
The reviewer suggests that the addition of a 'taskType' field to classify tasks as '.lighting' is straightforward. However, they raise a question about whether there might be a better classification method for task types, indicating potential future improvements in how tasks are categorized and managed within the chunk meshing process.

## Related Questions
- What other task types are currently being considered for classification?
- How does the addition of 'taskType' impact the performance of chunk meshing tasks?
- Are there any potential memory implications from adding this new field to ChunkMesh?
- Can you provide more details on the performance issues that led to this change?
- Is there a plan to refactor task classification in the future based on reviewer feedback?
- How does this change affect backwards compatibility with existing chunk meshing logic?

*Source: unknown | chunk_id: github_pr_445_comment_1628890561*
