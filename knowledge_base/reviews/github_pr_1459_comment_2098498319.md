# [src/blueprint.zig] - PR #1459 review diff

**Type:** review
**Keywords:** block specifiers, weight parsing, error messages, strictly positive, pattern initialization, splitScalar, containsAtLeastScalar, parseFloat
**Symbols:** Pattern, initFromString, NeverFailingAllocator, source, specifiers, totalWeight, weightedEntries, ListUnmanaged, struct {block: Block, weight: f32}, main.stackAllocator, specifier, iterator, blockId, weight, expressionSeparator, weightSeparator, std.mem.splitScalar, std.mem.containsAtLeastScalar, std.fmt.parseFloat
**Concepts:** parsing, validation, error handling, data structures

## Summary
The code was modified to correctly parse and validate weights in block specifiers, ensuring they are greater than zero.

## Explanation
The code was modified to correctly parse and validate weights in block specifiers, ensuring they are greater than zero. The change involves updating the parsing logic for block specifiers in the `initFromString` function of the `Pattern` struct. Previously, the weight check used `<= 0`, which is incorrect since weights should be strictly positive. The reviewer suggests changing this to `> 0` and recommends using more descriptive error messages that are not intended for programmers. Specifically, the code now splits the specifier string into block ID and weight components using `expressionSeparator` (which is a comma) and `weightSeparator` (which is a percent sign). It then parses the weight as a float and checks if it is greater than zero. This ensures that the weights are valid and prevents potential errors in pattern initialization. The exact error messages suggested by the reviewer are 'Weight not a valid number' and 'Weight must be greater than 0'. These changes improve the robustness and clarity of the code.

## Related Questions
- What is the purpose of the `expressionSeparator` variable in the code?
- How does the code handle invalid weight values when parsing block specifiers?
- Why was the error message changed to use English words instead of technical terms?
- What is the role of the `main.stackAllocator` in this function?
- How does the code ensure that the weights are strictly positive?
- What changes were made to handle the separation of block ID and weight in the specifier string?

*Source: unknown | chunk_id: github_pr_1459_comment_2098498319*
