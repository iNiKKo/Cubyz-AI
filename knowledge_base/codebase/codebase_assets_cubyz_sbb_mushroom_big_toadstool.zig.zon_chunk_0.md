# [easy/codebase_assets_cubyz_sbb_mushroom_big_toadstool.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** blueprints, children, toadstool, variants, base models
**Symbols:** blueprints, children
**Concepts:** asset registry, blueprint hierarchy, variant mapping

## Summary
This chunk defines the blueprint registry for the big toadstool mushroom asset, listing six base variants and five child branch/cap variants.

## Explanation
The chunk contains a single top-level struct literal with two fields: blueprints (an array of six objects each holding an id string) and children (an object mapping color names to their respective blueprint ids). The blueprints field enumerates the base models for the big toadstool, indexed 0 through 5. The children field maps white, grey, crimson, green, and blue keys to the large_cap, small_cap, branch/red, branch/green, and branch/blue variants respectively.

## Related Questions
- What are the six base blueprint IDs for the big toadstool mushroom?
- Which child variant corresponds to the white color key in this configuration?
- How many total variants (base + children) does this chunk define for the big toadstool?
- What is the ID of the large cap variant defined under the children map?
- Does this chunk include any red branch variant, and if so what is its ID?
- Are there any green or blue branch variants listed in this configuration?

*Source: unknown | chunk_id: codebase_assets_cubyz_sbb_mushroom_big_toadstool.zig.zon_chunk_0*
