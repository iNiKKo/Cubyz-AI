# [hard/codebase_src_particles.zig] - Chunk 2

**Type:** implementation
**Keywords:** mutex locking, OpenGL rendering, dynamic buffer, randomization, collision handling
**Symbols:** ParticleSystem, ParticleSystem.maxCapacity, ParticleSystem.particleCount, ParticleSystem.particles, ParticleSystem.particlesLocal, ParticleSystem.previousPlayerPos, ParticleSystem.mutex, ParticleSystem.networkCreationQueue, ParticleSystem.particlesSSBO, ParticleSystem.pipeline, ParticleSystem.UniformStruct, ParticleSystem.uniforms
**Concepts:** particle system, graphics pipeline, collision detection, networking

## Summary
The ParticleSystem struct manages particle creation, updating, and rendering in the Cubyz engine.

## Explanation
The ParticleSystem struct handles the lifecycle of particles within the game. It initializes a graphics pipeline and an SSBO for dynamic buffer management. The update method processes each particle's movement, collision detection, and lifetime. Particles are added through the addParticle method, which sets their initial properties based on random values and emitter settings. The render method binds necessary textures and draws particles using OpenGL commands. The system also manages a network creation queue to handle particle spawning from network messages.

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
- How does the ParticleSystem handle particle collisions?
- What is the role of the mutex in the ParticleSystem?
- How are particles added to the system from network messages?
- Can you explain the process of rendering particles in the ParticleSystem?
- What determines the lifetime of a particle in the ParticleSystem? How is it randomized if necessary?
- How does the ParticleSystem manage its internal state, such as particle count and SSBO buffer?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_2*
