# [easy/codebase_src_gui_windows_debug_network_advanced.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, Connection, mutex locking, getStatistics, lossyChannel, secureChannel, slowChannel, draw.print, user list iteration, contentSize update
**Symbols:** window, renderConnectionData, render
**Concepts:** debug UI rendering, network connection statistics display, mutex locking for thread safety, channel queue visualization, RTT estimation display, bandwidth estimate display, user list iteration, window size dynamic update

## Summary
This chunk defines the debug network window UI component, declaring a GuiWindow instance and providing render functions that draw connection statistics for the client and server user list.

## Explanation
The chunk declares a top-level pub var window of type GuiWindow with specific configuration: relativePosition set to two attachment points (middle/selfAttachmentPoint/middle and upper/otherAttachmentPoint/upper), contentSize Vec2f{192, 128}, isHud false, showTitleBar false, hasBackground false, hideIfMouseIsGrabbed false. It imports main.network.Connection, main.vec.Vec2f, and the gui module to access GuiWindow and GuiComponent types. The renderConnectionData function takes a connection pointer, name slice, and y coordinate; it locks conn.mutex (defer unlock), initializes unconfirmed and queued arrays via @splat(0), calls getStatistics on lossyChannel, secureChannel, and slowChannel passing pointers into those arrays, then draws three lines using draw.print: the first shows RTT estimate divided by 1000.0 and bandwidthEstimateInBytesPerRtt divided by 1024.0; the second shows queued bytes shifted right 10 bits for each channel; the third shows unconfirmed bytes similarly shifted. Each draw.print increments y.* by 8. The pub fn render function initializes y at 0, checks if main.game.world is non-null and calls renderConnectionData with main.game.world.?.conn, name 'Client', and &y; adds 8 to y; checks if main.server.world is non-null, obtains userList via main.server.getUserListAndIncreaseRefCount(main.stackAllocator) (deferred freeUserListAndDecreaseRefCount), iterates over userList calling renderConnectionData for each user's conn with their name, then after the loop compares window.contentSize[1] to y and updates contentSize[1], calls updateWindowPosition if they differ.

## Related Questions
- What are the default values for the window configuration fields in this chunk?
- How does renderConnectionData ensure thread safety when accessing connection statistics?
- Which three network channels have their statistics retrieved and displayed?
- What is the purpose of shifting queued and unconfirmed bytes by 10 bits before printing?
- Under what condition does render update the window content size and call updateWindowPosition?
- How are server user connections iterated in the render function?
- What happens to userList after rendering if main.server.world is non-null?
- Does this chunk declare any pub const re-exports from other modules?
- Which draw API functions are invoked for printing connection data lines?
- Is there a defer block associated with getUserListAndIncreaseRefCount in render?

*Source: unknown | chunk_id: codebase_src_gui_windows_debug_network_advanced.zig_chunk_0*
