# [src/gui/windows/chat.zig] - PR #1244 review diff

**Type:** review
**Keywords:** chat window, message history, Minecraft, PowerShell Core, history behavior, modified versions, commit, navigation
**Symbols:** historyStart, fadeOutEnd, input, hideInput, upHistory, downHistory
**Concepts:** message history, user input, state preservation

## Summary
The review discusses the chat window's message history behavior, comparing it to Minecraft and PowerShell Core.

## Explanation
The reviewer examines how the chat window preserves old messages and commits new ones to history. They note that Minecraft restores history entries to an unmodified state when navigating through them but loses modified versions unless they are committed with 'enter'. In contrast, PowerShell Core keeps modified command versions until a commit is made, then only the committed version is preserved in history. The reviewer highlights differences in how these systems handle history navigation and modification.

## Related Questions
- How does the chat window handle message history preservation?
- What is the difference between Minecraft and PowerShell Core in terms of history navigation?
- When are modified command versions preserved in PowerShell Core?
- How does the chat window commit new messages to history?
- What happens to unmodified history entries when navigating through them in Minecraft?
- Is there a way to preserve all modified versions in the chat window like in PowerShell Core?

*Source: unknown | chunk_id: github_pr_1244_comment_2013455914*
