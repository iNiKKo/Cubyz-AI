# [issues/issue_2386.md] - Issue #2386 discussion

**Type:** review
**Keywords:** Callback, init, block, item, variadic, flexible, optional, modded, custom, callbacks, context, owner, ZonElement, BlockID
**Symbols:** Callback.init, ZonElement, BlockID
**Concepts:** Flexibility, Initialization Order, Modularity, Generic Types

## Summary
The discussion revolves around modifying the `Callback.init` function to include context about the block or item it belongs to, with a focus on flexibility and avoiding unnecessary complexity.

## Explanation
The discussion revolves around modifying the `Callback.init` function to include context about the block or item it belongs to, with a focus on flexibility and avoiding unnecessary complexity. The main points of discussion include whether to use variadic inits, ensuring that callbacks are initialized last, and considering the flexibility needed for both standard and modded owners. The maintainers suggest using a generic type like the block index or item index, while also considering future possibilities for optional parameters and custom callback creation functions for modded items.

The current implementation of `Callback.init` is as follows:
```zig
pub fn init(zon: ZonElement) ?*@This() {
```
The proposed change would be to modify this function signature to include an additional parameter representing the owner context, such as a block or item reference. The maintainers suggest changing it to:
```zig
pub fn init(zon: ZonElement, owner: *something) ?*@This() {
```
where `owner` is either an incomplete (not fully initialized) object of the block or item type.

The discussion also includes considerations for ensuring that callbacks are initialized last to avoid issues with uninitialized pointers. The maintainers confirm that callbacks are currently initialized last, which aligns with user comments.

Additionally, there is a suggestion to use generic types like `BlockID` or `ItemIndex`, and the possibility of making parameters optional in future implementations. Custom item types could have custom callback creation functions as well.

## Related Questions
- How can the `Callback.init` function be modified to include block or item context?
- What are the potential implications of initializing callbacks last?
- Can generic types like block index or item index be used effectively in this scenario?
- How should the implementation handle optional parameters for future use-cases?
- What are the considerations for supporting custom callback creation functions for modded items?

*Source: unknown | chunk_id: github_issue_2386_discussion*
