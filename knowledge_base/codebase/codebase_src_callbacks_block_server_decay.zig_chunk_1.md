# [medium/codebase_src_callbacks_block_server_decay.zig] - Chunk 1

**Type:** implementation
**Keywords:** decayable, branch, placedByHuman, foundWayToLog, cmpxchgBlock, blockDrops, random chance, model bounds, upward bias
**Symbols:** foundWayToLog, cmpxchgBlock, blockDrops
**Concepts:** decay callback, rotation validation, branch data handling, proximity log detection, atomic block replacement, random drop generation, model bounds sampling, upward bias direction

## Summary
Implements the server-side decay callback for blocks, handling rotation checks (decayable/branch), proximity log detection via foundWayToLog, atomic block replacement with cmpxchgBlock, and random drop generation when a leaf is replaced.

## Explanation
The function first validates that the block's mode is either 'cubyz:decayable' or 'cubyz:branch'; for decayable it requires data == 0 (ignoring otherwise), for branch it reads BranchData and ignores if placedByHuman. If neither matches, an error log is emitted with the block ID. When a world exists, it queries the block at coordinates (wx, wy, wz) to obtain leaf; if found, it calls self.foundWayToLog(world, leaf, wx, wy, wz) to check for nearby logs and returns .ignored if true. If no log is nearby, it attempts an atomic compare-and-swap replacement of the block with self.decayReplacement via world.cmpxchgBlock; on success (non-null result), it iterates over self.blockDrops: for each drop whose chance condition is met (chance == 1 or random < drop.chance using main.random.nextFloat seeded by &main.seed), it clones each item stack and spawns a drop at a randomized position derived from the leaf's model bounds, with an upward bias added to the Y component of the direction vector. The spawn uses main.server.world.?.drop(stack.clone(), pos, dir, 1). If cmpxchgBlock fails (returns null) or no world exists, the function returns .ignored.

## Related Questions
- What rotation modes are accepted for the decay callback and how is each validated?
- How does the function decide whether to ignore a block based on its data field or BranchData.placedByHuman?
- Describe the exact condition under which self.foundWayToLog causes the decay to be ignored.
- What happens when world.cmpxchgBlock returns null versus a non-null value in this context?
- How is the random drop chance evaluated for each entry in self.blockDrops?
- Explain how the spawn position is computed from leaf.mode().model bounds and main.random.nextFloat.
- What upward bias is applied to the direction vector before dropping items?
- Which global seed variable is used by main.random.nextFloat and why is it passed as &main.seed?
- How does the function handle the case where server.world is null or missing?
- What error message is logged if neither decayable nor branch rotation matches?

*Source: unknown | chunk_id: codebase_src_callbacks_block_server_decay.zig_chunk_1*
