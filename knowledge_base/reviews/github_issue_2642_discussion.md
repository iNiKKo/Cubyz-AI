# [issues/issue_2642.md] - Issue #2642 discussion

**Type:** review
**Keywords:** path finding, NavMesh, A*, entity types, performance, complexity, block data, line of sight, parkour, wall jumping
**Concepts:** pathfinding, NavMesh, A*, hierarchical navigation

## Summary
The discussion revolves around implementing a pathfinding system for different types of entities in Cubyz. The main proposal is to use a hierarchical NavMesh with A*, but there are concerns about its complexity and performance, especially regarding construction and updates.

## Explanation
The discussion revolves around implementing a pathfinding system for different types of entities in Cubyz. The main proposal is to use a hierarchical NavMesh with A*, but there are concerns about its complexity and performance, especially regarding construction and updates. Specifically, the maintainer questions the cost of constructing and updating the navmesh in response to player actions like placing or breaking blocks. Additionally, there is debate about whether a NavMesh is sufficient for enabling complex behaviors such as parkour, wall jumping, or short flight. The user suggests calculating different navmeshes based on entity types and loading relevant chunks dynamically. Another proposal is to use block data directly instead of constructing a navmesh, which the maintainer considers a simpler but potentially less optimal solution. The maintainer also proposes using line-of-sight as an alternative to NavMesh for immediate pathfinding needs until a more robust system can be developed.

## Related Questions
- What are the main concerns regarding the use of a NavMesh for pathfinding in Cubyz?
- How does the hierarchical NavMesh proposal address different entity types?
- Why is there debate about whether a NavMesh is sufficient for complex behaviors like parkour?
- What alternative solutions to NavMesh have been proposed for pathfinding in Cubyz?
- How does the maintainer justify the potential waste of time on implementing a complex system like NavMesh?
- What are the trade-offs between having a perfect pathfinding system and a simpler one?

*Source: unknown | chunk_id: github_issue_2642_discussion*
