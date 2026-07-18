# [src/blocks.zig] - PR #1143 review diff

**Type:** review
**Keywords:** Block, entity touch, checkEntityTouch, onEntityTouch, interaction handling, architectural review
**Symbols:** Block, _allowOres, _checkEntityTouch, canBeChangedInto, main.items.ItemStack, main.rotation.RotationMode.CanBeChangedInto, onEntityTouch, main.server.Entity
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added new methods `checkEntityTouch` and `onEntityTouch` to the Block struct in blocks.zig.

## Explanation
The reviewer added two new methods, `checkEntityTouch` and `onEntityTouch`, to the `Block` struct. The `checkEntityTouch` method checks if a block allows entities to touch it based on its type. The `onEntityTouch` method is intended to handle interactions when an entity touches the block, though the current implementation does nothing with the passed parameters. The reviewer expressed willingness to further develop these methods as needed.

## Related Questions
- What is the purpose of the `checkEntityTouch` method?
- How does the current implementation of `onEntityTouch` handle entity interactions?
- Is there any specific logic planned for the `onEntityTouch` method in future updates?
- How does the addition of these methods affect backwards compatibility with existing code?
- What are the potential implications of using function pointers for these methods instead of inline functions?
- Are there any thread safety concerns introduced by these new methods?

*Source: unknown | chunk_id: github_pr_1143_comment_1977728718*
