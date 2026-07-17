# [easy/codebase_assets_cubyz_blocks_trumpet_lily.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, viewThrough, absorbedLight, collide, model, rotation, texture, item, lodReplacement
**Symbols:** trumpet_lily
**Concepts:** block configuration, cuttable tags, tool-specific drops, replaceability, light absorption, model references, texture mapping, support block checking

## Summary
Defines the trumpet lily block configuration with cuttable/sliceable tags, low health, tool-specific drops, replaceability, light absorption properties, model/rotation references, texture mappings, and a support-check update callback.

## Explanation
This chunk declares a single block entity named trumpet_lily. Its tags are set to .cuttable and .sliceable, indicating it can be harvested with cutting tools. The blockHealth is 0.2, meaning it breaks quickly under any damage source. Drops are defined as an auto-item that requires the cuttable tool tag; no other drop sources are listed. SelectionCapabilities includes only .toolEffective, so players must use a tool to select it. Replaceable and degradable flags are true, allowing block replacement and degradation mechanics. ViewThrough is true, making the block transparent for rendering purposes. AbsorbedLight is 0x000000 (no light absorption). Collide is false, meaning entities pass through without collision. The model reference points to cubyz:flower/height_10, and rotation uses cubyz:planar. Texture mappings assign the same trumpet_lily texture for front/sides and trumpet_lily_top for top/bottom faces. The item representation references trumpet_lily.png. OnUpdate is set to .check_support_blocks, indicating a runtime check for support block validity.

## Related Questions
- What tags are assigned to the trumpet lily block?
- How does the trumpet lily handle player selection capabilities?
- Is the trumpet lily replaceable and degradable by default?
- Does the trumpet lily absorb light or is it fully transparent?
- Which model reference is used for rendering the trumpet lily?
- What rotation style is applied to the trumpet lily block?
- How are textures mapped across different faces of the trumpet lily?
- What item texture represents the trumpet lily in inventory views?
- Does the trumpet lily have any collision properties enabled?
- What update callback is registered for the trumpet lily on runtime?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_trumpet_lily.zig.zon_chunk_0*
