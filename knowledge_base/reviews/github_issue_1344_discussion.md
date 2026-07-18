# [issues/issue_1344.md] - Issue #1344 discussion

**Type:** review
**Keywords:** isServerSide, conn.user, PR #1298, maintainer, conflicts
**Concepts:** code refactoring, merge conflicts, pull requests

## Summary
The maintainer plans to create a pull request using `isServerSide` instead of checking if `conn.user != null`, but will wait until the previous PR (#1298) is merged to avoid conflicts.

## Explanation
The discussion revolves around improving the code by replacing a specific condition (`conn.user != null`) with a more appropriate flag (`isServerSide`). The maintainer acknowledges that this change should be made but will defer its implementation until another related pull request is finalized to prevent merge conflicts. This approach ensures that changes are integrated smoothly without introducing potential issues from concurrent modifications.

## Related Questions
- What is the purpose of using `isServerSide` instead of checking if `conn.user != null`?
- Why does the maintainer want to wait until PR #1298 is merged before making this change?
- How might merge conflicts arise from integrating changes concurrently?
- Can you explain the benefits of using `isServerSide` in this context?
- What are the potential drawbacks of deferring code refactoring until after another PR is merged?
- How does the maintainer ensure that the new implementation will be correct and maintainable?

*Source: unknown | chunk_id: github_issue_1344_discussion*
