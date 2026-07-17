# [hard/codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig] - Chunk 0

**Type:** algorithm
**Keywords:** BiomePoint, checkIfBiomeIsValid, getStartCoordinate, voronoiDistanceFunction, sorted list insertion, binary search, overlap validation, radius exclusion
**Symbols:** Chunk, BiomePoint, getStartCoordinate, checkIfBiomeIsValid, voronoiDistanceFunction, lessThan
**Concepts:** Voronoi seeding, biome overlap validation, Perlin-like noise, sorted list insertion, binary search for x-coordinate range, radius-based exclusion zones

## Summary
This chunk implements a noise-based Voronoi terrain generation system that seeds biomes using Perlin-like noise and iteratively validates placements against existing biome radii to prevent overlap.

## Explanation
The chunk defines the Chunk struct with wx, wy coordinates, a sorted list of BiomePoint entries (biome pointer, height, position, weight, radius), and maxBiomeRadius. It exposes init(allocator, tree, worldSeed, wx, wy, neighbors) which allocates a new Chunk, seeds biomes via TreeNode.getBiome using Perlin-like noise with seed derived from worldSeed and chunk coordinates, computes biome radius as drawnBiome.radius plus a random variation scaled by drawnBiome.radiusVariation, then repeatedly checks validity: checkIfBiomeIsValid is called against the local selectedBiomes list (sorted by x) to find insertion start via getStartCoordinate, and also checked against each neighbor's biomesSortedByX; if any biome overlaps beyond minDistance = (radius + other.radius)*0.85, placement is rejected and rejections counter increments up to 100 attempts. Valid placements insert a new BiomePoint into selectedBiomes using insertSorted with computed height from random float scaled by drawnBiome.maxHeight - minHeight plus minHeight, weight as 1/sqrt(pi*radius^2), and radius. After the loop, selectedBiomes is converted to an owned slice via toOwnedSlice and stored in Chunk.biomesSortedByX. The chunk also defines BiomePoint with a voronoiDistanceFunction that computes Euclidean distance scaled by weight (self.weight * sqrt((self.pos - pos).lengthSquare)), and lessThan comparing x-coordinate for sorting. getStartCoordinate performs a binary search over biomesSortedByX to find the first entry where pos[0] >= minX, using mid = (start + end)/2 - 1 and adjusting start/end until range <= 16. checkIfBiomeIsValid uses @ceil on biomeRadius, computes minX/maxX bounds relative to chunkLocalMaxBiomeRadius, finds insertion index via getStartCoordinate, then iterates from that index forward breaking when other.pos[0] >= maxX; for each candidate it checks if the squared distance between (x,y) and other.pos is less than minDistance^2. The Chunk struct is returned by init after allocating memory with NeverFailingAllocator. No public API beyond init is exposed here, but the chunk provides internal utilities for biome placement validation and sorting.

## Code Example
```zig
pub fn lessThan(lhs: @This(), rhs: @This()) bool {
	return lhs.pos[0] < rhs.pos[0];
}
```

## Related Questions
- How does the Chunk struct store biomes and what is the purpose of maxBiomeRadius?
- What is the role of getStartCoordinate in validating biome placements against existing ones?
- Explain how checkIfBiomeIsValid determines whether a new biome overlaps with any existing biome.
- Describe the calculation performed by voronoiDistanceFunction and why it uses weight scaling.
- How does BiomePoint.height derive from drawnBiome.maxHeight, drawnBiome.minHeight, and random noise?
- What is the purpose of the rejections counter in Chunk.init and how many attempts are made before failing?
- Why is selectedBiomes sorted by x-coordinate and how does that affect binary search performance?
- How does the chunk handle neighbor validation when placing a biome in a multi-chunk world?
- What memory allocation strategy is used for Chunk.biomesSortedByX after insertion loop completes?
- Does the chunk expose any public functions besides init, and what are their signatures?

*Source: unknown | chunk_id: codebase_src_server_terrain_climategen_NoiseBasedVoronoi.zig_chunk_0*
