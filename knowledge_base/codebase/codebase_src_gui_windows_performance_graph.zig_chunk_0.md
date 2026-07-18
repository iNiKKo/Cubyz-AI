# [easy/codebase_src_gui_windows_performance_graph.zig] - Chunk 0

**Type:** implementation
**Keywords:** performance graph, SSBO, pipeline, uniforms, line rendering
**Symbols:** init, deinit, render
**Concepts:** performance graph, SSBO, pipeline, uniforms, line rendering

## Summary
Performance graph rendering

## Explanation
This chunk initializes and renders a performance graph. It uses an SSBO to store frame times, binds a pipeline for rendering lines, sets uniforms for screen dimensions, start position, dimension, points, offset, and line color, and draws the graph on the window.

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
