# [issues/issue_2153.md] - Issue #2153 discussion

**Type:** review
**Keywords:** Zig update, panic code, stack tracing, debug info stripping, allow_stack_tracing
**Symbols:** b64535e, src/main.zig
**Concepts:** stack trace, debug info, strip module

## Summary
Discussion about updating Cubyz's panic code in `src/main.zig` to support Zig's new ability to toggle stack traces independently of the `strip` module option.

## Explanation
The discussion revolves around the integration of a new feature in Zig, which allows users to control stack trace output separately from the `strip` module. The maintainer asks about the behavior of stack traces when debug information is stripped. The user clarifies that currently, Zig's default stack tracing code will not output stack traces if the debug info is stripped.

## Related Questions
- What changes need to be made in `src/main.zig` to support the new stack trace feature?
- How does the current Zig code handle stack traces when debug info is stripped?
- Can you provide an example of how to use the `allow_stack_tracing` option in Cubyz?
- Is there a risk of introducing regressions when updating the panic code?
- What are the potential performance implications of enabling stack tracing independently of stripping?
- How does this change affect backwards compatibility with older Zig versions?

*Source: unknown | chunk_id: github_issue_2153_discussion*
