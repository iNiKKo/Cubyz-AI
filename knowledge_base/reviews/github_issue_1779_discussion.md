# [issues/issue_1779.md] - Issue #1779 discussion

**Type:** review
**Keywords:** particles, z plane, clipping, screen size, depth calculation, frustum culling, z-buffer, projection matrix
**Concepts:** depth buffer, camera frustum, projection matrix

## Summary
The issue involves particles clipping at the z plane after traveling a short distance, which appears to be influenced by screen size.

## Explanation
The issue involves particles clipping at the z plane after traveling approximately 70 blocks, which appears to be influenced by screen size. The maintainer notes that the behavior is dependent on the screen size and provides an attachment (https://github.com/user-attachments/assets/b2e03fa0-7fc1-4b0c-8033-1355a4f0270a) for further investigation. This suggests potential issues with how the z-buffer or projection matrix is handled, leading to incorrect depth values causing particles to prematurely clip.

## Related Questions
- What is the current implementation of depth buffer handling in Cubyz?
- How does the projection matrix affect particle rendering distance?
- Are there any known issues with frustum culling in the rendering engine?
- Can you provide a test case that consistently reproduces the clipping issue?
- Is there a relationship between screen resolution and z-buffer precision?
- What changes have been made to the rendering pipeline recently that might affect particle depth calculations?

*Source: unknown | chunk_id: github_issue_1779_discussion*
