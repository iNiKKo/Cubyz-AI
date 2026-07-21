# [medium/codebase_src_server_command.zig] - Chunk 0

**Type:** api
**Keywords:** command registration, permission handling, coordinate resolution, user input processing, deprecated functions
**Symbols:** Command, commands, init, deinit, execute, Coordinate, parse, resolveCoordinates, parseAxis, parseCoordinates, parsePlayerIndexAndIncreaseRefCount, commandList
**Concepts:** command system, permission checking, coordinate parsing, player management

## Summary
This chunk defines the command system for the server, including command registration, execution, and coordinate parsing.

## Explanation
This chunk defines the command system for the server, including command registration, execution, and coordinate parsing. The `Command` struct is declared with fields for an execution function (`exec`), name (`name`), description (`description`), usage instructions (`usage`), and permission path (`permissionPath`). Each field has a specific type: `exec` is a pointer to a function that takes arguments of type `[]const u8` and `*User`, `name` and `description` are slices of constant bytes (`[]const u8`), `usage` is also a slice of constant bytes (`[]const u8`), and `permissionPath` is a slice of constant bytes (`[]const u8`). A global `commands` map of type `std.StringHashMap(Command)` is initialized to store registered commands. The `init` function populates this map by iterating over the `commandList` struct's declarations, setting each command's fields accordingly and logging the registration process with a debug message for each command name. The `deinit` function deinitializes the `commands` map. The `execute` function handles command execution based on user input, checking permissions using `source.hasPermission(cmd.permissionPath)` and executing the appropriate command if valid. It also defines a `Coordinate` union for parsing relative or absolute coordinates, with methods to parse (`parse`) and resolve these coordinates (`resolveCoordinates`). The `parse` method of the `Coordinate` union takes an allocator, a name, an argument string, and an error message list, returning a parsed `Coordinate`. It checks if the argument is relative (indicated by leading `~`) or absolute and parses it accordingly. The `resolveCoordinates` function takes three `Coordinate` values and a player object, resolving them based on the player's position. Additionally, it includes deprecated functions for parsing axis values (`parseAxis`), player indices (`parsePlayerIndexAndIncreaseRefCount`), and coordinate sets (`parseCoordinates`). The `parseAxis` function takes an axis argument string, a player position, and a source user, returning a parsed floating-point number or relative value. It checks if the argument is relative (indicated by leading `~`) or absolute and parses it accordingly. The `parsePlayerIndexAndIncreaseRefCount` function takes a player index specifier starting with '@' and a source user, parsing the index and increasing the reference count for the user object associated with that index. The `parseCoordinates` function splits input arguments into three parts and calls `parseAxis` to parse each coordinate, resolving them based on the player's position. The `initExecutionFn` function is used to initialize the execution function for each command, creating an argument parser and defining the execution logic. The `Target` struct is used to manage user targets, with methods to create a target from a player index (`fromPlayerIndex`) and deinitialize the target (`deinit`).

## Code Example
```zig
pub fn execute(msg: []const u8, source: *User) void {
	const end = std.mem.indexOfScalar(u8, msg, ' ') orelse msg.len;
	const command = msg[0..end];
	if (commands.get(command)) |cmd| {
		if (!source.hasPermission(cmd.permissionPath)) {
			source.sendMessage("#ff0000No permission to use Command \"{s}\"", .{command});
			return;
		}
		source.sendMessage("#00ff00Executing Command /{s}", .{msg});
		cmd.exec(msg[@min(end + 1, msg.len)..], source);
	} else {
		source.sendMessage("#ff0000Unrecognized Command \"{s}\"", .{command});
	}
}
```

## Related Questions
- How are commands registered in the server?
- What is the structure of a command in this system?
- How does permission checking work for executing commands?
- How are coordinates parsed and resolved in this chunk?
- What functions are deprecated and why?
- How is player index parsing handled in this code?

*Source: unknown | chunk_id: codebase_src_server_command.zig_chunk_0*
