# [src/items.zig] - PR #1640 review diff

**Type:** review
**Keywords:** items.zig, global variables, enum, nextIndex, refactor, type safety, code organization
**Symbols:** register, itemListSize, newItem, arena.allocator(), texturePath, replacementTexturePath, id, zon, reverseIndices.put
**Concepts:** type safety, code organization, enum usage

## Summary
The change updates the way item indices are stored by converting them to an enum type.

## Explanation
The reviewer suggests refactoring the code to encapsulate global variables within an enum and introduces a `nextIndex` function. This architectural change aims to improve code organization and potentially enhance type safety by leveraging Zig's enum capabilities. The current modification changes how item indices are stored, converting them from integers to enums using `@enumFromInt`. This could prevent certain types of errors related to invalid index values and make the code more robust.

The specific line of code that was changed is:
```zig
- reverseIndices.put(newItem.id, .{.index = itemListSize}) catch unreachable;
+ reverseIndices.put(newItem.id, @enumFromInt(itemListSize)) catch unreachable;
```
The `nextIndex` function is intended to provide a way to get the next available index in the enum, which can help prevent errors related to invalid index values. The reviewer suggests that this function could be implemented to return the next integer value converted to an enum type, ensuring that each item has a unique and valid index.

## Related Questions
- What is the purpose of converting item indices to enums?
- How does this change improve type safety in the code?
- What are the potential benefits of encapsulating global variables within an enum?
- Can you explain the role of the `nextIndex` function in this refactoring?
- How might this change affect existing functionality in Cubyz?
- What are the implications of using `@enumFromInt` for index storage?
- Could this refactor lead to performance improvements?
- How does this modification align with the overall architecture of Cubyz?
- Are there any potential regressions introduced by this change?
- What additional steps should be taken to ensure backwards compatibility?

*Source: unknown | chunk_id: github_pr_1640_comment_2167347867*
