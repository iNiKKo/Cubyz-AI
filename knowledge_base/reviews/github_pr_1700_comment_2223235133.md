# [src/gui/windows/creative_inventory.zig] - PR #1700 review diff

**Type:** review
**Keywords:** filtering, tags, simplification, readability, maintainability, conditional, logic, inverted, complexity, performance
**Symbols:** initContent, VerticalList, items, main.items.iterator, searchString, item.id, std.mem.containsAtLeast, Item, baseItem, hasTag, block, blocks.Block
**Concepts:** Code readability, Maintainability, Conditional logic

## Summary
The review suggests simplifying the item filtering logic in the creative inventory by using a straightforward conditional check instead of a complex inverted logic structure.

## Explanation
**Explanation**

The reviewer points out that the current implementation uses an intricate and potentially error-prone inverted logic construct to filter items based on tags. The suggestion is to replace this with a simpler `if(item.hasTag(bestTag) or (item.block() orelse break).hasTag(bestTag))` condition, which would improve code readability and maintainability without altering functionality.

The original inverted logic construct in the code is as follows:
```zig
if(searchString.len > 1 and searchString[0] == '.') blk: {
    const bestTag = main.Tag.findSimilar(searchString[1..]) orelse break :blk;
    while(itemIterator.next()) |item| {
        if(!item.hasTag(bestTag)) {
            if(item.block()) |blockIndex| {
                if(!(main.blocks.Block{.typ = blockIndex, .data = 0}).hasTag(bestTag)) continue;
            } else {
                continue;
            }
        }
        items.append(Item{.baseItem = item.*});
    }
}
```
The suggested simplification is to replace the complex logic with a simpler conditional check:
```zig
if(item.hasTag(bestTag) or (item.block() orelse break).hasTag(bestTag))
```
This change aims to improve code readability and maintainability without altering the functionality of the creative inventory.

The specific `hasTag` method calls in the suggested replacement are crucial for understanding how the filtering logic should be simplified. The original code checks if an item has a tag or if its associated block (if any) has the tag, and only then appends the item to the list. The suggested simplification directly incorporates this logic into a single conditional statement, making it easier to read and maintain.

## Related Questions
- What is the purpose of the `initContent` function in the creative inventory?
- How does the current item filtering logic work in the creative inventory?
- Why was the inverted logic construct used in the original implementation?
- What are the benefits of simplifying the conditional check as suggested by the reviewer?
- Can you explain how the `hasTag` method works in the context of items and blocks?
- How might this change affect the performance of the creative inventory?

*Source: unknown | chunk_id: github_pr_1700_comment_2223235133*
