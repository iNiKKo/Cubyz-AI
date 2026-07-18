# [issues/issue_2760.md] - Issue #2760 discussion

**Type:** review
**Keywords:** entity component, player-specific, ECS, separation, confusion, development state
**Symbols:** playerIndex, zon
**Concepts:** Entity Component System (ECS), Separation of Concerns

## Summary
The discussion revolves around the introduction of a player-specific entity component in Cubyz. The initial pull request (#2660) added a `playerIndex` entry to the entity description, but it was noted that this should be its own component for clarity and separation.

## Explanation
The reviewer points out that while PR #2660 introduced a `playerIndex` field in the entity description, this change is not sufficient. The concern is that having player-specific data mixed with general entity data can lead to confusion and potential issues in the future. The reviewer suggests that this should be addressed when the ECS (Entity Component System) is more developed, implying that the current state of the ECS does not support or necessitate such a separation.

## Related Questions
- What is the current status of the ECS system in Cubyz?
- Why was the `playerIndex` entry added to the entity description?
- How does the introduction of a player-specific component improve code clarity?
- Are there any potential performance implications from separating player components?
- What other changes are needed for the ECS to support this separation?
- How will this change affect existing entities and their descriptions?
- Is there a timeline for when the ECS system will be more developed?
- What are the benefits of having separate entity components for different types of entities?
- How does this change align with the overall architecture of Cubyz?
- Are there any backward compatibility concerns with this change?

*Source: unknown | chunk_id: github_issue_2760_discussion*
