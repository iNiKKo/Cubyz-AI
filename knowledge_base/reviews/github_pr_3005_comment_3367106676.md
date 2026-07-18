# [src/proceduralItem/modifiers/restrictions/on_top_of.zig] - PR #3005 review diff

**Type:** review
**Keywords:** OnTopOf, satisfied, loadFromZon, printTooltip, NeverFailingAllocator, ModifierRestriction, ProceduralItem, ZonElement, main.Tag, ListManaged, architectural changes, backwards compatibility, type safety
**Symbols:** OnTopOf, satisfied, loadFromZon, printTooltip, NeverFailingAllocator, ModifierRestriction, ProceduralItem, ZonElement, main.Tag, main.List, main.ListManaged
**Concepts:** architectural changes, backwards compatibility, type safety

## Summary
Added `OnTopOf` struct with methods to check if a procedural item is on top of a specified tag, load from ZonElement, and print tooltip. Updated `printTooltip` method to use `ListManaged` instead of `List` due to recent changes.

## Explanation
The change introduces a new struct `OnTopOf` that encapsulates the logic for checking if a procedural item is positioned on top of another item with a specific tag. The `satisfied` method checks this condition by calling `checkForTagAt` on the procedural item. The `loadFromZon` method initializes an instance of `OnTopOf` from a ZonElement, handling missing fields gracefully by logging an error and using a default value. The reviewer notes that the `printTooltip` method needs to be updated to use `ListManaged` instead of `List`, as there were recent changes in the main codebase (#3129 and #3152) that deprecated the use of `List`. This update ensures compatibility with the latest architectural decisions.

## Related Questions
- What is the purpose of the `OnTopOf` struct?
- How does the `satisfied` method determine if a procedural item is on top of another item with a specific tag?
- What changes were made to the `printTooltip` method, and why?
- Why was it necessary to update the `printTooltip` method to use `ListManaged` instead of `List`?
- What are the implications of using `NeverFailingAllocator` in this context?
- How does the `loadFromZon` method handle missing fields in a ZonElement?
- What architectural decisions led to the deprecation of `List` in favor of `ListManaged`?
- Can you explain the role of `main.Tag` in the `OnTopOf` struct?
- How is error handling implemented when loading an `OnTopOf` from a ZonElement?
- What are the potential performance implications of using `NeverFailingAllocator`?
- How does the `checkForTagAt` method contribute to the functionality of the `OnTopOf` struct?
- What steps should be taken to ensure that all instances of `List` are updated to `ListManaged` in the codebase?

*Source: unknown | chunk_id: github_pr_3005_comment_3367106676*
