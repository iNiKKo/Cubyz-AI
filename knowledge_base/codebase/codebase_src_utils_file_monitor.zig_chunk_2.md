# [medium/codebase_src_utils_file_monitor.zig] - Chunk 2

**Type:** implementation
**Keywords:** file system changes, Windows API, FindFirstChangeNotificationA, WaitForMultipleObjects, callback functions
**Symbols:** mutex, justTheHandles, callbacks, notificationHandlers, listenToPath, removePath
**Concepts:** file monitoring, Windows API, directory change notifications

## Summary
Monitors file system changes using Windows API.

## Explanation
This chunk implements a file monitoring system that uses the Windows API to listen for changes in specified directories. It maintains a list of handles and callbacks associated with each directory being monitored. The `listenToPath` function sets up a notification handler for a given path, while `removePath` cleans up resources when a path is no longer needed. The main loop waits for file system changes using `WaitForMultipleObjects`, processes the results, and invokes the appropriate callback functions.

## Code Example
```zig
fn removePath(path: [:0]const u8) void {
		mutex.lock();
		defer mutex.unlock();
		if (notificationHandlers.fetchRemove(path)) |kv| {
			const index = std.mem.indexOfScalar(*DirectoryInfo, callbacks.items, kv.value).?;
			_ = callbacks.swapRemove(index);
			_ = justTheHandles.swapRemove(index);
			if (c.FindCloseChangeNotification(kv.value.notificationHandler) == 0) {
				std.log.err("Error while closing notification handler for path {s}: {}", .{path, std.os.windows.GetLastError()});
			}
			main.globalAllocator.free(kv.key);
			main.globalAllocator.destroy(kv.value);
		} else {
			std.log.err("Tried to remove non-existent notification handler for path {s}", .{path});
		}
	}
```

## Related Questions
- How does the file monitoring system handle multiple directories?
- What happens if a duplicate notification handler is added for the same path?
- How are errors logged in this chunk?
- What Windows API functions are used to monitor directory changes?
- How does the system ensure thread safety when managing resources?
- What steps are taken to clean up resources when a path is removed?

*Source: unknown | chunk_id: codebase_src_utils_file_monitor.zig_chunk_2*
