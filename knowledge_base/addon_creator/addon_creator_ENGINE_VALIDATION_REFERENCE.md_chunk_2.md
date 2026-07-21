# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 2

**Type:** documentation
**Keywords:** items.zig, BaseItem.init, Material.init, registerProceduralItem, stackSize, durability, massDamage, hardnessDamage, swingSpeed, textureRoughness, modifiers, item block field, blockPlacement
**Symbols:** BaseItem.init(), Material.init(), registerProceduralItem()

## Summary
Engine-side default values and error messages for every Cubyz item field, read directly from `items.zig`.

## Explanation
**Simple items** (`BaseItem.init()`): `.name` defaults to the item's own `id` -- the website never sets this field at all, so items exported via the website always display their raw id as the tooltip name. `.tags` defaults to empty. `.stackSize` defaults to `120`, matching the website. `.material` defaults to `null` (no material) -- the engine checks whether this is an **object**, not whether a `.material` tag is present (in practice these are coupled by the website's own logic). `.block` defaults to `null`, looked up via `blocks.getTypeById` -- same "Couldn't find block..." fallback-to-air behavior if the reference is bad. `.food` defaults to `0`.

**Material sub-object** (`Material.init()`, only runs if `.material` is present) -- these four have **no silent default**, a missing field logs an explicit error and falls back to `0` (for durability this effectively means the item breaks instantly): `.massDamage` missing logs `"Couldn't find material attribute 'massDamage'"`, becomes `0`. `.hardnessDamage` missing logs `"Couldn't find material attribute 'hardnessDamage'"`, becomes `0`. `.durability` missing logs `"Couldn't find material attribute 'durability'"`, becomes `0`. `.swingSpeed` missing logs `"Couldn't find material attribute 'swingSpeed'"`, becomes `0`. `.textureRoughness` **does** have a soft default: `1.0` if missing (website form defaults to `0.0` -- different). `.modifiers[].id`: if the id doesn't match a known modifier, logs `"Couldn't find modifier with id '{id}'. Replacing it with 'durable'"` and silently substitutes the "durable" modifier.

**Procedural items** (`registerProceduralItem()`): a completely separate, more advanced system (weighted parameter matrices mapping material properties to tool stats, `disabled`/`optional` slot arrays) that the website does not support at all -- only reachable by hand-writing the zon file.

## Related Questions
- What does a Cubyz item's .name/.material/.block field default to if omitted?
- What does a Cubyz item's .block field default to if omitted?
- Does a Cubyz item have a .block field, and what does it link to?
- What does the engine actually check to decide whether a Cubyz item has a material?
- What happens if a Cubyz item material's modifier id doesn't match a known modifier?
- What is a Cubyz "procedural item," and can the Addon Creator website create one?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_2*
