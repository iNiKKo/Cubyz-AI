# [easy/codebase_assets_cubyz_sbb_tree_tuften_young_tuft_canopy.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprint, identifier, string array, static data, tuft tree
**Symbols:** blueprints
**Concepts:** configuration, asset registry, tree generation

## Summary
This chunk defines a static configuration of blueprint identifiers for young tuft trees, organized into small and big size categories across five color variants.

## Explanation
The chunk contains only a single top-level struct with a public field named blueprints that holds an array of anonymous structs. Each element in the array is a struct literal containing exactly one field id of type string. The values are hardcoded identifiers prefixed with cubyz:tree/tuften/young/tufts/, followed by either small or big, then one of violet, pink, red, orange, or yellow.

## Related Questions
- What blueprint IDs are defined for young tuft trees in this configuration?
- How many distinct color variants exist across the small and big size categories?
- Is there any executable logic associated with these blueprint identifiers?
- Which file format is used to store this static data structure?
- Are the identifiers scoped globally or module-local within the Cubyz engine?
- Can additional blueprints be appended at runtime without modifying this chunk?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_tree_tuften_young_tuft_canopy.zig.zon_chunk_0*
