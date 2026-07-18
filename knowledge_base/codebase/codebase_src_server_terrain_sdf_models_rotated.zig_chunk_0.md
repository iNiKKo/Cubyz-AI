# [easy/codebase_src_server_terrain_sdf_models_rotated.zig] - Chunk 0

**Type:** world_generation
**Keywords:** Signed Distance Function, terrain modeling, randomization, vector rotation, bounds calculation
**Symbols:** id, Axis, Entry, child, axis, minAngle, maxAngle, Instance, initAndGetExtend, rotate, instantiate, generate
**Concepts:** terrain generation, SDF model, rotation transformation

## Summary
This chunk defines a rotated SDF model for terrain generation.

## Explanation
This chunk defines a rotated SDF model for terrain generation. It includes functions to initialize the model from configuration data, instantiate it with random rotation parameters, and generate distances based on sample positions after applying the rotation. The `initAndGetExtend` function sets up the model's properties by initializing the child model and setting default angle ranges if not specified (default minAngle is 0 radians and maxAngle is 2π radians). It also calculates the axis vector for each possible axis (x, y, z) as follows: `{1, 0, 0}` for `Axis.x`, `{0, 1, 0}` for `Axis.y`, and `{0, 0, 1}` for `Axis.z`. The function then determines the maximum diagonal extend based on the off-axis vectors. The `instantiate` function creates an instance of the rotated SDF by generating a random angle within the specified range in radians, calculating sine and cosine values for this angle, and rotating each corner of the child model's bounding box around the specified axis to determine the bounds. The `generate` function applies the rotation to a sample position using predefined rotation matrices for x, y, and z axes as follows: For `Axis.x`, it rotates `(y, z)`; for `Axis.y`, it rotates `(x, z)`, and for `Axis.z`, it rotates `(x, y)`. The actual distance calculation is then delegated to the child SDF.

## Code Example
```zig
const Axis = enum { x, y, z }
```

## Related Questions
- What is the purpose of the `initAndGetExtend` function?
- How does the `rotate` function work for different axes?
- What data structure holds the properties of a rotated SDF instance?
- How are the bounds calculated for the instantiated rotated SDF model?
- What is the role of the `generate` function in this chunk?
- How is randomness incorporated into the instantiation process?

*Source: unknown | chunk_id: codebase_src_server_terrain_sdf_models_rotated.zig_chunk_0*
