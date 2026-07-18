# [hard/codebase_src_particles.zig] - Chunk 1

**Type:** implementation
**Keywords:** SSBO, texture array, random range, image processing, hashmap
**Symbols:** ParticleManager, ParticleManager.particleTypesSSBO, ParticleManager.types, ParticleManager.typesLocal, ParticleManager.textures, ParticleManager.emissionTextures, ParticleManager.textureArray, ParticleManager.emissionTextureArray, ParticleManager.ParticleIndex, ParticleManager.particleTypeHashmap, ParticleManager.init, ParticleManager.deinit, ParticleManager.reset, ParticleManager.register, ParticleManager.readTextureDataAndParticleType, ParticleManager.readTexture, ParticleManager.createAnimationFrames, ParticleManager.extractAnimationSlice, ParticleManager.generateTextureArray
**Concepts:** particle system, texture management, error handling, animation frames

## Summary
The `ParticleManager` struct manages particle types and textures, initializing, deinitializing, resetting, and registering particles. It reads texture data, handles errors, and generates texture arrays.

## Explanation
The `ParticleManager` struct is responsible for managing particle types and their associated textures. It includes methods to initialize (`init`), deinitialize (`deinit`), and reset (`reset`) the particle system. The `register` method registers new particle types by reading texture data and parsing configuration from a ZonElement. Errors are logged if required fields are missing or if texture dimensions are incorrect. The `readTextureDataAndParticleType` function reads base and emission textures, checks for errors, and creates animation frames. The `generateTextureArray` method generates texture arrays for both base and emission textures and binds the particle types SSBO.

## Code Example
```zig
pub fn init() void {
	textureArray = .init();
	emissionTextureArray = .init();
	particleTypesSSBO = SSBO.init();
	ParticleSystem.init();
}
```

## Related Questions
- How does the `ParticleManager` initialize its components?
- What is the purpose of the `register` method in `ParticleManager`?
- How are errors handled when registering particle types?
- What steps are involved in generating texture arrays for particles?
- How does the `readTextureDataAndParticleType` function process textures?
- What is the role of the `particleTypesSSBO` buffer in the particle system?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_1*
