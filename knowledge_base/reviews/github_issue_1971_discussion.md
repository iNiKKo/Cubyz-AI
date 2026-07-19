# [issues/issue_1971.md] - Issue #1971 discussion

**Type:** review
**Keywords:** jumping, sprinting, remapping controls, Debian GNU/Linux, GNOME 48.4, Shift+Space, i3wm
**Concepts:** input handling, keybindings, environment-specific issues

## Summary
The user reports an inability to jump while sprinting after remapping controls in Cubyz on Debian GNU/Linux with GNOME 48.4.

## Explanation
The user reports an inability to jump while sprinting after remapping controls in Cubyz on Debian GNU/Linux with GNOME 48.4. The issue seems to be specific to the user's environment, as it cannot be reproduced in other setups or configurations. The maintainer suggests that there might be a global keybind for `Shift+Space` taking precedence, which could be affecting the game's behavior. The user later confirms that switching to i3wm resolves the issue, indicating that GNOME's configuration might be interfering with the game's input handling. Additionally, it was noted that the issue does not occur in the latest master branch, suggesting that changes made there might have resolved the problem.

## Related Questions
- Is there a known issue with GNOME's keybind handling that could interfere with game inputs?
- How does Cubyz handle input remapping, and are there any potential conflicts with system-wide keybindings?
- Can the game be configured to ignore certain global keybindings to prevent interference?
- Are there any logs or debug information available that could help identify the source of the input conflict?
- What changes were made in the latest master branch that might have resolved this issue, and how can they be applied to other environments?
- How can Cubyz be tested for compatibility with different desktop environments to ensure consistent behavior?

*Source: unknown | chunk_id: github_issue_1971_discussion*
