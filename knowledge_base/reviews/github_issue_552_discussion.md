# [issues/issue_552.md] - Issue #552 discussion

**Type:** review
**Keywords:** collision box, jump height, stepping, wall scaling, player physics
**Concepts:** collision detection, player movement, stepping mechanics

## Summary
The player can scale up 1.5 block walls due to collision box positioning.

## Explanation
The issue arises because the collision boxes are positioned slightly above the floor, allowing the player to step over 0.5 blocks. To prevent this, the jump height needs to be reduced below one block. This adjustment ensures that the player cannot scale up walls taller than one block by leveraging the stepping mechanism.

## Related Questions
- What is the current position of the collision boxes relative to the floor?
- How does reducing the jump height below one block prevent wall scaling?
- Are there any other mechanisms that could be adjusted to mitigate this issue?
- What impact might changing the jump height have on player gameplay experience?
- Is there a way to adjust the collision box position without affecting stepping mechanics?
- How can we ensure that the change does not introduce new bugs or unintended behavior?

*Source: unknown | chunk_id: github_issue_552_discussion*
