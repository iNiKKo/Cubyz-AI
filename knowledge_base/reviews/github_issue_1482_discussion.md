# [issues/issue_1482.md] - Issue #1482 discussion

**Type:** review
**Keywords:** Pawn, attack mode, player, pathfinding, obstacles, gaps, maintainer, dedicated test entity
**Concepts:** behavior, pathfinding, test entity

## Summary
Discussion about creating a 'Pawn' test entity for basic behavior and pathfinding.

## Explanation
The issue proposes the creation of a 'Pawn' entity to serve as a basic testing tool for behavior and pathfinding. The entity would have specific behaviors such as entering attack mode when it sees the player, walking towards the player while avoiding obstacles, jumping over gaps, and exiting attack mode if the player is far enough away. Additionally, the note mentions that the 'Pawn' does not have eyes on the back of its head, meaning it must be looking at you to spot you. The maintainer suggests that a dedicated test entity might not be necessary for this purpose.

## Related Questions
- What are the specific behaviors of the 'Pawn' test entity?
- Why does the maintainer think a dedicated test entity might not be necessary?
- How does the 'Pawn' entity handle obstacles and gaps in its pathfinding?
- Under what conditions does the 'Pawn' exit attack mode?
- Is there any mention of additional features or limitations for the 'Pawn' entity?
- What is the purpose of having a test entity like 'Pawn' in the development process?

*Source: unknown | chunk_id: github_issue_1482_discussion*
