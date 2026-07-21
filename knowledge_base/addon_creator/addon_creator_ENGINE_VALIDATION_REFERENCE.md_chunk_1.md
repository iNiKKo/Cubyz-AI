# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 1

**Type:** documentation
**Keywords:** blocks.zig register, blockHealth, blockResistance, selectionCapabilities, collide, viewThrough, friction, density, ore fallback, onTouch, drops
**Symbols:** register(), getTypeById, loadBlockDrop

## Summary
Engine-side default values and error messages for every Cubyz block field, read directly from `blocks.zig: register()`.

## Explanation
`.rotation` defaults to `"cubyz:no_rotation"` if missing (website form defaults to `"cubyz:stairs"` -- different, but the website always writes a value). `.blockHealth` defaults to `1`. `.blockResistance` defaults to `0`. `.tags`: if the resulting tag list is empty, logs `"Block {id} is missing 'tags' field"`. `.emittedLight` defaults to `0`. `.absorbedLight` defaults to `0xffffff` (16777215), matching the website's decimal default. `.degradable` defaults to `false`. **`.selectionCapabilities` is an optional array (`?[]SelectionCapability`) that determines which tools/items can select the block; it defaults to `.always` (any tool can select it), and is not exposed anywhere in the website UI -- hand-edit only.** `.replaceable` defaults to `false`. `.transparent` defaults to `false`. `.collide` defaults to **`true`** -- the default is "does collide," the opposite of leaving it off meaning no collision. `.viewThrough` defaults to `false`, but forced `true` if `transparent` or `alwaysViewThrough` is true. `.friction` defaults to `20`. `.bounciness` defaults to `0.0`. `.density` defaults to `main.physics.airDensity` (a named engine constant, not a literal number; website form defaults to `1.2`). `.terminalVelocity` defaults to `90`. `.mobility` defaults to `1.0`. `.allowOres` defaults to `false`. `.blockEntity` has no default, looked up via `block_entity.getByID`.

`.ore`: only processed if `.rotation == "cubyz:ore"`; if an `.ore` block exists but rotation isn't `"cubyz:ore"`, logs `"Ore must have rotation mode \"cubyz:ore\"!"` and the ore properties are silently dropped. Within `.ore`, engine-side raw fallbacks if sub-fields are missing: `veins=0`, `size=0`, `maxHeight=i32 max`, `minHeight=i32 min`, `density=0.5` -- very different from the website's own hardcoded ore defaults (`veins=4.5, size=20, maxHeight=-600, density=0.25`).

`.onInteract`/`.onBreak`/`.onUpdate`/`.onTick` default to `.noop`; if present but malformed, logs `"Failed to load onX event for block {id}"` and falls back to no-op. `.onTouch` follows the same pattern, message is `"Failed to load onTouch event for block {id}"`. `.drops` is parsed via `loadBlockDrop()`; each entry's item string supports `"auto"` (drops the block itself) or `"{count} {item}"`; unknown item ids are silently skipped (`continue`), not errored. Referencing a nonexistent block id anywhere (`.blockPlacement`, drop items, etc., via `getTypeById`) logs `"Couldn't find block {id}. Replacing it with air..."` and substitutes air -- doesn't crash.

## Related Questions
- What does a Cubyz block's .blockHealth/.emittedLight/.absorbedLight/.degradable/.replaceable/.transparent/.collide/.friction/.bounciness/.terminalVelocity/.mobility/.allowOres field default to if omitted?
- What is a Cubyz block's .selectionCapabilities field, and how is it set?
- What does a Cubyz block's .density field default to, and how does that differ from the website?
- What are the engine's raw fallback values inside a Cubyz block's .ore sub-object?
- What happens if a Cubyz block's onInteract/onBreak/onUpdate/onTick/onTouch callback is malformed?
- How does a Cubyz block's .drops field handle an unknown item id?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_1*
