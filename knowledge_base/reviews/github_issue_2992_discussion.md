# [issues/issue_2992.md] - Issue #2992 discussion

**Type:** review
**Keywords:** physics, entity system, non-player entities, server-side, cheat protection, sync system, item drops, projectiles, particles
**Symbols:** EntityComponent, EntitySystem, ECS
**Concepts:** Entity Component System (ECS), server-side physics, cheat protection, synchronization

## Summary
The issue proposes generalizing the physics code into an Entity System to allow non-player entities to experience physics and introduces server-side physics for cheat protection.

## Explanation
The discussion notes that while the physics implementation should remain separate from the ECS (Entity Component System) due to its necessity for item drops, projectiles, and particles, server-side physics verification is approved. This implies that player position changes will need to be synchronized through a sync system to ensure consistency between client and server.

## Related Questions
- How does the physics implementation remain separate from the ECS while still being used for item drops, projectiles, and particles?
- What specific changes are needed to sync player position changes through the sync system?
- How will server-side physics verification prevent cheating in the game?
- Can you explain the benefits of generalizing the physics code into an Entity System?
- What potential issues might arise from integrating server-side physics with the existing client-side prediction?
- How does the ECS architecture facilitate the addition of server-side physics?
- Are there any performance considerations when implementing server-side physics verification?
- What steps are necessary to ensure backward compatibility with existing physics implementations?
- How will the sync system handle discrepancies between client and server positions during gameplay?
- Can you provide a detailed plan for integrating server-side physics into the current architecture?

*Source: unknown | chunk_id: github_issue_2992_discussion*
