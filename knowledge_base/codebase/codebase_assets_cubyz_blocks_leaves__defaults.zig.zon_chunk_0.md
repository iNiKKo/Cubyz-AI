# [easy/codebase_assets_cubyz_blocks_leaves__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** decay, prevention, drops, chance, cuttable, forbiddenToolTags, rotation, tags, blockHealth, degradable
**Symbols:** onUpdate, decay, prevention, log, branch, drops, chance, items, auto, allowedToolTags, cuttable, forbiddenToolTags, rotation, tags, blockHealth, degradable, alwaysViewThrough, absorbedLight, model
**Concepts:** decay prevention, drop mechanics, tool tag filtering, light absorption, block health system, texture rotation

## Summary
Defines default configuration for leaf blocks including decay behavior, drop mechanics, tool interaction tags, and visual properties.

## Explanation
This chunk declares a single top-level struct instance (implicitly named by its field names) that configures leaf block defaults. The .onUpdate field specifies decay type as .decay with prevention set to the union {log, branch}, indicating that log and branch blocks prevent decay from occurring on adjacent leaves. The drops array contains two entries: the first allows auto-drops when any cuttable tool is used (allowedToolTags = {cuttable}), while the second explicitly defines a 0.01 chance drop of cubyz:apple when using forbidden tools tagged as cuttable, meaning apples only drop if the player uses a non-cuttable tool on leaves. The rotation field references cubyz:decayable for texture orientation. Tags include cuttable, sliceable, and leaf, defining interaction categories. blockHealth is set to 0.5 (half of a full block), degradable is true indicating leaves can be broken by any means, alwaysViewThrough is true allowing visibility through the block, absorbedLight uses hex value 0x363436 for light absorption calculations, and model references cubyz:cube as the default mesh.

## Related Questions
- What decay prevention types are defined for leaf blocks?
- How does the drops configuration handle auto-drops versus chance-based drops?
- Which tool tags allow or forbid apple drops from leaves?
- What is the default block health value for leaves and what does degradable true imply?
- How does alwaysViewThrough affect rendering of leaf blocks?
- What rotation model is assigned to decayable leaves by default?
- What light absorption hex value is used for leaves in this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_leaves__defaults.zig.zon_chunk_0*
