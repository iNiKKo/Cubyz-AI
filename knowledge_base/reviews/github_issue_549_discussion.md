# [issues/issue_549.md] - Issue #549 discussion

**Type:** review
**Keywords:** block placement, player collision, hitbox check, incorrect detection, maintainer comment
**Concepts:** collision detection, hitbox

## Summary
Issue with block placement due to player collision detection.

## Explanation
The issue arises from incorrect hitbox checks during block placement, causing the game to prevent placing blocks on sides where the player is slightly colliding. The maintainer notes that the wrong hitbox is being checked, suggesting a need to adjust the collision detection logic to accurately determine when the player can place blocks.

## Related Questions
- What is the current logic for determining if a block can be placed?
- How does the game define and use hitboxes for collision detection?
- Are there any existing tests that cover this specific issue?
- Can we identify which part of the code is responsible for checking the wrong hitbox?
- Is there a way to visualize the player's hitbox in-game to debug this issue?
- What are the implications of changing the hitbox check logic on other parts of the game?
- How can we ensure that the fix does not introduce new collision-related issues?
- Are there any similar issues reported for different types of blocks or terrain?
- Can we optimize the collision detection to improve performance without affecting accuracy?
- What is the expected behavior when a player's hitbox partially overlaps with a block?

*Source: unknown | chunk_id: github_issue_549_discussion*
