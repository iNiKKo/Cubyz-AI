# [easy/codebase_src_server_command_permission_perm.zig] - Chunk 0

**Type:** implementation
**Keywords:** command parser, permission add/remove, user permissions, argument parsing, error handling
**Symbols:** description, usage, Args, ArgParser, execute, errorMessage, ListType, command, Path
**Concepts:** command handling, permission management, argument parsing

## Summary
Handles command to manage player permissions with detailed argument parsing and error handling.

## Explanation
The chunk defines a '/perm' command that allows users to manage player permissions. The command supports several sub-commands with specific syntax:

1. `/perm <permissionPath>`: Checks if the current player has the specified permission path.
2. `/perm @<playerIndex> <permissionPath>`: Checks if a specified player (by index) has the given permission path.
3. `/perm <add/remove> <whitelist/blacklist> <permissionPath>`: Adds or removes a permission for the current player in the specified list.
4. `/perm <add/remove> <whitelist/blacklist> @<playerIndex> <permissionPath>`: Adds or removes a permission for a specified player (by index) in the specified list.

The command uses an `Args` union to parse arguments and perform corresponding operations on user permissions. The possible actions are 'add' and 'remove', while the lists can be either 'whitelist' or 'blacklist'. The `Args` union has two variants:

- `@"/perm <action> <list> <playerIndex> <permissionPath>": struct { action: enum { add, remove }, list: enum { whitelist, blacklist }, playerIndex: ?command.PlayerIndex, permissionPath: Path }
- `@"/perm <playerIndex> <permissionPath>": struct { playerIndex: ?command.PlayerIndex, permissionPath: Path }

Error handling is implemented during argument parsing and permission management:
- If a player index is provided, it checks if the target player exists.
- Permission paths must begin with a '/' character; otherwise, an error message is printed: `Permission path for <{s}> doesn't begin with a "/", got: {s}`.
- When adding or removing permissions, errors are handled by checking if the path already exists in the specified list before performing the operation. If the path does not exist and removal is attempted, an error message is displayed to inform the user: `Permission path {s} is not present inside users permission {s}list`.

The 'Path' struct ensures that permission paths begin with a '/' character, and error messages are printed if this condition is not met. User permissions are managed through the `ListType` enum which specifies whether a path belongs to a whitelist or blacklist. The `ListManaged` type is used for managing error messages.

## Code Example
```zig
pub fn parse(allocator: NeverFailingAllocator, name: []const u8, arg: []const u8, errorMessage: *List(u8)) error{ParseError}!Path {
	if (arg[0] != '/') {
		errorMessage.print(allocator, "Permission path for <{s}> doesn't begin with a "/", got: {s}", .{name, arg});
		return error.ParseError;
	}
	return .{.path = arg};
}
```

## Code Example
```zig
pub fn parse(allocator: NeverFailingAllocator, name: []const u8, arg: []const u8, errorMessage: *List(u8)) error{ParseError}!Path {
		if (arg[0] != '/') {
			errorMessage.print(allocator, "Permission path for <{s}> doesn't begin with a \"/\", got: {s}", .{name, arg});
			return error.ParseError;
		}
		return .{.path = arg};
	}
```

## Related Questions
- What is the purpose of the 'Args' union in the code?
- How does the 'ArgParser' work to parse command arguments?
- What are the possible actions and lists that can be used with the '/perm' command?
- Where is the error handling for parsing command arguments located?
- What is the 'Path' struct used for, and how is it parsed?
- How does the code handle permission addition or removal?
- What happens if a player has no permission for a specific path?
- How are user permissions managed in this system?
- Where is the error message printed when parsing command arguments fails?
- What is the 'ListType' enum used for, and how is it utilized in the code?
- How does the code handle errors related to permission paths?
- What is the 'command' module used for in this context?

*Source: unknown | chunk_id: codebase_src_server_command_permission_perm.zig_chunk_0*
