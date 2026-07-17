# [hard/codebase_src_graphics.zig] - Chunk 15

**Type:** implementation
**Keywords:** texture initialization, mipmap generation, GPU texture upload, image loading, OpenGL bindings
**Symbols:** Texture, Texture.textureID, Texture.init, Texture.initFromFile, Texture.initFromMipmapFiles, TextureArray, TextureArray.generate
**Concepts:** texture handling, mipmapping, GPU buffer management

## Summary
This chunk defines texture handling logic including initialization from files and mipmapping generation.

## Explanation
The chunk contains definitions for `Texture` and `TextureArray` structs, each with methods for initializing textures from files or generating mipmaps. The `generate` method in `TextureArray` handles creating a GPU buffer, calculating mipmap levels, and uploading texture data to the GPU. The `initFromFile` and `initFromMipmapFiles` methods in `Texture` handle loading images and setting up textures with appropriate parameters.

## Code Example
```zig
pub fn init() Texture {
	var self: Texture = undefined;
	c.glGenTextures(1, &self.textureID);
	return self;
}
```

## Related Questions
- How does the `Texture` struct initialize a texture from a file?
- What is the purpose of the `generate` method in the `TextureArray` struct?
- How are mipmaps generated and uploaded to the GPU in this chunk?
- What error handling is implemented when loading images for textures?
- How does the chunk ensure that texture dimensions are powers of two?
- What OpenGL parameters are set for textures in this implementation?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_15*
