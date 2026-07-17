# [easy/codebase_assets_cubyz_sbb_tree_tuften_tuft_tree.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, chance, id, children, tuft_canopy, straight, tilt, curvy, askew, stem
**Symbols:** .blueprints, .children
**Concepts:** blueprint registry, stem variants, spawn chance configuration, canopy child reference

## Summary
This chunk defines the blueprint registry for Tuften tuft trees, listing stem variants (straight, tilt, curvy, askew) with optional spawn chances and a single child canopy reference.

## Explanation
The chunk contains only configuration data: a .blueprints array of struct literals each providing an id string for a stem blueprint; some entries additionally include a chance field set to 0.5 (straight/9–10, tilt/7–10, curvy/7–8, askew/8–10). The .children map assigns the pink canopy blueprint 'cubyz:tree/tuften/tuft_canopy' as the child of these stems.

## Related Questions
- What stem blueprint IDs are defined for Tuften tuft trees?
- Which stem variants include a spawn chance and what is its value?
- How many straight stem entries exist in the blueprints array?
- Is there any duplicate entry in the blueprints list, and if so which one?
- What child canopy blueprint is referenced by these stems?
- Are any tilt or curvy variants missing a chance field?
- Does the children map contain only pink entries for Tuften tuft trees?
- How many total stem entries are present in the blueprints array?
- Which askew variant IDs appear in the configuration?
- What is the exact id string for the straight/8 entry?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_tree_tuften_tuft_tree.zig.zon_chunk_0*
