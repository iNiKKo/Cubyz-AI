# [src/tool/modifiers/bad_at.zig] - PR #2668 review diff

**Type:** review
**Keywords:** floating-point literals, consistency, math.hypot, strength calculation, Zig language
**Symbols:** loadData, combineModifiers, Data, main.ZonElement
**Concepts:** floating-point precision, mathematical correctness

## Summary
The code was modified to consistently use `.0` for floating-point literals and to correct the calculation in the `combineModifiers` function.

## Explanation
The reviewer pointed out that the original code used a mix of `.0` and no decimal point for floating-point numbers, which is inconsistent. The reviewer also noted a potential issue with the mathematical formula inside the `combineModifiers` function. The suggested change corrects both issues by ensuring all floating-point literals use `.0` and adjusting the formula to avoid division by zero or other numerical inaccuracies.

The original formula in the `combineModifiers` function was:
```zig
return .{.strength = 1.0 - 1.0/std.math.hypot(1.0/(1.0 - data1.strength), 1.0/(1.0 - data2.strength)), .tag = data1.tag};
```
The corrected formula is:
```zig
return .{.strength = 1.0 - 1.0/(1 + std.math.hypot(1.0/(1.0 - data1.strength) - 1, 1.0/(1.0 - data2.strength) - 1)), .tag = data1.tag};
```
This change ensures that the calculation is more numerically stable and avoids potential division by zero issues.

## Related Questions
- Why was it necessary to consistently use `.0` for floating-point literals?
- What was the original issue with the `combineModifiers` function's formula?
- How does the corrected formula prevent potential numerical inaccuracies?
- Are there any other parts of the codebase that should be reviewed for similar inconsistencies?
- Can you explain the purpose of using `std.math.hypot` in this context?
- What are the implications of changing floating-point literals to `.0` throughout the code?

*Source: unknown | chunk_id: github_pr_2668_comment_2935294140*
