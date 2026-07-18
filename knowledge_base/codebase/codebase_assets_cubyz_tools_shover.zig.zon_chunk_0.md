# [easy/codebase_assets_cubyz_tools_shover.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, disabled states, optional flags, parameters, matrix transformation
**Concepts:** tool configuration, attribute interaction

## Summary
This chunk defines configuration settings for a tool in the Cubyz voxel engine, including tags, disabled states, optional flags, and parameters that define how various attributes interact.

## Explanation
The chunk contains a single anonymous struct with several fields: `.tags`, `.disabled`, `.optional`, and `.parameters`. The `.tags` field is an array containing the tag `diggable`. The `.disabled` field is a 5x5 matrix of integers representing disabled states. The `.optional` field is another 5x5 matrix indicating optional flags. The `.parameters` field is an array of structs, each defining a transformation from one attribute to another using a matrix and a factor, with methods like `sum` or `average`. These parameters likely control how the tool affects different attributes in the game.

## Related Questions
- What tags are associated with this tool?
- How is the disabled state matrix structured?
- What optional flags are defined for this tool?
- How many parameters are defined for attribute interaction?
- What methods are used in the parameter transformations?
- What is the purpose of the matrix in each parameter struct?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_shover.zig.zon_chunk_0*
