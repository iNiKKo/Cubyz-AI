# [easy/codebase_assets_cubyz_tools_shover.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, disabled states, optional flags, parameters, matrix transformation
**Concepts:** tool configuration, attribute interaction

## Summary
This chunk defines configuration settings for a tool in the Cubyz voxel engine, including tags, disabled states, optional flags, and parameters that define how various attributes interact.

## Explanation
This chunk defines configuration settings for a tool in the Cubyz voxel engine. The `.tags` field contains the tag `diggable`. The `.disabled` field is a 5x5 matrix of integers representing disabled states: 

```
0, 0, 0, 1, 1,
0, 0, 0, 0, 1,
0, 0, 0, 0, 1,
1, 0, 0, 0, 1,
1, 1, 1, 1, 0
```
The `.optional` field is another 5x5 matrix indicating optional flags: 

```
1, 0, 1, 0, 0,
0, 1, 1, 1, 0,
1, 1, 1, 1, 0,
0, 1, 1, 0, 0,
0, 0, 0, 0, 0
```
The `.parameters` field is an array of structs defining transformations from one attribute to another using a matrix and a factor. Each struct specifies the source and destination attributes, the transformation method (`sum`, `average`), and the specific matrices and factors:

1. Source: massDamage, Destination: damage, Matrix: 
```
2.5, 2.0, 1.0, 0x0, 0x0,
2.0, 2.0, 1.5, 0.5, 0x0,
1.0, 1.5, 1.0, 0.5, 0x0,
0x0, 0.5, 0.5, 0.1, 0x0,
0x0, 0x0, 0x0, 0x0, 0.1
```
Factor: 0.06, Method: sum.
2. Source: massDamage, Destination: damage, Matrix: 
```
2.5, 2.0, 1.0, 0x0, 0x0,
2.0, 2.0, 1.5, 0.5, 0x0,
1.0, 1.5, 1.0, 0.5, 0x0,
0x0, 0.5, 0.5, 0.1, 0x0,
0x0, 0x0, 0x0, 0x0, 0.1
```
Factor: 0.24, Method: average.
3. Source: hardnessDamage, Destination: damage, Matrix: 
```
2.0, 1.0, 0.1, 0x0, 0x0,
1.0, 0.1, 0.1, 0.1, 0x0,
0.1, 0.1, 0.1, 0.1, 0x0,
0x0, 0.1, 0.1, 0.0, 0x0,
0x0, 0x0, 0x0, 0x0, 0.0
```
Factor: 0.2, Method: average.
4. Source: durability, Destination: maxDurability, Matrix: 
```
1.5, 1.0, 0.1, 0x0, 0x0,
1.0, 2.0, 1.0, 0.1, 0x0,
0.1, 1.0, 1.5, 0.5, 0x0,
0x0, 0.1, 0.5, 1.0, 0x0,
0x0, 0x0, 0x0, 0x0, 1.0
```
Factor: 0.8, Method: average.
5. Source: durability, Destination: maxDurability, Matrix: 
```
1.5, 1.0, 0.1, 0x0, 0x0,
1.0, 2.0, 1.0, 0.1, 0x0,
0.1, 1.0, 1.5, 0.5, 0x0,
0x0, 0.1, 0.5, 1.0, 0x0,
0x0, 0x0, 0x0, 0x0, 1.0
```
Factor: 0.2, Method: sum.
6. Source: swingSpeed, Destination: swingSpeed, Matrix: 
```
1.5, 1.5, 0.5, 0x0, 0x0,
1.5, 2.0, 1.5, 0.5, 0x0,
0.5, 1.5, 1.0, 0.5, 0x0,
0x0, 0.5, 0.5, 0.1, 0x0,
0x0, 0x0, 0x0, 0x0, 0.1
```
Factor: 1.2, Method: average.
7. Source: swingSpeed, Destination: swingSpeed, Matrix: 
```
1.5, 1.5, 0.5, 0x0, 0x0,
1.5, 2.0, 1.5, 0.5, 0x0,
0.5, 1.5, 1.0, 0.5, 0x0,
0x0, 0.5, 0.5, 0.1, 0x0,
0x0, 0x0, 0x0, 0x0, 0.1
```
Factor: -0.2, Method: sum.

## Related Questions
- What tags are associated with this tool?
- How is the disabled state matrix structured?
- What optional flags are defined for this tool?
- How many parameters are defined for attribute interaction?
- What methods are used in the parameter transformations?
- What is the purpose of the matrix in each parameter struct?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_shover.zig.zon_chunk_0*
