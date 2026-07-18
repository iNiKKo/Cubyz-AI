# [hard/codebase_src_graphics.zig] - Chunk 17

**Type:** api
**Keywords:** OpenGL textures, image file handling, GPU buffer generation, rendering, error handling
**Symbols:** Texture, Texture.textureID, Texture.init, Texture.initFromFile, Texture.initFromMipmapFiles, Texture.deinit, Texture.bindTo, Texture.bind, Texture.generate, Texture.render, Texture.size
**Concepts:** texture management, OpenGL rendering, image loading, mipmapping

## Summary
Defines the Texture struct and its methods for initialization, binding, generation, and rendering.

## Explanation
The Texture struct encapsulates OpenGL texture management. It provides methods to initialize textures from files or mipmaps, bind them for use in rendering, generate GPU buffers, and render images at specified positions and dimensions. The struct manages texture IDs and handles errors during image loading. It also includes methods to get the texture size.

## Code Example
```zig
pub fn init() Texture {
	var self: Texture = undefined;
	c.glGenTextures(1, &self.textureID);
	return self;
}
```

## Related Questions
- How does the Texture struct initialize a texture from a file?
- What methods are available for binding textures in the Texture struct?
- How is error handling implemented when loading images for textures?
- What parameters can be set on a texture using the Texture struct?
- How does the Texture struct handle mipmapping?
- What is the purpose of the generate method in the Texture struct?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_17*
