# [issues/issue_421.md] - Issue #421 discussion

**Type:** review
**Keywords:** Connection.collectPackets, function removed, performance improvement, issue #419, architectural changes, refactoring efforts
**Symbols:** Connection.collectPackets
**Concepts:** performance optimization, architectural change, refactoring

## Summary
The `Connection.collectPackets` function no longer exists.

## Explanation
The review indicates that the `Connection.collectPackets` function has been removed from the codebase. This change likely addresses performance issues by preventing unnecessary iteration through all packets every time a new packet is received, as originally intended in issue #419. The removal of this function could be due to architectural changes or refactoring efforts aimed at improving efficiency and maintainability.

## Related Questions
- What was the original purpose of `Connection.collectPackets`?
- How did its removal impact performance optimization?
- Are there any other functions that handle packet collection in the current codebase?
- Was this change part of a larger refactoring effort?
- How does the removal of `Connection.collectPackets` affect backwards compatibility?
- What were the architectural reasons behind removing this function?

*Source: unknown | chunk_id: github_issue_421_discussion*
