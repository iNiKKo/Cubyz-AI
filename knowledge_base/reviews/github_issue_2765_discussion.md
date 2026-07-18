# [issues/issue_2765.md] - Issue #2765 discussion

**Type:** review
**Keywords:** ctrl+select, ctrl+delete, underscore, word separation, resource IDs, intuitive behavior
**Concepts:** text selection, keyboard shortcuts, word boundaries

## Summary
Discussion on handling underscore '_' as a word separator in text selection features like ctrl+select and ctrl+delete.

## Explanation
The issue revolves around the behavior of text selection when using keyboard shortcuts like ctrl+shift+left arrow or ctrl+delete. The primary concern is whether underscores should be treated as part of words or as spaces. According to the maintainer, the current implementation treats underscores as part of words, especially in resource IDs, allowing for quicker modifications. Users argue that treating underscores as spaces aligns with common practices in code editors and browsers, making it more intuitive for non-programmers. The maintainer also notes that most people are not aware of this nuance outside of programming contexts.

## Related Questions
- What is the current implementation of underscore handling in text selection features?
- How does treating underscores as spaces affect user experience for non-programmers?
- Are there any performance implications of changing underscore handling in text editors?
- What are the potential regressions if underscores are treated as part of words?
- How do other popular code editors and browsers handle underscore separation in text selection?
- What is the impact on backwards compatibility when changing underscore handling?

*Source: unknown | chunk_id: github_issue_2765_discussion*
