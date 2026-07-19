# [src/assets.zig] - PR #2676 review diff

**Type:** review
**Keywords:** assets.zig, Palette, loadedAssets, rawModelData, std.StringHashMap, main.models.QuadInfo, const, architectural review, suggestion
**Symbols:** Palette, loadedAssets, rawModelData, std.StringHashMap, main.models.QuadInfo
**Concepts:** thread safety, global state management

## Summary
Added a new variable `rawModelData` to store model data in a string hash map. The reviewer suggests making it constant for better safety.

## Explanation
The change introduces a new global variable `rawModelData`, which is intended to hold model data using a string hash map of type `std.StringHashMap([]main.models.QuadInfo)`. The reviewer points out that the variable should be declared as `const` to enhance thread safety and prevent accidental modification, which could lead to bugs or inconsistent states in the application. Declaring `rawModelData` as `const` improves architectural design by ensuring that the model data cannot be altered unintentionally, thus reducing potential sources of errors.

## Related Questions
- What is the purpose of the `rawModelData` variable in the `assets.zig` file?
- Why does the reviewer suggest making `rawModelData` a constant?
- How might modifying `rawModelData` lead to bugs in the application?
- What are the implications of using a string hash map for storing model data?
- Can you explain the concept of thread safety in this context?
- How does declaring `rawModelData` as const improve architectural design?

*Source: unknown | chunk_id: github_pr_2676_comment_3036573059*
