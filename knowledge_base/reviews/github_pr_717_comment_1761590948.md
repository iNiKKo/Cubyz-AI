# [src/graphics/Window.zig] - PR #717 review diff

**Type:** review
**Keywords:** gamepad, deadzone, GLFW, hashmap, allocation, defer statement, button events, axis events, keyboard keys
**Symbols:** Window.zig, width, height, window, grabbed, scrollOffset, gamepadState, applyDeadzone, updateGamepadState, c.GLFWwindow, std.AutoHashMap, settings.controllerAxisDeadzone, main.globalAllocator, c.GLFW_JOYSTICK_LAST, c.glfwJoystickPresent, c.glfwJoystickIsGamepad, c.glfwGetGamepadState, c.GLFWgamepadstate, nextGamepadListener, c.GLFW_GAMEPAD_BUTTON_LAST, c.GLFW_GAMEPAD_AXIS_LAST
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added gamepad state management and deadzone handling in Window.zig.

## Explanation
The change introduces functionality to manage gamepad states using GLFW, including applying a deadzone to joystick axes. The code initializes a hashmap to store gamepad states for each connected joystick. It updates the gamepad state by checking if the joystick is present and a gamepad, then retrieves and processes the new state. Deadzones are applied to ensure small inputs are ignored. The code also handles button and axis press/release events, updating keyboard keys accordingly. A critical architectural review suggests adding a defer statement for allocation safety.

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
