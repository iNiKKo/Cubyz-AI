# [src/gui/windows/graphics.zig] - PR #2395 review diff

**Type:** review
**Keywords:** FPS cap, presets, refactoring, null check, configuration, readability, maintainability
**Symbols:** fpsCapRound, fpsCapFormatter, fpsCapCallback, FPSPresetsValue, FPSPresetsText, fpsCapGetIndex
**Concepts:** code refactoring, preset values, user interface configuration, null handling

## Summary
Refactored FPS cap handling by introducing presets and updating callback functions.

## Explanation
The change introduces a set of predefined FPS presets to simplify the configuration process. The `fpsCapRound` function has been replaced with an array of preset values (`FPSPresetsValue`) and corresponding text representations (`FPSPresetsText`). The reviewer suggests modifying the `fpsCapGetIndex` function to handle null values more gracefully by using an optional parameter and returning the length of the presets array if no valid FPS is provided. This refactoring aims to improve code readability and maintainability while ensuring that the FPS cap settings remain consistent and user-friendly.

## Related Questions
- What is the purpose of the `FPSPresetsValue` array?
- How does the new `fpsCapGetIndex` function handle null values?
- Why was the `fpsCapRound` function replaced with presets?
- What improvements does this refactoring bring to the FPS cap settings?
- How does the `fpsCapFormatter` function interact with the new presets?
- Can you explain the role of the `FPSPresetsText` array in the code?
- What is the significance of the reviewer's suggestion for null handling in `fpsCapGetIndex`?
- How might this refactoring affect backwards compatibility?
- Are there any potential performance implications from using presets instead of dynamic calculations?
- What changes were made to ensure thread safety in the FPS cap settings?

*Source: unknown | chunk_id: github_pr_2395_comment_2882116506*
