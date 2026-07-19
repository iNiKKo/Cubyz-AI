# [issues/issue_2879.md] - Issue #2879 discussion

**Type:** review
**Keywords:** extra directory, nested directories, save files, FileNotFound, cubyzDir, launchConfig.zon, singleplayer world, game launch, file manager
**Symbols:** launchConfig.zon, test_saves, test_world, world.zig.zon
**Concepts:** directory structure, file management, error handling

## Summary
The issue involves an extra directory being created within the specified save directory, leading to nested directories and causing errors when trying to access save files.

## Explanation
The issue involves an extra directory being created within the specified save directory, leading to nested directories and causing errors when trying to access save files. Specifically, setting `.cubyzDir` to `test_saves` results in a nested `test_saves` directory containing `saves/test_world/assets`. When `.cubyzDir` is set to `saves`, the game creates an additional level of directories such as `saves/saves/saves/test_world/assets`, which leads to errors like `[error]: Couldn't open save saves/saves/world.zig.zon: FileNotFound` when attempting to access the world file.

## Related Questions
- How does the game determine the directory structure for saves?
- What is the expected behavior of `cubyzDir` when setting up save directories?
- Can you provide a code snippet that handles the creation of save directories?
- How does the game handle errors when accessing nested save directories?
- Is there a configuration option to prevent the creation of nested directories?
- What is the impact of nested directories on performance and file management?
- How can we ensure that the game correctly identifies the root save directory?
- Are there any known issues with handling multiple levels of nested directories in Cubyz?
- Can you explain the logic behind the error message `[error]: Couldn't open save saves/saves/world.zig.zon: FileNotFound`?

*Source: unknown | chunk_id: github_issue_2879_discussion*
