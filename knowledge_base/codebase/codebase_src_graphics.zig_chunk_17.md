# [hard/codebase_src_graphics.zig] - Chunk 17

**Type:** api
**Keywords:** OpenGL textures, image file handling, GPU buffer generation, rendering, error handling
**Symbols:** Texture, Texture.textureID, Texture.init, Texture.initFromFile, Texture.initFromMipmapFiles, Texture.deinit, Texture.bindTo, Texture.bind, Texture.generate, Texture.render, Texture.size
**Concepts:** texture management, OpenGL rendering, image loading, mipmapping

## Summary
Defines the Texture struct and its methods for initialization, binding, generation, and rendering.

## Explanation
The Texture struct encapsulates OpenGL texture management, providing methods for initialization, binding, generation, and rendering textures. It manages texture IDs and handles errors during image loading. The struct includes methods to get the texture size.

### Initialization Methods
- **init**: Initializes a new texture by generating a unique texture ID using `glGenTextures`.
- **initFromFile**: Initializes a texture from an image file. If the image cannot be read, it logs an error in the format "Couldn't read image from {s}: {s}" where `{s}` is replaced by the path of the failed file and the specific error encountered, then uses a default image.
- **initFromMipmapFiles**: Initializes a texture with mipmaps. It generates multiple levels of detail for the texture based on the largest size provided and loads each level from a corresponding image file. The method uses `glTexImage2D` to specify the texture storage for each mipmap level and `glTexSubImage2D` to upload the image data.

### Binding Methods
- **bindTo**: Binds the texture to a specified binding point using `glActiveTexture` and `glBindTexture`.
- **bind**: Binds the texture without specifying a binding point.

### Generation Method
- **generate**: Generates the GPU buffer for the texture. It binds the texture, sets parameters such as filtering and wrapping, and uploads image data using `glTexImage2D`. The method is implemented as follows:
  ```zig
  pub fn generate(self: Texture, image: Image) void {
      self.bind();
      c.glTexImage2D(c.GL_TEXTURE_2D, 0, c.GL_RGBA8, image.width, image.height, 0, c.GL_RGBA, c.GL_UNSIGNED_BYTE, image.imageData.ptr);
      c.glTexParameteri(c.GL_TEXTURE_2D, c.GL_TEXTURE_MIN_FILTER, c.GL_NEAREST);
      c.glTexParameteri(c.GL_TEXTURE_2D, c.GL_TEXTURE_MAG_FILTER, c.GL_NEAREST);
      c.glTexParameteri(c.GL_TEXTURE_2D, c.GL_TEXTURE_WRAP_S, c.GL_REPEAT);
      c.glTexParameteri(c.GL_TEXTURE_2D, c.GL_TEXTURE_WRAP_T, c.GL_REPEAT);
  }
  ```

### Rendering Method
- **render**: Renders an image at specified positions and dimensions by binding the texture and calling a rendering function.

### Error Handling
- Both `initFromFile` and `initFromMipmapFiles` methods include error handling. Errors during image loading are logged using `std.log.err`, providing details such as the path of the failed file and the specific error encountered.

### Parameters
- The parameters set on a texture include:
  - `GL_TEXTURE_MAX_LOD`: Set to the maximum level of detail calculated from the largest size.
  - `GL_TEXTURE_MIN_FILTER`: Set to `GL_NEAREST_MIPMAP_LINEAR` for filtering between mipmap levels.
  - `GL_TEXTURE_MAG_FILTER`: Set to `GL_NEAREST` for magnification.
  - `GL_TEXTURE_WRAP_S`: Set to `GL_REPEAT` for wrapping in the S direction.
  - `GL_TEXTURE_WRAP_T`: Set to `GL_REPEAT` for wrapping in the T direction.
  - `GL_TEXTURE_LOD_BIAS`: Set to a specified bias value to adjust the level of detail.

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
