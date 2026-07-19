# [issues/issue_1212.md] - Issue #1212 discussion

**Type:** review
**Keywords:** cubic selection wand, creative inventory, visualize selections, aiming and clicking, mid air selection, better outline/texture
**Concepts:** user experience, world editing, selection tool

## Summary
The issue discusses the introduction of a cubic selection wand in Cubyz for more convenient world editing. The wand should be obtainable only through creative inventory, visualize selections, and allow users to select blocks by aiming and clicking.

## Explanation
This issue aims to enhance the user experience in world editing by introducing a selection wand that simplifies the process of selecting cubic regions. The wand will be obtainable only through creative inventory, visualize selections, and allow users to select blocks by aiming and clicking. The basic functionality involves setting `pos1` and `pos2` using commands, but the goal is to introduce a more intuitive method for selection. When holding the wand, it should outline the block being aimed at, with air blocks selecting the last air block in range and solid blocks selecting the first solid block in range. Right-clicking with the wand starts the selection at the current aim point and updates `pos2` as the player changes their aim until right-clicked again to complete the selection. The selection should be visualized as a wireframe in real-time. While mid-air selection and better visualization are mentioned as potential future enhancements, they are not part of the basic implementation.

## Related Questions
- What is the current status of the cubic selection wand implementation?
- Are there any plans to add mid-air selection functionality?
- How does the selection wand visualize selections in real-time?
- Is the selection wand only available through creative inventory?
- What are the future enhancements planned for the selection wand?
- How does the selection wand handle air blocks compared to solid blocks?

*Source: unknown | chunk_id: github_issue_1212_discussion*
