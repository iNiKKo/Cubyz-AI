# [easy/codebase_src_gui_gamepad_cursor.zig] - Chunk 0

**Type:** implementation
**Keywords:** texture init, cursor render, mouse pos, graphics bind, window grab
**Symbols:** size, texture, init, deinit, render
**Concepts:** gamepad cursor rendering, texture management, mouse position handling

## Summary
Gamepad cursor rendering logic

## Explanation
This chunk defines the gamepad cursor rendering logic for the Cubyz voxel engine. It initializes and deinitializes a texture, renders the cursor based on the mouse position, and binds it to the graphics context when necessary.

## Code Example
```zig
pub fn render() void { if (main.Window.lastUsedMouse or main.Window.grabbed) return; texture.bindTo(0); const mousePos = main.Window.getMousePosition(); graphics.draw.boundImage(@as(Vec2f, @splat(-size/2.0)) + (mousePos/@as(Vec2f, @splat(gui.scale))), .{size, size}); }
```

## Related Questions
- What is the purpose of the `render` function in this chunk?
- How does the cursor position affect its rendering?
- What texture is used for the gamepad cursor?
- When is the cursor rendered?
- What are the parameters passed to the `boundImage` function in the `render` function?
- What is the size of the cursor image?
- Where is the cursor positioned relative to the mouse position?
- How does the cursor handle window grabs?
- What happens if the window is not used by the mouse?
- What is the texture initialization process for the gamepad cursor?
- When is the `texture` variable initialized?
- What is the purpose of the `deinit` function in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_gamepad_cursor.zig_chunk_0*
