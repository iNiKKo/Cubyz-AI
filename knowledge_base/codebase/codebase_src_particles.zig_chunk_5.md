# [hard/codebase_src_particles.zig] - Chunk 5

**Type:** implementation
**Keywords:** struct, extern, random range, alignment, collision detection
**Symbols:** ParticleTypeLocal, ParticleTypeLocal.density, ParticleTypeLocal.rotVel, ParticleTypeLocal.dragCoefficient, ParticleTypeLocal.loopTime, Particle, Particle.pos, Particle.rot, Particle.currentFrame, Particle.light, Particle.typ, ParticleLocal, ParticleLocal.velAndRotationVel, ParticleLocal.frameRate, ParticleLocal.density, ParticleLocal.dragCoefficient, ParticleLocal.collides
**Concepts:** particle system, particle properties, particle state

## Summary
Defines particle types and structures for the Cubyz engine.

## Explanation
This chunk defines several structs related to particles in the Cubyz engine. `ParticleTypeLocal` contains properties like density, rotational velocity, drag coefficient, and loop time, each with a random range. `Particle` is an externally aligned struct representing individual particle data including position, rotation, current frame, light intensity, type identifier, and reserved space. `ParticleLocal` holds additional local state for particles such as velocity, rotation velocity, frame rate, density, drag coefficient, and collision status.

## Related Questions
- What are the fields in the ParticleTypeLocal struct?
- How is the Particle struct aligned?
- What additional state does the ParticleLocal struct hold?
- Can a particle have a loop time defined?
- What is the purpose of the reserved space in the Particle struct?
- How is the density property defined for particles?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_5*
