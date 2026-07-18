# [issues/issue_1.md] - Issue #1 discussion

**Type:** review
**Keywords:** high coordinates, collision bug, corner precision, issue closure, low priority
**Concepts:** collision detection, precision issues

## Summary
The collision bug at high coordinates (~1.8e7 x/z) was initially reported as fixed, but a new issue arose where passing through blocks at their corners with high precision is possible.

## Explanation
The original collision bug at high coordinates was addressed, but the resolution introduced a new problem where players could pass through blocks when standing exactly on their corner. The maintainer decided to close the issue due to its low priority and youth, suggesting that it may not warrant its own separate issue.

## Related Questions
- What was the original issue with collision at high coordinates?
- How did the fix for the original issue introduce a new problem?
- Why was the new issue considered low priority and not given its own separate issue?
- Are there any plans to address the new precision-related collision issue in the future?
- What is the current status of collision detection at high coordinates in Cubyz?
- How does the precision of player positioning affect collision detection in Cubyz?

*Source: unknown | chunk_id: github_issue_1_discussion*
