# [hard/codebase_src_graphics.zig] - Chunk 1

**Type:** api
**Keywords:** color management, translation, scaling, clipping, pipeline initialization, vertex array object
**Symbols:** draw, draw.color, draw.clip, draw.translation, draw.scale, draw.setColor, draw.restoreColor, draw.getColor, draw.setTranslation, draw.restoreTranslation, draw.setScale, draw.restoreScale, draw.setClip, draw.getScissor, draw.restoreClip, draw.SimpleVertex2D, draw.SimpleVertex2D.pos, draw.SimpleVertex2D.attributeDescriptions, draw.rectUniforms, draw.rectPipeline, draw.rectVao, draw.initRect, draw.deinitRect
**Concepts:** graphics rendering, color manipulation, translation and scaling, clipping

## Summary
The `draw` struct manages graphics drawing settings and provides functions to manipulate color, translation, scale, and clipping.

## Explanation
The `draw` struct manages graphics drawing settings and provides functions to manipulate color, translation, scale, and clipping. It includes methods to set and restore these settings, ensuring that changes can be reverted if necessary. The struct also handles the initialization and deinitialization of a simple rectangle pipeline used for rendering filled rectangles.

Key variables in the `draw` struct include:
- `color`: A Vec4f representing the current color with default value `[1.0, 1.0, 1.0, 1.0]`.
- `clip`: An optional Vec4i representing the clipping area with default value `null`.
- `translation`: A Vec2f representing the translation vector with default value `[0.0, 0.0]`.
- `scale`: A float representing the scale factor with default value `1.0`.

Key functions include:
- `setColor(newColorRgba: u32) Vec4f`: Sets the color using an RGBA value and returns the old color.
- `restoreColor(oldColor: Vec4f) void`: Restores the previous color.
- `getColor() Color`: Returns the current color as a Color struct.
- `setTranslation(newTranslation: Vec2f) Vec2f`: Sets the translation vector, scales it by the current scale factor, and returns the old translation.
- `restoreTranslation(previousTranslation: Vec2f) void`: Restores the previous translation.
- `setScale(newScale: f32) f32`: Sets the scale factor, multiplies it with the current scale, and returns the old scale. The new scale must be non-negative.
- `restoreScale(previousScale: f32) void`: Restores the previous scale.
- `setClip(clipRect: Vec2f) ?Vec4i`: Sets the clipping area based on a rectangle defined by its top-left corner and size, adjusts it relative to the current translation and scale, and returns the old clip. The new clip must have non-negative dimensions.
- `getScissor() ?c.VkRect2D`: Returns the current scissor rectangle in Vulkan format if clipping is enabled.
- `restoreClip(previousClip: ?Vec4i) void`: Restores the previous clipping area.

The `SimpleVertex2D` struct defines a simple 2D vertex with a position attribute. Its attribute descriptions specify that the position is stored as two 32-bit floating-point numbers in format `VK_FORMAT_R32G32_SFLOAT` at offset 0.

Initialization and deinitialization of the rectangle pipeline are handled by `initRect()` and `deinitRect()`. The `initRect()` function initializes the pipeline with shaders, uniforms, vertex attributes, and rendering states. It also sets up a simple vertex array object (`rectVao`) with predefined vertices for a rectangle.

## Code Example
```zig
pub fn restoreColor(oldColor: Vec4f) void {
	color = oldColor;
}
```

## Related Questions
- How do you set the color in the draw module?
- What is the purpose of the `restoreColor` function?
- How does the `setTranslation` function work?
- What are the steps to initialize the rectangle pipeline?
- How is the clipping area defined and managed?
- What is the role of the `SimpleVertex2D` struct in rendering?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_1*
