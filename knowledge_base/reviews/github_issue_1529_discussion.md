# [issues/issue_1529.md] - Issue #1529 discussion

**Type:** review
**Keywords:** random rotation, vertical origin, blueprints, Z-axis, alignment, horizontal rotations
**Concepts:** rotation, structure alignment, vertical origin block

## Summary
The discussion revolves around implementing random rotation for structures with vertical origins, including blueprints within those structures. Maintainers emphasize the need to ensure proper alignment and consider only Z-axis rotations due to structural constraints.

## Explanation
The discussion revolves around implementing random rotation for structures with vertical origins, including blueprints within those structures. Maintainers emphasize the need to ensure proper alignment between the structure's origin block and its parent-child blocks by rotating around the Z axis. A specific parameter is added to allow blueprints within these structures to be randomly rotated. The implementation includes a flag named `rotate_with_vertical_origin` that can be set to either `random` or `fixed`. This flag propagates to vertical child blocks but stops on horizontal child blocks. Maintainers also suggest rotating around the origin block for vertical structures and note that horizontal rotations are not feasible due to architectural constraints.

## Related Questions
- How does the current implementation handle the alignment of rotated structures with their parent-child blocks?
- What are the potential impacts of rotating structures around the Z axis on their overall stability and appearance?
- Can you provide a detailed explanation of how blueprints within structures will be affected by random rotations?
- Are there any specific use cases where horizontal rotations would be beneficial, despite the current limitations?
- How can we ensure that the rotation functionality does not introduce any regressions in existing structure generation logic?

*Source: unknown | chunk_id: github_issue_1529_discussion*
