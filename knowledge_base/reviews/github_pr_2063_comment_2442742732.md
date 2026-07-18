# [src/blocks.zig] - PR #2063 review diff

**Type:** review
**Keywords:** SortedBlockProperties, memory usage, dynamic resizing, magic value, resizeable, block properties, maxBlockCount, array storage, efficient memory, scalability
**Symbols:** SortedBlockProperties, _transparent, _collide, _id, _blockHealth, _blockResistance, _replacable, _selectable, _blockDrops, _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _blockTags, _light, _absorption, _gui, _mode, _modeData, _lodReplacement, _opaqueVariant, _friction, _bounciness, _density, _terminalVelocity, _mobility, _allowOres, _tickEvent, _touchFunction, _blockEntity, BlockProps
**Concepts:** Memory Management, Dynamic Resizing, Efficiency Optimization

## Summary
Refactored block property management by introducing a `SortedBlockProperties` function template for efficient memory usage and dynamic resizing.

## Explanation
The change introduces a new function template, `SortedBlockProperties`, which manages block properties using sorted arrays to save memory. This approach is particularly beneficial for rarely used properties, reducing the need for large arrays with `maxBlockCount` entries (65,536). The reviewer highlights that while the current magic value of 100-300 entries is sufficient for most cases, it should be resizeable to accommodate potential add-ons without falling back to array storage. This refactoring aims to improve memory efficiency and scalability.

## Related Questions
- How does the `SortedBlockProperties` function template handle dynamic resizing?
- What is the impact of the magic value on the performance and scalability of block properties?
- Can you explain how the binary search is used in the `getBlockPropertyValue` method?
- What are the benefits of using sorted arrays for rarely used block properties?
- How does the `resetSortedProperties` function ensure that all sorted properties are cleared?
- What changes would be necessary to make the magic value resizeable?

*Source: unknown | chunk_id: github_pr_2063_comment_2442742732*
