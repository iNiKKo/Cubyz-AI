# [easy/codebase_src_gui_gamepad_cursor.zig] - Chunk 0

**Type:** implementation
**Keywords:** Texture.initFromFile, graphics.draw.boundImage, main.Window.lastUsedMouse, gui.scale, deinit, render loop
**Symbols:** Texture, Vec2f, init, deinit, render
**Concepts:** texture resource management, mouse cursor rendering, GUI scale offsetting, input state gating

## Summary
This chunk defines the gamepad cursor texture resource and its render lifecycle within the GUI system.

## Explanation
The chunk imports std, main.graphics (for Texture), main.vec.Vec2f, and gui.zig. It declares a global var texture:Texture initialized to undefined, then provides pub fn init() which loads assets/cubyz/ui/gamepad_cursor.png into the texture variable via Texture.initFromFile. pub fn deinit() calls texture.deinit(). pub fn render() checks main.Window.lastUsedMouse or main.Window.grabbed and returns early if either is true; otherwise it binds the texture to slot 0, retrieves mousePos from main.Window.getMousePosition(), computes an offset using gui.scale (splat(-size/2.0) + mousePos/@as(Vec2f,@splat(gui.scale))), and draws a quad of size size via graphics.draw.boundImage.

## Related Questions
- What file path is used to load the gamepad cursor texture?
- Under what conditions does render() skip drawing the cursor?
- How is the mouse position offset applied before drawing the cursor quad?
- Which graphics API call binds the loaded texture to slot 0?
- Does this chunk provide any public initialization or cleanup functions for the cursor?
- What type is declared for the global texture variable?

*Source: unknown | chunk_id: codebase_src_gui_gamepad_cursor.zig_chunk_0*
