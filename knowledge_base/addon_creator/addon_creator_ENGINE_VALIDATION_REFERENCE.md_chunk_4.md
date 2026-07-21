# [medium/addon_creator_ENGINE_VALIDATION_REFERENCE.md] - Chunk 4

**Type:** documentation
**Keywords:** biomes.zig, Biome.init, minRadius, maxRadius, caveSmoothness, caveNoiseStrength, soilCreep, rivers, parentBiomes, transitionBiomes, tags _layer
**Symbols:** Biome.init()

## Summary
Engine-side default values and error messages for every Cubyz biome field, read directly from `server/terrain/biomes.zig: Biome.init()`.

## Explanation
**Simple items** (`BaseItem.init()`):
- `.name`: string, defaults to the item's own `id`. The website never sets this field at all -- items exported via the website always display their raw id as the tooltip name.
- `.tags`: tag list, empty by default.
- `.stackSize`: u16, defaults to `120`, matches the website.
- `.material`: object, defaults to `null` (no material). The engine checks whether this is an **object**, not whether a `.material` tag is present -- in practice these are coupled by the website's own logic.
- `.block`: string id, defaults to `null`. Looked up via `blocks.getTypeById` -- same "Couldn't find block..." fallback-to-air behavior as above if the reference is bad.
- `.food`: f32, defaults to `0`.

**Material sub-object** (`Material.init()`, only runs if `.material` is present) -- **these four have NO silent default**, a missing field logs an explicit error and falls back to `0`, which for durability effectively means the item breaks instantly:
- `.massDamage`: missing → "Couldn't find material attribute 'massDamage'", becomes `0`
- `.hardnessDamage`: missing → "Couldn't find material attribute 'hardnessDamage'", becomes `0`
- `.durability`: missing → "Couldn't find material attribute 'durability'", becomes `0`
- `.swingSpeed`: missing → "Couldn't find material attribute 'swingSpeed'", becomes `0`
- `.textureRoughness`: **does** have a soft default: `1.0` if missing (website form defaults to `0.0` -- different)
- `.modifiers[].id`: **if the id doesn't match a known modifier, logs "Couldn't find modifier with id '{id}'. Replacing it with 'durable'"** and silently substitutes the "durable" modifier

**Procedural items** (`registerProceduralItem()`): a completely separate, more advanced system (weighted parameter matrices mapping material properties to tool stats, `disabled`/`optional` slot arrays) that **the website does not support at all**. Only reachable by hand-writing the zon file.

## Related Questions
- What does a Cubyz biome's .stoneBlock/.fogDensity/.roughness/.interpolation/.caveSmoothness/.caveNoiseStrength/.caveRadiusFactor/.crystals/.soilCreep/.smoothBeaches field default to if omitted?
- Is a Cubyz biome's .rivers field exposed on the Addon Creator website?
- What happens if a Cubyz biome's minimum height is greater than its maximum height?
- What happens if a Cubyz biome's minRadius is greater than its maxRadius, or too small relative to the grid?
- What are Cubyz's .parentBiomes and .transitionBiomes fields used for?

*Source: unknown | chunk_id: addon_creator_ENGINE_VALIDATION_REFERENCE.md_chunk_4*
