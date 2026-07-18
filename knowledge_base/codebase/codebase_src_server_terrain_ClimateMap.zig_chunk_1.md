# [medium/codebase_src_server_terrain_ClimateMap.zig] - Chunk 1

**Type:** world_generation
**Keywords:** array manipulation, map stitching, fragment reuse, coordinate calculation, offset handling
**Symbols:** getBiomeMap, NeverFailingAllocator, Array2D, BiomeSample, ClimateMapFragment, MapFragment
**Concepts:** world_generation, biome generation

## Summary
Generates a biome map by stitching together smaller climate fragments.

## Explanation
The `getBiomeMap` function creates a large 2D array of biome samples based on smaller, pre-generated climate fragments. It calculates the starting and ending coordinates for these fragments relative to the requested area. The function iterates over each fragment, copying relevant biome data into the final map while adjusting for offsets. This approach allows efficient generation of large maps by reusing existing climate data.

## Code Example
```zig
pub fn getBiomeMap(allocator: NeverFailingAllocator, wx: i32, wy: i32, width: u31, height: u31) Array2D(BiomeSample) {
	const map = Array2D(BiomeSample).init(allocator, width >> MapFragment.biomeShift, height >> MapFragment.biomeShift);
	const wxStart = wx & ~ClimateMapFragment.mapMask;
	const wzStart = wy & ~ClimateMapFragment.mapMask;
	const wxEnd = wx +% width & ~ClimateMapFragment.mapMask;
	const wzEnd = wy +% height & ~ClimateMapFragment.mapMask;
	var x = wxStart;
	while (wxEnd -% x >= 0) : (x +%= ClimateMapFragment.mapSize) {
		var y = wzStart;
		while (wzEnd -% y >= 0) : (y +%= ClimateMapFragment.mapSize) {
			const mapPiece = getOrGenerateFragment(x, y);
			// Offset of the indices in the result map:
			const xOffset = (x -% wx) >> MapFragment.biomeShift;
			const yOffset = (y -% wy) >> MapFragment.biomeShift;
			// Go through all indices in the mapPiece:
			for (&mapPiece.map, 0..) |*col, lx| {
				const resultX = @as(i32, @intCast(lx)) + xOffset;
				if (resultX < 0 or resultX >= width >> MapFragment.biomeShift) continue;
				for (col, 0..) |*spot, ly| {
					const resultY = @as(i32, @intCast(ly)) + yOffset;
					if (resultY < 0 or resultY >= height >> MapFragment.biomeShift) continue;
					map.set(@intCast(resultX), @intCast(resultY), spot.*);
				}
			}
		}
	}
	return map;
}
```

## Related Questions
- What is the purpose of the `getBiomeMap` function?
- How does the function determine the starting and ending coordinates for climate fragments?
- What role do offsets play in copying biome data from fragments to the final map?
- How does the function handle cases where the resultX or resultY indices are out of bounds?
- What is the significance of `MapFragment.biomeShift` in this code?
- How does the function ensure efficient generation of large maps?

*Source: unknown | chunk_id: codebase_src_server_terrain_ClimateMap.zig_chunk_1*
