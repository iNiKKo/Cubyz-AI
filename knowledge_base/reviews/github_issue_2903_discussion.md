# [issues/issue_2903.md] - Issue #2903 discussion

**Type:** review
**Keywords:** formatter, tabs in comments, commenting efficiency, out of scope, multi-cursor, zig maintainers
**Concepts:** code formatting, commenting, multi-cursor

## Summary
The issue discusses the need for the Zig formatter to move tabs in comments to before the start of the comment, improving the efficiency of commenting out large blocks of code. The maintainers have declined this feature request, citing it as out of scope and suggesting alternative methods like using multi-cursor.

## Explanation
The issue discusses a request for the Zig formatter to move tabs in comments to before the start of the comment, aiming to improve the efficiency of commenting out large blocks of code. The maintainers have declined this feature request, stating that it is not within the scope of the formatter and referencing another issue (#2148) as a potential solution. They also suggest using multi-cursor functionality with the `Pos1` button to toggle cursor positions between the start of the line and the end of the indentation for efficient commenting.

## Related Questions
- What is the current behavior of the Zig formatter when commenting out multiple lines?
- Why have the maintainers declined to implement tabs in comments for the formatter?
- What alternative methods does the maintainer suggest for efficient code commenting in Zig?

*Source: unknown | chunk_id: github_issue_2903_discussion*
