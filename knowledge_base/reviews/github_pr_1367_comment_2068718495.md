# [src/particles.zig] - Chunk 2068718495

**Type:** review
**Keywords:** ParticleSystem, Emitter, refactor, separate struct, shape implementation, architectural review, modularity, coupling, maintainability, clean code
**Symbols:** ParticleSystem, ParticleType, EmmiterProperties, EmmiterShape
**Concepts:** architectural separation of concerns, modularity, refactoring, code coupling reduction, maintainability

## Summary
Reviewers suggest refactoring particle emission logic by extracting Emitter-related parameters and shape-specific implementations from the ParticleSystem struct into a dedicated emitter struct to improve architectural separation of concerns.

## Explanation
The current codebase mixes high-level particle system management (particle arrays, shader uniforms, collision handling) with low-level emitter behavior (shape definitions, spawn logic). Reviewers argue that this violates clean architecture principles: the ParticleSystem should only manage state and rendering, while emission details belong in a separate Emitter struct. This separation will make the codebase more modular, easier to test, and allow future extensions (e.g., new particle types) without bloating the core system. Additionally, moving shape implementations out of ParticleSystem reduces coupling and potential regression risks when modifying collision or update logic.

## Related Questions
- What are the current fields in ParticleSystem that relate to emitter behavior?
- Which functions in particles.zig handle particle spawning logic?
- Are there any existing Emitter structs defined elsewhere in the codebase?
- How is EmmiterProperties currently used within ParticleSystem?
- What shape-related data structures are embedded in ParticleSystem?
- Does ParticleSystem contain any collision handling specific to emitters?
- Where are particle type definitions stored relative to emission logic?
- Is there a separation between update and spawn responsibilities in the current design?
- How does the reviewer define 'bulk of this function' in context of Emitter parameters?
- What would be the minimal interface for an extracted Emitter struct?

*Source: unknown | chunk_id: github_pr_1367_comment_2068718495*
