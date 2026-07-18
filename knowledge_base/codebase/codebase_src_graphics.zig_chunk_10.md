# [hard/codebase_src_graphics.zig] - Chunk 10

**Type:** implementation
**Keywords:** color manipulation, OpenGL rendering, text shadows, glyph drawing, viewport settings
**Symbols:** shadowColor, renderShadow
**Concepts:** text rendering, shadows, OpenGL

## Summary
Handles text rendering and shadow effects for graphical display.

## Explanation
This chunk contains functions responsible for rendering text with shadows. The `shadowColor` function calculates a shadow color based on the perceived brightness of the original color, making dark colors white for better readability. The `renderShadow` function duplicates much of the logic in the main render function but applies the shadow effect by adjusting colors and positions. It uses OpenGL to set up rendering states, bind textures, and draw glyphs with modified effects.

## Code Example
```zig
fn shadowColor(color: u24) u24 {
		const r: f32 = @floatFromInt(color >> 16);
		const g: f32 = @floatFromInt(color >> 8 & 255);
		const b: f32 = @floatFromInt(color & 255);
		const perceivedBrightness = @sqrt(0.299*r*r + 0.587*g*g + 0.114*b*b);
		if (perceivedBrightness < 64) {
			return 0xffffff; // Make shadows white for better readability.
		} else {
			return 0;
		}
	}
```

## Related Questions
- How is the shadow color calculated?
- What changes are made to the rendering state in `renderShadow`?
- How does the function handle line wrapping and text positioning?
- What OpenGL functions are used for setting up the render pipeline?
- How is the perceived brightness of a color determined?
- What modifications are applied to glyphs when rendering shadows?
- How does the function manage memory allocation for line wraps?
- What is the purpose of the `shadowColor` function in text rendering?
- How does the function ensure that the original rendering state is restored after shadow rendering?
- What role do uniform variables play in the OpenGL setup?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_10*
