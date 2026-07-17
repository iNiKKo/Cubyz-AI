# [easy/codebase_src_gui_windows_performance_graph.zig] - Chunk 0

**Type:** implementation
**Keywords:** SSBO, GL_LINE_STRIP, frame times, uniforms, rendering
**Symbols:** window, lastFrameTime, index, ssbo, pipeline, border, uniforms
**Concepts:** performance graph, SSBO, GL_LINE_STRIP

## Summary
Performance graph rendering

## Explanation
This chunk initializes and renders a performance graph window. It uses an SSBO to store frame times, binds a pipeline for drawing lines, sets uniforms for screen dimensions, positions, and colors, and draws the graph using GL_LINE_STRIP.

## Code Example
```zig
pub fn render() void {
	lastFrameTime[index] = @floatCast(main.lastFrameTime.load(.monotonic)*1000.0);
	index = (index + 1)%@as(u31, @intCast(lastFrameTime.len));
	draw.text("32 ms", 0, 16, 8);
	draw.text("16 ms", 0, 32, 8);
	draw.text("00 ms", 0, 48, 8);
	{
		const oldColor = draw.setColor(0x80ffffff);
		defer draw.restoreColor(oldColor);
		draw.line(.{border, 24}, .{window.contentSize[0] - border, 24});
		draw.line(.{border, 40}, .{window.contentSize[0] - border, 40});
		draw.line(.{border, 56}, .{window.contentSize[0] - border, 56});
	}
	pipeline.bind(null);
	c.glUniform1i(uniforms.points, lastFrameTime.len);
	c.glUniform1i(uniforms.offset, index);
	c.glUniform3f(uniforms.lineColor, 1, 1, 1);
	var pos = Vec2f{border, border};
	var dim = window.contentSize - @as(Vec2f, @splat(2*border));
	pos *= @splat(draw.setScale(1));
	pos += draw.setTranslation(.{0, 0});
	dim *= @splat(draw.setScale(1));
	pos = @floor(pos);
	dim = @ceil(dim);
	pos[1] += dim[1];

	c.glUniform2f(uniforms.screen, @floatFromInt(main.Window.width), @floatFromInt(main.Window.height));
	c.glUniform2f(uniforms.start, pos[0], pos[1]);
	c.glUniform2f(uniforms.dimension, dim[0], draw.setScale(1));
	ssbo.bufferData(f32, &lastFrameTime);
	ssbo.bind(5);
	c.glDrawArrays(c.GL_LINE_STRIP, 0, lastFrameTime.len);
}
```

## Related Questions
- What is the purpose of the `uniforms` struct in this chunk?
- How does the `render` function calculate the position and dimensions for drawing the graph lines?
- What is the role of the `lastFrameTime` array in this performance graph rendering process?
- How many frames are stored in the `lastFrameTime` array before it overwrites itself?
- What color is used to draw the graph lines?
- Which OpenGL function is used to bind the pipeline for drawing?
- What is the purpose of the `c.glUniform1i` calls in this chunk?
- How are the frame times stored and accessed within the SSBO?
- What is the relationship between the `index` variable and the `lastFrameTime` array?
- Which OpenGL function is used to draw a line strip using the stored frame times?
- What is the purpose of the `draw.line` calls in this chunk?
- How are the positions and dimensions for drawing the graph lines calculated?

*Source: unknown | chunk_id: codebase_src_gui_windows_performance_graph.zig_chunk_0*
