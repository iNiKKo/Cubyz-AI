# [issues/issue_1679.md] - Issue #1679 discussion

**Type:** review
**Keywords:** Zig update, maintenance, centralization, dependency, patching, standard library
**Symbols:** render.zig, fmt.zig, test_runner.zig
**Concepts:** dependency management, code organization, standard library integration

## Summary
Discussion about moving Zig copy-pasted files to a separate repository for easier maintenance and dependency management.

## Explanation
The issue report highlights the annoyance of maintaining multiple Zig files scattered across different locations, particularly after updates. The maintainer is seeking a centralized approach to manage these files more efficiently. There's also a desire to use `render.zig` without modifying the standard library, suggesting a need for a cleaner integration method.

## Related Questions
- Where are the current locations of `render.zig`, `fmt.zig`, and `test_runner.zig`?
- How can we centralize these Zig files into a separate repository?
- What is the best way to include these files as dependencies in the main game?
- Is there a method to use `render.zig` without patching the standard library?
- How will this change affect the build process and dependency resolution?
- Are there any potential compatibility issues with existing code when moving these files?

*Source: unknown | chunk_id: github_issue_1679_discussion*
