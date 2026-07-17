# [src/blocks.zig] - Chunk 2081718007

**Type:** review
**Keywords:** refactor, top-level variable, unnecessary nesting, NamedCallbacks, deinit, getFunctionPointer, architectural review, Zig conventions, coupling, lifecycle
**Symbols:** Block, TickFunction, TickFunctions, super, utils.NamedCallbacks, init, deinit, getFunctionPointer
**Concepts:** callback registration, struct nesting, API surface reduction, module-level state management, lifecycle coupling prevention

## Summary
Refactored the block registration system to use a top-level `tickFunctions` variable instead of embedding it inside the `TickFunctions` struct, addressing reviewer concerns about unnecessary nesting and improving clarity.

## Explanation
The original design wrapped all tick callbacks inside the `TickFunctions` struct via a `super` field initialized with `utils.NamedCallbacks`. Reviewers pointed out that this extra layer of indirection is redundant: the same functionality can be achieved by declaring `tickFunctions` as a top-level `pub var` of type `utils.NamedCallbacks(TickFunctions, TickFunction)`. This change eliminates the need for the struct to hold its own callbacks, simplifies initialization (no longer needing a separate `init()` that sets `super`), and makes the API surface flatter. Architecturally, moving the variable outside the struct aligns with Zig’s convention of keeping global registries at module scope rather than nested within per-entity structs, reducing coupling between block definitions and the callback registry. It also prevents potential issues where a block might be deinitialized while still holding references to the inner `super` callbacks, as the top-level variable can be managed independently of any particular block struct lifecycle.

## Related Questions
- What is the exact type of `utils.NamedCallbacks` and how does it manage callbacks?
- Why was the original design using a nested `super` field inside `TickFunctions` considered problematic?
- How does moving `tickFunctions` to module scope affect initialization order in `blocks.zig`?
- Does the new top-level declaration require any changes to how blocks register their tick callbacks?
- What happens to existing code that references `TickFunctions.init()` after this refactor?
- Is there a risk of memory leaks if `tickFunctions` is not properly deinitialized alongside other module globals?
- How does the reviewer’s suggestion align with Zig best practices for global registries?
- Could the removal of the nested struct impact any future extensions that might want to embed callbacks inside block structs?
- What are the implications for thread safety if `tickFunctions` is accessed concurrently after this change?
- Does the new design simplify or complicate the error handling path when retrieving a callback by ID?

*Source: unknown | chunk_id: github_pr_1338_comment_2081718007*
