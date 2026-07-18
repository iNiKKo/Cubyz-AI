# [issues/issue_1900.md] - Issue #1900 discussion

**Type:** review
**Keywords:** crash, first open, high render distance, texture reloads, anisotropic filtering, complete darkness, player-emitted light, improved visibility
**Concepts:** crash, render distance, texture reloads, logging

## Summary
The issue involves crashes on first open and while moving fast with high render distances. The maintainer suspects texture reloads due to setting changes as a cause.

## Explanation
The user reported two types of crashes: one immediately upon opening the application and another while moving quickly at high render distances. The maintainer analyzed logs and concluded that the first crash might have occurred before any window opened, possibly during early initialization. For the second crash, the logs indicated that frequent texture reloads due to setting changes (like anisotropic filtering) could be the cause, similar to a previously reported issue (#1495). The user also mentioned concerns about complete darkness in caves, suggesting a potential need for player-emitted light or improved visibility mechanisms.

## Related Questions
- What were the exact steps to reproduce the crash on first open?
- How did the logs indicate that texture reloads caused the second crash?
- Is there a way to prevent crashes due to frequent texture reloads?
- What is the current status of the idea for player-emitted light in caves?
- Are there any plans to improve visibility mechanisms in dark areas?
- Can you provide more details on how the application handles early initialization and potential crashes?

*Source: unknown | chunk_id: github_issue_1900_discussion*
