# [issues/issue_911.md] - Issue #911 discussion

**Type:** review
**Keywords:** shader compilation errors, flash, beep, popup window, crash, debug mode, client-only messages, chat
**Concepts:** user experience, error handling, notifications

## Summary
Discussion about making shader compilation errors more noticeable to users.

## Explanation
Discussion about making shader compilation errors more noticeable to users. The issue revolves around improving user awareness of shader compilation errors during gameplay. The discussion includes potential solutions like flashing the screen, beeping, or opening a popup window to make these errors more noticeable. There's also consideration for sending client-only messages in the chat as an alternative to crashing in debug mode. The maintainer notes that many shader errors occur on the title screen, suggesting that error notifications should not disrupt gameplay too much and exploring trade-offs between different methods of error notification (e.g., flashing vs. beeping). Additionally, it is noted that crashing can still be considered as an option in debug mode for certain user experiences. Requires fixing all warnings (#910) first.

## Related Questions
- What are the potential impacts of making shader compilation errors more intrusive?
- How can we ensure that error notifications do not disrupt gameplay too much?
- Are there any existing systems in Cubyz that could be adapted for this purpose?
- What are the trade-offs between different methods of error notification (e.g., flashing vs. beeping)?
- How can we test the effectiveness of these changes in a real-world scenario?
- Is there a way to prioritize certain types of errors over others in terms of intrusiveness?

*Source: unknown | chunk_id: github_issue_911_discussion*
