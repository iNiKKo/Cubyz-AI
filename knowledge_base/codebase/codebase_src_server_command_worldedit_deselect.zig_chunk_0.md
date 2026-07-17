# [easy/codebase_src_server_command_worldedit_deselect.zig] - Chunk 0

**Type:** api
**Keywords:** command parsing, data clearing, network update, user interface, error handling
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command handling, argument parsing, world edit data, network communication

## Summary
Clears the selected positions in a world edit operation.

## Explanation
The function `execute` handles the '/deselect' command. It parses the arguments using an argument parser, then clears the selection positions (`pos1` and `pos2`) in the user's world edit data. It also sends a network update to clear the selection on the client side.

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;

defer errorMessage.deinit(main.stackAllocator);

_ = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
	source.sendMessage("#ff0000{s}", .{errorMessage.items});
	return;
};

source.worldEditData.selectionPosition1 = null;
source.worldEditData.selectionPosition2 = null;

main.network.protocols.genericUpdate.sendWorldEditPos(source.conn, .clear, null);
source.sendMessage("Cleared selection.", .{});
}
```

## Related Questions
- What does the '/deselect' command do?
- How is the argument parsing handled in this function?
- Where is the world edit data updated?
- How is network communication initiated to update the client side?
- What happens if an error occurs during argument parsing?
- Which module handles the user interface messages?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_deselect.zig_chunk_0*
