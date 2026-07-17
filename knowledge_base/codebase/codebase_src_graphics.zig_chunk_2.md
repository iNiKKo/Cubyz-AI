# [hard/codebase_src_graphics.zig] - Chunk 2

**Type:** implementation
**Keywords:** OpenGL, vertex arrays, shaders, uniforms, drawing functions
**Symbols:** rectBorderVao, rectBorderPipeline, rectBorderUniforms, lineUniforms, linePipeline, lineVao, circleUniforms, circlePipeline, circleVao
**Concepts:** OpenGL rendering, 2D graphics drawing, vertex arrays, shaders

## Summary
This chunk defines functions for drawing rectangles with borders, lines, and circles using OpenGL.

## Explanation
The chunk contains several functions to draw different shapes using OpenGL. It initializes and deinitializes pipelines and vertex arrays for each shape type. The `rectBorder` function draws a rectangle border by setting up the pipeline, uniforms, and drawing the vertices. The `line` function draws a line between two points, and the `rectOutline` function draws an outline of a rectangle using lines. The `initCircle` function initializes the circle drawing pipeline and vertex array, but the deinitialization is incomplete.

## Code Example
```zig
fn deinitRectBorder() void {
	rectBorderPipeline.deinit();
	rectBorderVao.deinit();
}
```

## Related Questions
- What is the purpose of the `rectBorder` function?
- How does the `line` function calculate the direction vector for drawing a line?
- What are the uniforms used in the circle drawing pipeline?
- Why is the deinitialization of the circle pipeline incomplete?
- How many vertices are used to draw a rectangle border?
- What shader files are used for drawing lines and circles?
- How does the `rectOutline` function ensure the outline is drawn correctly?
- What is the role of the `initLine` function in the graphics module?
- How are the positions and dimensions scaled before drawing shapes?
- What OpenGL functions are used to draw arrays in this chunk?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_2*
