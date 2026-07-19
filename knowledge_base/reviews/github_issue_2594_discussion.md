# [issues/issue_2594.md] - Issue #2594 discussion

**Type:** review
**Keywords:** headless servers, moderators, kick command, manage player window, feedback messages, terminal, chat moderation, web UIs, activity logs, global chat feed
**Symbols:** /kick, manage player window
**Concepts:** permissions, command-line interface (CLI), user feedback, global visibility, activity logging

## Summary
Discussion on enabling a manage player window for headless servers and integrating kick command functionality.

## Explanation
Discussion on enabling a manage player window for headless servers and integrating kick command functionality.

The discussion centers around enabling a manage player window for headless servers to allow moderators with specific permissions to perform actions like kicking players. The proposed solution involves three main steps: creating the /kick command, rewriting the manage player window to use this command in the background, and restricting the visibility of the manage player window based on user permissions after implementing #2588.

The /kick command is intended to be used by moderators with specific permissions. The syntax for the /kick command is not explicitly stated but is implied to be a standard command-line interface (CLI) command. The command should allow moderators to kick players from the server, and it should generate feedback messages such as 'User has no permission to use /kick' or 'User ... has been kicked'.

There is debate about whether feedback messages should be printed in the chat or terminal. The maintainer suggests reducing feedback to only print errors into the terminal, while a user argues that error messages like 'User has no permission to use /kick' and confirmation messages like 'User ... has been kicked' should appear in the chat for clarity and transparency.

In headless server environments, it is suggested that a full global chat feed be available for practical reasons such as chat moderation without being on the server. Additionally, there are discussions about separating global chat messages from command I/O for future web UIs and preserving activity logs of player actions for at least a few minutes into the past to allow retrospective review of suspicious activities.

The maintainer also mentions that information about someone being kicked or banned should be global, to work as a wall of shame. This is important for maintaining transparency and accountability in server management.

Linux logs somewhere attempts to use commands that require root access somewhere, or at least PCs at my university always threatened to do so 😅

## Related Questions
- How does the /kick command interact with the manage player window?
- What are the current limitations in reading stdin for headless servers?
- Why is global visibility of kick/ban messages important for headless servers?
- How can feedback messages be effectively managed between chat and terminal?
- What considerations should be made for separating global chat from command I/O?
- How will activity logs be preserved and used for retrospective review?

*Source: unknown | chunk_id: github_issue_2594_discussion*
