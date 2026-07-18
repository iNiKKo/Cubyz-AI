# [issues/issue_2402.md] - Issue #2402 discussion

**Type:** review
**Keywords:** chat clearing, command history, inventory clearing, user experience, security concerns, maintenance burden
**Symbols:** /clear, /clearInventory, /clear chat, /clear chatHistory
**Concepts:** Command Design, User Experience, Security, Maintenance

## Summary
Discussion about adding a `/clear chat` command and optionally clearing the command history, with considerations for user experience and security.

## Explanation
The discussion revolves around implementing a `/clear chat` command to empty the chat, with potential options to clear specific parts of it such as `/clear chatHistory`. The main proposal is to rename existing commands for clarity (e.g., `/clear inventory`, `/clear chat`). There are debates about clearing the command history due to security concerns and maintenance burdens. Use-cases include cleaning up insults from a malicious user, preparing lobbies between rounds, or displaying loading information. However, there's concern that clearing entire chat might be excessive for such scenarios. The proposal also includes tracking who said what in future implementations so admins can selectively remove messages of specific players using syntax like `/clear chat <username>`. Clearing command history is seen as trivial to implement but adds maintenance work and potential misuse risks.

## Related Questions
- What are the proposed commands for clearing inventory, chat, and chat history?
- Why was renaming existing clear commands suggested?
- What are the use-cases for the `/clear chat` command?
- How does tracking message origins help in selective removal of messages?
- What are the security concerns with clearing command history?
- What is the timeline for implementing #1737?

*Source: unknown | chunk_id: github_issue_2402_discussion*
