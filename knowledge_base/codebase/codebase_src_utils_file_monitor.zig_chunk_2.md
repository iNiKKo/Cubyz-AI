# [medium/codebase_src_utils_file_monitor.zig] - Chunk 2

**Type:** implementation
**Keywords:** Windows API, FindFirstChangeNotificationA, FindNextChangeNotification, StringHashMap, ListManaged, mutex locking
**Symbols:** WindowsImpl, WindowsImpl.HANDLE, WindowsImpl.notificationHandlers, WindowsImpl.callbacks, WindowsImpl.justTheHandles, WindowsImpl.mutex, WindowsImpl.DirectoryInfo, WindowsImpl.DirectoryInfo.callback, WindowsImpl.DirectoryInfo.userData, WindowsImpl.DirectoryInfo.notificationHandler, WindowsImpl.DirectoryInfo.needsUpdate, WindowsImpl.DirectoryInfo.path, WindowsImpl.init, WindowsImpl.deinit, WindowsImpl.handleEvents, WindowsImpl.listenToPath, WindowsImpl.removePath
**Concepts:** file system monitoring, directory change notifications

## Summary
The WindowsImpl struct manages file system change notifications on Windows, using handles and callbacks.

## Explanation
The WindowsImpl struct provides functionality to monitor directories for changes on a Windows platform. It uses the Windows API functions like FindFirstChangeNotificationA and FindNextChangeNotification to set up and handle directory change notifications. The struct maintains several data structures: notificationHandlers (a StringHashMap mapping paths to DirectoryInfo), callbacks (a ListManaged of DirectoryInfo pointers), and justTheHandles (a ListManaged of HANDLEs). It also uses a mutex for thread safety when accessing these shared resources. The init function initializes these data structures, while deinit cleans them up. The handleEvents function waits for directory changes and invokes the appropriate callback when a change is detected. The listenToPath function adds a new path to be monitored, and removePath removes an existing path from monitoring.

## Code Example
```zig
fn init() void {
	notificationHandlers = .init(main.globalAllocator.allocator);
	callbacks = .init(main.globalAllocator);
	justTheHandles = .init(main.globalAllocator);
}
```

## Related Questions
- How does WindowsImpl initialize its data structures?
- What is the purpose of the mutex in WindowsImpl?
- How does WindowsImpl handle directory change notifications?
- What happens if a duplicate path is added to be monitored?
- How are resources cleaned up when WindowsImpl deinitializes?
- What error handling is implemented for Windows API calls?

*Source: unknown | chunk_id: codebase_src_utils_file_monitor.zig_chunk_2*
