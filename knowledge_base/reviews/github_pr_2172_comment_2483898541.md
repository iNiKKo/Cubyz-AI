# [src/main.zig] - PR #2172 review diff

**Type:** review
**Keywords:** keyboard bindings, union, menu entries, refactor, clean code, readable code
**Symbols:** KeyBoard, Window.Key, setHotbarSlot, MenuEntry
**Concepts:** refactoring, cleanliness, readability

## Summary
Refactored keyboard bindings into a union to handle different types of menu entries cleanly, including headings and bindings.

## Explanation
The change refactors the keyboard bindings by introducing a `MenuEntry` union that can either be a heading or a binding. This approach aims to address the issue of differently-sized arrays, making the code cleaner and more readable. The previous implementation used an array of `Window.Key` structures, which led to issues with handling different types of menu entries (e.g., headings) and managing differently-sized arrays. By using a union, the new implementation can handle both headings and bindings in a single array, simplifying the code structure and improving readability.

Here is an example of how the `MenuEntry` union might be used in the code:

```zig
const MenuEntry = union(enum) {
    heading: []const u8,
    binding: Window.Key,
};

pub var keys = [_]MenuEntry {
    .{.heading = "Display"},
    .{.binding = .{.key = c.GLFW_KEY_1, .pressAction = setHotbarSlot(1)}},
    // other entries...
};
```

The full list of keyboard bindings and their corresponding actions is as follows:

- **Display** (heading)
- **Hotbar 1**: GLFW_KEY_1
- **Hotbar 2**: GLFW_KEY_2
- **Hotbar 3**: GLFW_KEY_3
- **Hotbar 4**: GLFW_KEY_4
- **Hotbar 5**: GLFW_KEY_5
- **Hotbar 6**: GLFW_KEY_6
- **Hotbar 7**: GLFW_KEY_7
- **Hotbar 8**: GLFW_KEY_8
- **Hotbar 9**: GLFW_KEY_9
- **Hotbar 10**: GLFW_KEY_0
- **Hotbar 11**: GLFW_KEY_MINUS
- **Hotbar 12**: GLFW_KEY_EQUAL
- **Hotbar left**: GLFW_GAMEPAD_BUTTON_LEFT_BUMPER
- **Hotbar right**: GLFW_GAMEPAD_BUTTON_RIGHT_BUMPER
- **cameraLeft**: GLFW_GAMEPAD_AXIS_RIGHT_X (negative)
- **cameraRight**: GLFW_GAMEPAD_AXIS_RIGHT_X (positive)
- **cameraUp**: GLFW_GAMEPAD_AXIS_RIGHT_Y (negative)
- **cameraDown**: GLFW_GAMEPAD_AXIS_RIGHT_Y (positive)
- **hideMenu**: GLFW_KEY_F1
- **hideDisplayItem**: GLFW_KEY_F2
- **debugOverlay**: GLFW_KEY_F3
- **performanceOverlay**: GLFW_KEY_F4
- **gpuPerformanceOverlay**: GLFW_KEY_F5
- **networkDebugOverlay**: GLFW_KEY_F6
- **advancedNetworkDebugOverlay**: GLFW_KEY_F7

## Related Questions
-  What was the primary issue with the previous keyboard binding implementation?
-  How does the new `MenuEntry` union improve the code structure?
-  Can you explain the benefits of using a union for menu entries in this context?
-  What other approaches were considered before settling on the current solution?
-  How might the use of a union impact performance or memory usage?
-  Are there any potential drawbacks to this refactoring approach?

*Source: unknown | chunk_id: github_pr_2172_comment_2483898541*
