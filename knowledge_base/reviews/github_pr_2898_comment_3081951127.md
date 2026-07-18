# [src/items.zig] - PR #2898 review diff

**Type:** review
**Keywords:** Item, onLeftClick, ProceduralItem, BaseItem, architectural pattern, delegation, localization, changes, maintenance, bug prevention
**Symbols:** Item, onLeftClick, ProceduralItem, BaseItem
**Concepts:** architectural pattern, delegation, localization of changes

## Summary
A new function `onLeftClick` is added to the `Item` union, which calls into identical functions of `ProceduralItem` and `BaseItem`. The reviewer suggests following an architectural pattern where `Item` functions only delegate to corresponding functions in these structs to ensure changes are localized.

## Explanation
The addition of the `onLeftClick` function introduces a new method for handling left-click events on items. The reviewer advocates for an architectural approach where this method is implemented in both `ProceduralItem` and `BaseItem`, with `Item` delegating to these implementations. This pattern ensures that any divergence in behavior between different item types is confined to their respective structs, making the codebase easier to maintain and reducing the risk of introducing bugs through changes in one part affecting others.

## Related Questions
- What is the purpose of the `onLeftClick` function in the `Item` union?
- Why does the reviewer suggest delegating to `ProceduralItem` and `BaseItem`?
- How does this architectural pattern help with code maintenance?
- Can you provide an example of how the `onLeftClick` function might be implemented in `ProceduralItem` and `BaseItem`?
- What are the potential benefits of following this architectural pattern?
- How might changes to one item type affect others if this pattern is not followed?

*Source: unknown | chunk_id: github_pr_2898_comment_3081951127*
