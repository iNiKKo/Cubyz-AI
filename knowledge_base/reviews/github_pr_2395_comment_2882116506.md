# [src/gui/windows/graphics.zig] - PR #2395 review diff

**Type:** review
**Keywords:** FPS cap, presets, refactoring, null check, optional parameter
**Symbols:** fpsCapRound, fpsCapFormatter, fpsCapCallback, FPSPresetsValue, FPSPresetsText, fpsCapGetIndex
**Concepts:** code refactoring, null safety, preset values

## Summary
Refactored FPS cap handling by introducing presets and updating callback functions.

## Explanation
The change introduces a set of predefined FPS presets with corresponding text labels. The `fpsCapRound` function has been replaced with an array of preset values (`FPSPresetsValue`) and their formatted strings (`FPSPresetsText`). The reviewer suggests modifying the `fpsCapGetIndex` function to handle null values more gracefully by using an optional parameter and returning the length of the presets array if no valid FPS value is provided. This refactoring aims to improve code clarity, maintainability, and prevent potential null pointer issues.

## Related Questions
- What is the purpose of the `FPSPresetsValue` array?
- How does the new `fpsCapGetIndex` function handle null values?
- Why was the `fpsCapRound` function replaced with presets?
- What changes were made to the FPS cap formatter?
- How does the refactoring improve code maintainability?
- What is the impact of introducing preset FPS values on performance?

*Source: unknown | chunk_id: github_pr_2395_comment_2882116506*
