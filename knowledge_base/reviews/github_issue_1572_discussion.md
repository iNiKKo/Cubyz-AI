# [issues/issue_1572.md] - Issue #1572 discussion

**Type:** review
**Keywords:** particles.zig, renaming, packed struct, id() method, type() method, fromId function, items.zig, exhaustive enums, design choice, maintenance
**Symbols:** ParticleIndex, ParticleTypeIndex
**Concepts:** readability, code consistency, packed struct, method design

## Summary
The issue discusses improving the readability and consistency of the `particles.zig` file by renaming and restructuring types, methods, and functions.

## Explanation
The issue discusses improving the readability and consistency of the `particles.zig` file by renaming and restructuring types, methods, and functions. Specifically, the following changes are proposed:

- Rename `ParticleIndex` to `ParticleTypeIndex`
- Change `ParticleTypeIndex` into a `packed struct` offering an `id()` method that returns the ID of the particle type.
- Add a new `packed struct` called `ParticleIndex` to replace plain `u32`, with a `type()` method returning `ParticleTypeIndex` and a `fromId` function for converting IDs to `ParticleTypeIndex` instances.

The reviewer questions the relevance of using packed structs compared to exhaustive enums used in `items.zig` and seeks clarification on the purpose of the `id()` method. The discussion highlights that some functionality is currently implemented as functions on `ParticleManager`, which is considered a messy design choice.

## Related Questions
- What is the purpose of renaming `ParticleIndex` to `ParticleTypeIndex`?
- How does changing `ParticleTypeIndex` to a packed struct improve readability?
- Why is adding an `id()` method to `ParticleTypeIndex` beneficial?
- What functionality will be replaced by using `ParticleIndex` instead of plain `u32`?
- How does the proposed `type()` method in `ParticleIndex` enhance code clarity?
- What are the advantages of using packed structs over exhaustive enums in this context?

*Source: unknown | chunk_id: github_issue_1572_discussion*
