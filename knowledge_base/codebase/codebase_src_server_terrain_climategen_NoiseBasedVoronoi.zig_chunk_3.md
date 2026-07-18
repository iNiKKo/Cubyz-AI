# [hard/codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig] - Chunk 3

**Type:** world_generation
**Keywords:** random number generation, vector math, biome sampling, map manipulation, assertions
**Symbols:** drawCircleOnTheMap, addSubBiomesOf, addTransitionBiomes
**Concepts:** terrain generation, climate simulation, Voronoi diagrams

## Summary
This chunk implements noise-based Voronoi climate generation for terrain in the Cubyz engine.

## Explanation
The chunk contains functions for determining the closest biome point, drawing circles on a pre-map with biome data, adding sub-biomes to a map, and handling transition biomes. It uses random number generation, vector math, and assertions for validation. The primary responsibility is generating climate data based on Voronoi noise patterns.

## Code Example
```zig
fn drawCircleOnTheMap(preMap: *[preMapSize][preMapSize]BiomeSample, biome: *const Biome, biomeRadius: f32, wx: i32, wy: i32, width: u31, height: u31, pos: Vec2i, comptime skipMismatched: bool, parentBiome: *const Biome) !void {
		const relPos = @as(Vec2f, @floatFromInt(pos -% Vec2i{wx, wy}))/@as(Vec2f, @splat(terrain.SurfaceMap.MapFragment.biomeSize));
		const relRadius = biomeRadius/terrain.SurfaceMap.MapFragment.biomeSize;
		const min = @floor(@max(Vec2f{0, 0}, relPos - @as(Vec2f, @splat(relRadius))));
		const max = @ceil(@min(@as(Vec2f, @floatFromInt(Vec2i{width, height}))/@as(Vec2f, @splat(terrain.SurfaceMap.MapFragment.biomeSize)), relPos + @as(Vec2f, @splat(relRadius))));
		if (skipMismatched) {
			var x: f32 = min[0];
			while (x < max[0]) : (x += 1) {
				const yOffset: f32 = @mod(x, 2)*0.5;
				var y: f32 = min[1] + yOffset;
				while (y < max[1]) : (y += 1) {
					const distSquare = vec.lengthSquare(Vec2f{x, y} - relPos);
					if (distSquare < relRadius*relRadius) {
						if (preMap[@trunc(x)][@trunc(y)].biome != parentBiome) {
							return error.biomeMismatch;
						}
					}
				}
			}
		}
		var x: f32 = min[0];
		while (x < max[0]) : (x += 1) {
			const yOffset: f32 = @mod(x, 2)*0.5;
			var y: f32 = min[1] + yOffset;
			while (y < max[1]) : (y += 1) {
				const distSquare = vec.lengthSquare(Vec2f{x, y} - relPos);
				if (distSquare < relRadius*relRadius) {
					const entry = &preMap[@trunc(x)][@trunc(y)];
					var seed = entry.seed;
					const newHeight = @as(f32, @floatFromInt(biome.minHeight)) + @as(f32, @floatFromInt(biome.maxHeight - biome.minHeight))*random.nextFloat(&seed);
					entry.* = .{
						.biome = biome,
						.roughness = std.math.lerp(biome.roughness, entry.roughness, biome.keepOriginalTerrain),
						.hills = std.math.lerp(biome.hills, entry.hills, biome.keepOriginalTerrain),
						.mountains = std.math.lerp(biome.mountains, entry.mountains, biome.keepOriginalTerrain),
						.height = std.math.lerp(newHeight, entry.height, biome.keepOriginalTerrain),
						.seed = entry.seed,
					};
				}
			}
		}
	}
```

## Related Questions
- What is the purpose of the `drawCircleOnTheMap` function?
- How does the `addSubBiomesOf` function determine the number of sub-biomes to add?
- What assertion checks are performed in this chunk?
- How is the height calculated for a biome sample in the pre-map?
- What role do transition biomes play in the climate generation process?
- How does the chunk handle cases where adding sub-biomes fails?

*Source: unknown | chunk_id: codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig_chunk_3*
