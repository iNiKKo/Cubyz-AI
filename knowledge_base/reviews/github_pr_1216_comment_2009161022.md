# [src/blocks.zig] - PR #1216 review diff

**Type:** review
**Keywords:** inline function, pointer return, global accessibility, architectural review, data manipulation, encapsulation, function scope
**Symbols:** Block, modeData, createBlockModel
**Concepts:** architectural design, data encapsulation, function scope

## Summary
A new inline function `modeData` is added to the `Block` struct, which returns a pointer to `u16`. The reviewer suggests that instead of making this editable globally, it should be managed within the `createBlockModel` function.

## Explanation
The addition of the `modeData` function introduces a new way to access block mode data. However, the reviewer expresses concern about global accessibility and suggests encapsulating this functionality within the `createBlockModel` function. This change aims to improve architectural integrity by restricting the scope of data manipulation, potentially reducing side effects and improving maintainability.

## Related Questions
- What is the purpose of the `modeData` function in the `Block` struct?
- Why does the reviewer suggest modifying the `createBlockModel` function instead of making `modeData` globally accessible?
- How might encapsulating data manipulation within `createBlockModel` improve architectural integrity?
- What potential side effects could arise from making `modeData` globally editable?
- How does restricting the scope of data manipulation contribute to maintainability?
- Can you explain the benefits and drawbacks of using an inline function in this context?

*Source: unknown | chunk_id: github_pr_1216_comment_2009161022*
