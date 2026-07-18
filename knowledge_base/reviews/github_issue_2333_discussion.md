# [issues/issue_2333.md] - Issue #2333 discussion

**Type:** review
**Keywords:** aarch64-windows support, Zig update, translate-c issues, upstream fixes, dependency synchronization
**Symbols:** aarch64-windows, Zig, translate-c
**Concepts:** backwards compatibility, dependency management

## Summary
The issue discusses reenabling aarch64-windows support by updating Zig to a newer version that includes fixes for upstream issues.

## Explanation
The discussion revolves around enabling aarch64-windows support in Cubyz, which is currently blocked due to unresolved issues in the translate-c library. The user suggests updating Zig to version 0.16.0 dev 2565, as the relevant issues have been closed upstream. However, the maintainer notes that Zig's master branch has not yet incorporated these fixes from translate-c, indicating a delay in the update process.

## Related Questions
- What is the current status of Zig's translate-c code in relation to the upstream fixes?
- When is the expected release date for Zig version 0.16.0 dev 2565?
- How can we ensure that Cubyz remains compatible with future updates to Zig and its dependencies?
- What are the potential risks associated with updating Zig to a development version?
- Is there a timeline for when Zig's master branch will incorporate the translate-c fixes?
- How does the reenabling of aarch64-windows support impact Cubyz's build process?

*Source: unknown | chunk_id: github_issue_2333_discussion*
