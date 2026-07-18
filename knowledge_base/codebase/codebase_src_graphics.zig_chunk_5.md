# [hard/codebase_src_graphics.zig] - Chunk 5

**Type:** implementation
**Keywords:** OpenGL, uniforms, vertex array object, text rendering, string formatting
**Symbols:** customShadedRect, text, print
**Concepts:** graphics rendering, rectangle drawing, text rendering

## Summary
Handles rendering of rectangles and text in the graphics system.

## Explanation
The code defines functions for drawing shaded rectangles and text. The `customShadedRect` function adjusts position and dimensions based on scale and translation, retrieves the viewport size, sets various uniforms, and draws a rectangle using a vertex array object (VAO). The `text` function calls an external rendering function to display text at specified coordinates and font size. The `print` function formats a string using Zig's formatting utilities and then calls `text` to render it.

## Code Example
```zig
pub fn text(_text: []const u8, x: f32, y: f32, fontSize: f32) void {
    TextRendering.renderText(_text, x, y, fontSize, .{});
}
```

## Related Questions
- How does the `customShadedRect` function adjust the rectangle's position and size?
- What are the uniforms set in the `customShadedRect` function?
- Which OpenGL functions are used to draw a rectangle in this code?
- How is text rendered in this graphics module?
- What does the `print` function do, and how does it differ from the `text` function?
- How is memory managed for formatted strings in the `print` function?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_5*
