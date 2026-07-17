# [src/callbacks/callbacks.zig] - PR #2144 review diff

**Type:** review
**Keywords:** callbacks.zig, ClientBlockCallback, ServerBlockCallback, BlockTouchCallback, runFunction, field naming, Discord poll
**Symbols:** ClientBlockCallback, ServerBlockCallback, BlockTouchCallback, Callback, Result
**Concepts:** Generics, Struct Templates, Function Pointers, Polymorphism

## Summary
A new Zig file `callbacks.zig` is introduced to define various block-related callbacks and their initialization functions. The review discusses the naming of a function pointer field within a struct.

## Explanation
The code snippet introduces three types of block callbacks: `ClientBlockCallback`, `ServerBlockCallback`, and `BlockTouchCallback`. Each callback type is defined using a generic `Callback` struct template that takes parameters and a list type. The reviewer notes the persistence of the `runFunction` field within this struct and suggests renaming it, proposing a poll on Discord to gather wider input for naming conventions.

## Related Questions
- What is the purpose of the `init` function in the `callbacks.zig` file?
- How does the `Callback` struct template work in this code snippet?
- Why is there a discussion about renaming the `runFunction` field?
- What are the potential implications of using `*anyopaque` for the data field in the Callback struct?
- Can you explain the role of the `Result` enum in these callback definitions?
- How might the introduction of these callbacks impact the overall architecture of Cubyz?

*Source: unknown | chunk_id: github_pr_2144_comment_2481527950*
