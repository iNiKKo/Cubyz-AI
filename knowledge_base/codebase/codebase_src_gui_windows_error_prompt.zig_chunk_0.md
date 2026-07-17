# [easy/codebase_src_gui_windows_error_prompt.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, Texture, controller mappings, openDirInWindow, closeWindowFromRef, rootComponent, updateWindowPositions, deinit
**Symbols:** fileExplorerIcon, window, init, deinit, openLog, padding, update, onOpen, onClose
**Concepts:** GUI window lifecycle, error prompt display, controller mapping download detection, log directory navigation, component layout with padding, icon button action binding

## Summary
This chunk implements a GUI error prompt window that displays when controller mappings are downloaded, containing an icon, a label with error text, and a button to open the logs directory.

## Explanation
The chunk defines a GuiWindow named 'window' with specific content size (128x64), background enabled, and relative positioning attached to itself at lower points. It imports main.files, main.settings, Vec2f from main.vec, Texture from main.graphics, and gui components including GuiWindow, Label, VerticalList, Button. A global Texture variable 'fileExplorerIcon' is initialized in the init() function by loading an image file. The deinit() function cleans up the texture. openLog() calls main.files.openDirInWindow with path 'logs'. update() checks if controller mappings were downloaded via main.Window.Gamepad.wereControllerMappingsDownloaded(), and if true, closes the window using gui.closeWindowFromRef. onOpen() initializes a VerticalList with padding 8 and height 300, adds a Label centered with yellow text stating errors occurred and directing to logs, adds a Button with icon at position (0,0) sized (16,16), sets its action to openLog, finishes the list center-aligned, assigns it as window.rootComponent, adjusts contentSize based on component positions plus padding, and calls gui.updateWindowPositions. onClose() safely deinitializes the rootComponent if present.

## Code Example
```zig
pub fn deinit() void {
	fileExplorerIcon.deinit();
}
```

## Related Questions
- What happens when controller mappings are downloaded?
- How is the error message displayed in the window?
- Which function opens the logs directory?
- What is the purpose of the padding constant?
- How does onOpen initialize the VerticalList?
- Where is the fileExplorerIcon texture loaded from?
- What occurs when onClose is called?
- Does update() modify window content size dynamically?
- Is gui.updateWindowPositions always called in onOpen?
- Can the error prompt be closed manually before controller mappings download?

*Source: unknown | chunk_id: codebase_src_gui_windows_error_prompt.zig_chunk_0*
