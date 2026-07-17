# [src/blocks.zig] - Chunk 3179750006

**Type:** review
**Keywords:** enum, SelectionRule, SelectionCapability, u8, allocation, zero bytes, compiler error, array, memory safety, Zig
**Symbols:** SelectionRule, SelectionCapability
**Concepts:** enum allocation size, zero-byte enum bug, memory safety, allocator constraints, type definition refactoring

## Summary
Refactors the SelectionRule enum into a new SelectionCapability enum(u8) to explicitly allocate one byte per value, preventing Zig’s zero-byte allocation error for single-value enums.

## Explanation
The original code defined SelectionRule as an unnamed enum with three values (always, toolEffective, never). In Zig, any enum that has only a single possible value is represented by 0 bytes; when the compiler tries to allocate an array of such enums, it fails because there are no bytes to store. To avoid this runtime error and make the intent clear, the change introduces SelectionCapability as an explicit enum(u8) with at least one variant (the diff shows only a placeholder). By forcing the enum to occupy 8 bits, the allocator can safely create arrays of these values. This is a defensive architectural tweak that ensures memory safety for future extensions where more selection capabilities may be added without hitting the zero-byte limitation.

## Related Questions
- What happens when a Zig enum has only one value?
- Why does the allocator error on zero-byte enums?
- How is SelectionCapability defined in the diff?
- Does the new enum still support multiple values?
- Where else in blocks.zig are single-value enums used?
- What would be a safe way to extend SelectionCapability later?
- Is there any runtime cost for using an explicit u8 enum?
- How does this change affect existing code that uses SelectionRule?
- Can we infer the original number of variants from the old name?
- What is the minimal variant count required for an enum(u8)?
- Does the diff show any other modifications to Ore or related types?
- Is there a comment explaining why always was chosen as the sole value?

*Source: unknown | chunk_id: github_pr_2987_comment_3179750006*
