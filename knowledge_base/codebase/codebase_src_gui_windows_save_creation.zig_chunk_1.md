# [medium/codebase_src_gui_windows_save_creation.zig] - Chunk 1

**Type:** api
**Keywords:** window closure, component deinitialization, resource cleanup, conditional execution, optional chaining
**Symbols:** onClose
**Concepts:** GUI window management, component lifecycle

## Summary
Handles the closure of a GUI window, deinitializing its root component if present.

## Explanation
The chunk contains a single function `onClose` which is responsible for handling the event when a GUI window is closed. It checks if there is a root component associated with the window. If such a component exists, it calls the `deinit` method on this component to properly deinitialize and clean up resources.

## Code Example
```zig
pub fn onClose() void {
	if (window.rootComponent) |*comp| {
		comp.deinit();
	}
}
```

## Related Questions
- What is the purpose of the `onClose` function?
- How does the function handle the presence of a root component?
- What method is called on the root component if it exists?
- Is there any error handling in the `onClose` function?
- Can you explain the use of optional chaining in this code snippet?
- What happens to the window when its root component is deinitialized?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_creation.zig_chunk_1*
