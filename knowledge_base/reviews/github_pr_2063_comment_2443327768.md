# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** SortedBlockProperties, function template, property management, efficient storage, dynamic handling, struct-oriented design, module scope, block properties, Zig language, code refactoring
**Symbols:** SortedBlockProperties, _transparent, _collide, _id, _blockHealth, _blockResistance, _replacable, _selectable, _blockDrops, _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _blockTags, _light, _absorption, _gui, _mode, _modeData, _lodReplacement, _opaqueVariant, _friction, _bounciness, _density, _terminalVelocity, _mobility, _allowOres, _tickEvent, _touchFunction, _blockEntity
**Concepts:** Efficient data storage, Dynamic property handling, Struct-oriented design, Module scope management

## Summary
Refactored block properties management by introducing a `SortedBlockProperties` function template for efficient property storage and retrieval, encapsulating properties within a struct to align with Zig's module scope and struct-oriented design principles.

## Explanation
The refactoring aims to improve the efficiency and maintainability of block property management in Cubyz. By using a function template `SortedBlockProperties`, the code now dynamically handles different data types for block properties, optimizing storage and retrieval operations. The introduction of this template allows for more flexible and scalable property handling, reducing redundancy and improving performance. Additionally, the reviewer emphasizes that all methods should be moved into the struct to align with Zig's module scope and struct-oriented design principles, promoting a more cohesive and modular code structure.

## Related Questions
- What is the purpose of the `SortedBlockProperties` function template?
- How does the new struct-based approach improve code maintainability?
- What are the benefits of using Zig's module scope in this refactoring?
- How does the binary search algorithm contribute to efficient property retrieval?
- What changes were made to handle different data types for block properties?
- How is memory management handled within the `SortedBlockProperties` struct?
- What is the role of the `resetSortedProperties` function in this refactoring?
- How does this refactoring align with Zig's design principles?
- What potential performance improvements can be expected from this change?
- How does the new approach impact backward compatibility with existing code?

*Source: unknown | chunk_id: github_pr_2063_comment_2443327768*
