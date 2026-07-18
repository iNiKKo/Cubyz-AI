# [issues/issue_1321.md] - Issue #1321 discussion

**Type:** review
**Keywords:** build-exe, X11, Wayland, verbose-link, global cache, debug build, stack trace, setup issue
**Symbols:** Cubyz, zig, debug_linux.sh, .cache/zig, Cubyz/.zig-cache
**Concepts:** build system, caching, debugging, compiler issues

## Summary
Discussion about Cubyz build issues, focusing on cache deletion and Zig compiler debug builds.

## Explanation
The discussion revolves around troubleshooting build failures in Cubyz, particularly related to the Zig compiler. The maintainer asks for detailed information about the user's setup, including screenshots of directories and the presence of caches. The user provides suggestions to run scripts with verbose output using `./debug_linux.sh --verbose --verbose-link` before and after deleting the `.cache/zig` and `Cubyz/.zig-cache` directories. The maintainer then recommends using a debug build of the Zig compiler to gather more information if the issue persists, as it will provide a stack trace when built in debug mode. Ultimately, due to lack of sufficient data, the maintainer closes the issue, suggesting the user reopen it with new information if the problem continues.

## Related Questions
- What is the purpose of running `./debug_linux.sh --verbose --verbose-link`?
- How does deleting all caches including `.cache/zig` affect the build process?
- Why might a debug build of the Zig compiler provide more information about build failures?

*Source: unknown | chunk_id: github_issue_1321_discussion*
