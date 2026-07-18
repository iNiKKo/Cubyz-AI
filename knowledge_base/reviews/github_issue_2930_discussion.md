# [issues/issue_2930.md] - Issue #2930 discussion

**Type:** review
**Keywords:** @cImport, deprecation, single .c files, comments, maintainability, best practices
**Concepts:** code organization, documentation

## Summary
The maintainer suggests consolidating all includes into a single C file and adding comments to explain their purposes, as `@cImport` has been deprecated upstream.

## Explanation
The discussion centers on the deprecation of `@cImport`, which was marked for removal due to changes in upstream dependencies. The maintainer proposes centralizing all includes into a single C file and documenting them with comments to enhance maintainability and clarity. This approach aims to align with best practices for code organization and documentation, ensuring that future developers can easily understand the purpose of each include statement.

## Related Questions
- What is the reason behind deprecating `@cImport`?
- How does centralizing includes in one file improve maintainability?
- Why did the maintainer suggest adding comments to explain include purposes?

*Source: unknown | chunk_id: github_issue_2930_discussion*
