# [hard/codebase_src_graphics.zig] - Chunk 3

**Type:** implementation
**Keywords:** OpenGL, pipeline, vertex array, uniforms, shader, circle, image, 9-slice, custom shader
**Symbols:** circleColor, circlePipeline, circleVao, initCircle, deinitCircle, circle, imageUniforms, imagePipeline, initImage, deinitImage, boundImage, boundSubImage, drawSlice, bound9SliceImage, customShadedImage
**Concepts:** OpenGL rendering, circle drawing, image rendering, vertex arrays, shaders

## Summary
Handles rendering of circles and images using OpenGL pipelines and vertex arrays.

## Explanation
This chunk manages the initialization, deinitialization, and drawing of circles and images. It defines two main structures: `circleUniforms` for circle rendering and `imageUniforms` for image rendering. The `initCircle` function initializes the circle pipeline and vertex array with predefined vertices. The `deinitCircle` function cleans up these resources. The `circle` function sets up and draws a circle at a specified center and radius, adjusting for scale and translation. Similarly, `initImage` initializes the image pipeline, and `deinitImage` deinitializes it. The `boundImage` and `boundSubImage` functions bind and draw images with optional UV offsets. The `drawSlice` function draws a portion of an image, and `bound9SliceImage` uses this to render 9-sliced images. The `customShadedImage` function provides a flexible way to draw images with custom shaders.

## Code Example
```zig
fn deinitCircle() void {
	circlePipeline.deinit();
	circleVao.deinit();
}
```

## Related Questions
- What is the purpose of the `initCircle` function?
- How does the `circle` function adjust for scale and translation?
- What resources are cleaned up by the `deinitImage` function?
- How does the `boundSubImage` function handle UV offsets?
- What is the role of the `drawSlice` function in rendering images?
- How does the `customShadedImage` function set up image drawing?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_3*
