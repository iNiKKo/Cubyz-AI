# [issues/issue_1262.md] - Issue #1262 discussion

**Type:** review
**Keywords:** test placement, unit test, BinaryReader, Writer, maintainer guidelines, code structure
**Symbols:** BinaryReader, Writer
**Concepts:** unit testing, code organization

## Summary
The issue discusses adding a simple test for the BinaryReader/Writer to ensure proper functionality across supported data types.

## Explanation
The discussion revolves around the placement rules for tests. The maintainer suggests that tests should be placed in the same file as the code they are testing, either immediately below the tested function or at the end of the file. This approach aims to keep related code and its tests together, improving maintainability and traceability.

## Related Questions
- What are the rules for placing tests in the Cubyz codebase?
- Why is it recommended to place tests in the same file as the code they test?
- How should tests be organized within a file according to the maintainer's guidelines?
- Can you provide examples of how tests are currently structured in the Cubyz codebase?
- What are the benefits of keeping tests and code together in the same file?
- Are there any specific tools or frameworks used for writing unit tests in Cubyz?

*Source: unknown | chunk_id: github_issue_1262_discussion*
