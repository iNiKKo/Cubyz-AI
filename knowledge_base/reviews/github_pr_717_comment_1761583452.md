# [src/graphics/Window.zig] - PR #717 review diff

**Type:** review
**Keywords:** gamepad, GLFWgamepadstate, AutoHashMap, deadzone, input handling, readability, maintenance
**Symbols:** width, height, window, grabbed, scrollOffset, gamepadState, applyDeadzone
**Concepts:** Gamepad Input Handling, Structural Organization, Input Deadzone Adjustment

## Summary
Added gamepad state management functions and deadzone application logic to the Window.zig file.

## Explanation
The change introduces a new variable `gamepadState` to store gamepad states using an `std.AutoHashMap`. A helper function `applyDeadzone` is added to adjust input values based on a specified deadzone. The reviewer suggests grouping all gamepad-related code into a single struct for better readability and maintainability.

## Related Questions
- What is the purpose of the `applyDeadzone` function?
- How does the `gamepadState` variable store gamepad states?
- Why was it suggested to group all gamepad-related code into one struct?
- What is the impact of the deadzone adjustment on input values?
- How might this change affect existing gamepad input handling in Cubyz?
- Is there a risk of memory leaks with the use of `AutoHashMap` for gamepad states?

*Source: unknown | chunk_id: github_pr_717_comment_1761583452*
