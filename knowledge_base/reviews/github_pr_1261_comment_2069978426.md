# [src/blocks.zig] - PR #1261 review diff

**Type:** review
**Keywords:** healingRatio, inline, customizability, optimization, opt out
**Symbols:** Block, healingRatio
**Concepts:** inline functions, member functions, optimization

## Summary
Added a `healingRatio` inline function to the `Block` struct.

## Explanation
The change introduces a new member function `healingRatio` within the `Block` struct, which returns a fixed value of 0.05. The reviewer points out that this implementation implies customizability, which could be misleading. Additionally, the reviewer emphasizes that this is intended as an optimization and should not allow any form of opting out.

## Related Questions
- What is the purpose of the `healingRatio` function in the `Block` struct?
- Why was the `healingRatio` function added as an inline member function?
- Does the current implementation of `healingRatio` allow for customization?
- How does this change impact the overall performance of the block system?
- What are the potential implications of making `healingRatio` non-customizable?
- Is there a risk of introducing bugs with the fixed value in `healingRatio`?

*Source: unknown | chunk_id: github_pr_1261_comment_2069978426*
