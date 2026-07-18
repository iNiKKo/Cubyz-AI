# [issues/issue_1728.md] - Issue #1728 discussion

**Type:** review
**Keywords:** physics refactoring, update function split, fixed frame rate, collision detection, surface properties, ECS, client-server physics, fall damage, trampoline effect, spring model
**Concepts:** modularity, fixed frame rate simulation, surface properties calculation, ECS integration, client-server architecture

## Summary
The issue proposes refactoring the physics system by splitting update functions into smaller parts, simulating physics at a fixed frame rate, and calculating surface properties on collision. It also discusses the integration of ECS, client-server physics handling, and potential improvements for fall damage calculations.

## Explanation
The current physics system is described as chaotic with poor interaction between different effects like climbing, friction, bounciness, and collision. The proposed changes aim to improve modularity by splitting the update function into smaller functions, ensuring consistent simulation through a fixed frame rate, and calculating surface properties only during collisions to optimize performance. The discussion also touches on the role of ECS in this system, with the maintainer emphasizing that the core physics logic should be separate from ECS but callable by it. There is also a debate about whether physics should be handled client-side or server-side, with concerns about client performance and cheating. The issue concludes with suggestions for improving fall damage calculations, such as treating blocks as springs to reduce impact energy.

## Related Questions
- How does the proposed fixed frame rate simulation improve the consistency of physics calculations?
- What are the potential performance implications of calculating surface properties only during collisions?
- How would integrating ECS with the refactored physics system affect maintainability and scalability?
- What are the security concerns associated with client-side physics handling in multiplayer environments?
- How could treating blocks as springs reduce fall damage, and what challenges might this approach present?
- What is the rationale behind splitting the update function into smaller parts, and how does this enhance understandability?
- How would the proposed changes impact the interaction between different physics effects like climbing and friction?
- What are the potential benefits of separating core physics logic from ECS, and how should they be implemented?
- How could the spring model for fall damage calculations be integrated into the existing system without disrupting current behavior?
- What considerations should be made when deciding whether to handle physics client-side or server-side in a multiplayer game?

*Source: unknown | chunk_id: github_issue_1728_discussion*
