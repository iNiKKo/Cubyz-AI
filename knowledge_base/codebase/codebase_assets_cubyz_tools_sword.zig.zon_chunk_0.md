# [easy/codebase_assets_cubyz_tools_sword.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** configuration, matrix, attributes, interaction, disabled states
**Concepts:** tool configuration, attribute interaction

## Summary
This chunk defines configuration data for a sword tool in the Cubyz voxel engine, including tags, disabled states, optional settings, and parameters that define how different attributes interact.

## Explanation
The chunk contains a single anonymous struct with four fields: `.tags`, `.disabled`, `.optional`, and `.parameters`. The `.tags` field is an array of booleans indicating sliceable properties. The `.disabled` field is a 5x5 matrix of booleans representing disabled states for different configurations. The `.optional` field is another 5x5 matrix of booleans indicating optional settings. The `.parameters` field is an array of structs, each defining how one attribute (source) affects another (destination) through a 5x5 matrix and a factor, with a specified method (sum or average). This configuration data is used to define the behavior and properties of the sword tool within the game.

## Related Questions
- What are the tags defined for the sword tool?
- How is the disabled state configured for the sword tool?
- What optional settings are available for the sword tool?
- How does mass damage affect the sword's damage attribute?
- What method is used to calculate the effect of durability on maxDurability?
- How does swing speed interact with itself in different configurations?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_sword.zig.zon_chunk_0*
