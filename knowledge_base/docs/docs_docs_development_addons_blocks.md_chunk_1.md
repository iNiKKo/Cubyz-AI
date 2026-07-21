# [easy/docs_docs_development_addons_blocks.md] - Chunk 1

**Type:** documentation
**Keywords:** emittedLight, absorption, onInteract, rotation, lodReplacement, opaqueVariant, LOD0.5, Leaves Quality, rotation modes, no_rotation, branch, carpet, direction, fence, hanging, ore rotation, planar, sign, stairs, texture_pile, torch
**Symbols:** emittedLight, absorption, onInteract, rotation, lodReplacement, opaqueVariant

## Summary
Cubyz block `zig.zon` fields covering lighting, interaction callbacks, and LOD/rendering (part 2 of 3), plus the full list of rotation modes.

## Explanation
| Property | Type | Description |
|----------|------|-------------|
| `emittedLight` | `u32` | Amount of light emitted by the block. |
| `absorption` | `u32` | Amount of light absorbed by the block. |
| `onInteract` | `ClientBlockCallback` | Callback executed when the block is interacted with. |
| `rotation` | `RotationMode` | Rotation mode used by the block (see Rotation Modes below). |
| `lodReplacement` | `u16` | **Block used as a replacement in `LOD1` and higher** (the exact threshold is LOD1, not just "lower detail levels" generically). |
| `opaqueVariant` | `[]Tag` | **An opaque variant of the block, used specifically at `LOD0.5` and whenever the "Leaves Quality" graphics option is active.** This is the entire purpose of the field -- nothing more. |

**`opaqueVariant` in one sentence: it is an opaque variant used at LOD0.5 and with the Leaves Quality option.** (`lodReplacement` is a different, separate field -- it swaps the block at LOD1+, not LOD0.5.)

### Rotation Modes
`no_rotation` (none), `branch` (branch-style), `carpet` (carpet-like blocks), `direction` (faces a specific direction), `fence` (fence connections), `hanging` (hanging blocks), `ore` (ore blocks), `planar` (constrained to a plane), `sign` (signs), `stairs` (stairs), `texture_pile` (texture pile blocks), `torch` (torches).

## Related Questions
- What is a Cubyz block's opaqueVariant field for?
- What is the difference between 'opaqueVariant' and 'lodReplacement'?
- How can I modify the LOD replacement for a block?
- What is the purpose of the `onInteract` callback in Cubyz blocks?
- What are some common rotation modes used for blocks in Cubyz?

*Source: unknown | chunk_id: docs_docs_development_addons_blocks.md_chunk_1*
