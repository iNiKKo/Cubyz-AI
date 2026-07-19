# [src/gui/windows/graphics.zig] - PR #2395 review diff

**Type:** review
**Keywords:** FPS cap, presets, rounding, formatter, callback, assertion, u16 range, lowerBound, allocator, unreachable
**Symbols:** resolutions, leavesQualities, fpsCapRound, fpsCapFormatter, fpsCapCallback, FPSPresetsValue, FPSPresetsText, fpsCapGetIndex
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Refactored FPS cap handling by introducing presets and updating callback logic.

## Explanation
The change introduces a set of predefined FPS presets stored in `FPSPresetsValue` and their corresponding text representations in `FPSPresetsText`. The function `fpsCapGetIndex` is added to find the index of a given FPS value within these presets. The reviewer suggests asserting that the FPS value is within the range of `u16` for safety, although this assertion is not included in the provided diff.

The `FPSPresetsValue` array contains specific values: `[5, 10, 15, 30, 50, 60, 75, 90, 100, 120, 144, 165, 170, 180, 200, 240, 260, 280, 300, 360, 480]`. The `FPSPresetsText` array contains the corresponding text representations: `['5 Hz', '10 Hz', '15 Hz', '30 Hz', '50 Hz', '60 Hz', '75 Hz', '90 Hz', '100 Hz', '120 Hz', '144 Hz', '165 Hz', '170 Hz', '180 Hz', '200 Hz', '240 Hz', '260 Hz', '280 Hz', '300 Hz', '360 Hz', '480 Hz', 'unlimited']`.

The `fpsCapGetIndex` function uses `std.sort.lowerBound` to find the index of a given FPS value within the `FPSPresetsValue` array. The reviewer suggests asserting that the FPS value is within the range of `u16` for safety, although this assertion is not included in the provided diff.

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
