# [issues/issue_3115.md] - Issue #3115 discussion

**Type:** review
**Keywords:** argparse, unlimited arguments, help command, multiple arguments, feature necessity
**Concepts:** argument parsing, command-line interface

## Summary
Discussion about adding array/slice support to argparse, with clarification that some commands already accept multiple arguments.

## Explanation
The discussion revolves around the necessity of adding support for an unlimited number of arguments in the argument parser. The maintainer initially questioned the need for this feature, but a user clarified that certain commands like 'help' can already handle multiple arguments (e.g., `/help time invite`). This clarification suggests that the current implementation might be more flexible than initially perceived.

## Related Questions
- How does the current argparse handle multiple arguments?
- What commands in Cubyz currently support multiple arguments?
- Why was there a misunderstanding about the 'help' command's argument handling?
- Is there a need to standardize how commands handle multiple arguments?
- Could adding array/slice support improve the flexibility of argparse?
- Are there any potential performance implications of supporting unlimited arguments?

*Source: unknown | chunk_id: github_issue_3115_discussion*
