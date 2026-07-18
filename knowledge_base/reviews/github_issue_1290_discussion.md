# [issues/issue_1290.md] - Issue #1290 discussion

**Type:** review
**Keywords:** inventory storage, binary format, BaseItem indexes, tool palette, memory efficiency, human-readable, server moderation, permissions, cheats disabled, file system access
**Symbols:** Item, BaseItem, BaseItemIndex, Tool, craftingGrid, materialGrid
**Concepts:** backwards compatibility, memory usage reduction, human-readable data, item migrations

## Summary
The discussion revolves around changing the inventory storage format to binary while retaining backwards compatibility, and considering changes to how items and tools are stored to reduce memory usage.

## Explanation
The discussion revolves around changing the inventory storage format to binary while retaining backwards compatibility. The current storage of inventories as Zon files is inefficient for larger inventories like chests, especially when considering items and tools. Proposals include using `BaseItem` indexes instead of string names for item migrations and adding a tool palette with similar considerations. Human-readable inventory data remains important for server hosts due to its utility in tasks such as searching for and removing illegal/cheated items, migrating player inventories, and setting gamemodes with cheats disabled. Specific commands mentioned include `/inventory open <player-query>#hand`, `/inventory clone <player-query>#hand`, `/inventory clear <player-query>#hand`, `/permissions set <player-query> #admin enabled`, `/permissions set <player-query> @worldedit enabled`, and `/permissions set <player-query> /set enabled`. Memory usage reduction is highlighted as a significant benefit, particularly for tools stored in crafting grids and material grids. The change from u64 to u16 would reduce memory usage 4 times on 64-bit systems.

## Related Questions
- What are the potential benefits and drawbacks of changing inventory storage to binary format?
- How would changing `Item` to use `BaseItemIndex` instead of pointers affect memory usage?
- What is the impact on memory usage if `Tool` uses `BaseItemIndex` instead of pointers?
- Why is human-readable inventory data important for server hosts?
- How can item migrations be effectively managed with the proposed changes?
- What are the long-term implications of decoupling server moderation from physical access to the file system?
- What specific commands and permissions are required for managing player inventories and gamemodes?

*Source: unknown | chunk_id: github_issue_1290_discussion*
