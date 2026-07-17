# [easy/codebase_assets_cubyz_sbb_tree_oak_young_branch.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprint, chance, identifier, array literal, null entry, oak tree, young branch, side deco, bolete, probability
**Symbols:** blueprints
**Concepts:** tree generation, branch placement, probability weighting, deco elements

## Summary
This chunk defines a static array of blueprint entries for young oak tree branches and side deco elements, each with an identifier string and a probability weight.

## Explanation
The chunk declares a single top-level anonymous struct containing one field named blueprints. This field is initialized as an array literal of nine elements. Each element is a struct literal with two fields: id (a string constant) and chance (a floating-point literal). The identifiers follow the pattern cubyz:tree/oak/young/branch/N for N from 0 to 7, then cubyz:deco/bolete_side, followed by a null entry. No executable logic is present; this is purely configuration data.

## Related Questions
- What is the identifier for the first young oak branch blueprint entry?
- Which blueprint entries have a chance value of 0.25?
- How many total blueprint entries are defined in this configuration array?
- Is there any null entry included in the blueprints array and at what index?
- What is the identifier for the deco element named bolete_side?
- Are all branch identifiers prefixed with cubyz:tree/oak/young/branch?
- Does this chunk contain any executable logic or function definitions?
- How many distinct chance values are used across all blueprint entries?
- What is the highest probability weight assigned to any single entry?
- Is there a pattern in the numeric suffixes of the branch identifiers?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_tree_oak_young_branch.zig.zon_chunk_0*
