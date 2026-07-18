# [easy/codebase_src_gui_windows_performance_graph.zig] - Chunk 0

**Type:** implementation
**Keywords:** performance graph, SSBO, pipeline, uniforms, line rendering
**Symbols:** init, deinit, render
**Concepts:** performance graph, SSBO, pipeline, uniforms, line rendering

## Summary
Performance graph rendering

## Explanation
This chunk initializes and renders a performance graph. Frame times are stored in a fixed-size ring buffer of **2048** samples (`lastFrameTime: [2048]f32`), with `index` tracking the current write position (also passed to the shader as the `offset` uniform so it knows where the ring buffer wraps). `init` creates an SSBO and a graphics pipeline from `graph.vert`/`graph.frag` shaders (cull mode none, no depth test/write, alpha blending). `render` appends the latest frame time (`main.lastFrameTime`, converted to milliseconds), draws "32 ms"/"16 ms"/"00 ms" reference labels and gridlines, then binds the pipeline and sets uniforms: `points` (2048), `offset` (`index`), `lineColor` (`1, 1, 1` -- white), `screen` (window width/height), `start`/`dimension` (the graph's position and size within an 8px `border`), before drawing the line via `GL_LINE_STRIP`. `deinit` releases the SSBO.

## Code Example
```zig
pub fn init() void {
	ssbo = graphics.SSBO.init();
	pipeline = graphics.Pipeline.init(
		"assets/cubyz/shaders/graphics/graph.vert",
		"assets/cubyz/shaders/graphics/graph.frag",
		"",
		&uniforms,
		graphics.VertexArray.EmptyVertex,
		&.{},
		.{.cullMode = .none},
		.{.depthTest = false, .depthWrite = false},
		.{.attachments = &.{.alphaBlending}},
	);
}
```

## Related Questions
- What is the purpose of the `init` function in this chunk?
- How does the `render` function calculate and draw the performance graph?
- What are the uniforms used for in the `render` function?
- How many frame times are stored in the SSBO?
- What is the offset value used in the `render` function?
- What color is the line rendered in the `render` function?
- How is the graph position and dimension calculated in the `render` function?
- What is the screen dimensions used for in the `render` function?
- How are the frame times stored in the SSBO?
- What is the purpose of the `deinit` function in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_performance_graph.zig_chunk_0*
