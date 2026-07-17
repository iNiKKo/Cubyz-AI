# [src/blocks.zig] - Chunk 2442742732

**Type:** review
**Keywords:** SortedBlockProperties, idxLookup, binarySearch, lowerBound, copyBackwards, maxSortedBlockProperties, isSortedProp, resetSortedProperties, sparse storage, O(log N), compile-time check, backwards compatible
**Symbols:** Ore, maxBlockCount, SortedBlockProperties, Cmp, BlockProps, maxSortedBlockProperties, getBlockPropertyValue, addBlockProperty, clear, getBlockSortedIdx, isSortedProp, resetSortedProperties
**Concepts:** sparse array storage, sorted index lookup, binary search, lower bound insertion, memory efficiency, compile-time trait checking, generic type specialization, backwards compatibility of property access

## Summary
Replaced raw fixed-size boolean arrays with a generic SortedBlockProperties struct using sorted index lookups for sparse block properties.

## Explanation
The original code used dense [maxBlockCount] arrays for every property, which is wasteful when most entries are false/zero. The reviewer flagged the magic constant maxSortedBlockProperties = 100 as unacceptable because add-ons could exceed it without any growth mechanism. The fix introduces a generic SortedBlockProperties type that stores only active block IDs in an idxLookup array and keeps values in parallel data arrays. For bool properties, getBlockPropertyValue performs a binary search on the sorted ID list; for other types, getBlockSortedIdx returns the index or null, then getBlockPropertyValue reads from data[idx]. addBlockProperty inserts into both idxLookup and data using lowerBound to maintain order, copying backwards to make room. The struct also exposes clear() to reset allocatedSize. A helper isSortedProp checks for the required methods at compile time, and resetSortedProperties iterates over BlockProps fields, clearing any that are sorted. This design trades O(N) linear scans for O(log N) lookups while keeping memory usage proportional to the number of set properties rather than maxBlockCount.

## Related Questions
- What is the maximum number of entries allowed in a sorted block property array?
- How does getBlockPropertyValue handle a missing block ID when using SortedBlockProperties for bools?
- Which function is responsible for inserting a new block ID while maintaining sorted order?
- Does addBlockProperty panic if the allocated size would exceed maxSortedBlockProperties?
- What happens to data values when a block property is cleared via resetSortedProperties?
- How does the code differentiate between bool and non-bool properties in SortedBlockProperties?
- Is getBlockSortedIdx used for any property type other than non-bools?
- Where are the idxLookup and data arrays initialized within BlockProps?
- What error is returned by getBlockPropertyValueByIdx when blockIdx is out of range?
- Does resetSortedProperties log anything before clearing sorted properties?

*Source: unknown | chunk_id: github_pr_2063_comment_2442742732*
