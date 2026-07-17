# [src/blocks.zig] - PR #2886 review diff

**Type:** review
**Keywords:** allowedToolTags, Tag.loadTagsFromZon, worldArena, stackAllocator, memory management, error handling, block drops, items.ItemStack
**Symbols:** loadBlockDrop, blockId, zon, items.BaseItemIndex.fromId, resultItems.append, main.worldArena.dupe, allowedToolTags, Tag.loadTagsFromZon, blockDrop.getChildOrNull, tagZon, tags.len, std.log.err, blockDrops[i], blockDrop.get, f32, forbiddenToolTags
**Concepts:** memory leak, thread safety, backwards compatibility

## Summary
The code now loads allowed tool tags from a ZonElement and assigns them to block drops. It also includes a check for empty allowed tool tags and logs an error if they are found.

## Explanation
The change introduces functionality to load 'allowedToolTags' from a ZonElement, which specifies the tools that can drop a particular block. This is done by checking if the 'allowedToolTags' field exists in the ZonElement and loading the tags accordingly. If the field is empty, an error message is logged. The reviewer notes that the use of 'main.stackAllocator' for loading tags should be replaced with 'main.worldArena' to prevent memory leaks, as the allocated memory would not be freed otherwise.

## Related Questions
- What is the purpose of the 'allowedToolTags' field in the ZonElement?
- How does the code handle an empty array for 'allowedToolTags'?
- Why is it recommended to use 'main.worldArena' instead of 'main.stackAllocator'?
- What potential issues could arise from not freeing memory allocated with 'main.stackAllocator'?
- How does the code ensure that only valid tools can drop a block?
- What changes would be necessary to make this feature backwards compatible?
- Can you explain the role of 'resultItems.append' in the context of loading block drops?
- How is the 'chance' field for block drops being handled in this update?
- What are the implications of using 'main.worldArena' for memory allocation in this context?
- How does the code handle the case where 'forbiddenToolTags' are specified?

*Source: unknown | chunk_id: github_pr_2886_comment_3107328161*
