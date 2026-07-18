# [issues/issue_1393.md] - Issue #1393 discussion

**Type:** review
**Keywords:** block outline, glLineWidth, driver support, visibility, rendering
**Concepts:** Graphics Rendering, Driver Compatibility, Visibility

## Summary
The issue discusses making the block outline more visible by thickening it or using an alternative display method due to poor support of `glLineWidth` on some drivers.

## Explanation
The current implementation of the block outline is criticized for being too thin (1-pixel wide), which can be difficult to see, particularly at lower resolutions. The discussion highlights that using `glLineWidth` to increase the line width is not a viable solution because it is poorly supported on some graphics drivers. This suggests that alternative methods for displaying the block outline need to be explored to ensure compatibility and visibility across different hardware configurations.

## Related Questions
- What are the alternative methods proposed for making the block outline more visible?
- Why is `glLineWidth` not a suitable solution for thickening the block outline?
- How can we ensure compatibility across different graphics drivers when implementing changes to the block outline?
- Are there any performance considerations when changing the way the block outline is displayed?
- What impact might this change have on the overall visual quality of the game?
- How will the new block outline display method be tested for cross-platform compatibility?

*Source: unknown | chunk_id: github_issue_1393_discussion*
