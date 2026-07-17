# [src/blocks.zig] - PR #1143 review diff

**Type:** review
**Keywords:** Block, checkEntityTouch, onEntityTouch, entity interaction, virtual function pointer, enum, boolean flag, main.items.ItemStack, main.rotation.RotationMode.CanBeChangedInto, main.server.Entity
**Symbols:** Block, _allowOres, _checkEntityTouch, canBeChangedInto, onEntityTouch, main.items.ItemStack, main.rotation.RotationMode.CanBeChangedInto, main.server.Entity
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added `checkEntityTouch` and `onEntityTouch` methods to the Block struct.

## Explanation
The change introduces two new methods to the Block struct: `checkEntityTouch`, which checks if a block allows entity interaction, and `onEntityTouch`, which handles the event when an entity touches the block. The reviewer suggests considering future plans for implementing more complex behavior, such as using virtual function pointers or enums instead of simple boolean flags.

## Related Questions
- What is the purpose of the `checkEntityTouch` method in the Block struct?
- How does the `onEntityTouch` method currently handle entity interactions?
- Why was it decided to add these methods to the Block struct?
- What are the potential implications of using a boolean flag for `_checkEntityTouch`?
- How might virtual function pointers or enums be implemented in the future?
- What changes would need to be made to support more complex entity interaction behaviors?

*Source: unknown | chunk_id: github_pr_1143_comment_1977647136*
