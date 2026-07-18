# [issues/issue_1911.md] - Issue #1911 discussion

**Type:** review
**Keywords:** zon files, camelCase, snake_case, CI checks, zig script, assets folder, formatter script
**Symbols:** zon, camelCase, snake_case, CI, zig
**Concepts:** naming conventions, code consistency, continuous integration

## Summary
The issue discusses inconsistent naming conventions (camelCase vs. snake_case) in zon files and proposes solutions to enforce consistency.

## Explanation
The maintainers discuss the inconsistency in naming conventions within zon files, where camelCase and snake_case are used interchangeably. They consider enforcing a single convention through CI checks but note that only a few variables are exposed. A suggestion is made to use an existing zon parser with a zig script to recursively check all keys in `*.zig.zon` files within the assets folder. Additionally, it's proposed to integrate this into an existing formatter script running in the CI.

## Related Questions
- How can we enforce a consistent naming convention in zon files?
- What is the current state of the zon parser and formatter script?
- Can the existing CI checks be modified to include naming convention enforcement?
- How many variables are exposed in the zon files, and why does this matter?
- What is the proposed zig script for checking key consistency, and how will it be integrated into the CI process?
- Are there any potential performance implications of adding a new check to the CI pipeline?

*Source: unknown | chunk_id: github_issue_1911_discussion*
