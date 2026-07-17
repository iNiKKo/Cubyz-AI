# [easy/codebase_src_gui_windows_advanced_controls.zig] - Chunk 0

**Type:** implementation
**Keywords:** gui, controls, settings, callbacks, slider
**Symbols:** settings, Vec2f, GuiComponent, GuiWindow, window, padding, delayCallback, delayFormatter, speedCallback, speedFormatter, onOpen, onClose
**Concepts:** advanced controls window, continuous sliders, settings update

## Summary
Advanced controls window implementation

## Explanation
This chunk defines the advanced controls window, which includes two continuous sliders for repeat delay and speed settings. It handles user input through callbacks and updates the settings accordingly.

## Code Example
```zig
fn delayFormatter(allocator: main.heap.NeverFailingAllocator, value: f32) []const u8 {
	return std.fmt.allocPrint(allocator.allocator, "#ffffffPlace/Break Delay: {d:.0} ms", .{value/1.0e6}) catch unreachable;
}
```

## Related Questions
- What is the purpose of the `delayCallback` function?
- How does the `delayFormatter` function format the repeat delay value?
- What is the initial value of the repeat delay setting in nanoseconds?
- Which components are added to the vertical list in the `onOpen` function?
- What is the size of the window after it is opened?
- What is the purpose of the `onClose` function?
- How does the `onClose` function handle the root component?
- What is the initial position and size of the window before it is opened?
- Which components are used to create the advanced controls window?
- What is the purpose of the `padding` variable?
- What is the range of values for the repeat delay slider in nanoseconds?
- What is the range of values for the repeat speed slider in nanoseconds?

*Source: unknown | chunk_id: codebase_src_gui_windows_advanced_controls.zig_chunk_0*
