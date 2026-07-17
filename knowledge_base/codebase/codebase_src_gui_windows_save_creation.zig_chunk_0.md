# [medium/codebase_src_gui_windows_save_creation.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, event callbacks, seed generation, world settings, window lifecycle
**Symbols:** window, padding, nameInput, seedInput, gamemodeInput, worldSettings, ZonMapEntry, worldPresets, selectedPreset, defaultPreset, presetButton, chooseSeed, gamemodeCallback, worldPresetCallback, allowCheatsCallback, testingModeCallback, createWorld, onOpen, onClose
**Concepts:** GUI window management, user input handling, world creation settings, error handling

## Summary
Handles the creation of a new world in the GUI.

## Explanation
This chunk manages the logic for creating a new world through a graphical user interface. It initializes various GUI components such as text inputs, buttons, and checkboxes to gather user input for world settings like name, seed, gamemode, and presets. The `chooseSeed` function determines the seed value based on user input or generates a random one. Callback functions handle changes in gamemode, preset selection, and cheat/testing mode toggles. The `createWorld` function processes the collected data to attempt creating a new world, handling any errors that occur during the process. The `onOpen` method initializes the GUI window with all necessary components, while `onClose` deinitializes them when the window is closed.

## Code Example
```zig
fn chooseSeed(seedStr: []const u8) u64 {
	if (seedStr.len == 0) {
		return main.random.nextInt(u64, &main.seed);
	} else {
		return std.fmt.parseInt(u64, seedStr, 0) catch {
			return std.hash.Wyhash.hash(0, seedStr);
		};
	}
}
```

## Related Questions
- What is the purpose of the `chooseSeed` function?
- How does the GUI handle user input for world settings?
- What happens when a new world creation fails?
- How are presets sorted and displayed in the GUI?
- What components are initialized in the `onOpen` method?
- How is memory managed for temporary strings in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_creation.zig_chunk_0*
