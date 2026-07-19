# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** SortedBlockProperties, function template, property management, efficient storage, dynamic handling, struct-oriented design, module scope, block properties, Zig language, code refactoring
**Symbols:** SortedBlockProperties, _transparent, _collide, _id, _blockHealth, _blockResistance, _replacable, _selectable, _blockDrops, _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _blockTags, _light, _absorption, _gui, _mode, _modeData, _lodReplacement, _opaqueVariant, _friction, _bounciness, _density, _terminalVelocity, _mobility, _allowOres, _tickEvent, _touchFunction, _blockEntity
**Concepts:** Efficient data storage, Dynamic property handling, Struct-oriented design, Module scope management

## Summary
Refactored block properties management by introducing a `SortedBlockProperties` function template for efficient property storage and retrieval, encapsulating properties within a struct to align with Zig's module scope and struct-oriented design principles.

## Explanation
The refactoring aims to improve the efficiency and maintainability of block property management in Cubyz. By using a function template `SortedBlockProperties`, the code now dynamically handles different data types for block properties, optimizing storage and retrieval operations. The introduction of this template allows for more flexible and scalable property handling, reducing redundancy and improving performance.

The `SortedBlockProperties` function template is designed to handle both boolean and non-boolean data types efficiently. For boolean properties, it uses a binary search algorithm to quickly determine if a block has a specific property by checking the presence of its ID in a sorted array. This approach minimizes memory usage and speeds up retrieval times.

For non-boolean properties, the template stores both the block IDs and their corresponding values in separate arrays, maintaining a sorted order. The binary search algorithm is used to find the index of a block ID, allowing for efficient access to its property value. This design ensures that adding or removing properties is done efficiently while keeping the data organized.

Memory management within the `SortedBlockProperties` struct is handled by dynamically resizing arrays as needed. When adding a new property, the struct checks if there is enough space in the array. If not, it panics and suggests increasing the size of the array to accommodate more entries. This ensures that memory usage is optimized without causing performance issues.

The `resetSortedProperties` function plays a crucial role in this refactoring by clearing all properties from the struct. It iterates over each property type defined in the `BlockProps` struct and calls the `clear` method on it, resetting the allocated size to zero. This function is useful for cleaning up resources when they are no longer needed, ensuring that memory is properly managed.

The reviewer emphasizes that all methods should be moved into the struct to align with Zig's module scope and struct-oriented design principles. By doing so, the code becomes more cohesive and modular, promoting better organization and maintainability.

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
