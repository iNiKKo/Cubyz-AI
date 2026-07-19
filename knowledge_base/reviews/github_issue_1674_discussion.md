# [issues/issue_1674.md] - Issue #1674 discussion

**Type:** review
**Keywords:** ore placement, logs, block type, rotation states, block models, mesh generation times
**Concepts:** block data, mesh generation, performance

## Summary
The issue discusses an anomaly where ore can be placed on logs except when the log is facing the ground sideways.

## Explanation
The issue discusses an anomaly where ore can be placed on logs except when the log is facing the ground sideways. This problem arises due to technical limitations in encoding both block type and rotation states within the current block data model. The maintainer notes that with the current model system, allowing multiple block models would cause a combinatorial explosion potentially leading to millions of separate block models, which may have negative consequences on mesh generation times. To fix it, we'd need to allow returning multiple block models, but this could lead to significant performance issues.

## Related Questions
- What is the current block data model that limits ore placement on logs?
- How would allowing multiple block models affect mesh generation performance?
- Are there any plans to refactor the block data model in future updates?
- Can the issue be resolved without changing the block data model?
- What are the potential consequences of a combinatorial explosion in block models?
- Is there a workaround for placing ore on logs with specific orientations?

*Source: unknown | chunk_id: github_issue_1674_discussion*
