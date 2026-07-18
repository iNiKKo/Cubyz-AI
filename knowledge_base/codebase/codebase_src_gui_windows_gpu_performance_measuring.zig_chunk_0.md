# [easy/codebase_src_gui_windows_gpu_performance_measuring.zig] - Chunk 0

**Type:** implementation
**Keywords:** OpenGL, query objects, performance measurement, GUI window, rendering stages
**Symbols:** Samples, names, buffers, curBuffer, queryObjects, activeSample, init, deinit, startQuery, stopQuery, window
**Concepts:** GPU performance measurement, OpenGL query objects, GUI rendering

## Summary
This chunk manages GPU performance measurement for various rendering stages in the Cubyz engine.

## Explanation
This chunk manages GPU performance measurement for various rendering stages in the Cubyz engine. It defines an enumeration `Samples` with specific values representing different rendering stages: screenbuffer clear, clear, skybox, pre-processing block animations, chunk rendering preparation, chunk rendering, entity rendering, block entity rendering, particle rendering, transparent rendering preparation, transparent rendering, bloom extract downsample, bloom first pass, bloom second pass, copy to screen, and GUI rendering. The chunk initializes OpenGL query objects for each sample using `init` function which generates 4 buffers of query objects. Functions `startQuery` and `stopQuery` manage starting and stopping these measurements by asserting that only one measurement can be active at a time. The `render` function updates a GUI window displaying the measured times for each sample, cycling through multiple buffers to average results over time.

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

*Source: unknown | chunk_id: codebase_src_gui_windows_gpu_performance_measuring.zig_chunk_0*
