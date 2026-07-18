# [issues/issue_2262.md] - Issue #2262 discussion

**Type:** review
**Keywords:** block selection, head intersection, non-collidable blocks, air block, void block, expected behavior, algorithm modification
**Concepts:** block selection, player interaction, line of sight

## Summary
The issue describes a bug where block selection always targets the block containing the player's head instead of the intended target block.

## Explanation
The problem arises from the current block selection algorithm, which prioritizes the block intersected by the player's head over other blocks in the line of sight. This behavior is incorrect and leads to unexpected results when the player is inside non-collidable blocks like air or void. The discussion suggests modifying the algorithm to select a different block type if the initial target is non-collidable, ensuring that the intended block is highlighted for placement.

## Related Questions
- What is the current algorithm for selecting target blocks in Cubyz?
- How does the player's head position affect block selection in Cubyz?
- Why is the initial target block selected when it is non-collidable?
- What changes are proposed to fix the block selection issue?
- How will the modified algorithm handle cases where all intersected blocks are non-collidable?
- Are there any potential performance implications of changing the block selection logic?

*Source: unknown | chunk_id: github_issue_2262_discussion*
