# [src/blocks.zig] - PR #2886 review diff

**Type:** review
**Keywords:** allowedToolTags, forbiddenToolTags, chance, worldArena, Tag.loadTagsFromZon, memory leak prevention, error logging
**Symbols:** loadBlockDrop, blockId, zon, items.BaseItemIndex.fromId, resultItems.append, main.worldArena.dupe, allowedToolTags, tagZon, Tag.loadTagsFromZon, main.stackAllocator, blockDrops[i], blockDrop.getChildOrNull, blockDrop.get, f32
**Concepts:** memory management, error handling, architectural design

## Summary
The code now loads allowed tool tags for block drops and checks if they are empty, logging an error if so. It also initializes the `chance` field and uses the `worldArena` for memory allocation.

## Explanation
This change introduces functionality to handle allowed tool tags for block drops, ensuring that if the array is empty, an error is logged. The specific error message logged is 'Field '.allowedToolTags' is an empty array. No tool can drop this blockDrop'. The `chance` field is initialized with a default value of 1. The use of `worldArena` for memory allocation is crucial for preventing memory leaks, as it ensures that allocated memory is properly managed and freed when no longer needed. Additionally, the code also loads forbidden tool tags using `Tag.loadTagsFromZon`. This ensures that both allowed and forbidden tool tags are correctly handled in the block drop logic.

## Related Questions
- What is the purpose of the `allowedToolTags` variable?
- How does the code handle empty arrays for allowed tool tags?
- Why is the `worldArena` used for memory allocation in this context?
- What is the default value for the `chance` field?
- How are errors logged if the `.allowedToolTags` array is empty?
- What is the role of `Tag.loadTagsFromZon` in this code snippet?

*Source: unknown | chunk_id: github_pr_2886_comment_3107328161*
