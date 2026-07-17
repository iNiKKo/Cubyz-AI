# [hard/codebase_src_particles.zig] - Chunk 1

**Type:** implementation
**Keywords:** particle system, network creation queue, mutex locking, SSBO buffer binding, air friction, collision resolution, texture loading fallback, animation frame extraction, delta time integration, player bounding box
**Symbols:** ParticleSystem, ParticleSystem.maxCapacity, ParticleSystem.particleCount, ParticleSystem.particles, ParticleSystem.particlesLocal, ParticleSystem.previousPlayerPos, ParticleSystem.mutex, ParticleSystem.networkCreationQueue, ParticleSystem.particlesSSBO, ParticleSystem.pipeline, UniformStruct, UniformStruct.projectionAndViewMatrix, UniformStruct.billboardMatrix, UniformStruct.ambientLight, ParticleSystem.uniforms, ParticleSystem.init, ParticleSystem.deinit, ParticleSystem.reset, ParticleSystem.update, generateTextureArray, createAnimationFrames, extractAnimationSlice
**Concepts:** particle system lifecycle, networked particle creation queue, per-particle motion integration, air friction and gravity simulation, collision resolution with player bounding box, texture loading fallback chain, animation frame extraction from sprite sheets

## Summary
This chunk defines the ParticleSystem struct and its lifecycle methods (init, deinit, reset) along with particle update logic that handles networked creation queues, per-particle motion integration, air friction, gravity, collision resolution against player bounding boxes, and texture loading for particle sprites.

## Explanation
The chunk declares a top-level const ParticleSystem struct containing several fields: maxCapacity (u32), particleCount (u32), particles array of type [maxCapacity]Particle, particlesLocal array of type [maxCapacity]ParticleLocal, previousPlayerPos (Vec3i), mutex (main.utils.Mutex), networkCreationQueue (List of {emitter, pos, count}), particlesSSBO (SSBO), pipeline (graphics.Pipeline), and uniforms (UniformStruct). The UniformStruct is defined inline with fields projectionAndViewMatrix, billboardMatrix, ambientLight. Inside the struct, init() creates a graphics.Pipeline using shaders from assets/cubyz/shaders/particles/..., binds SSBO buffer for Particle type at slot 13, and initializes particlesSSBO as a dynamic buffer of maxCapacity. deinit() frees pipeline and particlesSSBO. reset() clears networkCreationQueue to empty. update(deltaTime) locks the mutex, processes any queued particle creations from network (iterates over items, calls creation.emitter.spawnParticles with pos and count, then clears queue), unlocks mutex, computes player eye position as Vec3i via game.Player.getEyePosBlocking(), converts previousPlayerPos difference to float, then iterates particles by index i while i < particleCount. For each particle it reads currentFrame from the particle struct and frameRate from particlesLocal; subtracts deltaTime scaled by frameRate; if currentFrame drops below zero it removes that particle (decrements particleCount, shifts remaining entries left). Otherwise it computes position delta using velAndRotationVel[3] as rotation velocity, updates rot. It applies air friction: reads physics.airDensity, computes effective gravity based on baseGravity and playerAirTerminalVelocity, zeroes the rotation velocity component, subtracts effective gravity scaled by deltaTime to vertical velocity, then multiplies all velocities by exp(-frictionCoefficient*deltaTime). If particleLocal.collides is true it constructs a hitBox sized from ParticleManager.types.items[particle.typ].size (scaled -0.5..+0.5), computes v3Pos as playerPos plus offset and previousPlayerPosDifference, then applies collision resolution along X and Y axes using physics.collision.collides with .client side; if colliding it clamps the position to just inside the box bounds using epsilon offsets. The chunk also defines helper functions outside the struct: generateTextureArray() which calls textureArray.generate on textures.items (with isBroken=true, isMandatory=true) and emissionTextureArray.generate (isBroken=true, isMandatory=false), then binds particleTypesSSBO buffer at slot 14; createAnimationFrames(container, frameCount, image, isBroken) loops over frames appending either the original image or extractAnimationSlice(image, i); extractAnimationSlice computes frameHeight from image.height/frameCount, slices imageData vertically and returns a new Image with reduced height. The chunk includes texture loading logic: split textureId by ':' to get mod and id, construct gameAssetsPath and worldAssetsPath using main.stackAllocator (with defer frees), then call graphics.Image.readFromFile on worldAssetsPath first; if that fails it falls back to gameAssetsPath; if both fail it logs an error via std.log.err with paths and returns default. The chunk references external types: Particle, ParticleLocal, SSBO, Vec3i, Vec3d, Vec4f, Image, Emitter, physics.collision.Box, physics.airDensity, physics.baseGravity, physics.playerAirTerminalVelocity, physics.epsilon, game.Player.getEyePosBlocking(), main.List, main.utils.Mutex, graphics.Pipeline, graphics.VertexArray.EmptyVertex, ParticleManager.types.items, textureArray, emissionTextureArray, particleTypesSSBO. All these are used as fields or parameters within the struct's methods.

## Code Example
```zig
fn extractAnimationSlice(image: Image, frameIndex: usize) Image {
	const frameCount = image.height/image.width;
	const frameHeight = image.height/frameCount;
	const startHeight = frameHeight*frameIndex;
	const endHeight = frameHeight*(frameIndex + 1);
	var result = image;
	result.height = @intCast(frameHeight);
	result.imageData = result.imageData[startHeight*image.width .. endHeight*image.width];
	return result;
}
```

## Related Questions
- How does the particle system handle networked creation requests?
- What is the maximum capacity of the particle array and how is it enforced?
- Describe the sequence of operations in ParticleSystem.init().
- How are animation frames extracted from a sprite sheet image?
- What happens when a particle's currentFrame drops below zero during update?
- Explain the air friction calculation for particles.
- How does collision resolution clamp a particle against the player bounding box?
- Where are particle texture files loaded from and what fallback is used?
- What role does the mutex play in ParticleSystem.update()?
- How is the SSBO buffer bound to the graphics pipeline?
- What fields does UniformStruct contain and how are they used?
- Describe the difference between particles and particlesLocal arrays.

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_1*
