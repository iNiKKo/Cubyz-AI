# [src/gui/windows/workbench.zig] - PR #1478 review diff

**Type:** review
**Keywords:** inventory initialization, tool type ID, index, crafting stations, implementation detail, iterator behavior
**Symbols:** toggleTool, currentToolType, toolTypes, toolButton, label, updateText, openInventory, inv, Inventory, main.globalAllocator
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The code changes the way the inventory is initialized to use a struct with an index instead of directly using the tool type ID.

## Explanation
The reviewer points out that changing the inventory initialization to use a struct with an index instead of the tool type ID introduces a risk of breaking functionality silently when separate crafting stations are implemented. The reviewer also notes that this change relies on an implementation detail of the tool type iterator, which could lead to potential issues if the iterator's behavior changes.

The specific code changes include:
- Line 49: `toolButton.child.label.updateText(toolTypes.items[currentToolType].id());`
- Line 51: `inv = Inventory.init(main.globalAllocator, 26, .{.workbench = .{.index = @intCast(currentToolType)}}, .other);`

The reviewer emphasizes that the inventory initialization must remain an index into the array to avoid silent breaks when separate crafting stations are implemented. Additionally, the change relies on an implementation detail of the tool type iterator, which could lead to potential issues if the iterator's behavior changes.

## Related Questions
- What is the potential impact of changing the inventory initialization to use a struct with an index?
- How does this change affect the implementation detail of the tool type iterator?
- What are the risks associated with relying on the current behavior of the tool type iterator?
- How can we ensure that the code remains compatible with future changes in crafting stations?
- What steps should be taken to prevent silent breaks when implementing separate crafting stations?
- How does this change impact the overall architecture and design of the workbench module?

*Source: unknown | chunk_id: github_pr_1478_comment_2133640661*
