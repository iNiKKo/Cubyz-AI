# [easy/codebase_src_callbacks_block_server_check_support_blocks.zig] - Chunk 0

**Type:** implementation
**Keywords:** block replacement, neighbor support, rotation modes, atomic compare-exchange, drop chance, random direction bias, world mutation, callback parameters, model quads, replaceable blocks
**Symbols:** init, run, Neighbor.iterable, main.blocks.meshes.model, neighborBlock.replaceable, neighborModel.neighborFacingQuads, main.rotation.rotations, updateBlockFromNeighborConnectivity, params.block.mode, itemDropsOnChange, blockDrops, cmpxchgBlock, isDroppedWhenBrokenWithItem, random.nextFloat, normalize, drop
**Concepts:** server block callback, neighbor support checking, rotation mode updates, atomic block replacement, item drop handling, ECS world mutation

## Summary
Implements the server-side block callback that checks neighbor support and applies rotation-mode updates before replacing a block, handling drops when the replacement succeeds.

## Explanation
The chunk defines a public function init(_: ZonElement, _: main.callbacks.Creator) ?*@This() that returns an uninitialized pointer to itself. The run function receives params: main.callbacks.ServerBlockCallback.Params and computes absolute world coordinates (wx, wy, wz) by adding the block position offsets to the super chunk's pos fields. It then iterates over Neighbor.iterable, fetching each neighbor block via main.server.world.?.getBlock with an orelse fallback to a zeroed Block type, extracting its model using main.blocks.meshes.model(neighborBlock).model(), and setting neighborSupportive[neighbor.toInt()] = !neighborBlock.replaceable() and neighborModel.neighborFacingQuads[neighbor.reverse().toInt()].len != 0. A newBlock variable is initialized from params.block. An inline loop over comptime std.meta.declarations(main.rotation.rotations) checks if params.block.mode() matches the rotation mode by name; if so, it looks for an updateBlockFromNeighborConnectivity function on that rotation mode's struct field and calls it with (&newBlock, neighborSupportive), otherwise logs an error. If newBlock equals params.block unchanged, returns .ignored. Otherwise attempts cmpxchgBlock at (wx, wy, wz) with the old block and newBlock; if successful (returns null), computes dropAmount via params.block.mode().itemDropsOnChange(params.block, newBlock) and adds any drops from params.block.blockDrops(), iterating through them and dropping stacks that are not dropped when broken with item .null and whose chance is met by main.random.nextFloat(&main.seed). For each such stack, it normalizes a random direction vector (biasing upward by adding 4.0 to dir[2]), constructs a Vec3f position using the block model's min/max bounds plus uniform random offsets, then calls main.server.world.?.drop(stack.clone(), pos, dir, 1). Finally returns .handled if drops occurred or .ignored otherwise.

## Related Questions
- What does the init function return and why is it initialized with undefined?
- How are absolute world coordinates computed from super chunk position and block offsets?
- Why is neighborBlock fetched with an orelse fallback to a zeroed Block type?
- What condition determines whether a neighbor contributes to support for the new block?
- Which rotation modes trigger updateBlockFromNeighborConnectivity and how is it invoked?
- How does the code handle the case when newBlock equals params.block unchanged?
- What happens inside cmpxchgBlock when it returns null versus non-null?
- Why are drops filtered by isDroppedWhenBrokenWithItem(.null) before being spawned?
- Where does the upward bias in drop direction come from and how is it applied?
- How is the drop position computed using the block model's min/max bounds?
- What return value indicates that the callback handled the block replacement successfully?
- Are there any side effects beyond world mutation when updateBlockFromNeighborConnectivity runs?

*Source: unknown | chunk_id: codebase_src_callbacks_block_server_check_support_blocks.zig_chunk_0*
