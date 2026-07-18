# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 3

**Type:** implementation
**Keywords:** mouse interaction, window resizing, attachment points, orientation lines, icon textures
**Symbols:** updateHovered, getMinWindowWidth, updateWindowPosition, drawOrientationLines, drawIcons
**Concepts:** GUI window management, hover state handling, window positioning, icon rendering

## Summary
Handles GUI window interactions and rendering.

## Explanation
This chunk defines methods for updating the hover state of a GUI window, calculating its minimum width, updating its position based on various attachment points, drawing orientation lines, and rendering icons. It manages window resizing constraints, ensures proper positioning, and handles icon rendering with specific textures for close, zoom in, and zoom out functionalities.

## Code Example
```zig
pub fn getMinWindowWidth(self: *GuiWindow) f32 {
	return iconWidth*@as(f32, (if (self.closeable) 4 else 3));
}
```

## Related Questions
- How does the `updateHovered` function determine if a mouse position is within the title bar?
- What is the purpose of the `getMinWindowWidth` method in the GUI window class?
- How does the `updateWindowPosition` function handle window resizing constraints?
- What does the `drawOrientationLines` method draw on the screen?
- How are icons rendered in the GUI window using the `drawIcons` method?
- What conditions determine if a window's width is too small and needs to be resized?

*Source: unknown | chunk_id: codebase_src_gui_GuiWindow.zig_chunk_3*
