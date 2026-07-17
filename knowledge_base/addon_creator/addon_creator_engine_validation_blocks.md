# [reference/ENGINE_VALIDATION_REFERENCE.md] - Chunk blocks

**Type:** reference
**Keywords:** blockResistance, blockHealth, rotation, no_rotation, tags, ore, cubyz:ore, drops, block-defaults, missing-field
**Symbols:** blocks.zig, register, getTypeById
**Concepts:** engine-default-values, validation-errors, silent-fallback

## Summary
Exact engine-side default values and error messages for every Cubyz block field, read directly
from `blocks.zig: register()`. Covers what happens when a field is omitted from a hand-written
block `.zig.zon` file.

## Explanation
Engine defaults if a field is missing (source of truth -- may differ from the website's own form
defaults):
- `.rotation`: `"cubyz:no_rotation"` (website's form defaults to `"cubyz:stairs"` instead -- different)
- `.blockHealth`: `1`
- `.blockResistance`: `0`
- `.tags`: if the resulting tag list is empty, logs `"Block {id} is missing 'tags' field"` -- every block needs at least one tag. This is a `std.log.err` call only, with no `return`/early exit after it (confirmed in `blocks.zig`'s `register()`: the check at line 178 falls straight through into the rest of registration) -- the block does NOT fail to load or get skipped, it still gets fully registered with an empty tag list, just logged as a warning-level problem since tag-dependent behavior (drops, tool interactions, etc.) may not work correctly on it.
- `.emittedLight`: `0`
- `.absorbedLight`: `0xffffff` (16777215)
- `.degradable`: `false`
- `.selectionCapabilities`: `.always` (any tool can select it) -- not exposed anywhere in the website UI, hand-edit only
- `.replaceable`: `false`
- `.transparent`: `false`
- `.collide`: `true` (default IS collide -- opposite of leaving it off meaning no collision)
- `.viewThrough`: `false`, but forced `true` if `transparent` or `alwaysViewThrough` is true
- `.friction`: `20`
- `.bounciness`: `0.0`
- `.density`: `main.physics.airDensity` (a named engine constant, not a literal number; website form defaults to `1.2`)
- `.terminalVelocity`: `90`
- `.mobility`: `1.0`
- `.allowOres`: `false`

Ore rotation requirement: an `.ore` block is only processed if `.rotation == "cubyz:ore"` exactly.
If an `.ore` block exists but rotation isn't `"cubyz:ore"`, the engine logs
`"Ore must have rotation mode \"cubyz:ore\"!"` and the ore properties are silently dropped (the
block still loads, just without its ore behavior). Within `.ore`, engine-side raw fallbacks if
sub-fields are missing: `veins=0`, `size=0`, `maxHeight=i32 max`, `minHeight=i32 min`,
`density=0.5` -- very different from the website's own hardcoded ore defaults
(`veins=4.5, size=20, maxHeight=-600, density=0.25`).

Callbacks (`.onInteract`/`.onBreak`/`.onUpdate`/`.onTick`/`.onTouch`): default `.noop` if missing;
if present but malformed, logs `"Failed to load onX event for block {id}"` (or
`"Failed to load onTouch event for block {id}"`) and falls back to no-op.

Drops: parsed via `loadBlockDrop()`; unknown item ids in a drop entry are silently skipped
(`continue`), not errored.

Nonexistent block ID reference (in `.blockPlacement`, drop items, or anywhere else referencing a
block by id via `getTypeById`): the engine does NOT crash. It logs
`"Couldn't find block {id}. Replacing it with air..."` and substitutes air. This is the single
most useful diagnostic line in the whole engine for "my block reference doesn't seem to work."

## Related Questions
- What does Cubyz's blockResistance field default to if omitted?
- What rotation mode does a Cubyz block default to if .rotation is omitted?
- What rotation value must a block have for its ore properties to actually load in Cubyz?
- What happens if a Cubyz block has ore properties but the wrong rotation mode?
- What happens if a Cubyz block's tags field ends up empty?
- What's the one field the Cubyz engine truly requires for a block addon to be valid?
- What happens if I place a block ID that doesn't exist in an addon?

*Source: raw_cubyz_dataset/addon_creator/ENGINE_VALIDATION_REFERENCE.md | chunk_id: addon_creator_engine_validation_blocks*
