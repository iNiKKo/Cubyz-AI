# [src/server/world.zig] - PR #1338 review diff

**Type:** review
**Keywords:** optional parameters, early returns, refactoring, readability, control flow, indentation
**Symbols:** ServerWorld, tickBlocksInChunk, chunk.ServerChunk
**Concepts:** code readability, control flow, early returns

## Summary
The review suggests refactoring a function to use early returns and avoid passing optional parameters.

## Explanation
The reviewer recommends modifying the `tickBlocksInChunk` function to use early returns instead of nested if statements, which can reduce indentation levels. Additionally, the reviewer advises handling the optional parameter at the call site rather than within the function itself. This change aims to improve code readability and maintainability by simplifying the control flow.

The specific suggestion provided is:
```suggestion
	const ch = _chunk orelse return;
```
This line replaces the `if` statement with an early return, reducing indentation levels and improving readability. Handling the optional parameter at the call site means that the function signature can be simplified to avoid passing an optional parameter.

## Related Questions
- What is the purpose of the `tickBlocksInChunk` function?
- How does the reviewer suggest modifying the function to improve readability?
- Why should optional parameters be handled at the call site instead of within the function?
- Can you provide an example of how early returns can simplify code control flow?
- What are the benefits of reducing indentation levels in a function?
- How might this refactoring impact performance or correctness?

*Source: unknown | chunk_id: github_pr_1338_comment_2081725658*
