# [easy/codebase_assets_cubyz_blocks_grass_vegetation__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, viewThrough, absorbedLight, collide, model, lodReplacement
**Symbols:** tags, blockHealth, drops, items, allowedToolTags, selectionCapabilities, replaceable, degradable, viewThrough, absorbedLight, collide, model, lodReplacement, onUpdate
**Concepts:** block configuration, vegetation defaults, drop behavior, tool interaction tags, selection capabilities, light absorption, LOD replacement, support block checking

## Summary
Defines default configuration for grass vegetation blocks with cuttable/sliceable tags, health value, drop behavior, selection capabilities, replaceability, degradability, view-through property, light absorption, collision flag, model references, LOD replacement, and an onUpdate hook to check support blocks.

## Explanation
This chunk is a .zon configuration file containing a single top-level struct literal with fields: tags (array of cuttable/sliceable), blockHealth (float 0.2), drops (struct with items set to auto and allowedToolTags restricted to cuttable), selectionCapabilities (toolEffective), replaceable, degradable, viewThrough, absorbedLight (zeroed color), collide (false), model string pointing to cubyz:cross, lodReplacement string pointing to cubyz:air, and an onUpdate field of type check_support_blocks. No executable logic or function bodies are present; it serves purely as static data defining block properties.

## Related Questions
- What tags are assigned to grass vegetation blocks by default?
- How is the health value of a grass block defined in this configuration?
- Which tool tag is required for drops from grass blocks to occur automatically?
- Can grass blocks be selected with any tool, or only specific ones?
- Is grass replaceable and degradable according to these defaults?
- Does the grass model allow viewing through it?
- What color value is used for absorbed light on grass blocks?
- Do grass blocks collide with entities by default in this configuration?
- Which model string is referenced as the primary representation of grass?
- What LOD replacement model is specified when rendering distance is exceeded?
- What type of onUpdate hook is attached to grass blocks and what does it do?
- Are there any other block properties defined beyond tags, health, drops, capabilities, replaceability, degradability, view-through, light absorption, collision, model, LOD replacement, and onUpdate?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_grass_vegetation__defaults.zig.zon_chunk_0*
