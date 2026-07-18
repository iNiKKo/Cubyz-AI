# [easy/codebase_assets_cubyz_blocks_leaves__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** decay, item drops, rotation, tags, block health
**Concepts:** block configuration, leaf properties

## Summary
Defines default properties for leaves in the Cubyz voxel engine, including decay behavior, item drops, rotation rules, and material tags.

## Explanation
This chunk specifies configuration settings for leaf blocks in the Cubyz game. It includes detailed behavior when updated (decay), item drops with specific probabilities and conditions, rotational properties, material tags, block health, degradability, light absorption, and visual model.

- **Decay Behavior:** The `onUpdate` type is set to `.decay`, and the prevention mechanism includes `.log` and `.branch` types. This means leaves will decay unless they are logs or branches.
- **Item Drops:** There's a 1% chance of dropping an apple when leaves decay, specified in the `drops` section with `{chance = 0.01, items = {"cubyz:apple"}}`. Additionally, there is another drop configuration where an apple can also be dropped with a 1% chance if the tool used to break the leaf does not have the `.cuttable` tag.
- **Rotational Properties:** The `rotation` property is set to `"cubyz:decayable"`, indicating that leaves can rotate in certain ways based on this type.
- **Material Tags:** Leaves are tagged with `cuttable`, `sliceable`, and `leaf`. These tags define their behavior and interactions within the game world.
- **Block Health, Degradability, Light Absorption, and Model:** The block health is set to 0.5, degradability is enabled (`degradable = true`), leaves can always be viewed through (`alwaysViewThrough = true`), absorbed light value is `0x363436`, and the visual model assigned is `"cubyz:cube".`

## Related Questions
- What is the type of update behavior defined for leaves?
- Which items can leaves drop, and under what conditions?
- How are leaves tagged in this configuration?
- Is there a specific model assigned to leaf blocks?
- Can leaves be viewed through always?
- What is the absorbed light value for leaves?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_leaves__defaults.zig.zon_chunk_0*
