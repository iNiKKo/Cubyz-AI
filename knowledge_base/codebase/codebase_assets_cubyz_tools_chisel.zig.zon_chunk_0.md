# [easy/codebase_assets_cubyz_tools_chisel.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** configuration, matrix transformation, attribute interaction, chisel tool, disabled states, optional flags
**Concepts:** tool configuration, attribute mapping

## Summary
This chunk defines configuration settings for the chisel tool in Cubyz, including tags, disabled states, optional flags, and parameters that map various attributes like mass damage, hardness, durability, and swing speed to their respective destinations.

## Explanation
The chunk is a configuration file structured as a Zig object literal. It contains several key fields:

- `.tags`: A list of tags associated with the chisel tool, in this case, just `chiselable`.
- `.disabled`: A 5x5 matrix indicating which attributes are disabled for the chisel tool.
- `.optional`: Another 5x5 matrix indicating which attributes are optional for the chisel tool.
- `.parameters`: An array of parameter objects that define how different attributes (like mass damage, hardness, durability, and swing speed) affect other attributes. Each parameter object includes:
  - `.source`: The source attribute.
  - `.destination`: The destination attribute where the effect is applied.
  - `.matrix`: A 5x5 matrix defining the transformation from source to destination.
  - `.factor`: A scaling factor for the transformation.
  - `.method`: The method used to combine the transformed values (either `sum` or `average`).

This configuration file is likely used by the Cubyz engine to determine how the chisel tool interacts with different materials and attributes in the game world.

## Related Questions
- What tags are associated with the chisel tool?
- How is the disabled state matrix structured for the chisel tool?
- Which attributes have optional settings in the chisel configuration?
- How does mass damage affect other attributes according to the parameters?
- What methods are used to combine transformed values in the chisel's parameter mappings?
- Can you explain the structure of the `.parameters` array in the chisel configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_chisel.zig.zon_chunk_0*
