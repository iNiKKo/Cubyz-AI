# [issues/issue_2001.md] - Issue #2001 discussion

**Type:** review
**Keywords:** menu background rendering, framebuffer update, FOV change, halved FPS, UI open
**Symbols:** framebuffer, FOV
**Concepts:** performance optimization, rendering pipeline

## Summary
The menu background rendering is proposed to be split into two separate functions to prevent unnecessary framebuffer updates when changing the FOV.

## Explanation
The discussion revolves around optimizing the rendering process by separating concerns. The reviewer suggests that updating the framebuffer should not occur every time the Field of View (FOV) changes, as this could lead to performance issues such as halved FPS when the UI is open. The maintainer confirms that this change would address the issue without introducing any regressions.

## Related Questions
- What is the impact of changing FOV on framebuffer updates?
- How does splitting the function improve performance?
- Are there any potential side effects from this change?
- Can you provide a code snippet showing the proposed changes?
- How does this affect the rendering pipeline overall?
- Is there a test case for verifying the FPS improvement?

*Source: unknown | chunk_id: github_issue_2001_discussion*
