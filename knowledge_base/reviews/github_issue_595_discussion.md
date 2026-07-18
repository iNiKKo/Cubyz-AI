# [issues/issue_595.md] - Issue #595 discussion

**Type:** review
**Keywords:** FPS counter, menu, text rendering bug, issue #400, commit f0c57d6c13d977c0c2b073070a8c2170a4ac412c
**Concepts:** text rendering, bug

## Summary
The FPS counter only displays when the menu is open, indicating a bug in text rendering.

## Explanation
The issue revolves around the FPS counter not being visible unless the menu is open. The maintainer initially thought it might be related to another issue (#400) and suspected it was resolved by recent changes in commit f0c57d6c13d977c0c2b073070a8c2170a4ac412c. However, upon further investigation, the problem persists, suggesting that the root cause of the text rendering issue remains unresolved.

## Related Questions
- What changes were made in commit f0c57d6c13d977c0c2b073070a8c2170a4ac412c that might have affected text rendering?
- Is there any known interaction between the FPS counter and menu rendering that could cause this issue?
- Could the problem be related to how the FPS counter is updated or rendered in the game loop?
- Are there any other parts of the codebase that handle text rendering and might be causing this bug?
- How can we ensure that the FPS counter is always visible regardless of whether the menu is open or not?
- What steps should be taken to prevent similar text rendering issues from occurring in the future?

*Source: unknown | chunk_id: github_issue_595_discussion*
