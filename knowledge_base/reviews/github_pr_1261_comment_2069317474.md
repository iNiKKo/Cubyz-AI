# [src/blocks.zig] - PR #1261 review diff

**Type:** review
**Keywords:** healingRatio, inline, Block, function, syntax, customization
**Symbols:** Block, healingRatio
**Concepts:** inline functions, member functions, syntactic sugar

## Summary
Added an inline function `healingRatio` to the `Block` struct, returning a fixed value of 0.05.

## Explanation
The change introduces an inline function `healingRatio` within the `Block` struct that returns a constant healing ratio of 0.05. This approach is criticized for requiring the use of `Block.healingRatio` instead of a member function, which is considered less syntactically pleasing and potentially more complex if custom healing ratios per block are needed in the future.

## Related Questions
- What is the purpose of the `healingRatio` function in the `Block` struct?
- Why was the `healingRatio` implemented as an inline function instead of a member function?
- How might the code be modified to support custom healing ratios per block?
- What potential performance implications does using an inline function have compared to a regular function call?
- Is there any risk of introducing bugs by changing the way healing ratios are accessed in the `Block` struct?
- How could this change affect future maintenance and scalability of the codebase?

*Source: unknown | chunk_id: github_pr_1261_comment_2069317474*
