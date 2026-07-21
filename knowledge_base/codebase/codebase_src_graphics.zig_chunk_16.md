# [hard/codebase_src_graphics.zig] - Chunk 16

**Type:** implementation
**Keywords:** OpenGL, texture array, mipmaps, gamma correction, nearest sampling
**Symbols:** TextureArray, TextureArray.textureID, TextureArray.init, TextureArray.deinit, TextureArray.bind, TextureArray.lodColorInterpolation, TextureArray.generate
**Concepts:** texture array management, mipmap generation, alpha correction, OpenGL texture handling

## Summary
The TextureArray struct manages the creation and destruction of a texture array in OpenGL, including generating mipmaps with optional alpha correction.

## Explanation
The TextureArray struct manages the creation and destruction of a texture array in OpenGL, including generating mipmaps with optional alpha correction. It includes methods to initialize (`init`), deinitialize (`deinit`), and bind (`bind`) the texture array. The `generate` method is responsible for creating the GPU buffer, uploading images, and generating mipmaps with optional alpha correction. This involves calculating the maximum dimensions of the input images, ensuring they are powers of two, and then filling a buffer using nearest sampling to create each mipmap level. The `lodColorInterpolation` function computes the color for each pixel in the mipmap levels based on surrounding pixels, applying gamma correction if specified. Specifically, it takes an array of four colors and a boolean indicating whether alpha correction should be applied, and returns a single interpolated color. It converts the integer color values to floating-point, calculates weighted sums with optional alpha correction, computes the square root of these sums, and then truncates them back to integers. The texture dimensions are adjusted to the nearest power of two by finding the smallest power of two greater than or equal to the maximum width or height.

## Code Example
```zig
pub fn init() TextureArray {
	var self: TextureArray = undefined;
	c.glGenTextures(1, &self.textureID);
	return self;
}
```

## Related Questions
- How does the TextureArray struct initialize a texture array in OpenGL?
- What method is used to delete a texture array in the TextureArray struct?
- Can you explain how mipmaps are generated in the TextureArray struct?
- What role does alpha correction play in mipmap generation within the TextureArray struct?
- How does the TextureArray struct ensure that image dimensions are powers of two?
- What is the purpose of the lodColorInterpolation function in the TextureArray struct?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_16*
