# [src/blocks.zig] - PR #1143 review diff

**Type:** review
**Keywords:** Block, entity touch, function pointer, dynamic behavior, architectural review
**Symbols:** Block, _allowOres, _checkEntityTouch, canBeChangedInto, onEntityTouch
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added new methods `checkEntityTouch` and `onEntityTouch` to the Block struct in blocks.zig.

## Explanation
The changes introduce two new functions within the Block struct: `checkEntityTouch` and `onEntityTouch`. The `checkEntityTouch` function checks if a block allows entities to touch it by returning the value from the `_checkEntityTouch` array based on the block type. The `onEntityTouch` method is intended to handle actions when an entity touches the block but currently does not perform any actions; all parameters are ignored and the method simply returns without executing any code, as indicated by the line `_ = self; _ = entity; _ = posX; _ = posY; _ = posZ; _ = isEntityInside;`, which assigns each parameter to an underscore, effectively ignoring them. The reviewer suggests using function pointers for future implementation, indicating a potential need for more dynamic behavior in how blocks interact with entities.

## Related Questions
- What is the purpose of the `checkEntityTouch` method in the Block struct?
- How does the `onEntityTouch` method currently handle entity interactions with blocks?
- Why did the reviewer suggest using function pointers for block-entity interactions?
- Is there any potential impact on performance or memory usage with these new methods?
- What architectural considerations were taken into account when adding these methods?
- How might these changes affect backwards compatibility with existing Cubyz code?

*Source: unknown | chunk_id: github_pr_1143_comment_1977731254*
