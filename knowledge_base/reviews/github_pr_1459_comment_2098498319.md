# [src/blueprint.zig] - PR #1459 review diff

**Type:** review
**Keywords:** initFromString, specifiers, weights, error messages, positive numbers, descriptive language
**Symbols:** Pattern, initFromString, NeverFailingAllocator, source, specifiers, totalWeight, weightedEntries, ListUnmanaged, main.stackAllocator, specifier, iterator, blockId, weight, expressionSeparator, weightSeparator
**Concepts:** error handling, string parsing, data validation

## Summary
The code modifies the `initFromString` function in `blueprint.zig` to handle block specifiers with weights, ensuring weights are positive and using more descriptive error messages.

## Explanation
The change introduces a new variable `expressionSeparator` to split the input string into specifiers. It then checks if each specifier contains a weight separator. If it does, it splits the specifier further to separate the block ID from the weight. The weight is parsed as a float and checked to ensure it is greater than zero, returning an appropriate error message if not. The reviewer suggests using more descriptive language in the error messages for better clarity.

## Related Questions
- What is the purpose of the `expressionSeparator` variable in the code?
- How does the code handle specifiers that do not contain a weight separator?
- What error is returned if the parsed weight is less than or equal to zero?
- Why was the reviewer concerned about using '<=' instead of '>' for weight validation?
- How does the code ensure that block IDs are correctly extracted from specifiers?
- What changes were made to improve the clarity of the error messages?

*Source: unknown | chunk_id: github_pr_1459_comment_2098498319*
