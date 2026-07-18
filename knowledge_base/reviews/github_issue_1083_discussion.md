# [issues/issue_1083.md] - Issue #1083 discussion

**Type:** review
**Keywords:** zig fmt, zon files, CI, 0.14.0, code conventions, tabs
**Concepts:** code formatting, continuous integration (CI), version control

## Summary
Discussion about running `zig fmt` on all zon files in the CI, with a maintainer comment indicating that it's possible but requires waiting for `zig fmt` to support zon files in version 0.14.0.

## Explanation
The issue report suggests that only tabs differ between the current code and the formatting expected by `zig fmt`, which could be easily adjusted before running the check. The maintainer confirms that it is feasible to implement this change but notes that it will need to wait until version 0.14.0 of `zig fmt` adds support for zon files. This indicates a planned enhancement in the tooling that will facilitate better code formatting and consistency across the project.

## Related Questions
- What is the current status of `zig fmt` support for zon files?
- When is version 0.14.0 of `zig fmt` expected to be released?
- How can we adjust tabs before running `zig fmt` in the CI?
- Are there any other formatting tools that support zon files?
- What are the benefits of using `zig fmt` for code formatting?
- How will this change impact the overall codebase consistency?

*Source: unknown | chunk_id: github_issue_1083_discussion*
