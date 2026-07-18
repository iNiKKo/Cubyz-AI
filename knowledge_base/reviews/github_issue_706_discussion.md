# [issues/issue_706.md] - Issue #706 discussion

**Type:** review
**Keywords:** block placement, chunk border, missing face, remeshing, separate thread, visual artifacts
**Concepts:** thread safety, performance

## Summary
The issue of a missing face when placing a block at a chunk border due to neighbor chunk meshes not being uploaded in the same frame has been addressed by ensuring remeshing happens on a separate thread.

## Explanation
The original problem was caused by the delay in uploading neighbor chunk meshes, which led to visual artifacts like missing faces when blocks were placed near chunk borders. The solution involves moving the remeshing process to a separate thread, reducing the likelihood of such issues occurring. This change leverages multi-threading to improve performance and ensure smoother rendering.

## Related Questions
- How does the remeshing process work in Cubyz?
- What is the impact of multi-threading on rendering performance in Cubyz?
- Are there any potential thread safety issues with the new remeshing approach?
- How can we verify that neighbor chunk meshes are being uploaded correctly?
- What steps should be taken to ensure backward compatibility with older versions?
- Is there a way to test for visual artifacts after implementing this change?

*Source: unknown | chunk_id: github_issue_706_discussion*
