# [src/particles.zig] - Chunk 2071284377

**Type:** review
**Keywords:** particle, buffer, allocation, cache, locality, optimization, heterogeneous, SSBO, update, memory, performance, refactor, GPU
**Symbols:** ParticleManager, ParticleSystem, ParticleType, SSBO, UniformStruct, EmmiterProperties, Particle
**Concepts:** memory locality, cache optimization, heterogeneous data structures, buffer allocation strategy, GPU compute performance, SSBO usage, refactor motivation, performance tuning

## Summary
The reviewer suggests replacing the single large particle buffer with multiple smaller buffers allocated per particle type to improve memory locality and reduce cache misses during updates.

## Explanation
In the current implementation, all particles are stored in a contiguous `[]Particle` array (`particles`) that is updated sequentially. When different particle types have vastly different lifetimes or update frequencies, this causes poor cache utilization: frequently updated particles may be evicted from cache while others sit idle. The reviewer’s concern is architectural rather than syntactic; they propose allocating distinct SSBOs (or host-side arrays) for each particle type so that the GPU/CPU can work on a smaller, more coherent subset of data at any given time. This change would require modifying `ParticleManager` to track per-type buffers and updating `ParticleSystem.update` to iterate over those separate buffers instead of one monolithic list. The motivation is performance (better cache behavior) without sacrificing correctness; it also aligns with the existing pattern of using SSBOs for GPU-side data (`particleTypesSSBO`). No regression prevention is explicitly mentioned, but splitting buffers inherently reduces the risk of a single large allocation failing or causing OOM under heavy particle counts. The refactor is driven by the observed TODO comment about optimizing updates and the reviewer’s intuition that heterogeneous lifetimes demand heterogeneous storage.

## Related Questions
- What is the current maximum capacity of the particle buffer defined in ParticleSystem?
- How are particles currently stored and iterated over during updates?
- Which SSBO bindings are used for particle data versus type metadata?
- Where is the UniformStruct defined and what uniform slots does it occupy?
- What fields does EmmiterProperties contain that affect particle motion?
- Is there any existing code that splits particles by type before rendering?
- How does ParticleManager register a new particle type and where are its textures stored?
- What is the alignment and size of the Particle struct as logged during init?
- Are there any TODO comments related to optimizing particle updates in this file?
- Which graphics module functions are imported for SSBO handling?

*Source: unknown | chunk_id: github_pr_1367_comment_2071284377*
