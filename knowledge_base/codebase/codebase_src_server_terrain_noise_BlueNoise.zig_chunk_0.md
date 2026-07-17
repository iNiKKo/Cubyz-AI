# [easy/codebase_src_server_terrain_noise_BlueNoise.zig] - Chunk 0

**Type:** world_generation
**Keywords:** blue noise, feature grid, seeded random, neighbor check, distance limit, aligned blocks, packed coordinates, runtime safety, allocator ownership, pattern array, compression masks, region data
**Symbols:** sizeShift, size, sizeMask, featureShift, featureSize, featureMask, pattern, load, sample, getRegionData
**Concepts:** noise generation, grid sampling, terrain features, region extraction, random seeding, coordinate compression

## Summary
Loads a pre-seeded noise map and provides region sampling for terrain generation.

## Explanation
The chunk defines constants sizeShift=7, featureShift=2, and derives size, sizeMask, featureSize, featureMask. It declares a global var pattern: [size*size]u8 initialized to undefined. The public function load() sets runtime safety off, seeds random with 54095248685739, runs repetitions=4 of iterations=16 passes over the grid; each pass picks a random point and attempts to move it by checking all neighbors within dx/dy in [-2..2], computing neighbor coordinates using sizeShift/featureShift masks, calculating squared distance from (xOffset,yOffset), and continuing only if distSqr < 8. After the inner loops finish, pattern[i] is set to the point and break exits the iteration loop. The sample(x,y) function reads a compressed coordinate from pattern. getRegionData(allocator,x,y,width,height) aligns x/y down to feature boundaries using featureMask, computes xMin/xMax/yMin/yMax, allocates a main.List(u32), iterates over aligned blocks, calls sample on each block's top-left, decodes the 8-bit value into (val>>3,val&7) offsets, adds those to local coordinates, and appends packed u32 results if they fall within the requested width/height. Finally it returns result.toOwnedSlice(allocator).

## Related Questions
- What is the default seed value used by load() and why is runtime safety disabled?
- How does load() ensure the pattern grid becomes valid after each repetition?
- Why are repetitions set to 4 and iterations to 16 in this implementation?
- What coordinate transformation does sample(x,y) perform on its arguments?
- Explain how getRegionData aligns input coordinates before sampling the pattern.
- What happens inside the innermost loop of load() when a neighbor fails the distance check?
- How are the packed u32 results constructed from xRes and yRes in getRegionData?
- Why does getRegionData use featureMask to compute xMin/xMax/yMin/yMax?
- Is pattern ever initialized before load() is called, or only after load()? What is its initial state?
- What would happen if distSquareLimit were increased beyond 8 in the neighbor check?
- How does the break statement affect control flow after setting pattern[i] = point?
- Does getRegionData guarantee that returned coordinates are within [0,width) × [0,height)?

*Source: unknown | chunk_id: codebase_src_server_terrain_noise_BlueNoise.zig_chunk_0*
