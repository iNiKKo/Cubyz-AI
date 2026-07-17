# [easy/codebase_src_gui_windows_gpu_performance_measuring.zig] - Chunk 0

**Type:** implementation
**Keywords:** OpenGL, queries, performance, Cubyz, GUI
**Symbols:** Samples, names, buffers, curBuffer, queryObjects, activeSample, window, render
**Concepts:** performance measurement, OpenGL queries, GUI rendering performance

## Summary
Performance measurement for Cubyz GUI windows on Windows GPU

## Explanation
This chunk initializes and manages performance queries for rendering samples in the Cubyz GUI. It uses OpenGL to measure time elapsed during various rendering stages and displays the results.

## Code Example
```zig
pub fn startQuery(sample: Samples) void {
	std.debug.assert(activeSample == null); // There can be at most one active measurement at a time.
	activeSample = sample;
	c.glBeginQuery(c.GL_TIME_ELAPSED, queryObjects[curBuffer][@intFromEnum(sample)]);
}
```

## Related Questions
- How does the performance measurement system work in Cubyz?
- What are the different rendering samples measured by this system?
- Where is the GUI window defined in this codebase?
- How many buffers are used for performance queries?
- What is the purpose of the `activeSample` variable?
- How are OpenGL queries started and stopped?
- What is the format of the time results retrieved from OpenGL queries?
- Where is the total rendering time displayed on the GUI?
- How does the code handle multiple active measurements simultaneously?
- What is the purpose of the `window` struct in this codebase?
- How are the performance query objects created and deleted?
- What is the default size of the GUI window?

*Source: unknown | chunk_id: codebase_src_gui_windows_gpu_performance_measuring.zig_chunk_0*
