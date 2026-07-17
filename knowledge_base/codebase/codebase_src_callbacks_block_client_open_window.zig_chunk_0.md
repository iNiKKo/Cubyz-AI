# [easy/codebase_src_callbacks_block_client_open_window.zig] - Chunk 0

**Type:** implementation
**Keywords:** windowName, openWindow, setMouseGrabbed, ZonElement, worldArena, callbacks, dupe, handled
**Symbols:** windowName, init, run
**Concepts:** callback block, GUI window opening, mouse grab release, ZonElement parsing, arena allocation

## Summary
Defines the OpenWindow callback block that initializes a window name from a ZonElement and runs a GUI openWindow call with mouse grab released.

## Explanation
The chunk declares a top-level struct (implicitly via pub fn init returning ?*@This()) containing one field windowName ([]const u8). The init function is called by the callbacks system; it receives a ZonElement zon and ignores the Creator argument. It creates an instance in main.worldArena using create(@This()), then populates the struct: it calls zon.get with key "name" to retrieve the window name string, dupes that slice into main.worldArena (dupe(u8, ...)), assigns to result.*.windowName, and if zon.get fails returns null with an error log via std.log.err. The run method takes self: *@This() and a ClientBlockCallback.Params argument which is ignored; it calls main.gui.openWindow(self.windowName) to open the window, then calls main.Window.setMouseGrabbed(false) to release mouse capture, finally returning .handled.

## Code Example
```zig
pub fn init(zon: ZonElement, _: main.callbacks.Creator) ?*@This() {
	const result = main.worldArena.create(@This());
	result.* = .{
		.windowName = main.worldArena.dupe(u8, zon.get([]const u8, "name") orelse {
			std.log.err("Missing field \"name\" for open_window event.", .{});
			return null;
		}),
	};
	return result;
}
```

## Related Questions
- What is the purpose of the windowName field in this callback block?
- How does init retrieve the window name from the ZonElement?
- What happens if zon.get fails to find the "name" key during initialization?
- Which function is called by run to open the GUI window?
- Why is main.Window.setMouseGrabbed(false) invoked after opening the window?
- Does the run method use any data from its Params argument?

*Source: unknown | chunk_id: codebase_src_callbacks_block_client_open_window.zig_chunk_0*
