# [issues/issue_3115.md] - Issue #3115 discussion

**Type:** review
**Keywords:** argparse, unlimited arguments, help command, multiple arguments, feature necessity
**Concepts:** argument parsing, command-line interface

## Summary
Discussion about adding array/slice support to argparse, with clarification that some commands already accept multiple arguments.

## Explanation
The discussion centers around adding support for an unlimited number of arguments to argparse. The maintainer initially questioned whether commands like 'help' accept multiple arguments, but a user clarified that `/help time invite` works as expected and prints the help information for both `time` and `invite`. This example demonstrates that certain commands can indeed handle multiple arguments. However, the maintainer still expressed doubt about the necessity of this feature.

## Related Questions
- How does the current argparse handle multiple arguments?
- What specific example shows that 'help' supports multiple arguments?
- Why did the maintainer question the need for supporting unlimited arguments?

*Source: unknown | chunk_id: github_issue_3115_discussion*
