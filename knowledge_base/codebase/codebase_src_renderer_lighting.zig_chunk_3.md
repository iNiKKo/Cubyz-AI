# [hard/codebase_src_renderer_lighting.zig] - Chunk 3

**Type:** implementation
**Keywords:** propagateDestructive, textureOcclusionData, lightSampleListForAxisAlignedModels, alignedNormalDirection, hasOnlyCornerVertices, circular buffer queue, mutex locking, corner interpolation, packed light values
**Symbols:** propagateLightsDestructive, LightVector, getValues, getLightAt, getCornerLight, getLightSampleAligned, packLightValues, getLight
**Concepts:** light propagation, neighbor mesh fetching, texture occlusion data, corner interpolation, quad fast paths, mutex locking, destructive updates, ambient occlusion, packed light values

## Summary
Implements lighting propagation and sampling for chunk meshes, including destructive neighbor updates, corner interpolation, texture occlusion handling, and quad-specific fast paths.

## Explanation
The chunk defines a public method propagateLightsDestructive that iterates over an input BlockPos slice, pushes entries into a circular buffer queue with sourceDir=6 and activeValue=0b111, then calls self.propagateDestructive to build constructiveEntries. For each entry it resolves the appropriate channelChunk (sun vs ambient), locks its mutex, reads blockLight from mesh.lightingData[0] or extracts color from ch.data if sun, computes value as elementwise max with light, skips all-black entries, writes .fromArray(.{0,0,0}) to channelChunk.data at entry.toIndex(), and pushes the resulting value back into the queue. After releasing the mutex it calls propagateDirect on the queue. The chunk also defines LightVector as @Vector(8, u16). getValues combines blockLight (mesh.lightingData[0]) and sunLight (mesh.lightingData[1]), asserts little-endian CPU, casts their raw() values to a 64-bit integer with sunLight in the high 32 bits, then bit-casts to @Vector(8, u8). getLightAt maps world coordinates into chunk-local BlockPos using chunkMask, checks for exact match and returns getValues(parent,pos), otherwise computes neighbor mesh offsets via parent.pos.wx/wy/wz plus voxelSize scaling, fetches the neighbor mesh from mesh_storage.getMesh with those coords (or returns @splat(0) if missing), and calls getValues on that neighbor. getCornerLight builds a float position by casting pos to Vec3f, adding normal scaled by 0.5, subtracting 0.5, floors to startPos, computes interp as the fractional part, then loops over dx/dy/dz in [0..1] with weights derived from interp (1-interp when dx==0 else interp), truncates weight*256 to u16 integerWeight, calls getLightAt for each corner offset, accumulates into val, and finally divides by @splat(256). getLightSampleAligned first calls getLightAt for the given pos, then if parent.pos.voxelSize==1 it fetches nextVal at pos+%direction.relX/Y/Z, computes diff as elementwise min of @splat(8) with lightVal-|nextVal, and adjusts lightVal by subtracting diff*@splat(5)/@splat(2). packLightValues takes [4]LightVector, initializes result:undefined, loops i over 0..3, shifts each component right by 3 bits and packs into a u32 with bit positions 25/20/15/10/5/0 (skipping index 3), returning the packed array. getLight is a public function that receives parent: *ChunkMesh, blockPos: Vec3i, textureIndex: u16, quadIndex: QuadIndex; it extracts normal from quadInfo and extraQuadInfo, checks if blocks.meshes.textureOcclusionData[textureIndex].load(.monotonic) fails (no ambient occlusion), in which case it calls getLightAt(parent, blockPos components) and packs the splatted result. If extraQuadInfo.alignedNormalDirection is present, it initializes lightValues: [4]LightVector to @splat(@splat(0)), iterates over extraQuadInfo.lightSampleListForAxisAlignedModels, calls getLightSampleAligned for each sample offset with dir, accumulates weighted contributions into lightValues[i], divides all by @splat(256), and packs. If extraQuadInfo.hasOnlyCornerVertices is true, it initializes rawVals: [4]LightVector to undefined, loops i over 0..3, reads quadInfo.corners[i] as Vec3f, computes fullPos = blockPos +%@trunc(vertexPos), calls getCornerLight(parent, fullPos, normal) into rawVals[i], and packs. Finally it initializes rawVals: [4]LightVector to undefined again (for the general case not shown in the snippet).

## Related Questions
- How does propagateLightsDestructive handle sun versus ambient lighting channels?
- What is the purpose of sourceDir=6 and activeValue=0b111 in the light queue entries?
- Under what condition does getLight skip texture occlusion data entirely?
- How are neighbor meshes fetched when a block lies outside the current chunk bounds?
- What happens to rawVals when extraQuadInfo.hasOnlyCornerVertices is true?
- Why is there an assertion on builtin.cpu.arch.endian() in getValues?
- How does packLightValues arrange the 8 u16 components into four u32 values?
- What is the effect of dividing lightValues by @splat(256) before packing?
- Does getCornerLight perform any fallback when a neighbor mesh is missing?
- How are vertex positions from quadInfo.corners[i] converted to integer block coordinates?

*Source: unknown | chunk_id: codebase_src_renderer_lighting.zig_chunk_3*
