# [src/gui/windows/graphics.zig] - PR #2395 review diff

**Type:** review
**Keywords:** FPS cap, presets, rounding, formatter, callback, assertion, u16 range, lowerBound, allocator, unreachable
**Symbols:** resolutions, leavesQualities, fpsCapRound, fpsCapFormatter, fpsCapCallback, FPSPresetsValue, FPSPresetsText, fpsCapGetIndex
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Refactored FPS cap handling by introducing presets and updating callback logic.

## Explanation
The change introduces a set of predefined FPS presets stored in `FPSPresetsValue` and their corresponding text representations in `FPSPresetsText`. The function `fpsCapGetIndex` is added to find the index of a given FPS value within these presets. The reviewer suggests asserting that the FPS value is within the range of `u16` for safety, although this assertion is not included in the provided diff.

## Related Questions
- What is the purpose of the `FPSPresetsValue` array?
- How does the `fpsCapGetIndex` function work with the `FPSPresetsValue` array?
- Why was the assertion for `u16` range suggested but not included in the diff?
- What changes were made to the FPS cap formatter and callback functions?
- How do the new presets affect the user interface for setting FPS limits?
- Is there a risk of memory leaks with the current allocator usage?
- How does this change impact backwards compatibility with older versions of Cubyz?
- What is the role of `std.sort.lowerBound` in finding the FPS preset index?
- Are there any potential thread safety issues introduced by these changes?
- How does the new FPS cap handling compare to the previous implementation?

*Source: unknown | chunk_id: github_pr_2395_comment_2882120756*
