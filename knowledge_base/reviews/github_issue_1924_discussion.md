# [issues/issue_1924.md] - Issue #1924 discussion

**Type:** review
**Keywords:** UI, settings, controller, deadzone, vJoy, camera movement, title bar buttons
**Symbols:** settings.zig
**Concepts:** input handling, controller support, user interface

## Summary
Users report issues with closing the settings UI on Windows-x86_64 version 0.0.0, potentially related to controller input handling.

## Explanation
Users report issues with closing the settings UI on Windows-x86_64 version 0.0.0, potentially related to controller input handling. The issue arises when users attempt to close the settings UI using the title bar buttons while controllers are connected or configured. The maintainer suggests that the problem might be due to the title bar buttons not working with controllers. Users have also noted that this issue affects camera movement, indicating a broader bug within the game's input handling. The default deadzone setting in Cubyz is 0%, and users report issues when trying to close the settings UI. To resolve these issues, disabling vJoy can help, but it does not address the root cause of the problem. Users have reported experiencing camera movement on its own, which may indicate a bug within the game's input handling rather than with their controller. The discussion includes mentions of vJoy and the need for a larger deadzone in the settings to resolve these issues. Additionally, users needed to disconnect all controls (both physical and virtual) to close the menus.

## Related Questions
- What is the current implementation of title bar button handling in Cubyz?
- How does Cubyz handle input from both physical and virtual controllers?
- Are there any known issues with deadzone settings in Cubyz's control configuration?
- Can disabling vJoy resolve other UI interaction problems in Cubyz?
- What changes need to be made to support controller input for closing the settings UI?
- How can we ensure that camera movement is not affected by controller inputs?
- Is there a plan to update the default deadzone settings in Cubyz?
- Are there any plans to improve the compatibility of Cubyz with different controllers?
- What steps should be taken to prevent similar input handling issues in future updates?
- How can we test the effectiveness of changes made to resolve these UI interaction problems?

*Source: unknown | chunk_id: github_issue_1924_discussion*
