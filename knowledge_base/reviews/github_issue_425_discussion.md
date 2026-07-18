# [issues/issue_425.md] - Issue #425 discussion

**Type:** review
**Keywords:** MacOS, default keybinds, ctrl + space, print screen, GLFW_KEY_, isMac
**Symbols:** GLFW_KEY_...
**Concepts:** platform-specific behavior, keybindings

## Summary
Discusses invalid default keybindings on macOS and proposes conditional handling based on platform.

## Explanation
The issue highlights that certain default keybindings in Cubyz are problematic on macOS, specifically the behavior of 'ctrl + space' which changes keyboard language and gets stuck. Additionally, screenshots don't work because macOS lacks a print screen key. The maintainer suggests modifying the code to use different key bindings for macOS by checking if the platform is macOS and then using appropriate GLFW_KEY constants.

## Related Questions
- What is the current implementation for handling keybindings in Cubyz?
- How does Cubyz determine if the platform is macOS?
- Are there any other keybindings that need to be adjusted for macOS?
- What are the potential impacts of changing keybindings on user experience?
- Is there a plan to create separate settings.json files for different platforms?
- How can we ensure that the new key bindings work correctly across all macOS versions?

*Source: unknown | chunk_id: github_issue_425_discussion*
