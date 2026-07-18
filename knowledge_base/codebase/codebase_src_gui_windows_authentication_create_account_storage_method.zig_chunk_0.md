# [easy/codebase_src_gui_windows_authentication_create_account_storage_method.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, button click, component initialization, window positioning, deinitialization
**Symbols:** window, padding, next, onOpen, onClose
**Concepts:** GUI component management, user input handling, window lifecycle

## Summary
Handles the GUI logic for selecting account storage methods during account creation.

## Explanation
This chunk defines a GUI window that allows users to choose how they want to store their Account Code. It includes a vertical list of buttons, each corresponding to a different storage method: **"Password Manager (recommended)"** (the recommended default), "Save as file", and "Write it down yourself". The `next` function is called when a button is clicked, which closes the current window, sets the selected storage method, and opens the next relevant window (`"authentication/create_account_account_code"`). The `onOpen` function initializes the GUI components and layout when the window is opened, while the `onClose` function deinitializes them when the window is closed.

## Code Example
```zig
fn next(storageMethod: usize) void {
	gui.closeWindowFromRef(&window);
	gui.windowlist.@"authentication/create_account_account_code".setStorageMethod(@enumFromInt(storageMethod));
	gui.openWindow("authentication/create_account_account_code");
}
```

## Related Questions
- What is the purpose of the `next` function?
- How does the GUI window handle user input for selecting storage methods?
- What components are initialized when the window opens?
- What happens to the GUI components when the window closes?
- How is the content size of the window determined?
- Which storage method is recommended by default?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_create_account_storage_method.zig_chunk_0*
