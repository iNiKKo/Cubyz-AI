# [issues/issue_2386.md] - Issue #2386 discussion

**Type:** review
**Keywords:** Callback, init, block, item, variadic, flexible, optional, modded, custom, callbacks, context, owner, ZonElement, BlockID
**Symbols:** Callback.init, ZonElement, BlockID
**Concepts:** Flexibility, Initialization Order, Modularity, Generic Types

## Summary
The discussion revolves around modifying the `Callback.init` function to include context about the block or item it belongs to, with a focus on flexibility and avoiding unnecessary complexity.

## Explanation
The maintainers and users are discussing how to enhance the `Callback.init` function to provide more context by including information about the block or item. The main points of discussion include whether to use variadic inits, ensuring that callbacks are initialized last, and considering the flexibility needed for both standard and modded owners. The maintainers suggest using a generic type like the block index or item index, while also considering future possibilities for optional parameters and custom callback creation functions for modded items.

## Related Questions
- How can the `Callback.init` function be modified to include block or item context?
- What are the potential implications of initializing callbacks last?
- Can generic types like block index or item index be used effectively in this scenario?
- How should the implementation handle optional parameters for future use-cases?
- What are the considerations for supporting custom callback creation functions for modded items?
- Is there a risk of introducing complexity by adding more context to the `Callback.init` function?

*Source: unknown | chunk_id: github_issue_2386_discussion*
