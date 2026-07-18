# [issues/issue_2903.md] - Issue #2903 discussion

**Type:** review
**Keywords:** formatter, tabs in comments, commenting efficiency, out of scope, multi-cursor, zig maintainers
**Concepts:** code formatting, commenting, multi-cursor

## Summary
The issue discusses the need for the Zig formatter to move tabs in comments to before the start of the comment, improving the efficiency of commenting out large blocks of code. The maintainers have declined this feature request, citing it as out of scope and suggesting alternative methods like using multi-cursor.

## Explanation
The issue highlights a common frustration among developers when trying to comment out multiple lines of code in Zig, where editors typically create a straight line of double slashes instead of respecting tabs. The maintainers have declined this feature request, stating that it is not within the scope of the formatter and referencing another issue (#2148) as a potential solution. They also suggest using multi-cursor functionality as an alternative method for commenting out code efficiently.

## Related Questions
- What is the current behavior of the Zig formatter when commenting out multiple lines?
- Why have the maintainers declined to implement tabs in comments for the formatter?
- What alternative methods does the maintainer suggest for efficient code commenting in Zig?
- Is there any ongoing discussion or potential solutions for implementing tabs in comments in future versions of Zig?
- How can developers improve their workflow when commenting out large blocks of code in Zig?
- Are there any plans to expand the scope of the formatter to include more features like tabs in comments?

*Source: unknown | chunk_id: github_issue_2903_discussion*
