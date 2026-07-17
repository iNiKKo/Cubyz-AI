# [hard/codebase_src_graphics.zig] - Chunk 0

**Type:** api
**Keywords:** Vec4f, bitCast, glGetIntegerv, VK_FORMAT_R32G32_SFLOAT, lossyCast, attributeDescriptions, VkRect2D
**Symbols:** draw, Mat4f, Vec4i, Vec4f, Vec2f, Vec2i, Vec3f, ComputePipeline, Pipeline, Window, NeverFailingAllocator, SimpleVertex2D, vulkan
**Concepts:** draw API surface, color state management, translation scaling, clip rect bounds adjustment, viewport scissor conversion

## Summary
This chunk defines a public draw API surface (color/translation/scale/clip state and their setters/restorers) plus a minimal SimpleVertex2D struct for 2D rendering, along with internal uniforms and pipeline variables.

## Explanation
The chunk imports std and builtin, then re-exports types from vec.zig (Mat4f, Vec4i, Vec4f, Vec2f, Vec2i, Vec3f) as public constants. It pulls main.Window and NeverFailingAllocator from the main module, and imports c for OpenGL bindings. From graphics/pipelines.zig it publicly re-exports ComputePipeline and Pipeline. The draw struct holds mutable state: color (Vec4f), clip (?Vec4i), translation (Vec2f), scale (f32). It provides setColor(newColorRgba) which bit-casts a u32 RGBA into Color, multiplies each channel by the normalized integer value divided by 255.0, returns the old color; restoreColor(oldColor) simply assigns back to color. getColor() rounds each component of color scaled up by 255.0 and returns a Color struct with r,g,b,a fields. setTranslation(newTranslation) adds newTranslation scaled by current scale to translation, returning the previous translation; restoreTranslation(previousTranslation) restores translation directly. setScale(newScale) asserts non-negative, multiplies scale by newScale, returns old scale; restoreScale(previousScale) assigns back. setClip(clipRect) asserts clipRect is non-negative, reads the OpenGL viewport via c.glGetIntegerv(c.GL_VIEWPORT), computes a new Vec4i from translation and scaled clipRect, then adjusts the new clip to stay within any existing clip bounds (swaps/shifts when newClip[0] < oldClip[0], etc.), clamps width/height to non-negative, stores in clip, returns old clip. getScissor() converts clip or null into a c.VkRect2D with offset.x/y from clipRect[0]/[1] and extent.width/height as lossy casts of clipRect[2]/[3]. restoreClip(previousClip) assigns back to clip. SimpleVertex2D is defined inside draw with pos: [2]f32; its attributeDescriptions static array contains a single VkVertexInputAttributeDescription at location 0, format VK_FORMAT_R32G32_SFLOAT, offset computed via @offsetOf(@This(), 

## Related Questions
- What does setColor do with the RGBA input?
- How is translation combined with scale in setTranslation?
- Why does setClip read GL_VIEWPORT before computing newClip?
- What happens to clip bounds when they overlap existing clip?
- How does getScissor map Vec4i to VkRect2D fields?
- Where are the vertex attribute descriptions defined for SimpleVertex2D?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_0*
