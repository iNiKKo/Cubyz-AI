# [issues/issue_3177.md] - Issue #3177 discussion

**Type:** review
**Keywords:** custom procedural tool, server recognition, hallucination, steps to reproduce, observed behavior
**Concepts:** client-server architecture, procedural content generation

## Summary
The issue reports that the game accepts a custom procedural tool created by copying an existing one, but the maintainer disputes this claim.

## Explanation
The issue reports that a custom procedural tool created by copying an existing one is accepted by the game, but the maintainer disputes this claim. The maintainer's comment explicitly states: 'No it doesn't. Your client is just hallucinating that it works.' This implies that while the client might report success in creating and using the custom procedural tool, the server does not actually recognize or process it correctly.

## Related Questions
- What is the expected behavior when a custom procedural tool is created by copying an existing one?
- How does the server verify the recognition of a custom procedural tool?
- Are there any known issues with client-side hallucinations in this context?
- Can you provide more details on the steps to reproduce the issue?
- What logs or error messages should be checked to diagnose the problem?
- Is there a way to ensure that the server correctly processes custom procedural tools?

*Source: unknown | chunk_id: github_issue_3177_discussion*
