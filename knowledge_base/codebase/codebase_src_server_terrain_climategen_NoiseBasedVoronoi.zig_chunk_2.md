# [hard/codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig] - Chunk 2

**Type:** world_generation
**Keywords:** 2D array, interleaved pattern, smoothing, voronoi distances, cubic interpolation
**Symbols:** GenerationStructure, GenerationStructure.chunks, GenerationStructure.init, GenerationStructure.deinit, smoothInterpolation, findClosestBiomeTo, drawCircleOnTheMap
**Concepts:** terrain generation, Voronoi noise, biome interpolation

## Summary
This chunk defines the `GenerationStructure` struct and its methods for initializing and deinitializing terrain generation, including noise-based Voronoi interpolation for biome sampling.

## Explanation
**Explanation**

The `GenerationStructure` struct manages a 2D array of chunks used in terrain generation. The `init` method initializes these chunks in an interleaved pattern using specific offsets to ensure smooth transitions between biomes. The neighbor offsets are defined as follows:

```zig
const offset: [4][2]u31 = .{
    .{0, 0},
    .{0, 1},
    .{1, 0},
    .{1, 1},
};
const neighborOffsets: [4][]const [2]i32 = .{
    &.{},
    &.{.{0, -1}, .{0, 1}},
    &.{.{-1, 0}, .{1, 0}, .{-1, -1}, .{1, -1}, .{-1, 1}, .{1, 1}},
    &.{.{0, -1}, .{0, 1}, .{-1, 0}, .{1, 0}, .{-1, -1}, .{1, -1}, .{-1, 1}, .{1, 1}},
};
```

The `deinit` method cleans up allocated resources by deinitializing each chunk and the chunks array. The `smoothInterpolation` function performs cubic interpolation for smoother biome transitions using the formula:

```zig
fn smoothInterpolation(x: f32) f32 {
    return x*x*(3 - 2*x);
}
```

The `findClosestBiomeTo` method calculates the closest biome based on Voronoi distances and interpolates properties like height, roughness, hills, and mountains. The `drawCircleOnTheMap` method draws a circle of biomes on the map, considering radius and position adjustments. The biome radius is defined as:

```zig
const relRadius = biomeRadius/terrain.SurfaceMap.MapFragment.biomeSize;
```

The method also adjusts for mismatched biomes if `skipMismatched` is true.

*Source: unknown | chunk_id: codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig_chunk_2*

## Code Example
```zig
pub fn deinit(self: GenerationStructure, allocator: NeverFailingAllocator) void {
	for (self.chunks.mem) |chunk| {
		chunk.deinit(allocator);
	}
	self.chunks.deinit(allocator);
}
```

## Related Questions
- What does the `init` method of `GenerationStructure` do?
- How are chunks initialized in an interleaved pattern?
- What is the purpose of the `smoothInterpolation` function?
- How does the `findClosestBiomeTo` method determine the closest biome?
- What is the role of the `drawCircleOnTheMap` method?
- How does the `deinit` method clean up resources?

*Source: unknown | chunk_id: codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig_chunk_2*
