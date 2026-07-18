# [medium/codebase_src_gui_windows_save_selection.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, world list, button callbacks, texture initialization, thread spawning, directory navigation
**Symbols:** window, padding, width, buttonNameArena, needsUpdate, mode, deleteIcon, fileExplorerIcon, WorldInfo, worldList, init, deinit, openWorld, openWorldWrap, deleteWorld, openFolder, update
**Concepts:** GUI window management, world selection and interaction, texture handling, networking for world opening

## Summary
Handles the save selection GUI window, managing world list display and interaction.

## Explanation
This chunk defines the logic for a GUI window responsible for saving selections. It includes functions to initialize and deinitialize textures, open worlds, delete worlds, and navigate folders. The `update` function refreshes the window state if needed. The chunk manages a list of world information and uses various components like buttons, labels, and text inputs for user interaction.

## Code Example
```zig
pub fn init() void {
	deleteIcon = Texture.initFromFile("assets/cubyz/ui/delete_icon.png");
	fileExplorerIcon = Texture.initFromFile("assets/cubyz/ui/file_explorer_icon.png");
}
```

## Related Questions
- How does the `init` function initialize textures?
- What is the purpose of the `openWorldWrap` function?
- How does the `deleteWorld` function handle world deletion confirmation?
- What components are used in the save selection GUI window?
- How is the `update` function triggered to refresh the window state?
- What error handling is implemented when opening a world?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_selection.zig_chunk_0*
