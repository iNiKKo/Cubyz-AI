# [hard/codebase_src_gui_GuiWindow.zig] - Chunk 3

**Type:** implementation
**Keywords:** mouse interaction, window resizing, attachment points, orientation lines, icon textures
**Symbols:** updateHovered, getMinWindowWidth, updateWindowPosition, drawOrientationLines, drawIcons
**Concepts:** GUI window management, hover state handling, window positioning, icon rendering

## Summary
Handles GUI window interactions and rendering.

## Explanation
This chunk defines methods for updating the hover state of a GUI window, calculating its minimum width, updating its position based on various attachment points, drawing orientation lines, and rendering icons. It manages window resizing constraints, ensures proper positioning, and handles icon rendering with specific textures for close, zoom in, and zoom out functionalities.

The `updateHovered` function determines if a mouse position is within the title bar by checking if the scaled mouse position's y-coordinate is less than the title bar height and if the window either shows the title bar or allows reordering of windows. If these conditions are met, it updates the hover state of the title bar.

The `getMinWindowWidth` method calculates the minimum width of a GUI window based on whether it is closeable. If the window is closeable, its minimum width is set to four times the icon width; otherwise, it is set to three times the icon width.

The `updateWindowPosition` function handles window resizing constraints by ensuring that the window's content size does not fall below its minimum width. If the content size is too small, it logs an error and resizes the window accordingly. It then updates the window's position based on its attachment points relative to either the frame or other windows.

The `drawOrientationLines` method draws orientation lines on the screen based on the window's attachment points. These lines help visualize how the window is attached to the frame or other windows.

The `drawIcons` method renders icons in the GUI window using specific textures for close, zoom in, and zoom out functionalities. The icons are positioned according to whether the window is closeable and the size of the window.

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
