# [medium/codebase_src_gui_windows_save_selection.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, ConnectionManager, ServerWorld.Mode, Texture.initFromFile, Thread.spawn, cubyzDir, readToZon, std.sort.insertion, NeverFailingAllocator, GarbageCollection.syncPoint, atomic flag polling, file system iteration, .zon serialization reading, button callbacks
**Symbols:** WorldInfo, openWorldWrap, deleteWorld, openFolder, update, onOpen, readingSaves
**Concepts:** save selection GUI, world list population, server thread spawning, file system iteration, .zon serialization reading, vertical list rendering, button callbacks, window lifecycle management, atomic flag polling, garbage collection sync point, insertion sort by last used time

## Summary
Implements the save-selection GUI window that lists worlds from the saves folder, handles creation and deletion actions, and spawns a server thread when opening a world.

## Explanation
The chunk defines a GuiWindow with content size 128x256. It imports ConnectionManager, settings, Vec2f, NeverFailingAllocator, Texture, and various GUI components (GuiComponent, GuiWindow, Button, HorizontalList, Label, TextInput, VerticalList). It declares pub var window as a GuiWindow instance, padding constant 8, width constant 160, buttonNameArena allocator, needsUpdate bool flag, mode ServerWorld.Mode, deleteIcon and fileExplorerIcon textures. WorldInfo struct holds lastUsedTime i64, name []const u8, fileName []const u8; worldList is a List(WorldInfo) initialized empty. init() loads delete_icon.png and file_explorer_icon.png from assets/cubyz/ui/. deinit() frees both textures. openWorld(name: []const u8) initializes a ConnectionManager at index 0 (empty struct), logs error if it fails, then spawns main.server.startFromNewThread with name, localPort, mode; sets thread name to 'Server' via main.io; polls main.server.running atomic flag with acquire ordering and sleeps between checks while also calling GarbageCollection.syncPoint(); after the loop assigns clientConnection.world = &main.game.testWorld, prints IP:port string using stackAllocator, defers free, sets main.game.world = &main.game.testWorld, calls testWorld.init(ipPort, clientConnection) and logs error on failure; closes all currently open GUI windows via gui.openWindows.items iteration then opens the HUD. openWorldWrap(index) is a callback that passes worldList.items[index].fileName to openWorld. deleteWorld(index) closes the 'delete_world_confirmation' window, sets its delete name to worldList.items[index].fileName, and reopens it. openFolder(index) constructs a path '{cubyzDir}/saves/{worldName}' using stackAllocator, defers free, then calls main.files.openDirInWindow(path). update() checks needsUpdate flag; if true resets it and calls onClose/onOpen. onOpen() initializes buttonNameArena from globalAllocator, creates a VerticalList with padding 8 and height 300, adds a Label at (0,0) width 160 centered showing '**Select World**' or '**Select World to Host**' depending on mode, adds a Button 'Create New World' at (0,0) width 128 whose onAction callback is gui.openWindowCallback('save_creation'). Then enters readingSaves label: opens main.files.cubyzDir().openIterableDir('saves'), logs error and breaks if it fails; defers dir.close(); iterates entries via iterator.next(main.io), logging errors and breaking on failure. For directory entries, constructs worldInfoPath 'saves/{entryName}/world.zig.zon', defers free, reads the .zon file with main.files.cubyzDir().readToZon into stackAllocator, logs error if read fails, continues; defers worldInfo.deinit(stackAllocator). Extracts lastUsedTime via worldInfo.get(i64,'lastUsedTime') orelse 0, name via worldInfo.get([]const u8,'name') orelse entryName, and fileName as a dupe of entryName into globalAllocator. Appends to worldList using main.globalAllocator with struct {fileName,lastUsedTime,name}. After the loop, sorts worldList.items in-place using std.sort.insertion with a closure lessThan that compares rhs.lastUsedTime -% lhs.lastUsedTime < 0 (descending by lastUsedTime).

## Related Questions
- What does the openWorld function do when initializing a connection manager?
- How are world entries added to the worldList after parsing their .zon files?
- What happens if opening the saves folder fails during onOpen?
- Why is there an atomic flag poll loop in openWorld before proceeding?
- Where are the delete_icon and file_explorer_icon textures loaded from?
- What callback is attached to the Create New World button?
- How does the chunk sort the world list by lastUsedTime?
- Which GUI component is used to render the vertical list of worlds?
- What error handling strategy is used when reading a .zon file fails?
- Does onOpen initialize any allocators before building the UI?
- Where are the textures freed in deinit?
- How does openFolder construct its path string?

*Source: unknown | chunk_id: codebase_src_gui_windows_save_selection.zig_chunk_0*
