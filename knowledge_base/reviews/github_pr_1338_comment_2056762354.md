# [src/chunk.zig] - Chunk 2056762354

**Type:** review
**Keywords:** Chunk, blockPosToTickableBlockMap, Hashmap, premature optimization, thread safety, random indexing, issue #77, tickable blocks
**Symbols:** Chunk, blockPosToEntityDataMap, blockPosToEntityDataMapMutex, blockPosToTickableBlockMap, blockPosToTickableBlockMutex
**Concepts:** data structure selection, premature optimization, thread safety, random indexing, hashmap limitations, tickable blocks management

## Summary
The change introduces two new fields to the Chunk struct: blockPosToTickableBlockMap and blockPosToTickableBlockMutex, alongside existing blockPosToEntityDataMap structures.

## Explanation
The reviewer's verbatim critique: "A Hashmap seems like a poor data structure for this, since you
cannot randomly index into it. Also since #77 I have changed my mind about keeping a list of
tickable blocks. Either way I think this would probably be a premature optimization for random
ticks anyways." The core objection is structural, not a complexity/big-O argument: a hashmap
doesn't support random/positional indexing the way a list does, which is what this random-tick
use case actually needs. Referencing issue #77, the reviewer notes that maintaining a list of
tickable blocks was already being reconsidered independently, and either way judges adding this
hashmap now to be likely premature optimization for random ticks.

## Related Questions
- What is the purpose of blockPosToTickableBlockMap in Chunk?
- Why does the reviewer consider Hashmap a poor choice for random indexing?
- How does issue #77 relate to tickable blocks management?
- Is there an alternative data structure suggested instead of Hashmap?
- What implications does adding blockPosToTickableBlockMutex have on thread safety?
- Does the reviewer suggest removing existing blockPosToEntityDataMap structures?
- How might premature optimization affect performance in random ticks?
- Are there any constraints mentioned regarding memory usage for these maps?
- Could blockPosToTickableBlockMap be used for deterministic tick scheduling?
- What is the expected lifecycle of entries in blockPosToTickableBlockMap?

*Source: unknown | chunk_id: github_pr_1338_comment_2056762354*
