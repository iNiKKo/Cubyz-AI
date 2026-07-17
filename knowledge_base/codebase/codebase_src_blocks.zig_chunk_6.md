# [hard/codebase_src_blocks.zig] - Chunk 6

**Type:** implementation
**Keywords:** texture loading, animation frames, block model registration, breaking animation sequences, GPU texture arrays, file path fallback, side-specific textures, compute shader dispatch, arena allocator, atomic occlusion flags
**Symbols:** findTexture, readTextureData, extractAnimationSlice, getTextureIndices, register, registerBlockBreakingAnimation, preProcessAnimationData, finishTextureLoading, reloadTextures, generateTextureArray
**Concepts:** texture loading, animation frame extraction, block model registration, breaking animation sequences, GPU texture array generation, file path fallback resolution, side-specific texture lookup, compute shader dispatch

## Summary
This chunk implements texture loading and management for the Cubyz voxel engine, including reading PNG textures from disk, extracting animation frames via slicing, registering block models with their textures, handling breaking animations, and generating GPU texture arrays.

## Explanation
The chunk defines several public functions: findTexture locates a texture by ID (splitting on ':' to get mod:id), checks if it's already in the list, attempts to open the file from an assetFolder path or falls back to a global assets path, and appends the ID and path to textureIds and texturePaths arrays. readTextureData reads a .zig.zon configuration for a texture (frames, time, fogDensity, fogColor, hasOcclusion), then loads base, emission, reflectivity, and absorption PNGs using readTextureFile, extracts each frame via extractAnimationSlice (which computes startHeight/endHeight based on image height divided by frames), and appends sliced images to blockTextures, emissionTextures, reflectivityTextures, absorptionTextures, and textureFogData. getTextureIndices reads side-specific texture IDs from a ZonElement (using sideNames for faces) and calls findTexture for each, falling back to a default index if any lookup fails. register is called when a new mesh is added; it creates a block model entry in _modelIndex using the current meshes.size as the type ID, then calls getTextureIndices for that slot, updates maxTextureCount, and increments meshes.size. registerBlockBreakingAnimation iterates over sequential PNG files under assets/cubyz/blocks/textures/breaking/, constructs IDs like cubyz:breaking/0, finds each texture, and appends to blockBreakingTextures until a missing file is encountered. preProcessAnimationData binds the animation compute pipeline, sets the time uniform, dispatches a GL compute shader with ceil division (commented TODO for @divCeil), and issues a memory barrier. finishTextureLoading allocates AnimationData and atomic bools for occlusion data, then calls readTextureData for each path in texturePaths. reloadTextures clears all texture arrays while retaining capacity, re-reads textures via readTextureData, and calls generateTextureArray to build GPU arrays (blockTextureArray.generate is called with blockTextures.items; emissionTextureArray.generate is also invoked). The chunk uses main.worldArena as the arena allocator for most appends, main.stackAllocator for temporary paths, and main.files.cwd() for file system access. It relies on Image.readFromFile, readTextureFile, extractAnimationSlice, and generateTextureArray from other modules.

## Code Example
```zig
fn extractAnimationSlice(image: Image, frame: usize, frames: usize) Image {
	if (image.height < frames) return image;
	var startHeight = image.height/frames*frame;
	if (image.height%frames > frame) startHeight += frame else startHeight += image.height%frames;
	var endHeight = image.height/frames*(frame + 1);
	if (image.height%frames > frame + 1) endHeight += frame + 1 else endHeight += image.height%frames;
	var result = image;
	result.height = @intCast(endHeight - startHeight);
	result.imageData = result.imageData[startHeight*image.width .. endHeight*image.width];
	return result;
}
```

## Related Questions
- How does findTexture resolve a missing texture file when the assetFolder path is not found?
- What happens to animation frames if image.height < frames in extractAnimationSlice?
- Which arrays are populated by readTextureData for each frame of a texture?
- How does register use getTextureIndices and what value is passed as the default index on failure?
- What condition causes registerBlockBreakingAnimation to stop iterating over breaking textures?
- Why is main.worldArena used for appending blockTextures while main.stackAllocator is used for temporary paths?
- Does preProcessAnimationData bind a compute pipeline before dispatching, and what uniform values are set?
- How does finishTextureLoading allocate memory for animationData and textureOcclusionData?
- What sideNames entries are looked up in getTextureIndices when i < sideNames.len?
- Is generateTextureArray called after reloadTextures completes its re-read loop?
- Can a texture ID contain multiple colons, and how does findTexture split it?
- What error is returned if opening the file fails with something other than FileNotFound?

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_6*
