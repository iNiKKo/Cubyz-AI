# [issues/issue_2844.md] - Issue #2844 discussion

**Type:** review
**Keywords:** chat message, command execution, /, ., \, prefix checking
**Concepts:** command parsing, chat message handling

## Summary
Discussion about chat message commands in Cubyz, focusing on the use of '/' at the beginning.

## Explanation
The issue revolves around the handling of chat messages that start with a '/'. The maintainer initially suggests using '//' or './foobar', but the user points out that the current implementation only checks if the first character is a '/' and then executes the command. This indicates a potential oversight in the command parsing logic, as it might not handle other common prefixes like '.' or '\'. The discussion highlights the need to ensure robust command execution based on different prefixes.

## Related Questions
- What is the current implementation for command execution in chat messages?
- How does Cubyz handle different prefixes in chat commands?
- Is there a plan to support additional prefixes like '.' or '\' in future updates?
- What are the potential security implications of allowing multiple command prefixes?
- Can you provide more details on how the command parsing logic works in Cubyz?
- Are there any known issues with the current command execution mechanism?

*Source: unknown | chunk_id: github_issue_2844_discussion*
