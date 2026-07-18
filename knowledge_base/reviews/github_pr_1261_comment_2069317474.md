# [src/blocks.zig] - PR #1261 review diff

**Type:** review
**Keywords:** healingRatio, inline, fixed value, member function, syntactically pleasing, per-block customization
**Symbols:** Block, healingRatio
**Concepts:** inline functions, member functions, syntactic sugar

## Summary
Added an inline function `healingRatio` to the `Block` struct, returning a fixed value of 0.05.

## Explanation
The change introduces an inline function `healingRatio` within the `Block` struct that returns a constant healing ratio of 0.05. The reviewer notes that this approach deviates from using a member function directly, which they find less syntactically pleasing and potentially more complex if per-block customization is needed in the future.

## Related Questions
- What is the purpose of the `healingRatio` function in the `Block` struct?
- Why was an inline function chosen for `healingRatio` instead of a member variable?
- How might the code be modified to support per-block healing ratios in the future?
- What potential performance implications does using an inline function have compared to a member variable?
- Is there any risk of introducing bugs by changing from a member function to an inline function?
- How would this change affect backwards compatibility with existing code?

*Source: unknown | chunk_id: github_pr_1261_comment_2069317474*
