# [reference/ENGINE_VALIDATION_REFERENCE.md] - Chunk items

**Type:** reference
**Keywords:** stackSize, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, material, item-defaults, procedural-items
**Symbols:** items.zig, BaseItem.init, Material.init, registerProceduralItem
**Concepts:** engine-default-values, validation-errors, silent-fallback

## Summary
Exact engine-side default values and error messages for every Cubyz item field, read directly
from `items.zig: BaseItem.init()` and `Material.init()`. Covers simple items, the material
sub-object, and procedural items.

## Explanation
Simple item fields, engine default if missing:
- `.name`: falls back to the item's own `.id` -- the website never sets this field at all, so items exported via the website always display their raw id as the tooltip name
- `.tags`: empty list
- `.stackSize`: `120` (matches the website's own default)
- `.material`: `null` (no material) -- engine checks whether this is an object, not whether a `.material` tag is present
- `.block`: `null` -- looked up via `blocks.getTypeById`, same "Couldn't find block... Replacing it with air" fallback behavior as block references
- `.food`: `0`

Material sub-object (`Material.init()`, only runs if `.material` is present) -- these FOUR fields
have NO silent default; a missing field logs an explicit error and falls back to exactly `0`,
which for durability specifically means the item breaks instantly:
- `.massDamage` -- missing logs `"Couldn't find material attribute 'massDamage'"`, becomes `0`
- `.hardnessDamage` -- missing logs `"Couldn't find material attribute 'hardnessDamage'"`, becomes `0`
- `.durability` -- missing logs `"Couldn't find material attribute 'durability'"`, becomes `0`
- `.swingSpeed` -- missing logs `"Couldn't find material attribute 'swingSpeed'"`, becomes `0`

One material field DOES have a real (non-zero) soft default, unlike the four above:
- `.textureRoughness` -- defaults to `1.0` if missing (the website's own form defaults to `0.0` instead -- different)

`.modifiers[].id` -- if the id doesn't match a known modifier, logs
`"Couldn't find modifier with id '{id}'. Replacing it with 'durable'"` and silently substitutes
the "durable" modifier.

Procedural items (`registerProceduralItem()`): a completely separate, more advanced system
(weighted parameter matrices mapping material properties to tool stats, disabled/optional slot
arrays) that the website does not support at all -- only reachable by hand-writing the zon file.

## Related Questions
- What's the default stack size for a Cubyz item if not specified?
- What does a Cubyz item's display name fall back to if .name isn't set?
- Which four Cubyz item material fields have no soft default and fall back to exactly 0 if missing?
- What happens if durability is missing from a Cubyz item's material block?
- What's the default value for textureRoughness in a Cubyz item's material block?

*Source: raw_cubyz_dataset/addon_creator/ENGINE_VALIDATION_REFERENCE.md | chunk_id: addon_creator_engine_validation_items*
