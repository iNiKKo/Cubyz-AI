# [hard/codebase_src_graphics.zig] - Chunk 18

**Type:** api
**Keywords:** OpenGL, cube map textures, color manipulation, texture generation, framebuffer binding
**Symbols:** CubeMapTexture, CubeMapTexture.textureID, CubeMapTexture.init, CubeMapTexture.deinit, CubeMapTexture.bindTo, CubeMapTexture.bind, CubeMapTexture.generate, CubeMapTexture.faceNormal, CubeMapTexture.faceUp, CubeMapTexture.faceRight, CubeMapTexture.bindToFramebuffer, Color, Color.r, Color.g, Color.b, Color.a, Color.toArgb
**Concepts:** OpenGL texture management, Color representation and conversion

## Summary
Defines a CubeMapTexture struct for handling cube map textures in OpenGL and a Color struct for color manipulation.

## Explanation
The chunk defines two main structures: `CubeMapTexture` and `Color`. The `CubeMapTexture` struct manages the lifecycle of an OpenGL cube map texture, including initialization (`init`), deletion (`deinit`), binding to a specific texture unit (`bindTo`), general binding (`bind`), generating texture data (`generate`), and binding to a framebuffer (`bindToFramebuffer`). It also provides utility functions for determining face normals (`faceNormal`), up vectors (`faceUp`), and right vectors (`faceRight`) based on the cube map face index. The `Color` struct represents a color with red, green, blue, and alpha components, providing a method to convert it to ARGB format (`toArgb`). The `init` function generates a new texture ID using `glGenTextures`. The `deinit` function deletes the texture using `glDeleteTextures`. The `bindTo` function binds the texture to a specific texture unit. The `bind` function binds the texture without specifying a texture unit. The `generate` method sets up the cube map texture by calling `glTexImage2D` for each face of the cube map and setting various texture parameters using `glTexParameteri`. Specifically, it sets `GL_TEXTURE_MIN_FILTER` to `GL_LINEAR`, `GL_TEXTURE_MAG_FILTER` to `GL_LINEAR`, `GL_TEXTURE_WRAP_S` to `GL_CLAMP_TO_EDGE`, `GL_TEXTURE_WRAP_T` to `GL_CLAMP_TO_EDGE`, `GL_TEXTURE_WRAP_R` to `GL_CLAMP_TO_EDGE`, `GL_TEXTURE_BASE_LEVEL` to 0, and `GL_TEXTURE_MAX_LEVEL` to 0. The `faceNormal` function returns vectors representing the normal directions for each face of the cube map: `{1, 0, 0}` for +x, `{-1, 0, 0}` for -x, `{0, 1, 0}` for +y, `{0, -1, 0}` for -y, `{0, 0, 1}` for +z, and `{0, 0, -1}` for -z. The `faceUp` function returns vectors representing the up directions for each face of the cube map: `{0, -1, 0}` for +x, `{-1, 0, 0}`, `{0, 0, 1}` for +y, `{0, 0, -1}` for -y, `{0, -1, 0}` for +z, and `{-1, 0, 0}` for -z. The `faceRight` function returns vectors representing the right directions for each face of the cube map by computing the cross product of the normal and up vectors for each face. The `bindToFramebuffer` function binds the cube map texture to a framebuffer attachment using `glFramebufferTexture2D`.

## Code Example
```zig
pub fn init() CubeMapTexture {
	var self: CubeMapTexture = undefined;
	c.glGenTextures(1, &self.textureID);
	return self;
}
```

## Related Questions
- How do you initialize a CubeMapTexture?
- What methods are available for binding a CubeMapTexture?
- How does the `generate` method work in CubeMapTexture?
- What is the purpose of the `faceNormal` function in CubeMapTexture?
- How is color converted to ARGB format using the Color struct?
- What OpenGL functions are used in the CubeMapTexture methods?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_18*
