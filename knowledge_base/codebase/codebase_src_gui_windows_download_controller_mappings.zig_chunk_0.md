# [easy/codebase_src_gui_windows_download_controller_mappings.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, Label, onOpen, update, onClose, deinit, padding, rootComponent, closeable, contentSize
**Symbols:** files, settings, Vec2f, GuiComponent, GuiWindow, window, padding, update, onOpen, onClose
**Concepts:** GUI window management, controller mappings download UI, component lifecycle hooks, label initialization, window size adjustment, download completion check

## Summary
This chunk defines the GUI window controller for displaying and managing downloaded gamepad mappings, handling initialization with a label, size adjustments, and closing logic based on download completion.

## Explanation
The chunk imports main modules (files, settings, Vec2f) and GUI components (GuiWindow, GuiComponent, Button, CheckBox, Label, VerticalList, HorizontalList). It declares a global window variable of type GuiWindow with fixed content size {128,64}, background enabled, and non-closeable. The update function checks if main.Window.Gamepad.wereControllerMappingsDownloaded() returns true; if so it closes the window via gui.closeWindowFromRef(&window). The onOpen function initializes a Label with padding 8 and text 'Downloading controller mappings...', sets it as the root component, adjusts content size to fit the label plus padding, and calls gui.updateWindowPositions(). The onClose function safely deinitializes the root component if present.

## Related Questions
- What is the default content size of the window declared in this chunk?
- Which GUI component is used to display the download status message?
- Under what condition does the update function close the window?
- How is the window's root component initialized when the window opens?
- Does the window allow users to close it manually, and how is that configured?
- What happens to the root component during onClose if it exists?
- Which imported module provides the Vec2f type used for sizing?
- How does onOpen adjust the content size after setting the label?
- Is there any logic in this chunk that handles errors from the download check?
- What padding value is applied to the label and window sizing calculations?

*Source: unknown | chunk_id: codebase_src_gui_windows_download_controller_mappings.zig_chunk_0*
