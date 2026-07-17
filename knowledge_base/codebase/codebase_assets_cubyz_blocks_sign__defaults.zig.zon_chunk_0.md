# [easy/codebase_assets_cubyz_blocks_sign__defaults.zig.zon] - Chunk 0

**Type:** configuration
**Keywords:** choppable, wood, drops, auto, viewThrough, collide, rotation, model, blockEntity, edit_sign
**Symbols:** .tags, .blockHealth, .drops, .viewThrough, .alwaysViewThrough, .collide, .rotation, .model, .side, .ceiling, .floor, .blockEntity, .onInteract
**Concepts:** block defaults, sign configuration, item drops, view properties, rotation model paths, interaction types

## Summary
Defines the default configuration for a sign block in Cubyz, specifying its tags, health, drops, view properties, rotation model paths, and interaction behavior.

## Explanation
This chunk declares a single top-level struct instance (implicitly named by context) containing all static defaults for the sign block. The .tags field lists .choppable and .wood as string literals; .blockHealth is an integer literal 2; .drops contains one element with items set to the auto enum variant; .viewThrough and .alwaysViewThrough are boolean literals true; .collide is a boolean literal false; .rotation holds the string literal cubyz:sign; .model is a struct with three fields (side, ceiling, floor) each holding string literals referencing cubyz:sign/side, cubyz:sign/ceiling, and cubyz:sign/floor respectively; .blockEntity is the string literal cubyz:sign; .onInteract contains one element whose type field holds the enum variant edit_sign. All fields are initialized with compile-time constants or string literals, indicating this chunk serves purely as configuration data with no executable logic.

## Related Questions
- What tags are assigned to the sign block by default?
- How much health does the sign block have out of its maximum?
- Which item drop configuration is used for the sign block?
- Does the sign block allow viewing through it by default?
- Is there a separate alwaysViewThrough flag and what value does it hold?
- Can players collide with the sign block under these defaults?
- What rotation identifier is specified for the sign block model?
- Which three model parts are referenced in the .model field?
- What block entity name is associated with this sign configuration?
- What interaction type is defined when a player interacts with the sign?

*Source: unknown | chunk_id: codebase_assets_cubyz_blocks_sign__defaults.zig.zon_chunk_0*
