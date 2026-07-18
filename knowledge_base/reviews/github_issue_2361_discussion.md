# [issues/issue_2361.md] - Issue #2361 discussion

**Type:** review
**Keywords:** jump, forward, steps, hopping, bouncing, physics engine, video
**Concepts:** player physics, input handling, movement state transitions

## Summary
The issue describes player physics behavior where holding jump and forward buttons results in inconsistent jumping up steps, including hopping twice or bouncing off solid blocks.

## Explanation
The reported issue involves inconsistencies in the player's movement physics when both jump and forward inputs are held simultaneously. The maintainer requests a video to better understand the specific actions causing these issues. The problem likely stems from how the game handles input states and transitions between different movement states, such as jumping and colliding with surfaces.

## Related Questions
- What specific input states are being handled when the jump and forward buttons are held?
- How does the game determine the timing and duration of jumps in this scenario?
- Are there any known issues with collision detection that could cause bouncing off solid blocks?
- Can you provide a video demonstrating the issue for better understanding?
- What changes have been made to player physics recently that might be related to this problem?
- How does the game handle transitions between different movement states, such as jumping and colliding?
- Are there any configuration options or settings that could affect the player's jump behavior?
- Can you identify any potential bugs in the collision response system that might cause hopping or bouncing?
- What is the expected behavior of the player when both jump and forward inputs are held simultaneously?
- How does the game handle edge cases where the player collides with multiple surfaces while jumping?

*Source: unknown | chunk_id: github_issue_2361_discussion*
