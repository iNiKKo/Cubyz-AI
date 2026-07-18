# [src/gui/windows/save_selection.zig] - PR #1785 review diff

**Type:** review
**Keywords:** realpathAlloc, openDirInWindow, path resolution, deprecation, standard library, file system, architecture
**Symbols:** openFolder, path, main.stackAllocator.allocator, worldList.items[index].fileName, main.files.openDirInWindow, globalPath, main.files.cubyzDir().dir.realpathAlloc
**Concepts:** file path resolution, deprecation of standard library functions, architectural stability

## Summary
The code replaces `openDirInWindow` with a call to `realpathAlloc`, which is intended to resolve file paths. However, this change introduces potential issues as `realpathAlloc` is scheduled for removal from the standard library.

## Explanation
The reviewer points out that using `realpathAlloc` can lead to various problems and is planned to be deprecated, as indicated by issue #1351. This suggests that relying on this function could cause maintenance issues in the future. The architectural concern here is the potential for introducing bugs or compatibility issues if the library changes or removes this functionality. The reviewer's comment highlights the need to consider alternative approaches to path resolution to ensure long-term stability and maintainability of the code.

## Related Questions
- What are the potential issues with using `realpathAlloc` in this context?
- How can we refactor the code to avoid relying on a deprecated function?
- Are there alternative functions or methods available for resolving file paths in Zig?
- What is the impact of removing `realpathAlloc` from the standard library on our project?
- How can we ensure that our code remains compatible with future versions of the Zig standard library?
- What are the benefits and drawbacks of using `realpathAlloc` compared to other path resolution methods?

*Source: unknown | chunk_id: github_pr_1785_comment_2298352554*
