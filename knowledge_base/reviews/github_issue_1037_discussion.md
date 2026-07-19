# [issues/issue_1037.md] - Issue #1037 discussion

**Type:** review
**Keywords:** dynamic friction, consistent deceleration, realistic sliding, accessories, spiky boots
**Concepts:** dynamic friction, player movement physics

## Summary
Discussion about implementing dynamic friction to make player sliding more realistic based on speed.

## Explanation
The discussion revolves around the issue of consistent deceleration times for players regardless of their speed when hitting blocks. The maintainer notes that currently, no matter what speed a player hits a block at (whether walking or hyper flying), it will always slow down after exactly 4 seconds. This behavior is proposed to be changed by introducing dynamic friction, which would adjust the deceleration rate based on the player's velocity. Additionally, this change aims to make sliding more realistic and introduces the possibility of reviving old behaviors through accessories like spiky boots that could negate or modify this new dynamic friction.

## Related Questions
- What is the current behavior of player deceleration when hitting blocks?
- How does dynamic friction aim to improve this behavior?
- Can you explain how accessories like spiky boots could be used to revive old behaviors?

*Source: unknown | chunk_id: github_issue_1037_discussion*
