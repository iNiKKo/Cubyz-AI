# [easy/codebase_assets_cubyz_blocks_vine__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, vine_decay, toolEffective, replaceable, degradable, viewThrough, absorbedLight, collision, model, rotation, LOD
**Symbols:** .tags, .blockHealth, .onUpdate, .drops, .selectionCapabilities, .replaceable, .degradable, .viewThrough, .absorbedLight, .collide, .model.top, .model.bottom, .rotation, .lodReplacement
**Concepts:** block defaults, item drops, tool tags, update behavior, selection capabilities, light absorption, collision settings, model definitions, rotation configuration, LOD replacement

## Summary
Defines default configuration for the vine block, specifying its tags, health, update behavior, drop rules, selection capabilities, replaceability, degradability, light absorption, collision settings, and model/rotation definitions.

## Explanation
This chunk declares a single top-level struct literal containing all default properties of the vine block. The .tags field lists cuttable and sliceable tags; .blockHealth is set to 0.3; .onUpdate references the vine_decay update type; .drops contains an item with auto drop behavior restricted to cuttable tools via allowedToolTags; .selectionCapabilities includes toolEffective; .replaceable and .degradable are both true; .viewThrough is true; .absorbedLight is zero (0x000000); .collide is false; the .model object defines top as cubyz:cross and bottom as cubyz:cross_with_texture_1; .rotation is set to cubyz:hanging; .lodReplacement points to cubyz:air.

## Related Questions
- What tags are assigned to the vine block by default?
- How is the health of the vine block configured in this chunk?
- Which update type is associated with the vine block's behavior?
- Under what conditions does the vine drop items, and which tools allow drops?
- What selection capabilities does the vine block support out of the box?
- Is the vine block replaceable by default, and can it degrade?
- Does the vine block allow viewing through it, and how is light absorption handled?
- Are there any collision settings defined for the vine block in this configuration?
- What model assets are referenced for the top and bottom of the vine block?
- How is the rotation of the vine block specified by default?
- Which LOD replacement asset is used when the vine becomes invisible?
- Can I infer any other blocks that share these exact default values from this chunk?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_vine__defaults.zig.zon_chunk_0*
