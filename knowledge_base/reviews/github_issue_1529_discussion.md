# [issues/issue_1529.md] - Issue #1529 discussion

**Type:** review
**Keywords:** random rotation, vertical origin, blueprints, Z-axis, alignment, horizontal rotations
**Concepts:** rotation, structure alignment, vertical origin block

## Summary
The discussion revolves around implementing random rotation for structures with vertical origins, including blueprints within those structures. Maintainers emphasize the need to ensure proper alignment and consider only Z-axis rotations due to structural constraints.

## Explanation
The primary focus is on adding functionality to randomly rotate structures that have a vertical origin block. The discussion highlights the importance of maintaining alignment between the structure's origin block and its parent-child blocks, which necessitates rotating around the Z axis. Maintainers also suggest allowing blueprints within these structures to be rotated as well. However, there are limitations regarding horizontal rotations, as they would require additional work and may not align with current architectural constraints.

## Related Questions
- How does the current implementation handle the alignment of rotated structures with their parent-child blocks?
- What are the potential impacts of rotating structures around the Z axis on their overall stability and appearance?
- Can you provide a detailed explanation of how blueprints within structures will be affected by random rotations?
- Are there any specific use cases where horizontal rotations would be beneficial, despite the current limitations?
- How can we ensure that the rotation functionality does not introduce any regressions in existing structure generation logic?
- What architectural changes are necessary to support horizontal rotations in the future?

*Source: unknown | chunk_id: github_issue_1529_discussion*
