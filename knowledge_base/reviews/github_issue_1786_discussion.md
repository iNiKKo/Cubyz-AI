# [issues/issue_1786.md] - Issue #1786 discussion

**Type:** review
**Keywords:** cwd(), files.zig, wrapper functions, explicitness, error prone, pull request, file read/write, save access points
**Symbols:** cwd, files.zig
**Concepts:** code clarity, error prevention, maintenance

## Summary
Discussion about removing wrappers over `cwd()` in `files.zig` to improve explicitness and reduce potential errors.

## Explanation
The discussion revolves around the removal of wrapper functions around the `cwd()` system call in the `files.zig` file. The maintainers suggest either extracting references for easier tracking or creating a separate pull request to minimize scope. They also propose touching all file read/write locations to ensure comprehensive migration, which could help verify that all save access points are updated correctly.

## Related Questions
- What are the potential benefits of removing wrappers over `cwd()` in `files.zig`?
- How can touching all file read/write locations help verify migration completeness?
- Why might a separate pull request be preferred to reduce scope?
- What is the purpose of extracting references for easier tracking?
- How does explicitness improve code clarity and maintainability?
- What are the risks associated with not updating all save access points during migration?

*Source: unknown | chunk_id: github_issue_1786_discussion*
