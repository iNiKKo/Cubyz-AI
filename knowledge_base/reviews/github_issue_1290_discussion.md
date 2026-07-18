# [issues/issue_1290.md] - Issue #1290 discussion

**Type:** review
**Keywords:** inventory storage, binary format, BaseItem indexes, tool palette, memory efficiency, human-readable, server moderation, permissions, cheats disabled, file system access
**Symbols:** Item, BaseItem, BaseItemIndex, Tool, craftingGrid, materialGrid
**Concepts:** backwards compatibility, memory usage reduction, human-readable data, item migrations

## Summary
The discussion revolves around changing the inventory storage format to binary while retaining backwards compatibility, and considering changes to how items and tools are stored to reduce memory usage.

## Explanation
The issue discusses the current storage of inventories as Zon files, which is inefficient for larger inventories like chests. The proposal includes changing the storage format to binary, using `BaseItem` indexes instead of string names for item migrations, and adding a tool palette with similar considerations. The maintainers suggest that while human-readable inventory data is useful for server hosts, this feature should not block improvements in inventory storage efficiency. Memory usage reduction is highlighted as a significant benefit, particularly for tools stored in crafting grids and material grids.

## Related Questions
- What are the potential benefits and drawbacks of changing inventory storage to binary format?
- How would changing `Item` to use `BaseItemIndex` instead of pointers affect memory usage?
- What is the impact on memory usage if `Tool` uses `BaseItemIndex` instead of pointers?
- Why is human-readable inventory data important for server hosts?
- How can item migrations be effectively managed with the proposed changes?
- What are the long-term implications of decoupling server moderation from physical access to the file system?

*Source: unknown | chunk_id: github_issue_1290_discussion*
