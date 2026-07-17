# [easy/codebase_assets_cubyz_biomes_ocean_warm_island_base.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** palm tag, ground structure, sand layers, coconut tree, hibiscus variants, tussock grass, degradable mode, placement chance, density rules, parent biome
**Symbols:** tags, minHeight, maxHeight, radius, hills, ground_structure, structures, parentBiomes
**Concepts:** biome configuration, terrain generation parameters, structure placement probabilities, degradable structures, flower patch density rules, parent biome linking

## Summary
Defines configuration data for a warm ocean island biome including terrain height limits, palm tag classification, ground structure composition with sand layers, and probabilistic placement rules for coconut trees, hibiscus flower patches, and tussock grass.

## Explanation
This chunk contains only static configuration data in .zon format. It declares tags (palm), minHeight (5), maxHeight (6), radius (32), hills count (4), ground_structure specifying sand layers ('2 to 3 cubyz:sand'), and structures defining probabilistic generation rules: a coconut tree structure with id 'cubyz:sbb', type 'cubyz:tree/palm/coconut', degradable placement mode, and 0.015 chance; two flower_patch entries both using id 'cubyz:flower_patch' but differing in blocks (tussock vs hibiscus variants 0-3), with respective chances (0.06 and 0.02), widths (3), variations (2), densities (0.5 and 0.3), and priorities (both 0.2); parentBiomes containing a single entry linking to 'cubyz:ocean/warm/island/shelf' with chance 1 and parentEdgeDistance 37.

## Related Questions
- What is the minimum height value defined for this warm ocean island biome configuration?
- Which tag is assigned to classify this biome as a palm environment?
- How many hills are specified in the terrain generation parameters for this biome?
- What ground structure layers are listed under the ground_structure field?
- Identify the id and type of the tree structure defined with degradable placement mode.
- What is the chance probability value assigned to the coconut tree structure entry?
- List all block types included in the first flower_patch structure definition.
- What are the width, variation, density, and priority values for the hibiscus flower patch entry?
- Which parent biome id is referenced under the parentBiomes field with chance 1?
- What value is assigned to the parentEdgeDistance field in the parentBiomes configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_biomes_ocean_warm_island_base.zig.zon_chunk_0*
