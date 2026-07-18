# [src/server/command/worldedit/selection.zig] - PR #3313 review diff

**Type:** review
**Keywords:** selection command, user experience, clarity of usage, pos1, pos2, cube command, radius, connected blocks
**Symbols:** selection, normalize, cube, radius, pos1, pos2, Block, command, User, Vec3i
**Concepts:** user experience, command clarity, block selection

## Summary
The review discusses issues with the selection command in Cubyz, particularly focusing on user experience and clarity of usage.

## Explanation
The reviewer points out that setting pos2 after pos1 can be awkward because it only allows clearing both positions. The reviewer suggests a future improvement where a unique wand could automatically select connected blocks upon clicking. Additionally, the reviewer questions the clarity of the `/selection cube` command, expressing uncertainty about the dimensions and positioning of the resulting block box.

## Related Questions
- How does the current selection command handle setting pos2 after pos1?
- What is the proposed improvement for selecting connected blocks using a unique wand?
- Can you explain the ambiguity in the dimensions of the block box created by the `/selection cube` command?
- What are the potential user experience improvements suggested for the selection command?
- How does the current implementation handle the setting and clearing of pos1 and pos2?
- What is the intended use case for the `/selection cube` command, and how clear is its behavior?

*Source: unknown | chunk_id: github_pr_3313_comment_3560517031*
