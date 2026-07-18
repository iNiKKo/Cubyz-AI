# [easy/codebase_assets_cubyz_blocks_cloth__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, health, drops, collision, model, rotation, degradability
**Concepts:** block configuration, item drops

## Summary
Defines default properties for the cloth block in Cubyz.

## Explanation
This chunk specifies the configuration settings for a cloth block within the Cubyz game engine. It sets various attributes such as tags, health, drop items, collision behavior, model, rotation, and degradability. The `.tags` field includes identifiers like 'cloth' and 'cuttable'. The `blockHealth` is set to 2, indicating the durability of the block. The `drops` array specifies that the block will automatically drop its own item when broken. The `collide` property is set to false, meaning the block does not obstruct movement or interactions. The `model` and `rotation` fields both reference 'cubyz:carpet', suggesting a visual representation of a carpet. Lastly, the `degradable` property is true, indicating that the block can degrade over time.

## Related Questions
- What are the tags assigned to the cloth block?
- How much health does the cloth block have?
- What items will drop when the cloth block is broken?
- Does the cloth block obstruct movement?
- Which model and rotation settings are used for the cloth block?
- Is the cloth block degradable?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_cloth__defaults.zig.zon_chunk_0*
