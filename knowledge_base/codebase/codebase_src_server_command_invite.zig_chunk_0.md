# [easy/codebase_src_server_command_invite.zig] - Chunk 0

**Type:** api
**Keywords:** server command, IP address, reference counting, error messages, user initialization
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, argument parsing, user management, error handling, memory management

## Summary
Handles the '/invite' command for inviting a player by IP address.

## Explanation
This chunk defines the logic for processing the '/invite' server command. The `Args` union specifies the expected input format as `/invite <ip>`, where `ip` is a string representing the IP address of the player to invite. If parsing fails, it sends an error message to the source user. If successful, it attempts to initialize a new user connection using the provided IP and handles any errors that occur during this process. The chunk also manages reference counting for user objects to ensure proper memory management.

The `execute` function takes two parameters: `args`, which is a union containing the parsed arguments, and `source`, which is a pointer to the user who executed the command. If there is an error while initializing the new user connection, it logs the error and sends an error message to the source user. The reference count for the user object is increased when the user is initialized and decreased when the function returns, ensuring that the memory is properly managed.

The `usage` string is defined as `/invite <ip>`, indicating the correct syntax for the command. The `Args` union is implemented as follows:
```zig
pub const Args = union(enum) {
    @"/invite <ip>": struct { ip: []const u8 },
};
```
The `execute` function is implemented as follows:
```zig
pub fn execute(args: Args, source: *User) void {
    const user = main.server.User.initAndIncreaseRefCount(main.server.connectionManager, args.@"/invite <ip>".ip) catch |err| {
        std.log.err("Error while trying to connect: {s}", .{@errorName(err)});
        source.sendMessage("#ff0000Error while trying to connect: {s}", .{@errorName(err)});
        return;
    };
    user.decreaseRefCount();
    return;
}
```

## Code Example
```zig
pub fn execute(args: []const u8, source: *User) void {
	var errorMessage: main.List(u8) = .empty;
	defer errorMessage.deinit(main.stackAllocator);

	const result = ArgParser.parse(main.stackAllocator, args, &errorMessage) catch {
		source.sendMessage("#ff0000{s}", .{errorMessage.items});
		return;
	};

	const user = main.server.User.initAndIncreaseRefCount(main.server.connectionManager, result.@"/invite <ip>".ip) catch |err| {
		std.log.err("Error while trying to connect: {s}", .{@errorName(err)});
		source.sendMessage("#ff0000Error while trying to connect: {s}", .{@errorName(err)});
		return;
	};
	user.decreaseRefCount();
	return;
}
```

## Related Questions
- What is the description of the '/invite' command?
- How does the chunk parse arguments for the '/invite' command?
- What happens if there is an error during argument parsing?
- How does the chunk handle errors when initializing a new user connection?
- What role does reference counting play in this chunk?
- How are error messages communicated to the source user?

*Source: unknown | chunk_id: codebase_src_server_command_invite.zig_chunk_0*
