# [hard/codebase_src_graphics.zig] - Chunk 5

**Type:** implementation
**Keywords:** OpenGL, uniforms, vertex array object, text rendering, string formatting
**Symbols:** customShadedRect, text, print
**Concepts:** graphics rendering, rectangle drawing, text rendering

## Summary
Handles rendering of rectangles and text in the graphics system.

## Explanation
The code defines functions for drawing shaded rectangles and text. The `customShadedRect` function adjusts position and dimensions based on scale and translation, retrieves the viewport size using `glGetIntegerv`, sets various uniforms including `screen`, `start`, `size`, `color`, and `scale`, and draws a rectangle using a vertex array object (VAO). Specifically, it uses `glUniform2f` to set 2D float uniforms for `screen`, `start`, and `uvOffset`, `glUniform1i` to set an integer uniform for `color`, and `glUniform1f` to set a float uniform for `scale`. The rectangle is drawn using `glDrawArrays` with `GL_TRIANGLE_STRIP`. The `text` function calls an external rendering function, `TextRendering.renderText`, to display text at specified coordinates and font size. The `print` function formats a string using Zig's formatting utilities and then calls `text` to render it, managing memory for the formatted string using `std.fmt.allocPrint` and `main.stackAllocator.free`. The uniforms set in the `customShadedRect` function are: `screen`, `start`, `size`, `color`, and `scale`. The OpenGL functions used to draw a rectangle include `glGetIntegerv`, `glUniform2f`, `glUniform1i`, `glUniform1f`, and `glDrawArrays`. Text rendering is handled by the `TextRendering.renderText` function.

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
