# [easy/codebase_src_gui_windows_chest.zig] - Chunk 0

**Type:** implementation
**Keywords:** gui, inventory, layout, memory management, initialization, cleanup
**Symbols:** window, padding, itemSlots, openInventory
**Concepts:** GUI, inventory management, layout

## Summary
Manages the GUI window for a chest inventory, including initialization, deinitialization, and updating the inventory display.

## Explanation
This chunk manages the GUI window for a chest inventory. It initializes the window with a grid of item slots based on the selected inventory. The `onOpen` function sets up the layout, while `onClose` cleans up resources when the window is closed. The `deinit` function frees allocated memory.

## Code Example
```zig
pub fn onOpen() void {
	const list = VerticalList.init(.{padding, padding + 16}, 300, 0);

	for (0..2) |y| {
		const row = HorizontalList.init();
		for (0..10) |x| {
			const index: usize = y*10 + x;
			const slot = ItemSlot.init(.{0, 0}, openInventory, @intCast(index), .default, .normal);
			itemSlots.append(main.globalAllocator, slot);
			row.add(slot);
		}
		list.add(row);
	}
	list.finish(.center);
	window.shiftClickableInventory = openInventory;
	window.rootComponent = list.toComponent();
	window.contentSize = window.rootComponent.?.pos() + window.rootComponent.?.size() + @as(Vec2f, @splat(padding));
	gui.updateWindowPositions();
}
```

## Related Questions
- What function initializes the GUI window for a chest inventory?
- How is the layout of item slots in the chest inventory set up?
- What happens when the chest inventory window is closed?
- Which memory management function is used to free allocated memory?
- Who calls the `onOpen` function?
- What data structure holds the item slots for the chest inventory?

*Source: unknown | chunk_id: codebase_src_gui_windows_chest.zig_chunk_0*
