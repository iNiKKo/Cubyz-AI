# [issues/issue_2033.md] - Issue #2033 discussion

**Type:** review
**Keywords:** music file, OGG, asset path, Linux Mint, issue #1785
**Concepts:** asset management, file path resolution

## Summary
The game fails to load a custom music OGG file from the specified path, despite it being present. The issue occurs on Linux Mint 22.1 Xia and is related to an oversight in handling asset paths.

## Explanation
The user reports that the game does not find a custom music file named 'funny.ogg' in the specified directories ('assets/funny/music/funny.ogg' and 'serverAssets/funny/music/funny.ogg'), even though the file exists. The maintainer notes this is related to an oversight mentioned in issue #1785, suggesting that there might be a bug or incorrect handling of asset paths in the game's codebase. Additionally, the user mentions that adding the mod as a global mod (in the assets folder next to the executable) allows the custom music to play, but this method may not work for multiplayer scenarios.

## Related Questions
- What is the current implementation for resolving asset paths in Cubyz?
- Are there any known issues with file path resolution on Linux systems?
- How does Cubyz handle global mods versus local mods in terms of asset loading?
- Is there a specific function or module responsible for loading music files in Cubyz?
- What changes were made in issue #1785 that might be related to this oversight?
- Are there any logs or error messages that could provide more insight into why the file is not being found?

*Source: unknown | chunk_id: github_issue_2033_discussion*
