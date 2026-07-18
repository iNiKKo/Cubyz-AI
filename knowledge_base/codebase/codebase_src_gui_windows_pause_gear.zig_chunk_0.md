# [easy/codebase_src_gui_windows_pause_gear.zig] - Chunk 0

**Type:** api
**Keywords:** GUI window, texture initialization, component setup, event handling, resource management
**Symbols:** window, padding, messageTimeout, messageFade, mutexComponent, history, expirationTime, historyStart, fadeOutEnd, input, hideInput, pauseIcon, init, deinit, onOpen, onClose
**Concepts:** GUI window management, texture handling, button component, window lifecycle events

## Summary
Manages the pause gear GUI window, including initialization, deinitialization, and handling of open/close events.

## Explanation
This chunk defines a GUI window for the pause gear in the Cubyz engine. `init` loads the texture `"assets/cubyz/ui/pause_icon.png"` into `pauseIcon`; `deinit` releases it. The `onOpen` method creates a 64x64 icon button using `pauseIcon` that opens the `"pause"` window when clicked, sets it as the window's root component, and sets `window.contentSize` to the button's size. The `onClose` method deinitializes the root component of the window when it is closed.

## Code Example
```zig
pub fn deinit() void {
	pauseIcon.deinit();
}
```

## Related Questions
- What is the purpose of the `init` function in this chunk?
- How does the `onOpen` method configure the pause gear window?
- What resources are cleaned up when the pause gear window is closed?
- What texture file is used for the pause icon?
- How is the content size of the window adjusted on open?
- What components are managed by this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_pause_gear.zig_chunk_0*
