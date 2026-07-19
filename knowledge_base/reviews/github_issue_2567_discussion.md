# [issues/issue_2567.md] - Issue #2567 discussion

**Type:** review
**Keywords:** fullscreen bug, GLFW, monitor switching, Linux Mint, Cubyz
**Symbols:** F11, fullscreen, glfwGetClosestMonitor, glfwGetPrimaryMonitor
**Concepts:** monitor management, fullscreen mode, window positioning

## Summary
The issue discusses a bug where pressing F11 to go fullscreen in Cubyz causes the window to switch to a different monitor instead of staying on the current one. A potential solution involving GLFW's `glfwGetClosestMonitor` function is suggested.

## Explanation
The issue discusses a bug where pressing F11 to go fullscreen in Cubyz causes the window to switch to a different monitor instead of staying on the current one. The maintainer suggests that while this behavior might not be directly supported by GLFW, there could be a workaround by determining which monitor the window is currently on using `glfwGetClosestMonitor`. A user proposes a code snippet from GLFW issue 1699 as a potential solution, involving checking the closest monitor to the window's current position. The proposed solution involves modifying the GLFW functions to ensure that the fullscreen toggle respects the intended display. Specifically, in glfwGetClosestMonitor, the function returns `glfwGetPrimaryMonitor()` if it is Linux to prevent potential bugs since testing on Wayland is not possible. This approach aims to ensure that the fullscreen toggle respects the intended display and can be adapted for multi-monitor setups.

## Related Questions
- How does GLFW determine the closest monitor to a window?
- What is the impact of using glfwGetPrimaryMonitor on Linux systems?
- Can the proposed solution be adapted for Wayland displays?
- Are there any known issues with GLFW's fullscreen mode on multi-monitor setups?
- How can we ensure that the fullscreen toggle respects the intended display in Cubyz?

*Source: unknown | chunk_id: github_issue_2567_discussion*
