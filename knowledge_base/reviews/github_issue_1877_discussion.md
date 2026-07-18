# [issues/issue_1877.md] - Issue #1877 discussion

**Type:** review
**Keywords:** chest locks, collaborative gameplay, unauthorized access, protector block, issue #81
**Concepts:** thread safety, backwards compatibility

## Summary
Discussion on implementing trivial locks for chests to prevent unauthorized access during collaborative gameplay.

## Explanation
Discussion on implementing trivial locks for chests to prevent unauthorized access during collaborative gameplay. Maintainers express concerns about the necessity of this feature after another issue (#81) is addressed, which might mitigate the problem. There's also mention of a protector block that could potentially lock containers and protect all chest inventories (and probably other block entity state) in the protected area unless configured otherwise.

## Related Questions
- Can you provide a detailed explanation of how the protector block will lock containers, including its impact on chest inventories and other block entity states?

*Source: unknown | chunk_id: github_issue_1877_discussion*
