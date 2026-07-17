# [easy/codebase_assets_cubyz_tools_shover.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, disabled, optional, parameters, massDamage, hardnessDamage, durability, swingSpeed, damage, maxDurability, sum, average
**Symbols:** .tags, .disabled, .optional, .parameters
**Concepts:** tool configuration, damage parameterization, stat transformation matrices, diggable item tagging, optional behavior flags

## Summary
Defines a configuration object for the Shover tool with tags, disabled flags, optional flags, and multiple damage parameter sets.

## Explanation
This chunk declares a single struct instance containing static configuration data. The .tags field is an array of enum values marking the item as diggable. The .disabled field is a 10-element bool array where indices 3,4,6,7,9 are true (the rest false). The .optional field is a 5x2 bool matrix indicating optional behavior flags per row/column. The .parameters field holds an array of five parameter objects; each object specifies a source stat (.massDamage, .hardnessDamage, or .durability), a destination stat (.damage, .maxDurability, or .swingSpeed), a 5x5 float matrix defining the transformation coefficients, a scalar factor (e.g., 0.06, 0.24, 0.8, -0.2), and an aggregation method (.sum or .average). No executable logic is present; this chunk serves purely as data configuration for tool behavior.

## Related Questions
- What does the .tags field indicate for this tool?
- Which indices in the .disabled array are marked as true?
- How many parameter sets are defined in the .parameters array?
- What is the source stat for the first parameter set?
- What aggregation method is used for the second parameter set?
- Does any parameter set use a negative factor, and if so which one?
- Which destination stat corresponds to the .swingSpeed source in the parameters?

*Source: unknown | chunk_id: codebase_assets_cubyz_tools_shover.zig.zon_chunk_0*
