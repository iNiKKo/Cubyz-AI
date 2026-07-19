# [issues/issue_549.md] - Issue #549 discussion

**Type:** review
**Keywords:** block placement, player collision, hitbox check, incorrect detection, maintainer comment
**Concepts:** collision detection, hitbox

## Summary
Issue with block placement due to player collision detection.

## Explanation
Issue with block placement due to player collision detection. The problem occurs when the game incorrectly checks the wrong hitbox, leading to a situation where placing blocks on sides of blocks you are walking into is prevented because the player's hitbox slightly overlaps or goes through corners of adjacent blocks. This issue persists even after stopping movement. Users have reported that the player’s hitbox can still be inside the block, causing placement restrictions. The maintainer confirmed that the game checks an incorrect hitbox during block placement, necessitating adjustments to collision detection logic.

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

*Source: unknown | chunk_id: github_issue_549_discussion*
