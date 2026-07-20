# [hard/codebase_src_graphics.zig] - Chunk 4

**Type:** implementation
**Keywords:** OpenGL, shaders, uniforms, rendering, circles, images
**Symbols:** deinitCircle, circle, imageUniforms, imagePipeline, initImage, deinitImage, boundImage, boundSubImage, drawSlice, bound9SliceImage, customShadedImage, customShadedRect
**Concepts:** circle rendering, image rendering, OpenGL shaders, uniforms management

## Summary
Handles drawing circles and images using OpenGL shaders.

## Explanation
This chunk manages the rendering of circles and images using OpenGL shaders. It defines functions to initialize and deinitialize resources for circle and image rendering, as well as methods to draw these shapes with various parameters such as position, size, color, and UV coordinates.

The `deinitCircle` function deinitializes the circle pipeline and vertex array object. The `circle` function handles drawing circles by binding a pipeline and setting uniform values for screen dimensions (`screen`), center (`center`), radius (`radius`), and color (`circleColor`). Specifically, the parameters for the `circle` function are `_center: Vec2f` (the center of the circle) and `_radius: f32` (the radius of the circle).

The `imageUniforms` struct defines uniforms used in image rendering, including `screen`, `start`, `size`, `color`, `uvOffset`, and `uvDim`. The `initImage` function initializes the image pipeline with specified shaders and uniform settings. The `deinitImage` function deinitializes the image pipeline.

The `boundImage` function binds an image to a given position and dimension using custom shaded image rendering. The `boundSubImage` function handles UV coordinates by setting them in the uniforms before drawing the sub-image. Specifically, the parameters for the `boundSubImage` function are `_pos: Vec2f`, `_dim: Vec2f`, `uvOffset: Vec2f`, and `uvDim: Vec2f`. The `drawSlice` function draws a slice of an image based on destination and UV coordinates.

The `bound9SliceImage` function draws a 9-slice image by dividing it into nine parts and drawing each part with appropriate UV coordinates. Specifically, the parameters for the `bound9SliceImage` function are `pos: Vec2f`, `dim: Vec2f`, `textureSize: Vec2f`, `slices: Vec2f`, and `sliceScale: f32`. The `customShadedImage` function provides more flexible drawing capabilities by allowing custom uniform settings, including screen dimensions (`screen`), start position (`start`), size (`size`), color (`color`), UV offset (`uvOffset`), and UV dimension (`uvDim`). Similarly, the `customShadedRect` function allows for custom shaded rectangle rendering with specified uniforms.

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
