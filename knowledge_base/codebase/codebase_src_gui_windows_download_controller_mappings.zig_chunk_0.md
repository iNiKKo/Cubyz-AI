# [easy/codebase_src_gui_windows_download_controller_mappings.zig] - Chunk 0

**Type:** implementation
**Keywords:** controller mapping download, window close, label initialization, component management, window size update
**Symbols:** files, settings, Vec2f, GuiComponent, GuiWindow, window, padding, update, onOpen, onClose
**Concepts:** controller mappings, download, window management, label display

## Summary
Downloads controller mappings and closes the window if they are already downloaded.

## Explanation
The `update` function checks if controller mappings have been downloaded. If so, it closes the window using `gui.closeWindowFromRef`. The `onOpen` function initializes a label displaying 'Downloading controller mappings...' and sets it as the root component of the window. It updates the window's size based on the label's position and size. The `onClose` function deinitializes the label if it exists.

## Code Example
```zig
pub fn update() void {
    if (main.Window.Gamepad.wereControllerMappingsDownloaded()) {
        gui.closeWindowFromRef(&window);
    }
}
```

## Related Questions
- What is the purpose of the `update` function in this chunk?
- How does the `onOpen` function initialize and set the root component of the window?
- What is the role of the `padding` variable in this chunk?
- What is the condition checked in the `update` function?
- What action is taken if controller mappings are downloaded?
- What happens when the window is closed?
- How is the label deinitialized in the `onClose` function?
- What is the purpose of the `window` variable in this chunk?
- How does the `window.contentSize` get updated in the `onOpen` function?
- What are the components used to create the window and its content?
- What is the relationship between the `update`, `onOpen`, and `onClose` functions?
- How does the `gui.closeWindowFromRef` function work?

*Source: unknown | chunk_id: codebase_src_gui_windows_download_controller_mappings.zig_chunk_0*
