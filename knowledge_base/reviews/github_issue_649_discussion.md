# [issues/issue_649.md] - Issue #649 discussion

**Type:** review
**Keywords:** chat crash, gui initialization, message processing, timing issue, null pointer
**Symbols:** update, GuiWindow.zig, updateAndRenderGui, main.zig, __tmainCRTStartup, mainCRTStartup
**Concepts:** thread safety, initialization order, null pointer dereference

## Summary
The game crashes when a chat message is received after joining but before the chat GUI is opened.

## Explanation
The crash occurs during the update of chat messages in the `chat.zig` file, specifically at line 120. The issue arises because the chat GUI has not been initialized yet when messages are being processed. This leads to a null pointer dereference or similar access violation. The discussion suggests that this might be related to timing issues between the game's initialization and the rendering of the GUI.

## Related Questions
- What is the sequence of events leading up to the chat message update?
- How does the game ensure that the GUI is fully initialized before handling messages?
- Is there a check in place to prevent updating chat messages if the GUI is not ready?
- Can adding a delay or condition to wait for GUI initialization resolve this issue?
- What are the potential side effects of modifying the message update logic to handle uninitialized GUIs?
- How can we improve the synchronization between GUI initialization and message processing?

*Source: unknown | chunk_id: github_issue_649_discussion*
