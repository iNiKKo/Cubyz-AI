# [hard/codebase_src_graphics.zig] - Chunk 3

**Type:** implementation
**Keywords:** OpenGL, 2D drawing, uniforms, vertex arrays, pipelines, shaders
**Symbols:** viewport, lineUniforms, linePipeline, lineVao, initLine, deinitLine, line, rectOutline, circleUniforms, circlePipeline, circleVao, initCircle, deinitCircle, circle
**Concepts:** OpenGL rendering, 2D graphics primitives, uniforms setup, vertex arrays, pipelines initialization

## Summary
Handles drawing various graphical primitives like rectangles, lines, and circles using OpenGL.

## Explanation
This chunk defines functions to draw rectangles, lines, and circles on the screen using OpenGL. It initializes and deinitializes pipelines and vertex arrays for each shape. The `line` function draws a line between two points, adjusting their positions based on scale and translation. The `rectOutline` function outlines a rectangle by drawing its border using lines. The `circle` function fills a circle by drawing triangles. Each function sets up OpenGL uniforms with necessary parameters like screen dimensions, position, size, color, and direction before rendering the shape.

The `initLine` function initializes the line pipeline with shaders located at "assets/cubyz/shaders/graphics/Line.vert" and "assets/cubyz/shaders/graphics/Line.frag". It sets up a vertex array with two vertices representing the start and end points of the line. The `deinitLine` function deinitializes the line pipeline and vertex array.

The `line` function calculates the positions of the line's endpoints by multiplying the input positions by the scale factor and adding the translation vector. It then sets the OpenGL uniforms for screen dimensions, start position, direction, and color before drawing the line using `glDrawArrays` with `GL_LINE_STRIP` mode.

The `initCircle` function initializes the circle pipeline with shaders located at "assets/cubyz/shaders/graphics/Circle.vert" and "assets/cubyz/shaders/graphics/Circle.frag". It sets up a vertex array with four vertices representing the corners of a square that bounds the circle. The `deinitCircle` function deinitializes the circle pipeline and vertex array.

The `circle` function calculates the center and radius of the circle by multiplying the input values by the scale factor and adding the translation vector for the center. It then sets the OpenGL uniforms for screen dimensions, center position, radius, and color before drawing the circle using `glDrawArrays` with `GL_TRIANGLE_STRIP` mode.

The `rectOutline` function outlines a rectangle by drawing its border using lines. It adjusts the direction vector to account for the inner edge of the rectangle being drawn. The `viewport` variable is used to get the current viewport dimensions from OpenGL, which are then passed as uniforms to the shaders.

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
