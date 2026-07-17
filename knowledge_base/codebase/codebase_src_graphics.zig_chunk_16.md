# [hard/codebase_src_graphics.zig] - Chunk 16

**Type:** api
**Keywords:** texture initialization, error handling, OpenGL bindings, mipmaps, cubemaps
**Symbols:** Texture, CubeMapTexture, Texture.init, Texture.deinit, Texture.bindTo, Texture.bind, Texture.generate, Texture.render, Texture.size, CubeMapTexture.init, CubeMapTexture.deinit, CubeMapTexture.bindTo, CubeMapTexture.bind, CubeMapTexture.generate, CubeMapTexture.faceNormal, CubeMapTexture.faceUp, CubeMapTexture.faceRight
**Concepts:** texture handling, cubemap textures, mipmap generation, OpenGL texture parameters

## Summary
This chunk defines texture handling logic including initialization, generation, binding, and rendering of textures and cubemap textures.

## Explanation
The chunk contains definitions for `Texture` and `CubeMapTexture` structs with methods to initialize, deinitialize, bind, generate, and render textures. It includes error handling for image file reading and sets various texture parameters such as filtering and wrapping modes. The `initFromMipmapFiles` function initializes a texture from a series of mipmap files. The chunk also provides utility functions like `faceNormal`, `faceUp`, and `faceRight` for cubemap textures.

## Code Example
```zig
pub fn deinit(self: Texture) void {
	c.glDeleteTextures(1, &self.textureID);
}
```

## Related Questions
- How does the `Texture` struct initialize from a file?
- What error handling is implemented when reading image files for textures?
- How are texture parameters set in the `generate` method of the `Texture` struct?
- What methods are available for binding and rendering textures?
- How does the `initFromMipmapFiles` function work to create a mipmap texture?
- What is the purpose of the `faceNormal`, `faceUp`, and `faceRight` functions in the `CubeMapTexture` struct?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_16*
