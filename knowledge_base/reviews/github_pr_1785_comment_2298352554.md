# [src/gui/windows/save_selection.zig] - Chunk 2298352554

**Type:** review
**Keywords:** realpathAlloc, deprecation, std.fs.Path, openDirInWindow, cubyzDir, issue #1351, canonicalize, allocation, catch unreachable, symlink resolution
**Symbols:** openFolder, main.files.openDirInWindow, main.files.cubyzDir, realpathAlloc
**Concepts:** thread safety, backwards compatibility, memory leak prevention, standard library deprecation, path canonicalization

## Summary
The change replaces a direct call to main.files.openDirInWindow with a path resolution using realpathAlloc before opening the directory.

## Explanation
The reviewer flagged that realpathAlloc is problematic because it is slated for removal from Zig's standard library (see issue #1351). By inserting a realpathAlloc call, the code now attempts to resolve symlinks and canonicalize the path at runtime. This introduces several concerns: 1) It may break backwards compatibility if future versions of std.fs.Path.realpathAlloc change behavior or are removed entirely; 2) It adds an extra allocation step that could affect performance in tight loops; 3) If realpathAlloc fails, the catch unreachable assumes success, which is risky given the planned removal. The architectural reasoning suggests that relying on a function known to be deprecated is poor practice and should be refactored to use a more stable API or handle path resolution differently (e.g., using std.fs.path.join with explicit canonicalization later).

## Related Questions
- What is the current status of realpathAlloc in Zig's standard library?
- Are there any alternative APIs recommended for path canonicalization before realpathAlloc removal?
- How does main.files.cubyzDir() construct its base directory path?
- What happens if realpathAlloc fails and the catch unreachable is hit?
- Is openDirInWindow expected to handle relative or absolute paths differently?
- Could replacing realpathAlloc with std.fs.path.join cause any regressions in existing tests?
- Where is issue #1351 referenced, and what specific changes does it propose?
- Does the codebase already have a custom path resolution utility that could replace realpathAlloc?
- What performance impact might adding realpathAlloc have on save_folder operations?
- Is there any documentation or comment in main.files explaining why openDirInWindow is used this way?

*Source: unknown | chunk_id: github_pr_1785_comment_2298352554*
