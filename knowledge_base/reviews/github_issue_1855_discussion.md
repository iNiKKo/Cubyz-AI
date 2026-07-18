# [issues/issue_1855.md] - Issue #1855 discussion

**Type:** review
**Keywords:** @select, deflate compressor, Zig version, issue_1855.md, issue_1854
**Concepts:** binary operations, boolean vectors, Zig language updates

## Summary
The issue discusses replacing the `@select` workaround with binary operations for bool vectors in Cubyz, pending an update to a newer Zig version that includes the necessary features.

## Explanation
The discussion revolves around updating the codebase to use binary operations instead of the `@select` workaround for handling boolean vectors. The maintainer notes that upgrading to Zig version 0.15.1 is not feasible due to the missing deflate compressor, and a newer version update is being tracked separately in issue #1854.

## Related Questions
- What is the current status of updating to Zig version 0.15.1?
- Why can't we update to Zig version 0.15.1 in this project?
- What are the planned changes for handling boolean vectors in Cubyz?
- Is there a timeline for resolving issue #1854 related to Zig updates?
- How does the `@select` workaround affect performance in current implementations?
- What are the benefits of using binary operations instead of `@select` for bool vectors?

*Source: unknown | chunk_id: github_issue_1855_discussion*
