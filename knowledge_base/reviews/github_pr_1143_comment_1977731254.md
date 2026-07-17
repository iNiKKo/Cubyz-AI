# [src/blocks.zig] - PR #1143 review diff

**Type:** review
**Keywords:** Block, checkEntityTouch, onEntityTouch, entity interaction, function pointer, dynamic behavior, block types
**Symbols:** Block, _allowOres, _checkEntityTouch, canBeChangedInto, main.items.ItemStack, main.rotation.RotationMode.CanBeChangedInto, onEntityTouch, main.server.Entity
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added new methods `checkEntityTouch` and `onEntityTouch` to the Block struct in blocks.zig.

## Explanation
The changes introduce two new methods to the Block struct: `checkEntityTouch` and `onEntityTouch`. The `checkEntityTouch` method checks if a block allows entities to touch it, while `onEntityTouch` is intended to handle interactions when an entity touches the block. The reviewer suggests using function pointers for further implementation, indicating a potential need for dynamic behavior based on block types.

## Related Questions
- What is the purpose of the `checkEntityTouch` method in the Block struct?
- How does the `onEntityTouch` method currently handle entity interactions?
- Why are function pointers being considered for future implementation?
- What potential issues could arise from adding these new methods to the Block struct?
- How might these changes affect backwards compatibility with existing block types?
- Is there a risk of memory leaks introduced by the new methods?

*Source: unknown | chunk_id: github_pr_1143_comment_1977731254*
