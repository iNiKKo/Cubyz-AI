# [hard/codebase_src_renderer_lighting.zig] - Chunk 4

**Type:** implementation
**Keywords:** vector operations, light interpolation, mesh data access, light packing, block positions
**Symbols:** LightVector, getValues, getLightAt, getCornerLight, getLightSampleAligned, packLightValues, getLight
**Concepts:** chunk meshing, lighting calculations, interpolation, rendering

## Summary
Handles lighting calculations for chunk meshes in the Cubyz voxel engine by defining functions to get light values at specific positions, interpolate light across corners, handle aligned normals, and pack light values into a format suitable for rendering. It includes detailed bit manipulations and vector operations.

## Explanation
This chunk defines several functions to calculate and retrieve lighting values for blocks within a chunk mesh in the Cubyz voxel engine. The primary responsibility is to ensure accurate and efficient lighting calculations based on block positions and mesh data.

### Functions Overview:
- **getValues(mesh: *ChunkMesh, pos: chunk.BlockPos)**
  - Retrieves both block light and sun light values at a given position within the mesh.
  - Asserts that the CPU architecture is little-endian.
  - Combines block light and sun light into a single `u64` value using bitwise operations and returns it as an `@Vector(8, u8)`.

- **getLightAt(parent: *ChunkMesh, x: i32, y: i32, z: i32)**
  - Calculates the light values at a specific position within or neighboring the chunk mesh.
  - Uses bitwise operations to determine if the queried position is within the current chunk and retrieves light data accordingly.

- **getCornerLight(parent: *ChunkMesh, pos: Vec3i, normal: Vec3f)**
  - Interpolates light values across corners of a block based on its position and normal vector.
  - Calculates interpolated positions and weights for each corner and aggregates the light values using these weights.

- **getLightSampleAligned(parent: *ChunkMesh, pos: Vec3i, direction: chunk.Neighbor)**
  - Retrieves aligned lighting samples along a specified direction from a given position.
  - Adjusts lighting based on differences between adjacent blocks if voxel size is 1.

- **packLightValues(rawVals: [4]LightVector)**
  - Packs light values into a format suitable for rendering by shifting and combining bits of each `u8` component in the `LightVector` array.

- **getLight(parent: *ChunkMesh, blockPos: Vec3i, textureIndex: u16, quadIndex: QuadIndex)**
  - Retrieves lighting values for a specific block position based on its texture index and quad information.
  - Uses precomputed samples if the normal direction is aligned; otherwise, it interpolates light across corners or vertices depending on conditions.

## Code Example
```zig
fn getValues(mesh: *ChunkMesh, pos: chunk.BlockPos) LightVector {
	const blockLight = mesh.lightingData[0].getValue(pos);
	const sunLight = mesh.lightingData[1].getValue(pos);
	std.debug.assert(builtin.cpu.arch.endian() == .little);
	const totalLight = @as(u64, sunLight.raw()) | (@as(u64, blockLight.raw()) << 32);
	return @as(@Vector(8, u8), @bitCast(totalLight));
}
```

## Related Questions
- What is the purpose of the `getValues` function?
- How does the `getCornerLight` function calculate light values?
- What data structure is used to store light vectors?
- How are lighting values packed for rendering in the `packLightValues` function?
- What conditions trigger the use of the fast path for aligned normals in the `getLight` function?
- How does the engine handle lighting calculations for blocks with texture occlusion disabled?

*Source: unknown | chunk_id: codebase_src_renderer_lighting.zig_chunk_4*
