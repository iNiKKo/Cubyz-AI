# [hard/codebase_src_graphics.zig] - Chunk 4

**Type:** implementation
**Keywords:** OpenGL, shaders, uniforms, rendering, circles, images
**Symbols:** deinitCircle, circle, imageUniforms, imagePipeline, initImage, deinitImage, boundImage, boundSubImage, drawSlice, bound9SliceImage, customShadedImage, customShadedRect
**Concepts:** circle rendering, image rendering, OpenGL shaders, uniforms management

## Summary
Handles drawing circles and images using OpenGL shaders.

## Explanation
This chunk manages the rendering of circles and images in a graphics engine. It defines functions to initialize and deinitialize resources for circle and image rendering, as well as methods to draw these shapes with various parameters such as position, size, color, and UV coordinates. The `circle` function handles drawing circles by binding a pipeline and setting uniform values for screen dimensions, center, radius, and color. Similarly, the `boundImage`, `boundSubImage`, and `bound9SliceImage` functions manage image rendering with different levels of detail and slicing options. The `customShadedImage` and `customShadedRect` functions provide more flexible drawing capabilities by allowing custom uniform settings.

## Code Example
```zig
fn deinitCircle() void {
	circlePipeline.deinit();
	circleVao.deinit();
}
```

## Related Questions
- How does the `deinitCircle` function work?
- What are the parameters for the `circle` function?
- What is the purpose of the `imageUniforms` struct?
- How does the `boundSubImage` function handle UV coordinates?
- What does the `bound9SliceImage` function draw?
- How are uniforms set in the `customShadedImage` function?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_4*
