# [src/graphics/Window.zig] - PR #717 review diff

**Type:** review
**Keywords:** gamepad, deadzone, GLFW, hashmap, allocation, defer statement, button events, axis events, keyboard keys
**Symbols:** Window.zig, width, height, window, grabbed, scrollOffset, gamepadState, applyDeadzone, updateGamepadState, c.GLFWwindow, std.AutoHashMap, settings.controllerAxisDeadzone, main.globalAllocator, c.GLFW_JOYSTICK_LAST, c.glfwJoystickPresent, c.glfwJoystickIsGamepad, c.glfwGetGamepadState, c.GLFWgamepadstate, nextGamepadListener, c.GLFW_GAMEPAD_BUTTON_LAST, c.GLFW_GAMEPAD_AXIS_LAST
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added gamepad state management and deadzone handling in Window.zig.

## Explanation
Added gamepad state management and deadzone handling in Window.zig.

The `applyDeadzone` function calculates the deadzone by applying a minimum value (`minValue = settings.controllerAxisDeadzone`) and a maximum range (`maxRange = 1.0 - minValue`). It then adjusts the input value within this range using the formula: `(value * maxRange) + minValue`. This ensures that values below the deadzone are set to zero, while values above the deadzone are scaled between `minValue` and `1.0`.

The code handles gamepad button press/release events by iterating through each button from `0` to `c.GLFW_GAMEPAD_BUTTON_LAST`. If a button transitions from not pressed to pressed, it triggers the associated action if any is set. Similarly, for axis press/release events, it checks if an axis value crosses the deadzone threshold and triggers the associated action.

The `nextGamepadListener` variable is used to handle a single gamepad event listener at a time. Once an event is processed, it is reset to null to prevent further processing until explicitly set again.

Memory for gamepad states is allocated using `main.globalAllocator.create(c.GLFWgamepadstate)` and deallocated using `main.globalAllocator.destroy(gamepadState.?.get(jid).?)`. It is suggested to add a defer statement after allocation to ensure proper memory management and prevent potential memory leaks.

The code updates keyboard keys based on gamepad input by checking if the key is associated with a gamepad button or axis. If it's a button, it updates the key's pressed state and value accordingly. If it's an axis, it applies the deadzone and updates the key's value based on the axis position.

The `c.GLFW_JOYSTICK_LAST` constant represents the last joystick index that can be checked using GLFW functions.

## Related Questions
- What is the purpose of the applyDeadzone function?
- How does the code handle gamepad button and axis press/release events?
- Why is a defer statement suggested for allocation safety?
- What changes were made to manage gamepad states in Window.zig?
- How does the code ensure small joystick inputs are ignored?
- What is the role of the nextGamepadListener variable?
- How is memory allocated and managed for gamepad states?
- What are the implications of not adding a defer statement for allocation?
- How does the code update keyboard keys based on gamepad input?
- What is the significance of the c.GLFW_JOYSTICK_LAST constant?

*Source: unknown | chunk_id: github_pr_717_comment_1761590948*
