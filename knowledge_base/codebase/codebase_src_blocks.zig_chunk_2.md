# [hard/codebase_src_blocks.zig] - Chunk 2

**Type:** implementation
**Keywords:** finishBlocks, registerBlockDrop, registerLodReplacement, registerOpaqueVariant, registerCallbacks, parseBlock, getTypeById, BaseItemIndex, Tag.loadTagsFromZon, ClientBlockCallback, ServerBlockCallback, BlockTouchCallback
**Symbols:** finishBlocks, registerBlockDrop, registerLodReplacement, registerOpaqueVariant, registerCallbacks, parseBlock, parseBlockWithOptions, getTypeById
**Concepts:** block registration, ZON parsing, tool tag filtering, event callbacks, LOD replacement, opaque variant resolution, block data payload parsing

## Summary
This chunk implements the block registration and parsing subsystem: it loads block drop definitions from ZON files (items, chance, tool tags), registers LOD replacements, opaque variants, and event callbacks; parses block identifiers with optional data payloads; provides a public API to resolve block types by ID.

## Explanation
The chunk defines several internal functions that are invoked during initialization. The main entry point is finishBlocks(zonElements: Assets.ZonHashMap), which iterates over the global size counter and calls registerBlockDrop, registerLodReplacement, registerOpaqueVariant, and registerCallbacks for each block ID stored in _id[]. Each register* function reads a ZON element (zon) corresponding to that block. registerBlockDrop parses the ZON's 'items' field as space‑separated strings: it trims whitespace, splits on spaces, takes the first token as name and counts subsequent tokens as amount (defaulting to 1), then looks up each name in items.BaseItemIndex.fromId(name) and appends a resultItems entry. It also reads 'allowedToolTags' and 'forbiddenToolTags' children via Tag.loadTagsFromZon(main.worldArena, ...) and logs an error if allowedToolTags is empty. The function returns a BlockDrop struct with fields items, chance (default 1), forbiddenToolTags, and allowedToolTags. registerLodReplacement reads the optional 'lodReplacement' child; if present it calls getTypeById(replacement) to resolve the replacement block type, otherwise stores typ itself. registerOpaqueVariant similarly reads 'opaqueVariant' and resolves via getTypeById, defaulting to typ. registerCallbacks initializes a series of callback fields: _onInteract uses ClientBlockCallback.init with zon.getChildOrNull(

## Related Questions
- What happens when a block drop's allowedToolTags field is empty?
- How does the chunk resolve an opaque variant for a given block type?
- Which callback types are registered by registerCallbacks and what do they represent?
- How does parseBlockWithOptions separate the block ID from its data payload?
- What error logging occurs if getTypeById cannot find a requested block ID?
- How is the items field of a BlockDrop constructed from space‑separated strings in ZON?

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_2*
