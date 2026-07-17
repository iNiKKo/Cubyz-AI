# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** register, zonElement, selectionRule, SelectionCapability, loadSelectionCapabilitiesFromZon, main.stackAllocator, main.worldArena.allocator, duplication, memory optimization, data loading
**Symbols:** register, _light, _absorption, _degradable, _selectionRule, SelectionRule, zon, ZonElement, main.stackAllocator, capabilitiesZon, SelectionCapability, loadSelectionCapabilitiesFromZon, main.worldArena.allocator
**Concepts:** memory management, allocator optimization, data loading, array handling

## Summary
The change introduces a new field `_selectionCapabilities` to store block selection capabilities, loaded from a ZonElement. The reviewer suggests passing `main.worldArena` directly as the allocator instead of duplicating the array.

## Explanation
The modification adds support for more complex selection rules by introducing `_selectionCapabilities`, which is populated by loading data from a ZonElement. The reviewer points out that duplicating the capabilities array with `main.stackAllocator` and then transferring ownership to `main.worldArena` could be optimized by directly using `main.worldArena` as the allocator. This change aims to improve memory management and potentially reduce overhead.

## Related Questions
- Why is the `selectionCapabilities` array being duplicated?
- What are the potential benefits of using `main.worldArena` directly as the allocator?
- How does this change affect memory usage in Cubyz?
- Is there a risk of memory leaks with the current implementation?
- Can you explain the purpose of the `zon.getChildOrNull` method?
- How does the new `_selectionCapabilities` field enhance block selection rules?
- What is the impact of changing the allocator on performance?
- Are there any potential regressions introduced by this change?
- How does this modification align with Cubyz's overall architecture goals?
- Can you provide examples of how `SelectionCapability` might be used in different scenarios?

*Source: unknown | chunk_id: github_pr_2987_comment_3177694224*
