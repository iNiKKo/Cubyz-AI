# [medium/codebase_src_gui_windows_save_selection.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, world list, button callbacks, texture initialization, thread spawning, directory navigation
**Symbols:** window, padding, width, buttonNameArena, needsUpdate, mode, deleteIcon, fileExplorerIcon, WorldInfo, worldList, init, deinit, openWorld, openWorldWrap, deleteWorld, openFolder, update
**Concepts:** GUI window management, world selection and interaction, texture handling, networking for world opening

## Summary
Handles the save selection GUI window, managing world list display and interaction.

## Explanation
This chunk defines the logic for a GUI window responsible for saving selections. It includes functions to initialize and deinitialize textures, open worlds with specific parameters, delete worlds through confirmation windows, navigate folders using file paths, and refresh the window state if needed. The `window` variable is initialized with a content size of Vec2f{128, 256}. The `WorldInfo` struct contains fields for lastUsedTime (i64), name ([]const u8), and fileName ([]const u8). The `openWorld` function initializes a connection manager, starts the server thread with parameters including world name, port number, and mode. Error handling is implemented to log errors encountered during initialization of connections, starting threads, renaming threads, opening worlds, and navigating directories. Specific error messages are logged for each failure point.

## Code Example
```zig
pub fn init() void {
	deleteIcon = Texture.initFromFile("assets/cubyz/ui/delete_icon.png");
	fileExplorerIcon = Texture.initFromFile("assets/cubyz/ui/file_explorer_icon.png");
}
```

## Related Questions
- What is the content size of the save selection GUI window?
- How does the `WorldInfo` struct define world information?
- What parameters are used in starting a server thread when opening a world?
- How are errors handled during the process of opening a world?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_selection.zig_chunk_0*
