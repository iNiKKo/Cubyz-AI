# [easy/codebase_src_gui_windows_social.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI Window, Settings Management, Event Handling, Copy Public Key, Logout
**Symbols:** settings, Vec2f, GuiWindow, window, padding, logoutButton, inGameDisabled
**Concepts:** GUI, Social Settings, Networking, Authentication

## Summary
Handles GUI window for social settings and actions

## Explanation
This chunk defines a GUI window for managing social settings. It initializes a `GuiWindow` with a fixed content size of (128, 256) and sets properties like `closeIfMouseIsGrabbed`. The window contains components such as CheckBoxes, Buttons, and a VerticalList to manage various settings and actions. Specifically:

- A CheckBox for toggling streamer mode (`main.settings.streamerMode`) with an event handler that saves the setting.
- Another CheckBox for displaying player index after their name (`main.settings.showPlayerIndexWithName`), also saving the setting.
- A Button to copy a public key, which is disabled if `KeyCollection.initialized` is false. The button action retrieves and copies the public key using `main.network.authentication.KeyCollection.getPublicKey()`.
- A Button for changing player name, which is disabled when in-game (`inGameDisabled = main.game.world != null`).
- A Logout Button that disables itself if either `inGameDisabled` or `KeyCollection.initialized` is false. The button action resets authentication and saves settings.

The window's size is dynamically updated based on its content, and the root component is set to a VerticalList containing all these components. Event handlers are defined for toggling streamer mode, displaying player index with names, copying public key, changing name, and logging out.

## Code Example
```zig
fn toggleStreamerMode(value: bool) void {
	main.settings.streamerMode = value;
	main.settings.save();
}

fn toggleNamesWithIndex(value: bool) void {
	main.settings.showPlayerIndexWithName = value;
	main.settings.save();
}
```

## Related Questions
- What is the exact size of the `GuiWindow`?
- How does the `logoutButton` get disabled in the code?
- Which settings are toggled by the CheckBoxes in the GUI?
- Where is the public key copied from and how is it handled?
- Under what conditions is the 'Change Name' button enabled or disabled?

*Source: unknown | chunk_id: codebase_src_gui_windows_social.zig_chunk_0*
