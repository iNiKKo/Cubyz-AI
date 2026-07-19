# [easy/codebase_src_gui_windows_main.zig] - Chunk 0

**Type:** implementation
**Keywords:** window initialization, button callbacks, component deinitialization, authentication handling, multiplayer setup
**Symbols:** window, padding, exitGame, singleplayerSelection, multiplayer, onOpen, onClose
**Concepts:** GUI window management, button actions, menu navigation

## Summary
Handles the main menu window logic for a GUI application.

## Explanation
This chunk defines the main menu window with four buttons: 'Singleplayer', 'Multiplayer', 'Settings', and 'Touch Grass' (the exit-game button, which calls `glfwSetWindowShouldClose`). The `singleplayerSelection` function sets the save-selection window's mode to `.singleplayer` and reopens it. The `multiplayer` function checks if `KeyCollection` is already initialized -- if so, it opens the multiplayer window directly. Otherwise, it branches on `storedAccount.typ`: if `.none` with no stored data, it opens the login window; if `.none` with stored data, it tries to decrypt the Account Code (opening the login window on error, otherwise initializing `KeyCollection` and opening the multiplayer window, logging a warning if decryption produced non-fatal errors); for any other account type, it opens the 'authentication/unlock' window. The `onOpen` function initializes the main menu window with these buttons, setting their positions to `(0, 0)` and actions as specified in the raw content. The `onClose` function deinitializes the root component.

## Code Example
```zig
fn exitGame() void {
	c.glfwSetWindowShouldClose(main.Window.window, c.GLFW_TRUE);
}
```

## Related Questions
- What is the purpose of the `exitGame` function?
- How does the `singleplayerSelection` function work?
- What steps are taken in the `multiplayer` function if authentication is not initialized?
- How is the main menu window initialized in the `onOpen` function?
- What happens when the main menu window is closed?
- How are errors handled during account decryption in the `multiplayer` function?

*Source: unknown | chunk_id: codebase_src_gui_windows_main.zig_chunk_0*
