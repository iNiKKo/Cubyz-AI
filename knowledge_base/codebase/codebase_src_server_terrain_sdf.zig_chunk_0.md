# [easy/codebase_src_server_terrain_sdf.zig] - Chunk 0

**Type:** implementation
**Keywords:** sdf generation, terrain carving, model registry, ZonElement parameters, additive blending, subtractive blending, stack arena allocation, biome offset lookup, voxel alignment, smooth union function
**Symbols:** NeverFailingAllocator, terrain, CaveBiomeMapView, vec, Vec3f, Vec3i, ZonElement, SdfModel, InitResult, VTable, initModel, generate, instantiate, modelRegistry, SdfInstance, smoothUnion, intersection
**Concepts:** signed distance field generation, procedural terrain carving, static model registry, parameterized ZonElement configuration, additive and subtractive blending modes, stack arena allocation pattern, biome offset lookup, voxel grid traversal with alignment

## Summary
Defines SDF model and instance structures for procedural terrain generation with additive/subtractive blending modes, a static registry of models loaded from sdf_models/_list.zig, and utility functions for smooth union/intersection used during voxel carving.

## Explanation
The chunk declares top-level constants: NeverFailingAllocator (imported from main.heap), terrain (main.server.terrain), CaveBiomeMapView (from terrain.CaveBiomeMap), vec (main.vec), Vec3f, Vec3i, ZonElement, and sdf_models (imported). It defines SdfModel as a struct with fields data, instantiateFn, maxBiomeCenterDistance, minAmount, maxAmount, mode (enum additive|subtractive), and InitResult. The initModel function reads parameters from a ZonElement, looks up the model id in modelRegistry (a StaticStringMap of VTable entries built comptime from sdf_models), calls vtable.initAndGetExtend to get model data and maxExtend bounds, clamps maxBiomeCenterDistance against cave biome size, defaults minAmount/maxAmount/mode if missing, and returns an InitResult. The generate method on SdfModel iterates amount times (randomized between minAmount and maxAmount), creates a stack arena for each instance, picks a random offset direction within maxBiomeCenterDistance, adjusts position by biomeMap.getCaveBiomeOffset, instantiates the model via instantiateFn, offsets its bounds relative to sdfPos, then calls instance.generate. The instantiate method simply forwards to the stored vtable.instantiateFn. SdfInstance is defined with fields data, generateFn, minBounds, maxBounds, centerPosOffset, and a generate method that computes voxel grid dimensions, clamps bounds by perimeter and voxelSize, iterates over voxels aligned to voxelSize, samples the signed distance field via generateFn at each position, applies smoothUnion (or intersection) with existing SDF values using interpolationSmoothness, and writes back. The smoothUnion function implements a quadratic blend based on Iquilez's smin article; intersection returns max(a,b). modelRegistry is built comptime by iterating over @typeInfo(sdf_models).@

## Related Questions
- How does initModel handle missing parameters in the ZonElement?
- What is the purpose of modelRegistry and how are its entries constructed at compile time?
- Describe the steps performed inside SdfModel.generate for each random instance.
- How are minBounds and maxBounds adjusted relative to sdfPos before generating an instance?
- What does smoothUnion compute and where does it get its blend factor from?
- In what order are voxels iterated in SdfInstance.generate and how is alignment enforced?
- Why is a stack arena created for each instance and when is it destroyed?
- How does the chunk decide between additive and subtractive mode during initModel?
- What role does getCaveBiomeOffset play in positioning an instance within the biome map?
- Can you explain how maxBiomeCenterDistance is clamped against cave biome size?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf.zig_chunk_0*
