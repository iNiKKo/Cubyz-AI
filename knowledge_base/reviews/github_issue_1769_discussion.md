# [issues/issue_1769.md] - Issue #1769 discussion

**Type:** review
**Keywords:** floating point errors, teleporting into walls, fixed point, hitbox resizing, floor blocks
**Concepts:** floating-point precision, fixed-point arithmetic, hitbox collision

## Summary
The issue involves players sometimes teleporting into walls due to floating-point errors when resizing the hitbox. The maintainer suggests transitioning to fixed-point arithmetic as a potential solution.

## Explanation
The problem arises from floating-point precision issues during hitbox resizing, causing collisions with floor blocks. The maintainer proposes switching to fixed-point arithmetic to mitigate these errors. This change aims to improve accuracy and prevent unintended teleportation into walls.

## Related Questions
- What are the potential benefits of using fixed-point arithmetic over floating-point in this scenario?
- How might transitioning to fixed-point affect performance in the game?
- Are there any known limitations or trade-offs associated with fixed-point arithmetic?
- Can you provide examples of other games that use fixed-point arithmetic for collision detection?
- What steps should be taken to ensure a smooth transition from floating-point to fixed-point calculations?
- How can we test the effectiveness of this change in preventing teleportation into walls?

*Source: unknown | chunk_id: github_issue_1769_discussion*
