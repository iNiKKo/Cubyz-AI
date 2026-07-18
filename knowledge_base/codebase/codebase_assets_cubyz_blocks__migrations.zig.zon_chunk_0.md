# [easy/codebase_assets_cubyz_blocks__migrations.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** migration, block identifier, update, mapping list, old name, new name
**Symbols:** migrations
**Concepts:** block migration, identifier update

## Summary
Block migration mappings

## Explanation
This chunk contains 114 block migration mappings (old identifier -> new identifier), covering renamed stone types (e.g. `stone` -> `slate`, `stone_bricks` -> `slate_bricks`), a full material-naming overhaul splitting flat names into `material/variant` paths (e.g. `basalt` -> `basalt/base`, later further split to `basalt/base` -> `basalt/smooth`), leaves/planks/fences reorganized under shared prefixes (e.g. `oak_leaves` -> `leaves/oak`, `oak_planks` -> `planks/oak`, `oak_fence` -> `fence/oak`), glow crystal color renames (e.g. `glow_crystal/dark_gray` -> `glow_crystal/grey`), and grass variant renames (e.g. `grass` -> `grass/temperate`, `dry_grass_vegetation` -> `grass/vegetation/dry`). `mossy_cobblestone` -> `cobblestone`; `void_stone` -> `voidstone/base`; `terracotta_bricks` -> `terracotta/bricks`.

## Related Questions
- What are the old and new block identifiers for 'glow_crystal/dark_gray'?
- How many block migration mappings are listed in this chunk?
- Which block identifier has been updated from 'stone_bricks' to 'slate_bricks'?
- What is the new name for 'mossy_cobblestone'?
- What is the new name for 'basalt'?
- What are the old and new block identifiers for 'void_stone'?
- Which block identifier has been updated from 'terracotta_bricks' to 'terracotta/bricks'?
- What is the new name for 'dry_grass_vegetation'?
- Which block identifier has been updated to 'leaves/oak'?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks__migrations.zig.zon_chunk_0*
