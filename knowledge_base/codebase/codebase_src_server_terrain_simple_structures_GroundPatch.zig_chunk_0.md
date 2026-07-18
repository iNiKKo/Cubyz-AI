# [easy/codebase_src_server_terrain_simple_structures_GroundPatch.zig] - Chunk 0

**Type:** implementation
**Keywords:** ground patch, block placement, elliptical distribution, terrain generation logic, randomization
**Symbols:** GroundPatch, loadModel, generate
**Concepts:** terrain generation, block placement, elliptical distribution

## Summary
GroundPatch generation logic in Cubyz terrain that defines elliptical distribution of blocks with specified dimensions and orientation based on parameters loaded from a ZonElement.

## Explanation
This chunk defines the GroundPatch structure and its generation logic. It loads parameters such as block type, width, variation, depth, and smoothness from a ZonElement. The generate function calculates the patch's dimensions and orientation using these parameters and iterates over a specified area in the chunk to apply the block at different heights based on an elliptical distribution.

The GroundPatch structure is defined with the following fields:
- `block`: main.blocks.Block (default value loaded from ZonElement)
- `width`: f32 (default 5.0 if not specified)
- `variation`: f32 (default 1.0 if not specified)
- `depth`: i32 (default 2 if not specified)
- `smoothness`: f32 (default 0.0 if not specified)

The generate function calculates the width and orientation of the ellipse, then iterates over a specified area in the chunk to apply the block at different heights based on an elliptical distribution. The smoothness parameter affects the placement of blocks within the ellipse.

Specifically:
- `width`: Determines the size of the patch.
- `variation`: Adds randomness to the width.
- `depth`: Controls how deep into the chunk the blocks are placed.
- `smoothness`: Influences the density and distribution of blocks within the ellipse.

## Code Example
```zig
pub fn generate(self: *GroundPatch, mode: GenerationMode, x: i32, y: i32, z: i32, chunk: *main.chunk.ServerChunk, caveMap: CaveMapView, caveBiomeMap: CaveBiomeMapView, seed: *u64, _: bool) void {
	const width = self.width + (random.nextFloat(seed) - 0.5)*self.variation;
	const orientation = 2*std.math.pi*random.nextFloat(seed);
	const ellipseParam = 1 + random.nextFloat(seed);

	// Orientation of the major and minor half axis of the ellipse.
	// For now simply use a minor axis 1/ellipseParam as big as the major.
	const xMain = @sin(orientation)/width;
	const yMain = @cos(orientation)/width;
	const xSecn = ellipseParam*@cos(orientation)/width;
	const ySecn = -ellipseParam*@sin(orientation)/width;

	const xMin = @max(0, x - @as(i32, @ceil(width)));
	const xMax = @min(chunk.super.width, x + @as(i32, @ceil(width)));
	const yMin = @max(0, y - @as(i32, @ceil(width)));
	const yMax = @min(chunk.super.width, y + @as(i32, @ceil(width)));

	var baseHeight = z;
	if (mode != .water_surface) {
		if (caveMap.isSolid(x, y, baseHeight)) {
			baseHeight = caveMap.findTerrainChangeAbove(x, y, baseHeight) - 1;
		} else {
			baseHeight = caveMap.findTerrainChangeBelow(x, y, baseHeight);
		}
	}

	var px = chunk.startIndex(xMin);
	while (px < xMax) : (px += 1) {
		var py = chunk.startIndex(yMin);
		while (py < yMax) : (py += 1) {
			const mainDist = xMain*@as(f32, @floatFromInt(x - px)) + yMain*@as(f32, @floatFromInt(y - py));
			const secnDist = xSecn*@as(f32, @floatFromInt(x - px)) + ySecn*@as(f32, @floatFromInt(y - py));
			const dist = mainDist*mainDist + secnDist*secnDist;
			if (dist <= 1) {
				var startHeight = z;

				if (mode == .water_surface) {
					startHeight -%= 1;
					startHeight &= ~chunk.super.voxelSizeMask;
				} else {
					if (caveMap.isSolid(px, py, startHeight)) {
						startHeight = caveMap.findTerrainChangeAbove(px, py, startHeight) -% 1;
					} else {
						startHeight = caveMap.findTerrainChangeBelow(px, py, startHeight);
					}
				}
				var pz = chunk.startIndex(startHeight - self.depth + 1);
				if (mode == .water_surface) {
					const surfaceHeight = caveBiomeMap.getSurfaceHeight(chunk.super.pos.wx + px, chunk.super.pos.wy + py) & ~chunk.super.voxelSizeMask;
					pz = @max(pz, surfaceHeight -% chunk.super.pos.wz);
				}
				if (@abs(startHeight -% baseHeight) > 5) continue;
				while (pz <= startHeight) : (pz += chunk.super.pos.voxelSize) {
					if (dist <= self.smoothness or (dist - self.smoothness)/(1 - self.smoothness) < random.nextFloat(seed)) {
						if (chunk.liesInChunk(px, py, pz)) {
							chunk.updateBlockInGeneration(px, py, pz, self.block);
						}
					}
				}
			}
		}
	}
}
```

## Related Questions
- What is the default value for the width parameter if not specified?
- How does the variation parameter affect the placement of blocks?
- What is the purpose of the depth parameter in GroundPatch generation?
- How does the smoothness parameter influence block distribution within the ellipse?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_GroundPatch.zig_chunk_0*
