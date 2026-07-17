# [src/gui/windows/debug.zig] - PR #532 review diff

**Type:** review
**Keywords:** fpsCap, allocPrint, memory management, rendering, settings
**Symbols:** window, render, draw.setColor, y, main.lastFrameTime.load, main.settings.vsync, fpsCapText, main.stackAllocator.allocator, std.fmt.allocPrint
**Concepts:** memory allocation, conditional rendering, thread safety

## Summary
Updated the debug window to conditionally display an FPS limit text based on settings.

## Explanation
The change introduces a conditional check for the `fpsCap` setting in the debug window's render function. If `fpsCap` is set, it allocates memory using `main.stackAllocator.allocator` to format and store the FPS limit text. The reviewer notes that they updated the code to use Zig's standard library functions, specifically mentioning `std.fmt.allocPrint`, and expresses hope that these changes won't need frequent updates due to potential future changes in the Zig language.

## Related Questions
- What is the purpose of the `fpsCapText` variable in the debug window render function?
- How does the code handle memory allocation for the FPS limit text?
- Why did the reviewer mention updating to use `std.fmt.allocPrint`?
- Is there any potential risk associated with using `unreachable` in this context?
- What changes might occur if Zig updates its standard library functions?
- How does the debug window handle rendering when `fpsCap` is not set?

*Source: unknown | chunk_id: github_pr_532_comment_1660703887*
