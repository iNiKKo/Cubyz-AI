# [easy/codebase_src_gui_windows_delete_world_confirmation.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, deleteTree, needsUpdate, globalAllocator, stackAllocator, std.mem.concat, std.fmt.allocPrint, catch unreachable
**Symbols:** window, deleteWorldName, padding, flawedDeleteWorld, deleteWorld, onOpen, onClose
**Concepts:** GUI window lifecycle, world deletion confirmation, tree deletion with error handling, UI refresh after deletion, vertical list layout, button action binding, memory allocation via globalAllocator and stackAllocator

## Summary
This chunk implements the GUI window for confirming deletion of a world, including initialization, layout construction with labels and buttons, error handling during tree deletion, and cleanup on close.

## Explanation
The chunk defines a global GuiWindow instance named window with content size Vec2f{128, 256}. It declares deleteWorldName as a var backed by main.globalAllocator. init() clears deleteWorldName to empty slice. deinit() frees deleteWorldName via main.globalAllocator.free. setDeleteWorldName(name) first frees the old deleteWorldName then duplicates name into it using main.globalAllocator.dupe(u8, name). flawedDeleteWorld(name) constructs a path by concatenating 'saves/' with name using std.mem.concat on main.stackAllocator.allocator; it catches unreachable if concat fails (implying no valid path can be formed), defers freeing the allocated path, then calls try main.files.cubyzDir().deleteTree(path). After deletion it sets gui.windowlist.save_selection.needsUpdate = true to trigger a UI refresh. deleteWorld() wraps flawedDeleteWorld(deleteWorldName) in a catch block; on error it logs via std.log.err with the world name and @errorName(err), then calls gui.closeWindowFromRef(&window). onOpen() builds a VerticalList with padding 8 and height 300, adds a Label centered at (0,0) containing formatted text 'Are you sure you want to delete the world **{s}**?' using std.fmt.allocPrint on main.stackAllocator.allocator (catches unreachable), then adds a Button labeled 'Yes' whose .onAction is set to .init(deleteWorld). list.finish(.center) centers the layout, and window.rootComponent is assigned list.toComponent(). The content size is recomputed as rootComponent.pos() + rootComponent.size() plus padding splat. gui.updateWindowPositions() is called. onClose() checks if window.rootComponent exists and calls comp.deinit() to free its resources.

## Related Questions
- What is the initial content size of the delete world confirmation window?
- How does setDeleteWorldName manage memory for the world name string?
- Which allocator is used to construct the deletion path in flawedDeleteWorld?
- What happens if std.mem.concat fails when building the save path?
- After deleting a world tree, how is the UI notified of the change?
- How does deleteWorld handle errors returned by flawedDeleteWorld?
- What text is displayed to the user on opening the confirmation window?
- Which function is assigned as the button's onAction when the Yes button is created?
- How is the content size adjusted after adding components in onOpen?
- What cleanup occurs in onClose if a root component exists?

*Source: unknown | chunk_id: codebase_src_gui_windows_delete_world_confirmation.zig_chunk_0*
