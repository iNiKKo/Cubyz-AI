# [issues/issue_1321.md] - Issue #1321 discussion

**Type:** review
**Keywords:** build-exe, X11, Wayland, verbose-link, global cache, debug build, stack trace, setup issue
**Symbols:** Cubyz, zig, debug_linux.sh, .cache/zig, Cubyz/.zig-cache
**Concepts:** build system, caching, debugging, compiler issues

## Summary
Discussion about Cubyz build issues, focusing on cache deletion and Zig compiler debug builds.

## Explanation
The discussion revolves around troubleshooting build failures in Cubyz, particularly related to the Zig compiler. The maintainer asks for detailed information about the user's setup, including screenshots of directories and the presence of caches. The user provides suggestions to run scripts with verbose output and delete caches. The maintainer then recommends using a debug build of the Zig compiler to gather more information if the issue persists. Ultimately, due to lack of sufficient data, the maintainer closes the issue, suggesting the user reopen it with new information if the problem continues.

## Related Questions
- What is the purpose of the `zig build-exe` command in Cubyz?
- How does deleting the `.cache/zig` and `Cubyz/.zig-cache` directories affect the build process?
- Why might a debug build of the Zig compiler provide more information about build failures?
- Can running `./debug_linux.sh --verbose --verbose-link` help identify the directory causing issues?
- What are the potential implications of using a debug build of the Zig compiler for production builds?
- How does Cubyz handle different display servers (X11 vs. Wayland)?

*Source: unknown | chunk_id: github_issue_1321_discussion*
