# [issues/issue_2361.md] - Issue #2361 discussion

**Type:** review
**Keywords:** jump, forward, steps, hopping, bouncing, physics engine, video
**Concepts:** player physics, input handling, movement state transitions

## Summary
The issue describes player physics behavior where holding jump and forward buttons results in inconsistent jumping up steps, including hopping twice or bouncing off solid blocks.

## Explanation
When holding the jump button while holding the forward button, the game does not smoothly jump up steps of grass or stone. Sometimes the player character hops up against the grass wall twice, and other times they get bounced off solid blocks when trying to jump up stone steps. The expected behavior is for the game to smoothly jump up steps without hopping or bouncing. The maintainer requests a video of the effect for better understanding. This problem likely stems from how the game handles input states and transitions between different movement states, such as jumping and colliding with surfaces.

## Related Questions
- What specific input states are being handled when the jump and forward buttons are held?
- How does the game determine the timing and duration of jumps in this scenario?
- Are there any known issues with collision detection that could cause bouncing off solid blocks?
- Can you provide a video demonstrating the issue for better understanding?
- What changes have been made to player physics recently that might be related to this problem?
- How does the game handle transitions between different movement states, such as jumping and colliding?

*Source: unknown | chunk_id: github_issue_2361_discussion*
