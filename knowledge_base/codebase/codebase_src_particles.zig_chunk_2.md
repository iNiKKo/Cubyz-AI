# [hard/codebase_src_particles.zig] - Chunk 2

**Type:** implementation
**Keywords:** gravity, drag coefficient, collision box, bit packing, SSBO, uniform upload, mutex locking, random seed, ZON parsing, frame rate control
**Symbols:** particle, physics, collision, rendering, networking, configuration, randomization
**Concepts:** particle physics integration, drag and gravity simulation, player-bound collision resolution, compressed lighting encoding, SSBO particle rendering, billboard matrix construction, networked emitter queue

## Summary
This chunk defines the particle system's physics integration loop (gravity, drag, collision resolution against player bounds), particle spawning via addParticle with seeded lifetime/rotation/drag properties, GPU rendering pipeline using SSBOs and billboard matrices, networked emitter creation queue protected by a mutex, and EmitterProperties configuration parsed from ZON files.

## Explanation
The chunk contains the main update loop that computes effective gravity based on air density, applies exponential drag via @exp, and handles collisions: when collides is true it transforms world position to player-relative coordinates, builds a hitBox sized by ParticleManager.types.items[particle.typ].size, calls physics.collision.collides for each axis with epsilon adjustments, then converts back to local space. When not colliding it simply adds velocity delta plus prevPlayerPosDifference. After the loop particle.pos and particle.rot are stored, rotVel is written into velAndRotationVel[3], lighting is compressed from a 6‑byte array via bit shifts (>>3) and packed into a u32, then i increments. The addParticle function seeds lifetime, density, rotation (either random or zero), drag coefficient, computes loopTime as lifeTime divided by optional loopTime field (or just lifeTime), creates a Particle with pos offset by previousPlayerPos cast to Vec3d, sets currentFrame based on frameCount, and initializes ParticleLocal with combined velocity/rotation vector, density, dragCoefficient, collides flag, and increments particleCount. The render function binds particlesSSBO.bufferSubData with the Particle struct, disables pipeline binding, multiplies projectionMatrix by viewMatrix translated by -game.Player.getEyePosBlocking() plus previousPlayerPos cast to Vec3d, uploads both matrices as uniforms, sets ambientLight uniform, builds a billboard matrix from camera rotation (rotationZ(-rot[2]+π/2) * rotationY(rot[0]-π/2)), binds texture arrays for emission and mesh storage, binds chunk_meshing.vao, computes maxQuads from chunk_meshing.maxQuadsInIndexBuffer, divides particleCount by maxQuads with std.math.divCeil (catch unreachable), then loops over batches drawing GL_TRIANGLES with glDrawElementsBaseVertex using the computed offset. getParticleCount simply returns particleCount. addParticlesFromNetwork acquires mutex.lock(), defers unlock, and appends a networkCreationQueue entry containing emitter, pos, count into main.worldArena. EmitterProperties is a struct with speed (RandomRange<f32>), lifeTime (RandomRange<f32>), randomizeRotation (bool); its parse method reads zon.getChild(

## Related Questions
- How is effective gravity computed for a particle given air density and baseGravity?
- What happens to a particle's position when it collides with the player bounds versus when it does not collide?
- Describe the exact steps taken inside addParticle to initialize lifetime, rotation, and drag coefficient using seeded random values.
- How is lighting data compressed into a single u32 for storage in each particle?
- What matrix operations are performed on viewMatrix before uploading it as a uniform during render?
- Explain how the billboard matrix is constructed from camera rotation components.
- Why does addParticlesFromNetwork use mutex.lock() and defer unlock(), and where is the queued data stored?
- How does EmitterProperties.parse handle missing ZON children for speed, lifeTime, or randomRotate?
- What role does chunk_meshing.maxQuadsInIndexBuffer play in determining draw batch sizes?
- Is there any handling of particle loopTime when it is present versus absent in the addParticle logic?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_2*
