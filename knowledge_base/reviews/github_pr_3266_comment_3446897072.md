# [mods/cubyz/rotations.zig] - Chunk 3446897072

**Type:** review
**Keywords:** consolidate, struct, import, pollution, cubyz, stairs, no_rotation, texture_pile, ore, hanging, torch, decayable, direction, planar, log
**Symbols:** pub const stairs, pub const no_rotation, pub const texture_pile, pub const ore, pub const hanging, pub const torch, pub const decayable, pub const direction, pub const planar, pub const log, pub const carpet, pub const branch, pub const fence, pub const sign, pub const cubyz, stairs
**Concepts:** modularization, namespace consolidation, API surface clarity, generated file pollution, block enumeration, addon discoverability, missing entry bug prevention

## Summary
The reviewer proposes consolidating all rotation-related block definitions into a single `cubyz` struct to simplify addon discovery and reduce generated file pollution, while also noting that the current list is incomplete.

## Explanation
Architecturally, scattering imports across many small files makes it harder for addon authors to quickly enumerate available blocks. By gathering them under one namespace (`pub const cubyz = struct { ... }`), we provide a clear API surface and avoid the need for generated stubs that can become stale or cause import pollution in the mods directory. The reviewer also points out an omission: some block types (likely those handled by `anti_cubyz` or other categories) are missing from this list, which would otherwise lead to common bug reports where addons fail because they cannot find a definition for a specific block.

## Related Questions
- What block types are currently missing from the `cubyz` struct that would cause addon failures?
- How does consolidating imports into a single struct affect the mod's import graph and build time?
- Are there any blocks that should be placed under a sub-struct (e.g., `anti_cubyz`) instead of the main `cubyz` namespace?
- What is the recommended pattern for exposing rotation-related blocks to addon authors without generating files?
- Does the reviewer suggest moving generated stubs into the same file as their definitions, or keeping them separate?
- How would this change impact backward compatibility with existing addons that import individual block modules?
- Is there a preferred ordering of entries in the `cubyz` struct (e.g., by category or alphabetical)?
- What steps should be taken to ensure no rotation-related blocks are omitted when updating the list?
- Should the `anti_cubyz` struct also be consolidated, and if so, how does it relate to `cubyz`?
- How can we verify that all imported modules (`rotations/*.zig`) are correctly referenced after consolidation?

*Source: unknown | chunk_id: github_pr_3266_comment_3446897072*
