# [hard/codebase_src_graphics.zig] - Chunk 17

**Type:** api
**Keywords:** OpenGL textures, image file handling, GPU buffer generation, rendering, error handling
**Symbols:** Texture, Texture.textureID, Texture.init, Texture.initFromFile, Texture.initFromMipmapFiles, Texture.deinit, Texture.bindTo, Texture.bind, Texture.generate, Texture.render, Texture.size
**Concepts:** texture management, OpenGL rendering, image loading, mipmapping

## Summary
Defines the Texture struct and its methods for initialization, binding, generation, and rendering.

## Explanation
The Texture struct encapsulates OpenGL texture management. It provides methods to initialize textures from files or mipmaps, bind them for use in rendering, generate GPU buffers, and render images at specified positions and dimensions. The struct manages texture IDs and handles errors during image loading. It also includes methods to get the texture size.

The `initFromFile` method initializes a texture from an image file. If the image cannot be read, it logs an error and uses a default image.

The `initFromMipmapFiles` method initializes a texture with mipmaps. It generates multiple levels of detail for the texture based on the largest size provided and loads each level from a corresponding image file.

Error handling is implemented in both `initFromFile` and `initFromMipmapFiles` methods, where errors during image loading are logged using `std.log.err`.

The parameters that can be set on a texture include:
- `GL_TEXTURE_MIN_FILTER`
- `GL_TEXTURE_MAG_FILTER`
- `GL_TEXTURE_WRAP_S`
- `GL_TEXTURE_WRAP_T`
- `GL_TEXTURE_LOD_BIAS`

These parameters are set using the `glTexParameteri` and `glTexParameterf` functions.

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
