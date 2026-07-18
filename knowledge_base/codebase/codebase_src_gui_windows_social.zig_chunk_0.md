# [easy/codebase_src_gui_windows_social.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI Window, Settings Management, Event Handling, Copy Public Key, Logout
**Symbols:** settings, Vec2f, GuiWindow, window, padding, logoutButton, inGameDisabled
**Concepts:** GUI, Social Settings, Networking, Authentication

## Summary
Handles GUI window for social settings and actions

## Explanation
This chunk defines a GUI window for managing social settings, including options to toggle streamer mode, display player index with names, copy public key, change name, and logout. It initializes various components like CheckBoxes, Buttons, and VerticalList, sets up event handlers for button actions, and updates the window size based on its content.

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
- What is the purpose of the `toggleStreamerMode` function?
- How does the `logoutButton` get disabled in the code?
- What components are added to the VerticalList in the `onOpen` function?
- What is the condition for enabling or disabling the 'Change Name' button?
- Where is the `copy` function defined and what does it do?
- How is the window size updated after adding components?
- What is the purpose of the `update` function in this chunk?
- Which settings are toggled by the CheckBoxes in the GUI?
- What is the condition for enabling or disabling the 'Logout' button?
- Where is the `onClose` function defined and what does it do?
- How is the window's root component set after adding components?
- What is the purpose of the `VerticalList.init` call in the `onOpen` function?

*Source: unknown | chunk_id: codebase_src_gui_windows_social.zig_chunk_0*
