# [easy/codebase_src_server_terrain_sdf_models_rectangular_cuboid.zig] - Chunk 0

**Type:** serialization
**Keywords:** rectangular cuboid, min radii, max radii, SDF model, instance generation, bounding box, ZonElement parsing, memory arena allocation
**Symbols:** id, Instance
**Concepts:** SDF model definition, instance generation with randomization, bounding box computation, ZonElement parsing, memory arena allocation

## Summary
Defines a rectangular cuboid SDF model with configurable min/max radii and generates random instances within those bounds.

## Explanation
The chunk declares a public identifier 'id' for the rectangular cuboid model. It imports Array3D, NeverFailingAllocator, sdf (SdfInstance), vec (Vec3f, Vec3i), and ZonElement from other modules. The Instance struct holds radii as Vec3f. initAndGetExtend reads minSideLengths and maxSideLengths from a ZonElement; if missing it defaults to 32 for min and doubles that for max, then returns an SdfModel.InitResult with the model pointer and computed extend bounds (floor of negative maxRadii to ceil of positive maxRadii). instantiate allocates an Instance on the given arena, seeds its radii by linearly interpolating between minRadii and maxRadii using a random float vector, and returns an SdfInstance containing the data pointer, a generateFn that points to the generate function (cast via meta.castFunctionSelfToAnyopaque), and precomputed minBounds, maxBounds, and centerPosOffset. generate computes an absolute distance from samplePos to each axis minus the instance radii, takes the maximum of those distances and zero, adds its length, then subtracts the minimum of zero and the maximum of the three per-axis distances (effectively returning a signed SDF value).

## Related Questions
- What is the default value used for minSideLengths when not provided in the ZonElement?
- How are maxSideLengths computed if they are missing from the configuration data?
- What does initAndGetExtend return and what fields are included in its result struct?
- Which function is assigned to generateFn in the returned SdfInstance and how is it cast?
- How is the radii of an instantiated cuboid derived from minRadii and maxRadii using a seed?
- What bounds (minBounds, maxBounds) are calculated for the generated instance and why?
- Describe the mathematical operation performed by generate to compute the SDF value.
- Does this chunk allocate memory directly or does it rely on an arena allocator provided by the caller?
- How is centerPosOffset computed relative to the instance radii?
- What type does Instance.radii hold and how many components does that vector have?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_rectangular_cuboid.zig_chunk_0*
