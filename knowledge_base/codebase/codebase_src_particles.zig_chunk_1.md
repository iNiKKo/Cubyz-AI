# [hard/codebase_src_particles.zig] - Chunk 1

**Type:** implementation
**Keywords:** SSBO, texture array, random range, image processing, hashmap
**Symbols:** ParticleManager, ParticleManager.particleTypesSSBO, ParticleManager.types, ParticleManager.typesLocal, ParticleManager.textures, ParticleManager.emissionTextures, ParticleManager.textureArray, ParticleManager.emissionTextureArray, ParticleManager.ParticleIndex, ParticleManager.particleTypeHashmap, ParticleManager.init, ParticleManager.deinit, ParticleManager.reset, ParticleManager.register, ParticleManager.readTextureDataAndParticleType, ParticleManager.readTexture, ParticleManager.createAnimationFrames, ParticleManager.extractAnimationSlice, ParticleManager.generateTextureArray
**Concepts:** particle system, texture management, error handling, animation frames

## Summary
The `ParticleManager` struct manages particle types and textures, initializing, deinitializing, resetting, and registering particles. It reads texture data, handles errors, and generates texture arrays.

## Explanation
The `ParticleManager` struct is a crucial component in managing particle types and textures within a game engine. It includes several key fields such as `particleTypesSSBO`, which is an SSBO used to store particle type data; `types`, a list of `ParticleType`; `typesLocal`, a list of `ParticleTypeLocal` containing local properties for each particle type; `textures`, a list of base textures; `emissionTextures`, a list of emission textures; `textureArray`, a texture array for base textures; `emissionTextureArray`, a texture array for emission textures; `ParticleIndex`, a type alias for `u16` used as an index for particle types; and `particleTypeHashmap`, a hashmap that maps particle type IDs to their indices. The methods of the `ParticleManager` struct include `init`, which initializes the texture arrays, SSBO, and particle system; `deinit`, which deinitializes these components; `reset`, which resets the particle types and textures; `register`, which registers new particle types by reading texture data and parsing configuration from a ZonElement; `readTextureDataAndParticleType`, which reads base and emission textures, checks for errors, and creates animation frames; `readTexture`, which reads a texture file from the specified path or uses a default image if the file is not found; `createAnimationFrames`, which creates animation frames from a texture; `extractAnimationSlice`, which extracts a specific frame from an animated texture; and `generateTextureArray`, which generates texture arrays for both base and emission textures and binds the particle types SSBO. Errors are logged if required fields are missing or if texture dimensions are incorrect.

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
- What is the purpose of each field in the `ParticleManager` struct?
- How does the `init` method initialize the `ParticleManager`?
- What steps are involved in registering a new particle type using the `register` method?
- How are errors handled during the registration process of particle types?
- What is the role of the `readTextureDataAndParticleType` function in processing textures for particles?
- How does the `generateTextureArray` method generate texture arrays for both base and emission textures?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_1*
