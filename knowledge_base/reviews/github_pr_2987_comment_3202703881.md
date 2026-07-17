# [src/blocks.zig] - Chunk 3202703881

**Type:** review
**Keywords:** SelectionCapabilities, alwaysSelectable, loadFromZon, allowsSelectionByItem, SelectionRule, enum, struct, refactor, redundancy, namespace
**Symbols:** SelectionCapabilities, alwaysSelectable, loadFromZon, allowsSelectionByItem, SelectionCapability
**Concepts:** refactoring, namespace hygiene, struct composition, API surface reduction, type locality

## Summary
Refactored `SelectionRule` enum into a new `SelectionCapabilities` struct to consolidate selection logic and reduce redundancy.

## Explanation
The original code used an enum `SelectionRule` with values like `always`, `toolEffective`, and `never`. Reviewers noted that this enum is only consumed inside the newly introduced `SelectionCapabilities` struct, making its global scope unnecessary. By moving the definition into `SelectionCapabilities`, we eliminate redundant information in the struct name (no longer needing to repeat 'Rule' or similar qualifiers) and simplify the public API surface. The new struct provides a default `alwaysSelectable` variant where capabilities are null, and includes helper functions: `loadFromZon` parses capability zones from a ZON element into an unmanaged list, and `allowsSelectionByItem` implements the selection logic—checking base items (including the special 'cubyz:selection_wand'), handling fluid tags, and delegating to per-capability checks. This refactor improves modularity, reduces namespace pollution, and aligns with Zig best practices for grouping related types.

## Related Questions
- What is the purpose of the `alwaysSelectable` variant in `SelectionCapabilities`?
- How does `loadFromZon` handle invalid `SelectionCapability` entries from a ZON element?
- In what order are checks performed inside `allowsSelectionByItem` before delegating to capabilities?
- Why was the original `SelectionRule` enum moved into `SelectionCapabilities` instead of remaining global?
- Does `loadFromZon` allocate memory for the capability list, and how does it ensure capacity?
- What happens if a block has the `.fluid` tag when evaluating selection with an item that is not fluid-placeable?
- How does the code treat the special base item ID 'cubyz:selection_wand' in `allowsSelectionByItem`?
- Is there any scenario where `alwaysSelectable` would be preferred over a populated capabilities list?
- What are the implications of using an unmanaged list for capabilities on memory management lifecycle?
- Could `loadFromZon` be made to return a slice instead of an owned list, and what trade-offs would that entail?

*Source: unknown | chunk_id: github_pr_2987_comment_3202703881*
