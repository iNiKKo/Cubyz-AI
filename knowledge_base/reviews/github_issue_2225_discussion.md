# [issues/issue_2225.md] - Issue #2225 discussion

**Type:** review
**Keywords:** player speed, jump height, movement speed, XY direction, crouch key, momentum retention, video demonstration
**Concepts:** physics engine, player movement, jumping behavior

## Summary
Discusses inconsistencies and potential bugs in the physics engine related to player movement and jumping behavior.

## Explanation
The discussion revolves around several issues with the physics engine in Cubyz, including how player speed affects jump height (specifically mentioning that high enough speeds can allow the player to fly), the impact of holding the jump key on movement speed, inconsistent jump heights when moving in an XY direction, and faster falling while crouching. The maintainer acknowledges some points as intended features but requests video demonstrations for better understanding. For instance, the player's speed influences jump height such that high enough speeds can allow flying, which is intended behavior. Holding the jump key lowers movement speed, and this is also an intended feature. Inconsistent jump heights when moving in an XY direction are noted, with the maintainer suggesting it is a common issue in voxel games. Faster falling while crouching is another acknowledged feature. Momentum retention during jumping is intended behavior, as mentioned by the maintainer. The user comments also discuss issues like movement being retained while jumping and the difficulty of judging where the player will stop due to momentum. The maintainer suggests not sprint-jumping and advises opening a new issue for unrelated concerns.

## Related Questions
- What is the intended behavior of player movement while jumping in Cubyz?
- How does the physics engine handle momentum retention during jumps?
- Can you provide a video demonstrating the issue with inconsistent jump heights when moving in an XY direction?
- Is there a plan to address the faster falling speed while crouching in future updates?
- What is the rationale behind allowing high speeds to influence jump height and potentially allow flying?
- Why is holding the jump key supposed to lower movement speed?
- How does Cubyz handle player input during jumps, particularly when sprinting?
- Are there any plans to change the behavior of momentum retention during jumping in future versions?
- What is the intended use case for the crouch key in relation to falling speed?
- Can you provide a video demonstrating the issue with high speeds influencing jump height and potentially allowing flying?

*Source: unknown | chunk_id: github_issue_2225_discussion*
