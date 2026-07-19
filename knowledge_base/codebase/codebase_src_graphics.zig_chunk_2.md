# [hard/codebase_src_graphics.zig] - Chunk 2

**Type:** implementation
**Keywords:** pipeline initialization, VAO management, OpenGL commands, shader binding, uniform setting, triangle strip drawing
**Symbols:** rectUniforms, rectPipeline, rectVao, initRect, deinitRect, rect, rectBorderUniforms, rectBorderPipeline, rectBorderVao, initRectBorder, deinitRectBorder, rectBorder, lineUniforms, linePipeline, lineVao, initLine
**Concepts:** graphics pipeline, vertex array object, OpenGL rendering, rectangle drawing, border rendering, line drawing

## Summary
This chunk defines functions and data structures for rendering rectangles, rectangle borders, and lines in a graphics pipeline.

## Explanation
This chunk defines functions and data structures for rendering rectangles, rectangle borders, and lines in a graphics pipeline. The chunk contains definitions for three main drawing functions: `rect`, `rectBorder`, and `drawLine`. Each function initializes its respective pipeline and vertex array object (VAO) with specific shaders and vertex data.

The `initRect` function initializes the rectangle rendering resources by creating a pipeline with the shader files "assets/cubyz/shaders/graphics/Rect.vert" and "assets/cubyz/shaders/graphics/Rect.frag", setting up uniform variables for screen, start, size, and rectColor. The vertex data for rectangles is defined as an array of `SimpleVertex2D` structs with positions (0, 0), (0, 1), (1, 0), and (1, 1). The `rect` function sets up and draws a filled rectangle by binding the pipeline, setting uniform values for screen dimensions, start position, size, and color, and then drawing the vertices using `glDrawArrays` with `GL_TRIANGLE_STRIP`.

The `initRectBorder` function initializes the border rendering resources similarly but uses different shaders "assets/cubyz/shaders/graphics/RectBorder.vert" and "assets/cubyz/shaders/graphics/RectBorder.frag". The vertex data for borders is more complex, involving positions that define lines forming a border around a rectangle. The `rectBorder` function sets up and draws a rectangle with a border by binding the pipeline, setting uniform values for screen dimensions, start position, size, color, and line width, and then drawing the vertices using `glDrawArrays` with `GL_TRIANGLE_STRIP`.

The `deinitRect` and `deinitRectBorder` functions manage the lifecycle of their respective rendering resources by deinitializing the pipeline and vertex array object. The `drawLine` function is partially defined but not fully implemented in the provided snippet.

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
