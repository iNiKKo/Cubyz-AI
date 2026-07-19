# [src/gui/windows/creative_inventory.zig] - PR #1700 review diff

**Type:** review
**Keywords:** VerticalList, initContent, items, searchString, Item, baseItem, hasTag, block, findSimilar, undefined
**Symbols:** VerticalList, initContent, items, main.items.iterator(), searchString, Item, baseItem, item.id(), std.mem.containsAtLeast, bestTags, main.Tag.findSimilar, item.hasTag, item.block
**Concepts:** tag-based search, iterator usage, data field handling

## Summary
The code now checks for tags in items and blocks, optimizing search functionality.

## Explanation
The change introduces a new condition to handle searches based on tags. It iterates over items and checks if they have specific tags or if their associated blocks have those tags. The reviewer suggests explicitly setting the 'data' field to undefined for clarity, although this is noted as a minor concern.

The code now includes a check for the 'searchString' length and whether it starts with a '.' character. If so, it finds similar tags using `main.Tag.findSimilar` and iterates over items to check if they have any of those tags or if their associated blocks have those tags.

## Related Questions
- What is the purpose of the 'bestTags' variable in this code?
- How does the new condition handle searches based on tags?
- Why is the 'data' field set to undefined in the reviewer's suggestion?
- What impact might this change have on performance?
- Is there a risk of memory leaks introduced by this modification?
- How does this change affect backward compatibility with previous versions?

*Source: unknown | chunk_id: github_pr_1700_comment_2223633968*
