# [hard/codebase_src_graphics.zig] - Chunk 10

**Type:** implementation
**Keywords:** color manipulation, OpenGL rendering, text shadows, glyph drawing, viewport settings
**Symbols:** shadowColor, renderShadow
**Concepts:** text rendering, shadows, OpenGL

## Summary
Handles text rendering and shadow effects for graphical display.

## Explanation
This chunk contains functions responsible for rendering text with shadows. The `shadowColor` function calculates a shadow color based on the perceived brightness of the original color, making dark colors white for better readability. The `renderShadow` function duplicates much of the logic in the main render function but applies the shadow effect by adjusting colors and positions. It uses OpenGL to set up rendering states, bind textures, and draw glyphs with modified effects.

The `shadowColor` function calculates the perceived brightness using the formula: `@sqrt(0.299*r*r + 0.587*g*g + 0.114*b*b)`, where `r`, `g`, and `b` are the red, green, and blue components of the color, respectively. If the perceived brightness is less than 64, the shadow color is set to white (`0xffffff`). Otherwise, it is set to black (`0x000000`).

The `renderShadow` function sets up the rendering state by translating and scaling the drawing context. It then iterates over each line of text, calculating the start and end positions for each line segment based on line breaks. For each glyph in a line, it retrieves the corresponding font glyph, applies the shadow color modification to the font effect, and draws the glyph at the adjusted position. The function also handles memory allocation for line wraps using `main.stackAllocator.alloc(f32, self.lineBreaks.items.len - 1)` and ensures that the original rendering state is restored after shadow rendering using `defer` statements.

The OpenGL functions used for setting up the render pipeline include `glGetIntegerv`, `glUniform2f`, `glUniform1f`, `glUniform1ui`, `glActiveTexture`, and `glBindTexture`. Uniform variables are used to pass values such as the scene dimensions, aspect ratio, color, and texture to the shader program.

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
