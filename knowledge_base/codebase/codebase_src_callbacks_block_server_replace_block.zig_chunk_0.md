# [easy/codebase_src_callbacks_block_server_replace_block.zig] - Chunk 0

**Type:** api
**Keywords:** cmpxchgBlock, parseBlock, ServerBlockCallback, worldArena, ZonElement, blockPos, super.pos, handled, server callbacks
**Symbols:** block, init, run
**Concepts:** server callbacks, block replacement, atomic block swap, ZON parsing, world arena allocation

## Summary
This chunk defines the server-side callback handler for block replacement events, parsing incoming ZON data to construct a new Block and atomically swapping it into the world via cmpxchgBlock.

## Explanation
The init function receives a ZonElement containing a 'block' field; if missing it logs an error and returns null. It creates a new instance of the block type in main.worldArena, populates its .block field by calling main.blocks.parseBlock on zon.get(...), then returns the constructed pointer. The run method is invoked with ServerBlockCallback.Params that include the target chunk's super.pos (wx, wy, wz) and params.blockPos offsets; it computes absolute world coordinates, calls main.server.world.?cmpxchgBlock to atomically replace self.block with params.block at those coordinates, and returns .handled.

## Code Example
```zig
pub fn init(zon: main.ZonElement, _: main.callbacks.Creator) ?*@This() {
	const result = main.worldArena.create(@This());
	result.* = .{
		.block = main.blocks.parseBlock(zon.get([]const u8, "block") orelse {
			std.log.err("Missing field \"block\" for replace_block event", .{});
			return null;
		}),
	};
	return result;
}
```

## Related Questions
- What happens if the ZON element lacks a 'block' field during init?
- How are absolute world coordinates computed in run?
- Which function performs the atomic block replacement and what does it return?
- Where is the new Block instance allocated before being populated?
- What type does init return when parsing succeeds versus fails?
- Does run modify self.block or params.block, and how are they swapped?
- How does this callback integrate with main.server.world?
- Is there any logging performed on error in this chunk?
- What is the purpose of the ignored Creator argument in init?
- Can init be called multiple times for the same block instance?

*Source: unknown | chunk_id: codebase_src_callbacks_block_server_replace_block.zig_chunk_0*
