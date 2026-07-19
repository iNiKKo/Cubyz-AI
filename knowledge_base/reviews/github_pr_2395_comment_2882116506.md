# [src/gui/windows/graphics.zig] - PR #2395 review diff

**Type:** review
**Keywords:** FPS cap, presets, refactoring, null check, configuration, readability, maintainability
**Symbols:** fpsCapRound, fpsCapFormatter, fpsCapCallback, FPSPresetsValue, FPSPresetsText, fpsCapGetIndex
**Concepts:** code refactoring, preset values, user interface configuration, null handling

## Summary
Refactored FPS cap handling by introducing presets and updating callback functions.

## Explanation
Refactored FPS cap handling by introducing presets and updating callback functions.

The change introduces a set of predefined FPS presets to simplify the configuration process. The `fpsCapRound` function has been replaced with an array of preset values (`FPSPresetsValue`) and corresponding text representations (`FPSPresetsText`). The reviewer suggests modifying the `fpsCapGetIndex` function to handle null values more gracefully by using an optional parameter and returning the length of the presets array if no valid FPS is provided. This refactoring aims to improve code readability and maintainability while ensuring that the FPS cap settings remain consistent and user-friendly.

**Specific Values:**
- `FPSPresetsValue`: `[5, 10, 15, 30, 50, 60, 75, 90, 100, 120, 144, 165, 170, 180, 200, 240, 260, 280, 300, 360, 480]`
- `FPSPresetsText`: `["5 Hz", "10 Hz", "15 Hz", "30 Hz", "50 Hz", "60 Hz", "75 Hz", "90 Hz", "100 Hz", "120 Hz", "144 Hz", "165 Hz", "170 Hz", "180 Hz", "200 Hz", "240 Hz", "260 Hz", "280 Hz", "300 Hz", "360 Hz", "480 Hz", "unlimited"]`

**Function Details:**
- `fpsCapFormatter` now uses the new presets to format the FPS limit text. If the FPS cap is unlimited, it returns `"#ffffffFPS: Unlimited"`. Otherwise, it formats the FPS limit as `"#ffffffFPS Limit: {d:.0}"` where `{d}` is the selected FPS value from `FPSPresetsValue`.

**Null Handling:**
The reviewer suggests modifying the `fpsCapGetIndex` function to handle null values more gracefully by using an optional parameter and returning the length of the presets array if no valid FPS is provided. This ensures that the function can handle cases where the FPS value might not be set, maintaining robustness in the configuration process.

**Backwards Compatibility:**
The refactoring does not explicitly address backwards compatibility, but it aims to maintain consistent behavior by using predefined values for FPS settings.

**Performance Implications:**
Using presets instead of dynamic calculations can improve performance by reducing computation overhead and providing a fixed set of options for the user to choose from.

**Thread Safety:**
The changes do not explicitly address thread safety, but they aim to improve code maintainability and readability, which can contribute to better overall system stability.

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
