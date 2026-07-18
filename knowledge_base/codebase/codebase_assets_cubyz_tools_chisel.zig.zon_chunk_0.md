# [easy/codebase_assets_cubyz_tools_chisel.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** configuration, matrix transformation, attribute interaction, chisel tool, disabled states, optional flags
**Concepts:** tool configuration, attribute mapping

## Summary
This chunk defines configuration settings for the chisel tool in Cubyz, including tags, disabled states, optional flags, and parameters that map various attributes like mass damage, hardness, durability, and swing speed to their respective destinations.

## Explanation
This chunk defines configuration settings for the chisel tool in Cubyz, including tags, disabled states, optional flags, and parameters that map various attributes like mass damage, hardness, durability, and swing speed to their respective destinations. The detailed structure is as follows:

- `.tags`: A list of tags associated with the chisel tool, in this case, just `chiselable`.
- `.disabled`: A 5x5 matrix indicating which attributes are disabled for the chisel tool: 
  ```
  0, 0, 1, 1, 1,
  0, 0, 0, 1, 1,
  1, 0, 0, 1, 1,
  1, 1, 1, 0, 0,
  1, 1, 1, 0, 0
  ```
- `.optional`: Another 5x5 matrix indicating which attributes are optional for the chisel tool: 
  ```
  0, 1, 0, 0, 0,
  1, 1, 1, 0, 0,
  0, 1, 1, 0, 0,
  0, 0, 0, 1, 1,
  0, 0, 0, 1, 0
  ```
- `.parameters`: An array of parameter objects that define how different attributes (like mass damage, hardness, durability, and swing speed) affect other attributes. Each parameter object includes:
  - `.source`: The source attribute.
  - `.destination`: The destination attribute where the effect is applied.
  - `.matrix`: A 5x5 matrix defining the transformation from source to destination.
  - `.factor`: A scaling factor for the transformation.
  - `.method`: The method used to combine the transformed values (either `sum` or `average`).

The specific parameters are:
- Mass damage to damage with sum method: 
  ```
  matrix = [0.5, 0.5, 0x0, 0x0, 0x0,
            0.5, 0.5, 0.5, 0x0, 0x0,
            0x0, 0.5, 0.5, 0x0, 0x0,
            0x0, 0x0, 0x0, 0.5, 0.5,
            0x0, 0x0, 0x0, 0.5, 0.5],
  factor = 0.2
  ```
- Mass damage to damage with average method: 
  ```
  matrix = [0.5, 0.5, 0x0, 0x0, 0x0,
            0.5, 0.5, 0.5, 0x0, 0x0,
            0x0, 0.5, 0.5, 0x0, 0x0,
            0x0, 0x0, 0x0, 0.5, 0.5,
            0x0, 0x0, 0x0, 0.5, 0.5],
  factor = 0.8
  ```
- Hardness damage to damage with average method: 
  ```
  matrix = [0.2, 0.1, 0x0, 0x0, 0x0,
            0.1, 0.1, 0.0, 0x0, 0x0,
            0x0, 0.0, 0.0, 0x0, 0x0,
            0x0, 0x0, 0x0, 0.0, 0.0,
            0x0, 0x0, 0x0, 0.0, 0.0],
  factor = 1.0
  ```
- Durability to maxDurability with sum method: 
  ```
  matrix = [1.5, 1.5, 0x0, 0x0, 0x0,
            1.5, 2.0, 1.0, 0x0, 0x0,
            0x0, 1.0, 0.5, 0.5, 0x0,
            0x0, 0x0, 0.5, 0.1, 0.1,
            0x0, 0x0, 0x0, 0.1, 0.1],
  factor = 0.2
  ```
- Durability to maxDurability with average method: 
  ```
  matrix = [1.5, 1.5, 0x0, 0x0, 0x0,
            1.5, 2.0, 1.0, 0x0, 0x0,
            0x0, 1.0, 0.5, 0.5, 0x0,
            0x0, 0x0, 0.5, 0.1, 0.1,
            0x0, 0x0, 0x0, 0.1, 0.1],
  factor = 0.8
  ```
- Swing speed to swingSpeed with sum method: 
  ```
  matrix = [1.0, 1.0, 0x0, 0x0, 0x0,
            1.0, 1.5, 1.0, 0x0, 0x0,
            0x0, 1.0, 1.0, 1.0, 0x0,
            0x0, 0x0, 1.0, 0.5, 0.5,
            0x0, 0x0, 0x0, 0.5, 0.5],
  factor = 1.2
  ```

## Related Questions
- What tags are associated with the chisel tool?
- How is the disabled state matrix structured for the chisel tool?
- Which attributes have optional settings in the chisel configuration?
- Can you provide the detailed parameters for mass damage to damage mappings?
- What methods and factors are used for hardness damage to damage mapping?
- Explain the structure of the `.parameters` array in detail, including specific matrices and factors.

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_chisel.zig.zon_chunk_0*
