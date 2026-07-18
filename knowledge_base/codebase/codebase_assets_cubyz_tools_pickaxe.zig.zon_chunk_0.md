# [easy/codebase_assets_cubyz_tools_pickaxe.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, disabled, optional, parameters, matrix, factor, method
**Concepts:** tool configuration, pickaxe attributes

## Summary
This chunk defines configuration settings for a pickaxe tool in the Cubyz voxel engine.

## Explanation
This chunk defines detailed configuration settings for a pickaxe tool in the Cubyz voxel engine. The JSON-like structure includes specific tags, disabled states, optional states, and multiple parameters that define how different attributes of the pickaxe interact. Each parameter specifies source, destination, matrix, factor, and method for calculating damage, durability, and swing speed. For example, one parameter uses massDamage as the source and damage as the destination with a matrix defined as follows:

```
2.5, 2.0, 1.5, 1.0, 0x0,
2.0, 1.5, 1.0, 0x0, 0x0,
1.5, 1.0, 0.5, 0x0, 0x0,
1.0, 0x0, 0x0, 0.1, 0x0,
0x0, 0x0, 0x0, 0x0, 0.1
```
The factor for this parameter is set to 0.2 and the method used is sum. Another parameter uses hardnessDamage as the source with a matrix defined as:

```
0.0, 0.0, 0.1, 0.1, 0x0,
0.0, 0.1, 0.0, 0x0, 0x0,
0.1, 0.0, 0.0, 0x0, 0x0,
1.0, 0x0, 0x0, 0.0, 0x0,
0x0, 0x0, 0x0, 0x0, 0.0
```
The factor for this parameter is set to 1.0 and the method used is average. Additionally, parameters are defined for durability with matrices such as:

```
0.5, 1.0, 1.0, 1.0, 0x0,
1.0, 2.0, 1.5, 0x0, 0x0,
1.0, 1.5, 1.5, 0x0, 0x0,
1.0, 0x0, 0x0, 1.0, 0x0,
0x0, 0x0, 0x0, 0x0, 0.5
```
The factor for these parameters is set to either 0.2 or 0.8 and the method used can be sum or average. Similarly, swing speed parameters are defined with matrices such as:

```
0.1, 0.5, 2.0, 2.5, 0x0,
0.5, 1.5, 0.5, 0x0, 0x0,
2.0, 0.5, 0.1, 0x0, 0x0,
2.5, 0x0, 0x0, 0.1, 0x0,
0x0, 0x0, 0x0, 0x0, 0.1
```
The factor for these parameters is set to either -0.2 or 1.2 and the method used can be sum or average.

## Related Questions
- What are the specific tags associated with the pickaxe tool?
- How is the disabled state configured for each block type in the pickaxe?
- What optional states are defined for the pickaxe?
- List all parameters and their corresponding matrices, factors, and methods used for calculating damage, durability, and swing speed.
- Provide the exact matrix values and method used for the first parameter that calculates damage.
- Detail the factor applied to the second parameter's matrix in the context of damage calculation.

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_pickaxe.zig.zon_chunk_0*
