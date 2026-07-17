# [src/blocks.zig] - Chunk 3107328085

**Type:** review
**Keywords:** leak, worldArena, allowedToolTags, ZonElement, Tag.loadTagsFromZon, stackAllocator, dupe, BaseItemIndex, optional, memory safety
**Symbols:** loadBlockDrop, items.BaseItemIndex.fromId, blockDrops, worldArena, dupe, Stack, allowedToolTags, getChildOrNull, Tag.loadTagsFromZon, stackAllocator
**Concepts:** memory leak prevention, arena allocation, optional fields, data parsing from ZON, block drop structure, allocator lifecycle management

## Summary
The code was updated to load allowed tool tags from a ZON element and store them in a new variable `allowedToolTags`, addressing a reviewer's concern about potential memory leaks by ensuring proper use of the world arena.

## Explanation
The original implementation directly duplicated items using `main.worldArena.dupe(main.items.ItemStack, resultItems.items)`. The reviewer flagged this as a leak because the duplication was not correctly tied to the arena lifecycle or possibly allocated outside expected bounds. To resolve this, the code now introduces an optional slice of tags (`allowedToolTags`) initialized to null. It checks if the block drop child named `allowedToolTags` exists via `getChildOrNull`. If present, it parses the ZON element using `Tag.loadTagsFromZon`, passing `main.stackAllocator` as the allocator source. This change ensures that any tag data is allocated from a known arena (the stack allocator) and will be freed appropriately when the block drop structure is cleaned up, preventing leaks. Architecturally, this adds a new optional field to the block drop representation, requiring downstream code to handle null cases or allocate storage for tags if needed.

## Related Questions
- What is the purpose of `allowedToolTags` in the block drop structure?
- How does `Tag.loadTagsFromZon` allocate memory for tags?
- Why was the original use of `worldArena.dupe` considered a leak?
- Does `stackAllocator` replace `worldArena` for tag storage, or is it an additional allocator?
- What happens if `getChildOrNull` returns null for `allowedToolTags`?
- Are there any downstream modifications required to handle the new optional tags field?
- Is `main.stackAllocator` guaranteed to be freed before program exit?
- How does this change affect serialization or deserialization of block drops?
- What constraints exist on the number of allowed tool tags per drop?
- Could parsing fail mid-stream and leave partial tag data allocated?

*Source: unknown | chunk_id: github_pr_2886_comment_3107328085*
