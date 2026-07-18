# [issues/issue_3130.md] - Issue #3130 discussion

**Type:** review
**Keywords:** List Initialization, Standard Library, Alias Removal, Pull Request #3205, Maintainer Comment
**Symbols:** .empty, {}
**Concepts:** Code Consistency, Initialization Methods

## Summary
The issue discusses switching from using `.{} to use `.empty` for initializing lists with default values.

## Explanation
The discussion revolves around updating the codebase to utilize the `.empty` method instead of the old standard library way represented by `.{}`. The maintainer reopened the issue due to a temporary alias that was added but later removed in pull request #3205. This change aims to improve consistency and clarity in list initialization.

## Related Questions
- What was the reason for removing the temporary alias in PR #3205?
- How does using `.empty` differ from using `.{}` in list initialization?
- Is there any performance impact expected from switching to `.empty`?
- Are there any backward compatibility concerns with this change?
- Who reopened the issue and why?
- What is the purpose of maintaining consistency in list initialization methods?

*Source: unknown | chunk_id: github_issue_3130_discussion*
