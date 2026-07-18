# [medium/codebase_src_gui_windows_save_creation.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, event callbacks, seed generation, world creation, preset management
**Symbols:** window, padding, nameInput, seedInput, gamemodeInput, worldSettings, ZonMapEntry, worldPresets, selectedPreset, defaultPreset, presetButton, chooseSeed, gamemodeCallback, worldPresetCallback, allowCheatsCallback, testingModeCallback, createWorld, onOpen
**Concepts:** GUI window management, user input handling, world creation settings, preset selection

## Summary
Handles the creation of a new world in the GUI.

## Explanation
This chunk manages the logic for creating a new world through a graphical user interface. It initializes various GUI components such as text inputs, buttons, and checkboxes to collect user input for world settings like name, seed, gamemode, and presets. The `chooseSeed` function determines the seed value based on user input or generates a random one. Callback functions handle changes in gamemode selection, preset selection, and cheat/testing mode toggles. The `createWorld` function processes the collected data to create a new world using the server's world creation API. The `onOpen` method initializes the GUI window with all necessary components and sets up their interactions.

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
- How does the GUI handle user input for world creation?
- What are the callback functions used in this chunk and what do they do?
- How is the seed value determined when creating a new world?
- What components are initialized in the `onOpen` method?
- How are presets managed and selected in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_creation.zig_chunk_0*
