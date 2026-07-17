# [easy/codebase_assets_cubyz_blocks_monstera.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** cuttable, sliceable, blockHealth, drops, toolEffective, replaceable, degradable, alwaysViewThrough, absorbedLight, lodReplacement
**Symbols:** tags, blockHealth, drops, selectionCapabilities, replaceable, degradable, collide, alwaysViewThrough, absorbedLight, model, rotation, texture, texture_top, texture_bottom, item, lodReplacement, onUpdate
**Concepts:** block configuration, asset references, tool interaction tags, selection capabilities, replaceability flags, degradability, collision settings, light absorption, LOD replacement, update hooks

## Summary
Defines the Monstera block configuration with cuttable/sliceable tags, health value, drop behavior, selection capabilities, replaceability, degradability, collision settings, light absorption, model/rotation/texture references, item texture, LOD replacement, and an onUpdate hook to check support blocks.

## Explanation
This chunk is a .zon configuration file that declares the Monstera block's static properties. It sets tags (.cuttable, .sliceable) which likely affect tool interaction logic elsewhere; blockHealth = 0.2 defines durability or health value for the block entity; drops are configured with an auto item and allowedToolTags restricted to .cuttable; selectionCapabilities is set to .toolEffective meaning only tools can select it; replaceable and degradable flags both true indicate it can be replaced by other blocks and degraded over time; collide false means physics collision is disabled for this block; alwaysViewThrough true makes the block transparent to rendering; absorbedLight = 0x121012 sets a light absorption value (hex); model, rotation, texture, texture_top, texture_bottom provide asset references for the block's visual representation; item contains a single field with texture pointing to monstera/leaf.png which is likely used when the block drops as an item; lodReplacement = cubyz:air specifies the low-detail replacement mesh; onUpdate defines a hook of type .check_support_blocks indicating runtime logic that will verify whether this block has supporting blocks beneath it, possibly affecting stability or drop behavior.

## Related Questions
- What tags are assigned to the Monstera block and what do they imply for tool interaction?
- How is the health of the Monstera block defined in this configuration?
- Which items can drop from the Monstera block and under what conditions?
- What selection capabilities does the Monstera block have and how does that affect gameplay?
- Is the Monstera block replaceable by other blocks and why might that be important?
- Does the Monstera block collide with entities or is it treated as non-solid?
- How does the alwaysViewThrough setting influence rendering of the Monstera block?
- What light absorption value is set for the Monstera block and how is it represented?
- Which model, rotation, and texture assets are referenced for the Monstera block?
- What LOD replacement is configured for the Monstera block when detail level drops?
- What type of update hook is defined for the Monstera block and what does it do?
- How is the item representation of the Monstera block specified in this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_monstera.zig.zon_chunk_0*
