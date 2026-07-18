# [hard/codebase_src_graphics.zig] - Chunk 3

**Type:** implementation
**Keywords:** OpenGL, 2D drawing, uniforms, vertex arrays, pipelines, shaders
**Symbols:** viewport, lineUniforms, linePipeline, lineVao, initLine, deinitLine, line, rectOutline, circleUniforms, circlePipeline, circleVao, initCircle, deinitCircle, circle
**Concepts:** OpenGL rendering, 2D graphics primitives, uniforms setup, vertex arrays, pipelines initialization

## Summary
Handles drawing various graphical primitives like rectangles, lines, and circles using OpenGL.

## Explanation
This chunk defines functions to draw rectangles, lines, and circles on the screen. It initializes and deinitializes pipelines and vertex arrays for each shape. The `line` function draws a line between two points, adjusting their positions based on scale and translation. The `rectOutline` function outlines a rectangle by drawing its border using lines. The `circle` function fills a circle by drawing triangles. Each function sets up OpenGL uniforms with necessary parameters like screen dimensions, position, size, color, and direction before rendering the shape.

## Code Example
```zig
fn deinitLine() void {
	linePipeline.deinit();
	lineVao.deinit();
}
```

## Related Questions
- How does the `line` function calculate the positions of the line's endpoints?
- What are the steps involved in initializing a circle pipeline and vertex array?
- How does the `rectOutline` function adjust the direction vector for drawing the rectangle border?
- What OpenGL functions are used to draw arrays in this chunk?
- Can you explain how the `circle` function sets up its uniforms before rendering?
- What is the purpose of the `viewport` variable in these drawing functions?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_3*
