# [src/chunk.zig] - Chunk 2679419162

**Type:** review
**Keywords:** Lod, voxelSize, enum, compile-time, lookup table, shift, optimization, benchmark, inline, tag_type
**Symbols:** Lod, voxelSize
**Concepts:** compile-time constant folding, lookup table vs shift optimization, enum tag conversion, inline function semantics, performance regression prevention

## Summary
Added a new `Lod` enum with helper functions and a `voxelSize()` method that uses a compile-time generated lookup table to return powers of two.

## Explanation
The change introduces an enumeration representing LOD levels (0–5) with inline helpers for min/max/next/previous/int conversion. The core addition is `voxelSize`, which builds a static array at compile time where each entry holds `1 << i` and returns the appropriate value based on the enum tag. Reviewers flagged that this lookup table may hinder compiler optimizations because it obscures the simple shift operation; they requested benchmark evidence before committing to the table approach.

## Related Questions
- What is the exact type returned by `Lod.voxelSize()`?
- How does `@splat(0)` initialize the lookup table in `voxelSize`?
- Why would a compiler struggle to optimize `*lod.voxelSize()` compared to `<< lod.toInt()`?
- Which enum fields are populated into the compile-time array by the loop over `Lod`'s fields?
- What is the maximum integer value representable by the `u31` returned from `voxelSize`?
- Does `next()` wrap around when called on `LOD5` or does it produce an invalid enum value?
- How does `min()` compute its result using `@typeInfo(Lod).@

*Source: unknown | chunk_id: github_pr_2482_comment_2679419162*
