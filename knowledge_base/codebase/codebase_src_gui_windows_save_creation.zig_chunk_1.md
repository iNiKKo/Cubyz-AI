# [medium/codebase_src_gui_windows_save_creation.zig] - Chunk 1

**Type:** implementation
**Keywords:** CheckBox, Button, TextInput, HorizontalList, worldSettings, build_options, tagged release, preset selection, seed input, UI layout
**Symbols:** allowCheatsCallback, testingModeCallback, worldPresetCallback, createWorld
**Concepts:** GUI window creation, preset selection, seed input validation, conditional build features

## Summary
This chunk implements the GUI window for creating a new world, including controls for cheats, testing mode, preset selection, and seed input.

## Explanation
The code builds a list of UI components to construct a world creation form. It adds a CheckBox for 'Allow Cheats' bound to worldSettings.allowCheats with the allowCheatsCallback. If not in tagged release build, it conditionally adds another CheckBox for 'Testing mode (for developers)' bound to worldSettings.testingMode with testingModeCallback. A Button labeled with the key of the currently selected preset from worldPresets is created and wired to worldPresetCallback; this button is added to the list. A Label 'Seed:' is instantiated, followed by a TextInput that accepts up to 22 characters (seed length) and triggers createWorld on newline or submit. These two are wrapped in a HorizontalList which is then positioned at (.center). The Create World Button is added next. Finally, list.finish(.center) centers the entire form, window.rootComponent is set to the resulting component, contentSize is computed by adding padding around the rootComponent's position and size, and gui.updateWindowPositions() is called to apply layout updates.

## Related Questions
- What callback is invoked when the user changes the 'Allow Cheats' checkbox?
- Under what build condition is the 'Testing mode (for developers)' checkbox omitted from the UI?
- Which preset key string is displayed on the preset selection button?
- How many characters are allowed in the seed input field before it stops accepting text?
- What action triggers when the user submits or presses Enter in the seed input?
- Where does the final world creation form get positioned within its window?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_creation.zig_chunk_1*
