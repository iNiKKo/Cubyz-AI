# [hard/codebase_src_graphics_Window.zig] - Chunk 1

**Type:** implementation
**Keywords:** keyboard input, game controller, async download, atomic operations, file I/O
**Symbols:** isControllerConnected, wereControllerMappingsDownloaded, ControllerMappingDownloadTask, ControllerMappingDownloadTask.curTimestamp, ControllerMappingDownloadTask.running, ControllerMappingDownloadTask.vtable, ControllerMappingDownloadTask.schedule, ControllerMappingDownloadTask.getPriority, ControllerMappingDownloadTask.isStillNeeded, ControllerMappingDownloadTask.run, ControllerMappingDownloadTask.clean, downloadControllerMappings, updateControllerMappings, init
**Concepts:** input handling, controller mapping update, asynchronous task scheduling

## Summary
Handles keyboard and game controller input, including downloading and updating controller mappings.

## Explanation
The chunk manages keyboard input by checking for changes in key states (pressed or axis values) and updating accordingly. It also handles mouse movement based on UI key inputs when the cursor is not grabbed. For game controllers, it checks if any are connected and whether their mappings have been downloaded. The `ControllerMappingDownloadTask` struct schedules a task to download controller mappings from a URL if needed, handling potential errors during the fetch and write process. It uses an atomic boolean to ensure only one download task runs at a time. The `downloadControllerMappings` function determines if a new download is necessary based on timestamps and joystick presence. The `updateControllerMappings` function updates in-memory controller mappings from a file or environment variable.

## Code Example
```zig
pub fn isControllerConnected() bool {
	return gamepadState.count() > 0;
}
```

## Related Questions
- How does the chunk handle keyboard input state changes?
- What determines if a controller mapping download is necessary?
- What happens if an error occurs during the controller mapping download?
- How are controller mappings updated in-memory?
- What role does the `ControllerMappingDownloadTask` struct play?
- How is the atomic boolean used to manage download tasks?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_1*
