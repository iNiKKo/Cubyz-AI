# [easy/codebase_assets_cubyz_tools_chisel.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, disabled, optional, parameters, massDamage, hardnessDamage, durability, swingSpeed, matrix, factor, method
**Symbols:** tags, disabled, optional, parameters
**Concepts:** voxel property configuration, attribute mapping, matrix blending, chiselable tags

## Summary
Defines a static configuration block for chiselable voxel properties containing tags, per-axis disable flags, optional status arrays, and multiple parameter sets mapping source attributes to destination fields via matrix transformations.

## Explanation
This chunk contains only a single top-level anonymous struct literal with no executable logic. It declares the field 'tags' as an array of one element tagged '.chiselable'. The field 'disabled' is a 5x5 boolean-like array (using integers) where specific axes are marked disabled: rows [0,1], cols [2,3] and diagonals [4,5]. The field 'optional' is another 5x5 array indicating optional status per axis. The field 'parameters' holds an array of five parameter objects; each object specifies a source attribute (massDamage, hardnessDamage, durability, swingSpeed), a destination attribute (damage, maxDurability, or the same attribute), a 5x5 numeric matrix defining linear blending coefficients, a scalar factor (0.2, 0.8, 1.0, -0.2, 1.2), and a method enum value (.sum or .average). No functions are defined here; all data is static configuration intended to be consumed by other modules.

## Related Questions
- What is the value of the tags array in this configuration?
- Which axes are marked as disabled by the disabled field?
- How many optional entries exist and which ones are enabled?
- List all source attributes defined across the parameters array.
- Describe the matrix coefficients for the first parameter entry.
- What method is used for the second parameter entry?
- Which destination attribute corresponds to the third parameter entry?
- Are any parameters configured with a negative factor value?
- How many parameters map swingSpeed to itself?
- Does this configuration define any hardnessDamage mappings?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_chisel.zig.zon_chunk_0*
