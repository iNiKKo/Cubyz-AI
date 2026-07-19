# [hard/codebase_src_particles.zig] - Chunk 2

**Type:** implementation
**Keywords:** mutex locking, OpenGL rendering, dynamic buffer, randomization, collision handling
**Symbols:** ParticleSystem, ParticleSystem.maxCapacity, ParticleSystem.particleCount, ParticleSystem.particles, ParticleSystem.particlesLocal, ParticleSystem.previousPlayerPos, ParticleSystem.mutex, ParticleSystem.networkCreationQueue, ParticleSystem.particlesSSBO, ParticleSystem.pipeline, ParticleSystem.UniformStruct, ParticleSystem.uniforms
**Concepts:** particle system, graphics pipeline, collision detection, networking

## Summary
The ParticleSystem struct manages particle creation, updating, and rendering in the Cubyz engine.

## Explanation
The ParticleSystem struct manages particle creation, updating, and rendering in the Cubyz engine. It initializes a graphics pipeline with shaders located at 'assets/cubyz/shaders/particles/particles.vert' and 'assets/cubyz/shaders/particles/particles.frag'. The pipeline is configured with depth testing enabled and no blending attachments. An SSBO (Shader Storage Buffer Object) is created with a dynamic buffer of size `maxCapacity` (524288), which holds particle data. The system uses a mutex to synchronize access to the network creation queue, ensuring thread safety when adding particles from network messages.

The update method processes each particle's movement, collision detection, and lifetime. Particles are added through the addParticle method, where their initial properties such as position, rotation, velocity, density, drag coefficient, and collision status are set based on random values and emitter settings. The render method binds necessary textures and draws particles using OpenGL commands, applying a billboard transformation to align particles with the camera.

The ParticleSystem also manages a network creation queue to handle particle spawning from network messages. This ensures that particles can be synchronized across different clients in a multiplayer environment.

The UniformStruct contains several fields: projectionAndViewMatrix (a Mat4f), billboardMatrix (a Mat4f), and ambientLight (a Vec3f). The addParticle method sets properties like lifeTime, density, rot, rotVel, dragCoeff, and collides based on random values and emitter settings.

Collision detection is handled by checking if a particle intersects with other objects in the environment. If a collision is detected, the particle's velocity and position are adjusted accordingly. The system uses a mutex to ensure thread safety when accessing shared resources like the network creation queue.

## Code Example
```zig
fn init() void {
		pipeline = graphics.Pipeline.init(
			"assets/cubyz/shaders/particles/particles.vert",
			"assets/cubyz/shaders/particles/particles.frag",
			"",
			&uniforms,
			graphics.VertexArray.EmptyVertex,
			&.{},
			.{},
			.{.depthTest = true, .depthWrite = true},
			.{.attachments = &.{.noBlending}},
		);

		particlesSSBO = SSBO.init();
		particlesSSBO.createDynamicBuffer(Particle, maxCapacity);
		particlesSSBO.bind(13);
	}
```

## Related Questions
-  How does the ParticleSystem handle particle collisions?
-  What is the role of the mutex in the ParticleSystem?
-  How are particles added to the system from network messages?
-  Can you explain the process of rendering particles in the ParticleSystem?
-  What determines the lifetime of a particle in the ParticleSystem? How is it randomized if necessary?
-  How does the ParticleSystem manage its internal state, such as particle count and SSBO buffer?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_2*
