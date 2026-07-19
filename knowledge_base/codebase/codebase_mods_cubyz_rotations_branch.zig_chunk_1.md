# [hard/codebase_mods_cubyz_rotations_branch.zig] - Chunk 1

**Type:** implementation
**Keywords:** quads, rotation, pattern determination, connectivity checking, switch statement
**Symbols:** addQuads, getPattern
**Concepts:** chunk meshing, branch patterns, connectivity data

## Summary
This chunk defines functions for determining and adding branch patterns based on connectivity data.

## Explanation
This chunk defines functions for determining and adding branch patterns based on connectivity data. The `addQuads` function takes a pattern, side, radius, output list, and texture slot offset to add rotated quads to the output list. It uses specific coordinates and dimensions to define each quad shape depending on the pattern type (dot, halfLine, line, bend, intersection, cross) as follows:

- **Dot**: Defined by coordinates `.{min, min}`, `.{min, max}`, `.{max, min}`, `.{max, max}`.
- **HalfLine**: Defined by coordinates `.{min, 0.0}`, `.{min, max}`, `.{max, 0.0}`, `.{max, max}`.
- **Line**: Defined by coordinates `.{min, 0.0}`, `.{min, 1.0}`, `.{max, 0.0}`, `.{max, 1.0}`.
- **Bend**: Defined by coordinates `.{0.0, 0.0}`, `.{0.0, max}`, `.{max, 0.0}`, `.{max, max}`.
- **Intersection**: Defined by coordinates `.{0.0, 0.0}`, `.{0.0, max}`, `.{1.0, 0.0}`, `.{1.0, max}`.
- **Cross**: Defined by coordinates `.{0.0, 0.0}`, `.{0.0, 1.0}`, `.{1.0, 0.0}`, `.{1.0, 1.0}`.

The `getPattern` function determines the branch pattern based on connectivity data for different directions (positive and negative X and Y) as follows:

- For zero connections (`count == 0`), if the side is not connected, it returns `.dot`. Otherwise, it returns null.
- For one connection (`count == 1`), it determines the direction based on which neighbor is connected and returns `.halfLine` with that direction.
- For two connections (`count == 2`), if both positive and negative X or Y are connected, it returns `.line`. Otherwise, it calculates a bend pattern based on connectivity data.
- For three connections (`count == 3`), it determines the direction by checking which neighbor is not connected and returns `.intersection` with that direction.
- For four connections (`count == 4`), it returns `.cross`.

## Code Example
```zig
fn addQuads(pattern: Pattern, side: Neighbor, radius: f32, out: *main.ListManaged(main.models.QuadInfo), textureSlotOffset: u32) void {
	const min: f32 = (8.0 - radius)/16.0;
	const max: f32 = (8.0 + radius)/16.0;
	switch (pattern) {
		.dot => {
			out.append(rotateQuad(.{
				.{min, min},
				.{min, max},
				.{max, min},
				.{max, max},
			}, pattern, min, max, side, textureSlotOffset));
		},
		.halfLine => {
			out.append(rotateQuad(.{
				.{min, 0.0},
				.{min, max},
				.{max, 0.0},
				.{max, max},
			}, pattern, min, max, side, textureSlotOffset));
		},
		.line => {
			out.append(rotateQuad(.{
				.{min, 0.0},
				.{min, 1.0},
				.{max, 0.0},
				.{max, 1.0},
			}, pattern, min, max, side, textureSlotOffset));
		},
		.bend => {
			out.append(rotateQuad(.{
				.{0.0, 0.0},
				.{0.0, max},
				.{max, 0.0},
				.{max, max},
			}, pattern, min, max, side, textureSlotOffset));
		},
		.intersection => {
			out.append(rotateQuad(.{
				.{0.0, 0.0},
				.{0.0, max},
				.{1.0, 0.0},
				.{1.0, max},
			}, pattern, min, max, side, textureSlotOffset));
		},
		.cross => {
			out.append(rotateQuad(.{
				.{0.0, 0.0},
				.{0.0, 1.0},
				.{1.0, 0.0},
				.{1.0, 1.0},
			}, pattern, min, max, side, textureSlotOffset));
		},
	}
}
```

## Related Questions
- What does the `addQuads` function do?
- How does the `getPattern` function determine the branch pattern?
- What are the possible patterns returned by `getPattern`?
- What is the role of the `rotateQuad` function in this chunk?
- How is connectivity data used to decide the pattern?
- What is the significance of the `radius` parameter in `addQuads`?
- How does the switch statement in `addQuads` handle different patterns?
- What conditions lead to a null return from `getPattern`?
- How are directions determined in the `getPattern` function?
- What is the structure of the output list in `addQuads`?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_branch.zig_chunk_1*
