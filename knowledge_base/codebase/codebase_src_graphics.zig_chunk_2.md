# [hard/codebase_src_graphics.zig] - Chunk 2

**Type:** implementation
**Keywords:** pipeline initialization, VAO management, OpenGL commands, shader binding, uniform setting, triangle strip drawing
**Symbols:** rectUniforms, rectPipeline, rectVao, initRect, deinitRect, rect, rectBorderUniforms, rectBorderPipeline, rectBorderVao, initRectBorder, deinitRectBorder, rectBorder, lineUniforms, linePipeline, lineVao, initLine
**Concepts:** graphics pipeline, vertex array object, OpenGL rendering, rectangle drawing, border rendering, line drawing

## Summary
This chunk defines functions and data structures for rendering rectangles, rectangle borders, and lines in a graphics pipeline.

## Explanation
The chunk contains definitions for three main drawing functions: `rect`, `rectBorder`, and `drawLine`. Each function initializes its respective pipeline and vertex array object (VAO) with specific shaders and vertex data. The `initRect` and `deinitRect` functions manage the lifecycle of the rectangle rendering resources, while `rect` sets up and draws a filled rectangle using OpenGL commands. Similarly, `initRectBorder` and `deinitRectBorder` handle the border drawing resources, and `rectBorder` renders a rectangle with a border. The `drawLine` function is partially defined but not fully implemented in the provided snippet.

## Code Example
```zig
fn deinitRect() void {
	rectPipeline.deinit();
	rectVao.deinit();
}
```

## Related Questions
- What is the purpose of the `initRect` function?
- How does the `rect` function set up and draw a rectangle?
- What resources are managed by `deinitRectBorder`?
- How is the vertex data structured for border rendering?
- What OpenGL command is used to draw the triangles in `rectBorder`?
- Why is the line width scaled by `scale` in `rectBorder`?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_2*
