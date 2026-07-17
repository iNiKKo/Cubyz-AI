# [hard/codebase_src_particles.zig] - Chunk 0

**Type:** implementation
**Keywords:** SSBO, TextureArray, Image, StringHashMapUnmanaged, worldArena, stackAllocator, openGl orientation, frame count validation, particle type registration, emission texture
**Symbols:** ParticleManager, ParticleManager.init, ParticleManager.deinit, ParticleManager.reset, ParticleManager.register, readTextureDataAndParticleType, readTexture, createAnimationFrames, extractAnimationSlice
**Concepts:** particle system management, texture loading, animation frame extraction, ZON configuration parsing, asset path resolution, error logging

## Summary
Manages particle system assets, types, and textures with initialization, registration from ZON files, texture reading, animation frame extraction, and cleanup.

## Explanation
The chunk defines a public ParticleManager struct that holds SSBOs for particle types, lists of ParticleType/ParticleTypeLocal, Image lists for base/emission textures, TextureArray instances, and a StringHashMapUnmanaged keyed by particle ID to an index. It exposes init() which creates the texture arrays and calls ParticleSystem.init(), deinit() which frees all allocated resources including calling ParticleSystem.deinit(), and reset() which clears all lists and maps and resets ParticleSystem. The register(pub fn) method reads a ZON element for a particle, extracts its texture ID via zon.get("texture"), logs an error if missing, then calls readTextureDataAndParticleType to load the base PNG and optional emission PNG (suffix "_emission.png"). It parses rotation velocity from zon.getChild("rotationVelocity") with defaults 20-60 degrees converted to radians, density from zon.getChild("density") defaulting 2-3, drag coefficient from zon.getChild("dragCoefficient") defaulting 0.5-0.6, and loopTime from zon.getChild("loopTime"). It builds a ParticleTypeLocal struct with these fields, inserts the particle ID into particleTypeHashmap using main.worldArena allocator (catch unreachable), appends the type to types and typesLocal lists, and logs debug output. The private readTextureDataAndParticleType function computes frame counts from texture dimensions (height/width), sets typ.frameCount, typ.startFrame based on current textures.items.len, and typ.size as base.width/16. It validates that base height is a multiple of width, emission height is a multiple of width if present, and that both textures share the same frame count; any violation logs an error with dimensions and assetsFolder/id and sets corresponding broken flags. It then calls createAnimationFrames for the base texture list (passing isBaseBroken) and for the emission texture list (passing isBaseBroken or isEmissionBroken or !hasEmission). The readTexture private function splits textureId on ':' to get mod:id, constructs two paths: worldAssetsPath = "{assetsFolder}/{mod}/particles/textures/{id}{suffix}" and gameAssetsPath = "assets/{mod}/particles/textures/{id}{suffix}", allocates them via main.stackAllocator (defer free), then attempts graphics.Image.readFromFile on worldAssetsPath with .openGl orientation; if that fails it falls back to gameAssetsPath, also readFromFile with .openGl; if both fail and status is .isMandatory it logs an error and returns the default image, otherwise returns whatever was loaded. createAnimationFrames iterates 0..frameCount, appending either the original image (if isBroken) or extractAnimationSlice(image,i). The private extractAnimationSlice computes frameHeight = image.height/frameCount, startHeight = frameHeight*frameIndex, endHeight = frameHeight*(frameIndex+1), copies result.imageData from [startHeight*width .. endHeight*width], and truncates height to frameHeight. All allocations use main.worldArena or main.stackAllocator as appropriate; no concurrency primitives are used here.

## Related Questions
- What are the required ZON fields for registering a particle type?
- How does ParticleManager handle missing or invalid texture files during initialization?
- Which allocator is used for inserting entries into particleTypeHashmap in register?
- What default values are applied when rotationVelocity, density, dragCoefficient, or loopTime are absent from the ZON element?
- Under what conditions does createAnimationFrames receive a broken image versus an original one?
- How is the frame count derived from texture dimensions and why must height be a multiple of width?
- What happens if both base and emission textures fail to load in readTextureDataAndParticleType?
- Does ParticleManager perform any synchronization or locking around its mutable state?
- Where are the paths for world assets versus game assets constructed relative to assetsFolder and textureId?
- How does extractAnimationSlice compute startHeight and endHeight from frameIndex?

*Source: unknown | chunk_id: codebase_src_particles.zig_chunk_0*
