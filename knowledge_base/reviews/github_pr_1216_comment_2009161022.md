# [src/blocks.zig] - PR #1216 review diff

**Type:** review
**Keywords:** inline function, pointer return, architecture review, block mode data, global accessibility
**Symbols:** Block, modeData, createBlockModel
**Concepts:** architectural design, encapsulation, global state management

## Summary
A new inline function `modeData` is added to the `Block` struct, which returns a pointer to `u16`. The reviewer suggests that instead of making this editable globally, it should be managed within the `createBlockModel` function.

## Explanation
The addition of the `modeData` function introduces a new way to access block mode data. However, the reviewer is concerned about potential global accessibility and suggests encapsulating this functionality within the `createBlockModel` function to maintain better control over how and where block modes are modified. This change aims to improve architectural integrity by reducing unintended side effects from global state manipulation.

## Related Questions
- What is the purpose of the `modeData` function in the `Block` struct?
- Why does the reviewer suggest modifying the `createBlockModel` function instead of making `modeData` globally editable?
- How might encapsulating block mode data within `createBlockModel` affect performance?
- What potential issues could arise from global state manipulation in this context?
- Can you explain the architectural reasoning behind the reviewer's suggestion?
- How does the addition of `modeData` impact thread safety considerations?

*Source: unknown | chunk_id: github_pr_1216_comment_2009161022*
