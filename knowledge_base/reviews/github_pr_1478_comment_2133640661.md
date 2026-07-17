# [src/gui/windows/workbench.zig] - Chunk 2133640661

**Type:** review
**Keywords:** workbench, toolTypes, index, Inventory, implementation detail, crafting station, forward compatibility, type safety, iterator, label update
**Symbols:** toggleTool, openInventory, toolButton.child.label.updateText, Inventory.init, toolTypes.items, currentToolType
**Concepts:** index-based storage, implementation detail coupling, forward compatibility, type safety, iterator contract, architectural refactoring, separate crafting stations

## Summary
The diff modifies the workbench initialization to store a typed index instead of a raw item reference, and updates the label text retrieval to use a method call.

## Explanation
The original code stored `toolTypes.items[currentToolType]` directly in the inventory struct field `.workbench`. This relies on an implementation detail: that the iterator returns items with a specific shape (likely containing an `id` string). The reviewer objects because this will break when separate crafting stations are introduced, as the current design assumes all tools live in one array. By changing to `{.index = @intCast(currentToolType)}`, the inventory now holds only an index into the global tool list, preserving type safety and allowing future expansion (e.g., different station arrays). The label update similarly changes from accessing `.id` directly on the item to calling a method `id()`; this suggests the iterator may return a struct where fields are accessed via methods rather than direct properties, or that the codebase is moving toward a more uniform API. Both changes eliminate reliance on concrete layout details and prepare for architectural refactoring.

## Related Questions
- What is the current shape of `toolTypes.items` and how does it expose an `id` field?
- Does `Inventory.init` accept a raw item reference or only an index in its `.workbench` variant?
- Where else in the codebase are items accessed via `items[currentToolType]` instead of an index?
- What changes would be required to support multiple crafting stations while keeping this index pattern?
- Is there a method `id()` defined on the iterator result type, and where is it declared?
- How does the reviewer’s comment about 'separate crafting stations' map to existing module boundaries?
- Could storing an index cause any runtime errors if `toolTypes` is reordered or resized?
- What is the purpose of `needsUpdate` in `toggleTool`, and how does it relate to the label update?
- Are there any other places that depend on the concrete layout of items returned by the iterator?
- If we refactor to use indices everywhere, what migration path exists for existing code using item references?

*Source: unknown | chunk_id: github_pr_1478_comment_2133640661*
