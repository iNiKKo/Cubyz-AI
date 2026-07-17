# [easy/codebase_src_server_terrain_sdf_models_rotated.zig] - Chunk 0

**Type:** implementation
**Keywords:** Axis enum, degreesToRadians, splat, floor, ceil, rotate function, seeded random, closure castFunctionSelfToAnyopaque, ZonElement getChild, SdfInstance instantiate
**Symbols:** id, Axis, Entry, Instance, initAndGetExtend, rotate, instantiate, generate
**Concepts:** SDF model rotation, axis enumeration, random angle generation, bounding box extension, corner iteration, seeded random float, closure serialization, ZonElement parsing

## Summary
This chunk defines the cubyz:rotated SDF model type that rotates child models around a configurable axis with random angles and computes extended bounds by rotating all eight corners of the child's bounding box.

## Explanation
The chunk declares an id constant for the rotated model, an Axis enum (x,y,z), an Entry struct holding a child SdfModel plus positionOffset and randomOffset fields, and an Instance struct containing a child SdfInstance, axis, sin/cos rotation values. The initAndGetExtend function parses a ZonElement: it retrieves the child model via getChild('child'), reads the 'axis' enum field (defaulting to null if missing), converts 'minAngle'/'maxAngle' strings from degrees to radians with defaults 0/360, constructs an axisVector using switch on Axis, computes offAxisVectors as Vec3f{1,1,1} minus that axis vector, derives maxDiagonal by splatting the length of min/max extents scaled by offAxisVectors, and returns a model with computed .min/.max bounds via floor/ceil after rotating the diagonal offsets. The rotate function implements per-axis 2D rotation matrices: for x it leaves X unchanged and rotates Y/Z; for y it leaves Y unchanged and rotates X/Z; for z it leaves Z unchanged and rotates X/Y, returning a Vec3f with the appropriate linear combinations of sin/cos applied to input components. The instantiate method uses a seeded random float between minAngle and maxAngle to compute sin/cos, calls child.instantiate(arena, seed) to obtain a child SdfInstance, initializes minBounds/maxBounds as extreme values (1e9/-1e9), then iterates over the eight corners of the child's bounding box (nested loops 0..2 for each axis, selecting min or max depending on index), rotates each corner using rotate(self.axis,-sin,cos,...) and updates bounds with floor/ceil. It allocates an Instance struct via arena.create and fills it with the rotated sin/cos values and the child instance. The returned SdfModel.InitResult contains a .generateFn field set to main.meta.castFunctionSelfToAnyopaque(generate), which is a closure that will call generate on the stored Instance data when invoked later. The generate function takes an Instance pointer and a samplePos Vec3f, rotates samplePos by the instance's sin/cos around its axis, then delegates to self.child.generateFn(self.child.data, rotatedPos) to obtain the final SDF value.

## Related Questions
- How does initAndGetExtend compute the extended bounds for a rotated SDF model?
- What default values are used when axis or angle parameters are missing from the ZonElement?
- How is the rotate function implemented differently for each Axis enum value?
- Why does instantiate use -sin and cos in the rotate call while generate uses sin and cos?
- What is the purpose of casting generate to Anyopaque via main.meta.castFunctionSelfToAnyopaque?
- How are the eight corners of a child SdfInstance's bounding box enumerated during instantiation?
- Does this chunk handle any error cases besides returning null for missing axis or angle fields?
- Is there any memory ownership transfer between the arena and the Instance struct created in instantiate?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_rotated.zig_chunk_0*
