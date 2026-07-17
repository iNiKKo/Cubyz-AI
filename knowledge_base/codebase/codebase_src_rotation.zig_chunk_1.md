# [medium/codebase_src_rotation.zig] - Chunk 1

**Type:** api
**Keywords:** rotation mode, neighbor dependency, block model, ray triangle intersection, coordinate transform, init reset deinit, string hash map, default functions, mat4f mulvec, float epsilon
**Symbols:** CanBeChangedInto, rotationModes, rotationMatrixTransform, rayTriangleIntersection
**Concepts:** block rotation modes, neighbor dependency, model generation, coordinate transformation, Möller–Trumbore intersection, registry initialization, function pointer defaults

## Summary
Defines the rotation mode registry and default functions for block data manipulation, including neighbor dependency handling, model generation, coordinate transformation, ray-triangle intersection, and lifecycle init/reset/deinit.

## Explanation
The chunk declares a union enum CanBeChangedInto with variants no, yes, yes_costsDurability, and yes_costsItems. It defines default function pointers for model creation (createBlockModel), data generation (generateData), neighbor-dependent updates (updateData), block modification (modifyBlock), ray intersection (rayIntersection), breaking callbacks (onBlockBreaking), change logic (canBeChangedInto, itemDropsOnChange), tag retrieval (getBlockTags), and formatting (formatBlockData). A global rotationModes std.StringHashMap is initialized in init() by iterating over @typeInfo(rotations).struct.decls and registering each mode via register(). reset() calls .reset() on each registered mode; deinit() cleans up the map and all modes. getByID(id) looks up a mode, falling back to cubyz:no_rotation if missing with an error log. register(comptime id, comptime Mode: type) constructs a RotationMode by copying fields from the provided Mode type into a new struct instance, using @hasDecl checks and field type matching; it then inserts via putNoClobber(id, result). The chunk also provides rotationMatrixTransform(quad, transformMatrix) which applies Mat4f.mulVec to quad.normal and each corner of quad.corners after translating by Vec3f{0.5, 0.5, 0.5} and scaling by 1, then recombining with vec.xyz. rayTriangleIntersection implements the Möller–Trumbore algorithm: it computes edge vectors e1/e2, cross product rayCrossE2, determinant det, checks near-zero det against std.math.floatEps(f32), calculates invDet, s = origin - triangle[0], u = invDot(s, rayCrossE2), rejects if u outside [0,1], computes sCrossE1, v = invDot(direction, sCrossE1), rejects if v<0 or u+v>1, then t = invDot(e2, sCrossE1) and returns t if > floatEps else null.

## Related Questions
- What is the purpose of CanBeChangedInto and its variants?
- How does rotationMatrixTransform modify a QuadInfo's normal and corners?
- Under what conditions does rayTriangleIntersection return null versus a t value?
- What happens in getByID when a requested rotation mode ID is not found?
- Describe the field-copying logic inside register for constructing RotationMode.
- How are rotation modes registered during init and cleaned up in deinit?
- Why does reset call .reset() on each mode rather than reinitializing fields?
- What role do default function pointers play in the RotationMode struct?
- How is the floatEps threshold used to avoid degenerate triangle intersections?
- Can a rotation mode be registered with a runtime type or only compile-time?

*Source: unknown | chunk_id: codebase_src_rotation.zig_chunk_1*
