# [issues/issue_706.md] - Issue #706 discussion

**Type:** review
**Keywords:** block placement, chunk border, missing face, remeshing, separate thread, visual artifacts
**Concepts:** thread safety, performance

## Summary
The issue of a missing face when placing a block at a chunk border due to neighbor chunk meshes not being uploaded in the same frame has been addressed by ensuring remeshing happens on a separate thread.

## Explanation
The issue of a missing face when placing a block at a chunk border due to neighbor chunk meshes not being uploaded in the same frame has been addressed. The original problem was caused by delays in uploading neighbor chunk meshes, leading to visual artifacts like missing faces near chunk borders. The solution involves moving the remeshing process to a separate thread, which significantly reduces the likelihood of such issues occurring. Since this change now happens on a separate thread, the maintainer has commented that we can close this issue as it is much less likely to occur.

## Related Questions
- How does the remeshing process work in Cubyz?
- What is the impact of multi-threading on rendering performance in Cubyz?
- Are there any potential thread safety issues with the new remeshing approach?
- How can we verify that neighbor chunk meshes are being uploaded correctly?
- What steps should be taken to ensure backward compatibility with older versions?
- Is there a way to test for visual artifacts after implementing this change?

*Source: unknown | chunk_id: github_issue_706_discussion*
