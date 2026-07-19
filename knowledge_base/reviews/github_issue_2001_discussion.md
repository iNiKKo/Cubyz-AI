# [issues/issue_2001.md] - Issue #2001 discussion

**Type:** review
**Keywords:** menu background rendering, framebuffer update, FOV change, halved FPS, UI open
**Symbols:** framebuffer, FOV
**Concepts:** performance optimization, rendering pipeline

## Summary
The menu background rendering is proposed to be split into two separate functions to prevent unnecessary framebuffer updates when changing the FOV.

## Explanation
The menu background rendering currently involves recreating the game's frame buffer twice per frame, which is unnecessary and could be optimized by splitting the function into two separate functions. This optimization would prevent redundant operations in the rendering pipeline, potentially leading to performance improvements. The discussion took place at https://github.com/PixelGuys/Cubyz/pull/1976#discussion_r2427322898.

The reviewer suggests that updating the framebuffer should not occur every time the Field of View (FOV) changes, as this could lead to performance issues such as halved FPS when the UI is open. However, the maintainer confirms that changing the FOV does not actually cause halved FPS with the UI open.

Splitting the function into two separate functions would involve separating the logic for updating the framebuffer from the logic for rendering the menu background. This separation would prevent unnecessary framebuffer updates when only the FOV changes, thus optimizing performance without introducing any potential side effects.

Here is a proposed code snippet showing how the function could be split:
```c
void updateFramebuffer() {
    // Update framebuffer logic here
}

void renderMenuBackground() {
    // Render menu background logic here
}
```

To verify the FPS improvement, a test case can be created that measures the frame rate before and after implementing the change. This will help ensure that the optimization has the desired effect on performance.

## Related Questions
- What is the impact of changing FOV on framebuffer updates?
- How does splitting the function improve performance?
- Are there any potential side effects from this change?
- Can you provide a code snippet showing the proposed changes?
- How does this affect the rendering pipeline overall?
- Is there a test case for verifying the FPS improvement?

*Source: unknown | chunk_id: github_issue_2001_discussion*
