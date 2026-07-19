# [src/gui/windows/graphics.zig] - PR #2395 review diff

**Type:** review
**Keywords:** FPS presets, dynamic calculation, conditional logic, runtime errors, explicit definition
**Symbols:** fpsCapRound, FPSPresetsValue
**Concepts:** code simplification, constant arrays

## Summary
Replaced the `fpsCapRound` function with a new constant array `FPSPresetsValue` to define FPS presets.

## Explanation
The original `fpsCapRound` function was replaced by a static array of FPS preset values. This change simplifies the code by removing the need for dynamic calculation and conditional logic, making it easier to maintain and understand. The reviewer suggests using a constant array to ensure that all possible FPS values are explicitly defined, which can help prevent runtime errors related to invalid or unexpected FPS settings.

The new `FPSPresetsValue` array contains the following FPS preset values: 5, 10, 15, 30, 50, 60, 75, 90, 100, 120, 144, 165, 170, 180, 200, 240, 260, 280, 300, 360, and 480. These values are explicitly defined to ensure that the FPS settings are valid and predictable.

## Related Questions
- What was the purpose of removing the `fpsCapRound` function?
- How does the new constant array `FPSPresetsValue` improve code maintainability?
- Can you explain why the reviewer suggests using a constant array for FPS presets?
- What potential issues could arise from dynamic FPS calculations in this context?
- How might the removal of `fpsCapRound` affect performance or stability?
- Is there any risk of introducing new bugs with the change to a static FPS preset array?

*Source: unknown | chunk_id: github_pr_2395_comment_2882110596*
