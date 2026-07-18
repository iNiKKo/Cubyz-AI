# [easy/codebase_src_gui_windows_gpu_performance_measuring.zig] - Chunk 0

**Type:** implementation
**Keywords:** OpenGL, query objects, performance measurement, GUI window, rendering stages
**Symbols:** Samples, names, buffers, curBuffer, queryObjects, activeSample, init, deinit, startQuery, stopQuery, window
**Concepts:** GPU performance measurement, OpenGL query objects, GUI rendering

## Summary
This chunk manages GPU performance measurement for various rendering stages in the Cubyz engine.

## Explanation
The chunk defines an enumeration `Samples` listing different rendering samples to measure. It initializes OpenGL query objects to track time elapsed for each sample. Functions `startQuery` and `stopQuery` manage starting and stopping these measurements. The `render` function updates a GUI window displaying the measured times for each sample, cycling through multiple buffers to average results over time.

## Code Example
```zig
pub fn init() void {
	for (&queryObjects) |*buf| {
		c.glGenQueries(buf.len, buf);
		for (buf) |queryObject| { // Start them to get an initial value.
			c.glBeginQuery(c.GL_TIME_ELAPSED, queryObject);
			c.glEndQuery(c.GL_TIME_ELAPSED);
		}
	}
}
```

## Related Questions
- What are the different rendering samples measured by this chunk?
- How many buffers are used for averaging results?
- What function initializes OpenGL query objects?
- How does the chunk manage starting and stopping performance measurements?
- What GUI window is updated with the measured times?
- How are the measured times displayed in the GUI window?

*Source: unknown | chunk_id: codebase_src_gui_windows_gpu_performance_measuring.zig_chunk_0*
