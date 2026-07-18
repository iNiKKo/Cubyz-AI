# [issues/issue_1679.md] - Issue #1679 discussion

**Type:** review
**Keywords:** Zig update, maintenance, centralization, dependency, patching, standard library
**Symbols:** render.zig, fmt.zig, test_runner.zig
**Concepts:** dependency management, code organization, standard library integration

## Summary
Discussion about moving Zig copy-pasted files to a separate repository for easier maintenance and dependency management.

## Explanation
The issue report discusses moving several Zig copy-pasted files (`render.zig`, `fmt.zig`, and `test_runner.zig`) to a separate repository for easier maintenance. The maintainer notes that after recent updates, managing these scattered files has become cumbersome. Centralizing them would simplify the update process and reduce unnecessary commits. Additionally, there is a desire to use `render.zig` without in-place patching of the standard library, suggesting a need for better integration methods.

## Related Questions
- Where are the current locations of `render.zig`, `fmt.zig`, and `test_runner.zig`?
- How can we centralize these Zig files into a separate repository?
- What is the best way to include these files as dependencies in the main game?
- Is there a method to use `render.zig` without patching the standard library?

*Source: unknown | chunk_id: github_issue_1679_discussion*
