# [medium/codebase_src_utils_file_monitor.zig] - Chunk 0

**Type:** implementation
**Keywords:** inotify_init, FIONREAD, ioctl, StringHashMap, AutoHashMap, mutex locking, needsUpdate flag, recursive scanning, callback deduplication, error handling
**Symbols:** CallbackFunction, Impl, NoImpl, LinuxImpl, DirectoryInfo, init, deinit, handleEvents, listenToPath, removePath
**Concepts:** file system monitoring, inotify integration, cross-platform abstraction, recursive directory watching, thread-safe event handling, callback invocation, error logging, memory allocation with global allocator

## Summary
Implements cross-platform file system monitoring via inotify on Linux, providing initialization, deinitialization, event handling, and path registration with recursive directory watching.

## Explanation
The chunk defines a public API surface (init, deinit, handleEvents, listenToPath, removePath) that delegates to an OS-specific Impl selected at compile time via builtin.os.tag. For LinuxImpl it declares global state: fd (the inotify file descriptor), watchDescriptors (a StringHashMap mapping path strings to DirectoryInfo structs), callbacks (an AutoHashMap from FD to DirectoryInfo), and a mutex for thread safety. The init function calls c.inotify_init, logs errors on failure, then allocates the two hashmaps using main.globalAllocator. deinit closes fd with c.close, logging errors, then iterates watchDescriptors freeing each entry's allocated path string, calling deinit on each DirectoryInfo (which frees its own watchDescriptors list), and finally destroying both hashmaps. handleEvents locks the mutex, checks available bytes via ioctl(FIONREAD), allocates a buffer for events, reads from fd, parses inotify_event structs by casting the buffer, skips entries where no callback is registered, sets needsUpdate=true on directories (IN_ISDIR mask), collects callbacks into triggeredCallbacks to avoid duplicate invocations. For each collected callback it checks needsUpdate; if true it calls updateRecursiveCallback which re-adds all watched descriptors under that path after recursively scanning subdirectories. After unlocking the mutex it invokes the user-provided callback with userData, then relocks before continuing. The chunk also defines NoImpl as a struct with empty stub implementations for all public functions to satisfy the API when not on Windows or Linux.

## Related Questions
- What happens when inotify initialization fails on Linux?
- How are watched directories recursively added to the monitor?
- Why is a triggeredCallbacks hashmap used inside handleEvents?
- Under what condition does updateRecursiveCallback get invoked?
- Which global allocator is used for hashmaps and why?
- What fields does DirectoryInfo contain and how are they freed?
- How does the chunk ensure thread safety when invoking callbacks?
- What stub implementation is provided for non-Linux/Windows targets?
- How does handleEvents parse raw inotify_event data from the buffer?
- What error logging pattern is used throughout LinuxImpl functions?

*Source: unknown | chunk_id: codebase_src_utils_file_monitor.zig_chunk_0*
