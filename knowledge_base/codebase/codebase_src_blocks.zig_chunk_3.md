# [hard/codebase_src_blocks.zig] - Chunk 3

**Type:** api
**Keywords:** packed struct, inline method, reverse indices, block data parsing, migration apply, std.mem.indexOfScalar, ListManaged append, formatBlockData call, selection capabilities, block drops array
**Symbols:** ParseBlockConfig, parseBlockData, parseBlock, parseBlockWithOptions, getBlockById, getBlockData, hasRegistered, Block, air, toInt, fromInt, transparent, collide, id, blockHealth, blockResistance, replaceable, selectionCapabilities, blockDrops, degradable, viewThrough, alwaysViewThrough, hasBackFace, tags, hasTag, light, absorption
**Concepts:** block parsing, packed struct layout, inline accessor methods, reverse index lookup, migration application, data serialization, error handling with std.log

## Summary
This chunk defines the core parsing and lookup logic for Cubyz blocks, including a packed struct definition with many inline accessor methods, plus public functions to parse block data strings, retrieve blocks by ID, check registration, and apply migrations.

## Explanation
The chunk declares ParseBlockConfig as a const struct with an applyMigrations bool field. It defines parseBlockData which splits on ':' and delegates ore parsing or parses raw u16 data; it logs warnings/errors via std.log.warn/std.log.err. The public parseBlock function wraps parseBlockWithOptions with an empty config. parseBlockWithOptions extracts the block ID up to the first ':', calls parseBlockData for the remainder, optionally applies a migration via main.migrations.applySingle if config.applyMigrations is true, then looks up the type in reverseIndices; if found it builds a Block with typ from reverseIndices and data either from parsing or the block's naturalStandard mode, otherwise logs an error and returns air. getBlockById locates the first ':' to split ID and addon name, finds the second ':' to locate data end, extracts id, then calls reverseIndices.get returning NotFound if missing. getBlockData similarly splits on ':', checks for empty data string (returning EmptyDataString), parses the remainder as u16 (catching InvalidData). hasRegistered simply returns reverseIndices.contains(id). The Block struct is a packed(u32) with fields typ:u16 and data:u16; it defines air as a public const Block{.typ=0,.data=0}. It provides toInt/fromInt for integer round-trip, transparent/collide/id/blockHealth/blockResistance/replaceable/viewThrough/alwaysViewThrough/hasBackFace/tags/hasTag/light/absorption all as inline methods returning values from static arrays (_transparent/_collide/_id/_blockHealth/_blockResistance/_replaceable/_selectionCapabilities/_blockDrops/_degradable/_viewThrough/_alwaysViewThrough/_hasBackFace/_tags/_light/_absorption). idAndData appends the block's ID string to a ListManaged(u8) and, if data is non-zero, appends ':' then calls self.mode().formatBlockData(self,list); selectionCapabilities returns _selectionCapabilities[self.typ]; blockDrops returns _blockDrops[self.typ]. All these methods are inline for zero-cost abstraction. The chunk relies on main.migrations.applySingle (external), reverseIndices (external map), std.mem.indexOfScalar/indexOfScalarPos, std.fmt.parseInt, and std.log for diagnostics.

## Related Questions
- How does parseBlockWithOptions handle the case when a block ID is not found in reverseIndices?
- What happens to the data field of a newly constructed Block when reverseIndices.get returns a resultType but blockData is null?
- In getBlockById, why does the function return error.MissingAddonNameSeparator if there is no ':' character in idAndData?
- How does hasRegistered differ from calling parseBlockWithOptions with an empty config on the same ID string?
- What are the exact conditions under which Block.idAndData will append a ':' before invoking formatBlockData?
- Which static arrays are accessed by the inline methods transparent, collide, id, blockHealth, etc., and how is their indexing performed?
- How does the packed struct definition of Block affect memory layout when toInt/fromInt are used for serialization?
- What role does main.migrations.applySingle play in parseBlockWithOptions and under what config flag is it invoked?
- If getBlockData receives an empty data string after splitting on ':', which error variant is returned and why?
- How does the chunk ensure that block IDs are normalized before lookup, given the optional migration step?

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_3*
