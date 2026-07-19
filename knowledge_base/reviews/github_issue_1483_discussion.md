# [issues/issue_1483.md] - Issue #1483 discussion

**Type:** review
**Keywords:** launcher, main menu, separate process, world switching, asset loading, state bleeding, settings update, developer experience, file watching, Vulkan rewrite
**Concepts:** state management, asset loading, process separation, multi-version handling, file watching

## Summary
The discussion revolves around moving the main menu to the launcher and starting the game in a separate process when opening a world or connecting to multiplayer. Pros include avoiding state bleeding bugs, simplifying asset loading, and faster world exits. Cons involve slower world switching, increased cost of world loading, and potential difficulties with multi-version handling.

## Explanation
The discussion revolves around moving the main menu to a launcher that starts the game in a separate process when opening a world or connecting to multiplayer. Pros include avoiding state bleeding bugs (e.g., #701), simplifying asset loading, and faster exits since the process can be closed without cleanup logic. This could also lead to a more responsive GUI during loading times with easier implementation of a loading screen. Cons involve slower world switching as users would need to close the game and switch to the launcher window. World loading might become more expensive because less work can be done upfront, such as asset preloading while in the menu. Multi-version handling could also become more complex since the launcher needs to tightly match with the base game (e.g., #227). The maintainers suggest that settings would ideally share a common window and actively save changes to file whenever modified, though this isn't implemented on all platforms yet (particularly macOS). For developer experience, recompilation of the launcher is necessary only when making changes; otherwise, an official distribution should be used. This means the launcher could be distributed separately as a sub-folder in the repository with its own build.zig file. The maintainers also note that macOS players might need to use polling solutions until a rewrite with Vulkan is implemented. Additionally, they suggest that the main menu and launcher could be the same executable launched with different arguments, which would mean the launcher wouldn't really be a separate entity.

## Related Questions
- How would the developer experience be? Would it always need to recompile the launcher first?
- How would settings updates work, especially on platforms like macOS where file watching isn't fully implemented?

*Source: unknown | chunk_id: github_issue_1483_discussion*
