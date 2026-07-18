# [src/gui/windows/graphics.zig] - PR #2395 review diff

**Type:** review
**Keywords:** FPS presets, dynamic calculation, conditional logic, runtime errors, explicit definition
**Symbols:** fpsCapRound, FPSPresetsValue
**Concepts:** code simplification, constant arrays

## Summary
Replaced the `fpsCapRound` function with a new constant array `FPSPresetsValue` to define FPS presets.

## Explanation
The original `fpsCapRound` function was replaced by a static array of FPS preset values. This change simplifies the code by removing the need for dynamic calculation and conditional logic, making it easier to maintain and understand. The reviewer suggests using a constant array to ensure that all possible FPS values are explicitly defined, which can help prevent runtime errors related to invalid or unexpected FPS settings.

## Related Questions
- What was the purpose of removing the `fpsCapRound` function?
- How does the new constant array `FPSPresetsValue` improve code maintainability?
- Can you explain why the reviewer suggests using a constant array for FPS presets?
- What potential issues could arise from dynamic FPS calculations in this context?
- How might the removal of `fpsCapRound` affect performance or stability?
- Is there any risk of introducing new bugs with the change to a static FPS preset array?

*Source: unknown | chunk_id: github_pr_2395_comment_2882110596*
