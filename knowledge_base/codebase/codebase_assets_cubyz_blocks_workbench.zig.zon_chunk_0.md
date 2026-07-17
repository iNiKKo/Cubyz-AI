# [easy/codebase_assets_cubyz_blocks_workbench.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** tags, blockHealth, drops, onInteract, open_window, model, rotation, texture, choppable, auto drops
**Symbols:** .tags, .blockHealth, .drops, .onInteract, .model, .rotation, .texture, .texture_front, .texture_left, .texture_right, .texture_top, .texture_bottom
**Concepts:** block definition, choppable tag, drop configuration, interaction handler, window UI trigger, model reference, planar rotation, multi-texture mapping

## Summary
Defines a workbench block with choppable tags, health value, drop configuration, interaction behavior (open_window), and six-sided texture references.

## Explanation
This chunk declares a single block definition object containing metadata for the workbench. The .tags field is set to an array with one element of type .choppable, indicating the block can be chopped. The .blockHealth scalar is assigned the integer value 10. The .drops field contains an array with one entry specifying that drops are handled via the .auto mode (no explicit item list). The .onInteract field defines interaction behavior as a struct with type set to .open_window and name set to the string literal workbench, meaning interacting opens a window UI element named workbench. The .model field references cubyz:cube, indicating the base mesh model used for rendering. The .rotation field is set to cubyz:planar, specifying planar rotation behavior. Six texture fields are present: .texture points to cubyz:workbench_back (back face), .texture_front points to cubyz:workbench_front (front face), and four side faces (.texture_left, .texture_right) both point to cubyz:workbench_side, while .texture_top and .texture_bottom point to cubyz:workbench_top and cubyz:workbench_bottom respectively.

## Related Questions
- What is the health value assigned to the workbench block?
- Which tag indicates that this block can be chopped?
- How are drops configured for this block (explicit list or auto)?
- What type of interaction handler does the onInteract field specify?
- What name string is associated with the open_window interaction?
- Which model reference is used for rendering this block?
- What rotation mode is set for the workbench block?
- How many distinct texture files are referenced in this definition?
- Which face of the block maps to cubyz:workbench_side?
- Are any of the texture fields omitted or null?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_workbench.zig.zon_chunk_0*
