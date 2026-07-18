# [issues/issue_1659.md] - Issue #1659 discussion

**Type:** review
**Keywords:** filtering, block tag, item tag, creative inventory, zon files, leading `.`
**Concepts:** user experience, search functionality, tag-based filtering

## Summary
The issue proposes adding functionality to filter items and blocks by tags in the creative inventory, using a leading `.` similar to zon files. The maintainer suggests checking both item and block tags.

## Explanation
This change aims to enhance player usability by allowing them to search for items based on their tags, which can be particularly useful for organizing and finding specific types of items or blocks. The proposal introduces a new filtering mechanism that distinguishes tag-based searches from regular searches through the use of a leading `.` character. This is consistent with how tags are handled in zon files, suggesting a familiar interface for players. The maintainer's comment emphasizes the importance of checking both item and block tags to ensure comprehensive search results.

## Related Questions
- How does the current search functionality in the creative inventory work?
- What is the proposed syntax for filtering items by tags?
- Why was a leading `.` chosen to indicate tag-based searches?
- How will the implementation ensure that both item and block tags are checked?
- Are there any potential performance implications of adding this feature?
- How will this change be tested to ensure it doesn't break existing functionality?

*Source: unknown | chunk_id: github_issue_1659_discussion*
