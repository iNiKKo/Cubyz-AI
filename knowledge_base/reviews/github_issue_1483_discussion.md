# [issues/issue_1483.md] - Issue #1483 discussion

**Type:** review
**Keywords:** launcher, main menu, separate process, world switching, asset loading, state bleeding, settings update, developer experience, file watching, Vulkan rewrite
**Concepts:** state management, asset loading, process separation, multi-version handling, file watching

## Summary
The discussion revolves around moving the main menu to the launcher and starting the game in a separate process when opening a world or connecting to multiplayer. Pros include avoiding state bleeding bugs, simplifying asset loading, and faster world exits. Cons involve slower world switching, increased cost of world loading, and potential difficulties with multi-version handling.

## Explanation
The proposal aims to improve the game's architecture by separating the main menu into a launcher, which would start the game in a separate process upon specific actions like opening a world or connecting to multiplayer. This change is expected to reduce bugs related to state management and simplify asset loading since the game process can be closed without performing cleanup logic. Additionally, it could lead to a more responsive GUI during loading times. However, this approach might slow down world switching as users would need to close the game and switch to the launcher window. World loading could also become more expensive because less work can be done upfront. Multi-version handling might become more complex since the launcher needs to tightly match with the base game. The discussion also touches on how settings would be updated, suggesting shared settings windows that actively save changes and watch for file modifications. There are concerns about the developer experience, particularly regarding whether recompilation of the launcher is necessary. The maintainers suggest distributing the launcher separately but acknowledge potential issues with file watching on macOS, which might require polling solutions until a rewrite with Vulkan is implemented.

## Related Questions
- How would the launcher detect changes in settings and apply them?
- What are the potential performance impacts of starting a new process for each world load?
- How can we ensure that the launcher remains responsive while monitoring file changes on macOS?
- What are the implications of making the launcher and game the same executable with different arguments?
- How would the multiplayer functionality be affected by this architectural change?
- What steps should be taken to prevent regressions in asset loading due to process separation?

*Source: unknown | chunk_id: github_issue_1483_discussion*
