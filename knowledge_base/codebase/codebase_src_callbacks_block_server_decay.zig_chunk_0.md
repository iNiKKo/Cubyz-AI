# [medium/codebase_src_callbacks_block_server_decay.zig] - Chunk 0

**Type:** implementation
**Keywords:** cubyz:decayable, cubyz:branch, placedByHuman, viewThrough, block replacement, randomized drops, prevention list, BFS search
**Symbols:** decayReplacement, prevention, blockDrops, init, getIndexInCheckArray, preventsDecay, foundWayToLog, run
**Concepts:** server callbacks, decay prevention, breadth-first search, block replacement, randomized drops, ZON parsing, rotation checks

## Summary
Implements the server-side decay callback for blocks, parsing replacement data from ZON files and performing a breadth-first search to detect nearby logs that prevent decay.

## Explanation
The chunk defines a public struct (implied by init/run signatures) with fields decayReplacement, prevention, blockDrops. The init function parses the provided ZonElement: it extracts a replacement block name via zon.get('replacement'), defaulting to air; loads custom drops from zon.getChildOrNull('drops') using blocks.loadBlockDrop; and builds a prevention list from zon.getChildOrNull('prevention') by iterating an array of Tag names, validating each with main.Tag.find. The run function first checks the incoming block's rotation: if cubyz:decayable it returns ignored unless data==0; if cubyz:branch it calls branch.BranchData.init to check placedByHuman and returns ignored if true; otherwise logs an error. If a world exists, it retrieves the leaf at the computed coordinates (wx,wy,wz) and calls foundWayToLog. foundWayToLog performs a BFS within a 5-block radius using a circular buffer queue and a checked boolean array indexed via getIndexInCheckArray. It marks blocks as checked, pops positions, fetches the block from world.getBlock, then evaluates prevention: if self.preventsDecay(log) returns true it stops searching; for branches it checks branch rotation and viewThrough; for non-branches it compares typ. When a log is found that does not prevent decay, run proceeds to replace the leaf with self.decayReplacement via world.cmpxchgBlock (ignoring on success). If replacement fails or no log exists, drops are emitted: each drop.chance is evaluated against main.random.nextFloat(&main.seed), and for qualifying drops items are spawned using main.server.world.?.drop with a randomized upward-biased direction computed from model bounds.

## Code Example
```zig
fn preventsDecay(self: *@This(), log: Block) bool {
	for (self.prevention) |tag| {
		if (log.hasTag(tag)) return true;
	}
	return false;
}
```

## Related Questions
- What happens if a decayable block has data != 0?
- How does the chunk handle cubyz:branch rotation in run?
- Where is the replacement block name read from the ZON file?
- What default value is assigned to decayReplacement when no replacement is specified?
- How are drop items spawned after a successful decay?
- Which function performs the BFS search for nearby logs?
- What does preventsDecay return if none of the tags match?
- How is the checked array indexed in foundWayToLog?
- Does the chunk modify world state directly or via callbacks?
- What error message is logged when an unexpected rotation is encountered?

*Source: unknown | chunk_id: codebase_src_callbacks_block_server_decay.zig_chunk_0*
