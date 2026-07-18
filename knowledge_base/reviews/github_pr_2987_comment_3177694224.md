# [src/blocks.zig] - PR #2987 review diff

**Type:** review
**Keywords:** selection capabilities, ZonElement, duplication, allocator, world arena, memory efficiency
**Symbols:** register, zon, SelectionRule, SelectionCapability, loadSelectionCapabilitiesFromZon, main.stackAllocator, main.worldArena
**Concepts:** memory management, allocation strategy

## Summary
The change introduces a new field `_selectionCapabilities` to store block selection capabilities, loaded from a ZonElement. The reviewer suggests passing `main.worldArena` directly for allocation instead of duplicating.

## Explanation
The code modification adds support for storing and managing block selection capabilities by loading them from a ZonElement. The reviewer points out that the current implementation duplicates the capabilities array using `main.stackAllocator`, which is unnecessary. By passing `main.worldArena` directly, the allocation can be more efficient and aligned with the intended memory management strategy of the application.

## Related Questions
- Why is it important to use `main.worldArena` for allocation instead of duplicating the array?
- What are the potential performance implications of duplicating the capabilities array?
- How does passing `main.worldArena` for allocation align with the overall memory management strategy in Cubyz?
- Can you explain the purpose of the `_selectionCapabilities` field and how it is used?
- What changes would be required to implement the reviewer's suggestion?
- How might this modification affect backward compatibility with existing block definitions?

*Source: unknown | chunk_id: github_pr_2987_comment_3177694224*
