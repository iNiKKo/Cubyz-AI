# [src/blocks.zig] - PR #1143 review diff

**Type:** review
**Keywords:** Block, checkEntityTouch, onEntityTouch, entity interaction, virtual function, enum, extensibility, future plans, architecture review, Cubyz development
**Symbols:** Block, _allowOres, checkEntityTouch, _checkEntityTouch, canBeChangedInto, onEntityTouch, main.items.ItemStack, main.rotation.RotationMode.CanBeChangedInto, main.server.Entity
**Concepts:** thread safety, backwards compatibility, memory leak, virtual functions, enums, extensibility

## Summary
Added `checkEntityTouch` and `onEntityTouch` methods to the Block struct. The reviewer suggests considering a more flexible approach using virtual functions or enums for future extensibility.

## Explanation
The change introduces two new methods, `checkEntityTouch` and `onEntityTouch`, to the Block struct in `blocks.zig`. The `checkEntityTouch` method returns whether a block allows entities to touch it based on its type. The `onEntityTouch` method is currently a placeholder that does nothing but accepts parameters for entity interaction. The reviewer raises concerns about future scalability, suggesting that instead of using a boolean array `_checkEntityTouch`, an optional function pointer or enum could be used to handle different behaviors more flexibly. This would allow for more complex interactions without modifying the core block structure.

## Related Questions
- What is the purpose of the `checkEntityTouch` method in the Block struct?
- How does the current implementation of `onEntityTouch` handle entity interactions?
- Why did the reviewer suggest using a function pointer or enum instead of a boolean array?
- Can you explain the potential benefits and drawbacks of implementing virtual functions for block interactions?
- What are the implications of changing `_checkEntityTouch` to an optional function pointer or enum?
- How might this change affect backwards compatibility with existing Cubyz code?

*Source: unknown | chunk_id: github_pr_1143_comment_1977647136*
