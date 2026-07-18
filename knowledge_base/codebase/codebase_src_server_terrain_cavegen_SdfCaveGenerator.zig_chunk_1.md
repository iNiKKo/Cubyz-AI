# [medium/codebase_src_server_terrain_cavegen_SdfCaveGenerator.zig] - Chunk 1

**Type:** world_generation
**Keywords:** Signed Distance Function, trilinear interpolation, voxel processing, noise generation, map fragment
**Symbols:** generateMap
**Concepts:** cave generation, SDF, noise

## Summary
Generates a cave map fragment using SDF (Signed Distance Function) and noise.

## Explanation
The `generateMap` function is responsible for generating a cave map fragment using Signed Distance Functions (SDF) and noise. It calculates the outer size, generates aligned noise, and processes each voxel to determine if it belongs to a cave or not. The function uses trilinear interpolation to handle details and skips fully inside or outside cave regions.

## Code Example
```zig
fn generateMap(map: *CaveMapFragment, output: Array3D(f32), biomeNoiseStrength: Array3D(f32), worldSeed: u64, comptime mode: Mode) void {
	const outerSize = map.pos.voxelSize*interpolatedPart;
	const outerSizeShift = std.math.log2_int(u31, outerSize);
	const outerSizeFloat: f32 = @floatFromInt(outerSize);

	const noise = FractalNoise3D.generateAligned(main.stackAllocator, map.pos.wx, map.pos.wy, map.pos.wz, outerSize, CaveMapFragment.width*map.pos.voxelSize/outerSize + 1, CaveMapFragment.width*map.pos.voxelSize/outerSize + 1, CaveMapFragment.height*map.pos.voxelSize/outerSize + 1, worldSeed ^ 4329561871 ^ 112*@intFromEnum(mode), noiseScale);
	defer noise.deinit(main.stackAllocator);

	for (noise.mem, output.mem, biomeNoiseStrength.mem) |*val, sdfVal, noiseStrength| {
		val.* = val.*/noiseScale*noiseStrength + sdfVal - @as(f32, @floatFromInt(map.pos.voxelSize - 1));
	}

	var x: u31 = 0;
	while (x < map.pos.voxelSize*CaveMapFragment.width) : (x += outerSize) {
		var y: u31 = 0;
		while (y < map.pos.voxelSize*CaveMapFragment.width) : (y += outerSize) {
			var z: u31 = 0;
			while (z < map.pos.voxelSize*CaveMapFragment.height) : (z += outerSize) {
				const val000 = getValue(noise, outerSizeShift, x, y, z);
				const val001 = getValue(noise, outerSizeShift, x, y, z + outerSize);
				const val010 = getValue(noise, outerSizeShift, x, y + outerSize, z);
				const val011 = getValue(noise, outerSizeShift, x, y + outerSize, z + outerSize);
				const val100 = getValue(noise, outerSizeShift, x + outerSize, y, z);
				const val101 = getValue(noise, outerSizeShift, x + outerSize, y, z + outerSize);
				const val110 = getValue(noise, outerSizeShift, x + outerSize, y + outerSize, z);
				const val111 = getValue(noise, outerSizeShift, x + outerSize, y + outerSize, z + outerSize);
				// Test if they are all inside or all outside the cave to skip these cases:
				const measureForEquality = @as(f32, sign(val000)) + @as(f32, sign(val001)) + @as(f32, sign(val010)) + @as(f32, sign(val011)) + @as(f32, sign(val100)) + @as(f32, sign(val101)) + @as(f32, sign(val110)) + @as(f32, sign(val111));
				if (measureForEquality == 8) {
					// No cave in here :)
					continue;
				}
				if (measureForEquality == -8) {
					// All cave in here :)
					var dx: u31 = 0;
					while (dx < outerSize) : (dx += map.pos.voxelSize) {
						var dy: u31 = 0;
						while (dy < outerSize) : (dy += map.pos.voxelSize) {
							mode.modifyRange(map, x + dx, y + dy, z, z + outerSize);
						}
					}
				} else {
					// Uses trilinear interpolation for the details.
					// Luckily due to the blocky nature of the game there is no visible artifacts from it.
					var dx: u31 = 0;
					while (dx < outerSize) : (dx += map.pos.voxelSize) {
						var dy: u31 = 0;
						while (dy < outerSize) : (dy += map.pos.voxelSize) {
							const ix = @as(f32, @floatFromInt(dx))/outerSizeFloat;
							const iy = @as(f32, @floatFromInt(dy))/outerSizeFloat;
							const lowerVal = ((1 - ix)*(1 - iy)*val000 + (1 - ix)*iy*val010 + ix*(1 - iy)*val100 + ix*iy*val110);
							const upperVal = ((1 - ix)*(1 - iy)*val001 + (1 - ix)*iy*val011 + ix*(1 - iy)*val101 + ix*iy*val111);
							// TODO: Determine the range that needs to be removed, and remove it in one go.
							if (upperVal*lowerVal > 0) { // All z values have the same sign → the entire column is the same.
								if (upperVal < 0) {
									// All cave in here :)
									mode.modifyRange(map, x + dx, y + dy, z, z + outerSize);
								} else {
									// No cave in here :)
								}
							} else {
								// Could be more efficient, but I'm lazy right now and I'll just go through the entire range:
								var dz: u31 = 0;
								while (dz < outerSize) : (dz += map.pos.voxelSize) {
									const iz = @as(f32, @floatFromInt(dz))/outerSizeFloat;
									const val = (1 - iz)*lowerVal + iz*upperVal;
									if (val < 0) {
										mode.modifyRange(map, x + dx, y + dy, z + dz, z + dz + map.pos.voxelSize);
									}
								}
							}
						}
					}
				}
			}
		}
	}
}
```

## Related Questions
- What is the purpose of the `generateMap` function?
- How does the function generate aligned noise?
- What role does trilinear interpolation play in this code?
- How are cave regions determined and processed?
- What happens if all values in a region have the same sign?
- How is memory managed for the noise object?
- What is the significance of the `map.pos.voxelSize` variable?
- How does the function handle fully inside or outside cave regions?
- What is the role of the `mode.modifyRange` method in this code?
- How is the outer size calculated and used in the function?

*Source: unknown | chunk_id: codebase_src_server_terrain_cavegen_SdfCaveGenerator.zig_chunk_1*
