# [medium/codebase_src_utils_file_monitor.zig] - Chunk 1

**Type:** implementation
**Keywords:** inotify, mutex locking, recursive directory traversal, event handling, callback invocation
**Symbols:** LinuxImpl, LinuxImpl.DirectoryInfo, LinuxImpl.DirectoryInfo.callback, LinuxImpl.DirectoryInfo.userData, LinuxImpl.DirectoryInfo.watchDescriptors, LinuxImpl.DirectoryInfo.needsUpdate, LinuxImpl.DirectoryInfo.path, LinuxImpl.fd, LinuxImpl.watchDescriptors, LinuxImpl.callbacks, LinuxImpl.mutex, LinuxImpl.init, LinuxImpl.deinit, LinuxImpl.addWatchDescriptorsRecursive, LinuxImpl.updateRecursiveCallback, LinuxImpl.handleEvents, LinuxImpl.addWatchDescriptor, LinuxImpl.removeWatchDescriptor, LinuxImpl.listenToPath, LinuxImpl.removePath
**Concepts:** file monitoring, inotify API, directory watching, callback management, thread safety

## Summary
The LinuxImpl struct provides functionality for monitoring file system changes using inotify on Linux systems.

## Explanation
This chunk defines a Linux-specific implementation of a file monitor using the inotify API. It includes functions to initialize and deinitialize the inotify instance, add and remove watch descriptors recursively, handle events, and manage callbacks. The `DirectoryInfo` struct holds information about directories being watched, including their paths, associated callback functions, user data, and watch descriptors. The implementation uses a mutex for thread safety, manages memory allocation with global and stack allocators, and logs errors using the standard logging library.

The `init()` function initializes an inotify instance by calling `c.inotify_init()`. If initialization fails, it logs an error message indicating the specific POSIX errno value. The `watchDescriptors` and `callbacks` are initialized as hash maps with global allocators.

The `deinit()` function closes the file descriptor using `c.close(fd)` and logs an error if closing fails. It then iterates through all watch descriptors, freeing associated memory and deinitializing the hash maps.

The `addWatchDescriptorsRecursive()` function recursively adds watch descriptors for directories by opening iterable directories, iterating over entries, and adding subdirectories to be watched. If any errors occur during directory operations or iteration, they are logged with specific error messages.

The `updateRecursiveCallback()` function updates the recursive callback mechanism by removing existing watch descriptors and re-adding them recursively starting from the root path of the directory being monitored.

The `handleEvents()` function processes inotify events by reading available bytes using `c.ioctl(fd, c.FIONREAD, &available)`, then reading events with `c.read(fd, events.ptr, available)`. It logs errors for any issues encountered during these operations. Events are processed to update the `needsUpdate` flag and trigger callbacks if necessary.

The `addWatchDescriptor()` function adds a watch descriptor for a given path using `c.inotify_add_watch(fd, path.ptr, c.IN_CLOSE_WRITE | c.IN_DELETE | c.IN_CREATE | c.IN_MOVE | c.IN_ONLYDIR)`. If adding the watch fails, it logs an error with the specific POSIX errno value.

The `removeWatchDescriptor()` function removes a watch descriptor using `c.inotify_rm_watch(fd, watchDescriptor)` and logs errors if removal fails except for invalid arguments (EINVAL).

The `listenToPath()` function initializes monitoring for a path by creating a `DirectoryInfo` instance with the provided callback and user data. It adds initial watch descriptors recursively and updates them.

The `removePath()` function removes monitoring for a path by removing all associated watch descriptors and freeing allocated memory.

## Code Example
```zig
fn init() void {
	fd = c.inotify_init();
	if (fd == -1) {
		std.log.err("Error while initializing inotifiy: {}", .{std.posix.errno(fd)});
	}
	watchDescriptors = .init(main.globalAllocator.allocator);
	callbacks = .init(main.globalAllocator.allocator);
}
```

## Related Questions
- How does the `LinuxImpl.init()` function initialize inotify, including error handling?
- What specific fields are included in the `DirectoryInfo` struct and what do they represent?
- How is recursive directory traversal implemented for adding watch descriptors?
- What exact error messages are logged during initialization and deinitialization of inotify?
- Which inotify event masks are used when adding a watch descriptor, and how are these events handled?
- How does the `handleEvents()` function process inotify events and manage callbacks?

*Source: unknown | chunk_id: codebase_src_utils_file_monitor.zig_chunk_1*
