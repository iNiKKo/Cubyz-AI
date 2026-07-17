# [src/assets.zig] - PR #2676 review diff

**Type:** review
**Keywords:** assets.zig, std.StringHashMap, main.models.QuadInfo, const, global variable, thread safety
**Symbols:** Palette, loadedAssets, rawModelData
**Concepts:** thread safety, immutability

## Summary
Added a new variable `rawModelData` to store model data, with a suggestion to make it constant.

## Explanation
The change introduces a new global variable `rawModelData` of type `std.StringHashMap([]main.models.QuadInfo)` in the `assets.zig` file. The reviewer suggests making this variable constant (`const`) to enhance immutability and potentially improve thread safety, as well as to prevent accidental modification of the data.

## Related Questions
- What is the purpose of the `rawModelData` variable in the `assets.zig` file?
- Why does the reviewer suggest making `rawModelData` constant?
- How might making `rawModelData` constant impact thread safety in the application?
- Is there any potential performance benefit from using a constant variable for model data?
- What are the implications of not making `rawModelData` constant?
- Could the introduction of `rawModelData` lead to memory leaks if not properly managed?

*Source: unknown | chunk_id: github_pr_2676_comment_3036573059*
