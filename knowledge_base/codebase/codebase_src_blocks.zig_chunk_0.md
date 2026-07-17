# [hard/codebase_src_blocks.zig] - Chunk 0

**Type:** implementation
**Keywords:** BlockDrop, Ore, SelectionCapabilities, toolEffective, proceduralItem, selection wand, fluid tags, block type matching, loadFromZon, maxBlockCount
**Symbols:** maxBlockCount, BlockDrop, Ore, SelectionCapabilities, _transparent, _collide, _id, _blockHealth, _blockResistance, _replaceable, _selectionCapabilities, _blockDrops, _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _tags, _light, _absorption, _onInteract, _onBreak, _onUpdate, _mode, _modeData, _lodReplacement, _opaqueVariant, _friction, _bounciness
**Concepts:** block properties, selection capabilities, ore generation, drop mechanics, per-block arrays

## Summary
This chunk defines the core block data structures and global state arrays for the voxel engine, including BlockDrop, Ore, SelectionCapabilities, and a comprehensive set of per-block property arrays.

## Explanation
The chunk imports several modules (main, chunk, graphics, items, models, rotation) and re-exports their public symbols as constants. It declares maxBlockCount as a 16-bit limit (65536). BlockDrop is a struct with fields items, chance, forbiddenToolTags, allowedToolTags; it exposes an inline method isDroppedWhenBrokenWithItem that checks procedural item tags against the drop's allowed/forbidden lists. Ore is a struct with size, density, veins, maxHeight, minHeight, blockType, seed. SelectionCapabilities is a union(enum) with two variants: always (void) and custom (packed struct(u1) containing toolEffective). The custom variant exposes allowsSelectionByItem which handles procedural item effectiveness, the selection wand baseItem, fluid tags, and exact block type matching; it also defines loadFromZon to parse capability flags from a ZonElement. A series of global arrays are declared with undefined initialization: _transparent, _collide, _id, _blockHealth, _blockResistance, _replaceable, _selectionCapabilities, _blockDrops, _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _tags, _light, _absorption, _onInteract, _onBreak, _onUpdate, _mode (pointer to RotationMode), _modeData, _lodReplacement, _opaqueVariant, _friction, _bounciness. These arrays represent the per-block property storage used elsewhere in the engine.

## Related Questions
- What is the maximum number of blocks defined by maxBlockCount?
- How does BlockDrop determine if a procedural item can drop when breaking a block?
- Which fields are present in the Ore struct for underground vein generation?
- What variants exist in SelectionCapabilities and how do they differ?
- How is toolEffective used inside the custom variant of SelectionCapabilities?
- Describe the logic of allowsSelectionByItem for baseItem type checks.
- What does loadFromZon return when parsing a ZonElement with capability flags?
- Which global arrays are declared to store per-block properties in this chunk?
- How is _mode typed and what does it point to?
- What is the purpose of _replaceable according to its comment?

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_0*
