# [hard/codebase_src_graphics_Window.zig] - Chunk 2

**Type:** implementation
**Keywords:** gamepad, keyboard, HTTP download, atomic operations, thread pool, file I/O
**Symbols:** isControllerConnected, wereControllerMappingsDownloaded, ControllerMappingDownloadTask, ControllerMappingDownloadTask.curTimestamp, ControllerMappingDownloadTask.running, ControllerMappingDownloadTask.vtable, ControllerMappingDownloadTask.schedule, ControllerMappingDownloadTask.getPriority, ControllerMappingDownloadTask.isStillNeeded, ControllerMappingDownloadTask.run, ControllerMappingDownloadTask.clean, downloadControllerMappings, updateControllerMappings, init, deinit, GamepadAxis, GamepadAxis.axis, GamepadAxis.positive, Key, Key.name, Key.pressed, Key.isToggling, Key.modsOnPress, Key.value, Key.key, Key.gamepadAxis, Key.gamepadButton, Key.mouseButton, Key.scancode
**Concepts:** input handling, controller mappings, HTTP requests, resource management

## Summary
Handles gamepad and keyboard input, including downloading and updating controller mappings.

## Explanation
This chunk manages gamepad and keyboard inputs within the Cubyz engine. It includes functions to check if a controller is connected (`isControllerConnected`), whether controller mappings have been downloaded (`wereControllerMappingsDownloaded`), and to schedule and execute the download of controller mappings (`downloadControllerMappings`). The `ControllerMappingDownloadTask` struct defines the task for downloading mappings, including scheduling, running the download via HTTP, writing the file, and cleaning up after completion. The `updateControllerMappings` function updates the in-memory gamepad mappings using either a custom configuration or the downloaded mappings file. Initialization (`init`) and deinitialization (`deinit`) functions manage resources related to gamepad state.

The `schedule` method of `ControllerMappingDownloadTask` schedules the download task, ensuring that only one download is running at a time. The `run` method performs the HTTP GET request to fetch controller mappings from a specified URL and writes them to a file. If an error occurs during the download or file writing process, it logs the error. After successful completion, it updates the in-memory mappings.

The `downloadControllerMappings` function checks if the current timestamp is more than 7 days since the last download or if any joystick present is not recognized as a gamepad, triggering a new download. The `updateControllerMappings` function reads the downloaded mappings file and updates the in-memory mappings using GLFW's `glfwUpdateGamepadMappings` function.

Atomic operations are used to manage the state of running tasks and ensure thread safety. The thread pool (`main.threadPool`) is utilized to execute the controller mapping download task asynchronously.

## Code Example
```zig
pub fn isControllerConnected() bool {
	return gamepadState.count() > 0;
}
```

## Related Questions
- How do you check if a controller is connected?
- What function schedules the download of controller mappings?
- Where does the engine store downloaded controller mappings?
- How does the engine handle errors during the download process?
- What is the purpose of the `updateControllerMappings` function?
- How does the engine manage gamepad state initialization and deinitialization?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_2*
