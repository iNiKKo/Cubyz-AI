# [easy/codebase_src_server_command_permission_perm.zig] - Chunk 0

**Type:** api
**Keywords:** argument parser, union enum, permission path, target resolution, add permission, remove permission, has permission check, whitelist blacklist, player index, error message
**Symbols:** Args, ArgParser, Path
**Concepts:** command parsing, permission management, whitelist/blacklist operations, player target resolution, error reporting via chat messages

## Summary
Implements the /perm command handler for modifying and querying player permissions via an argument parser that supports adding/removing from whitelists or blacklists, checking permission existence, and resolving target players by index.

## Explanation
The chunk defines a public execute function taking raw args bytes and a User pointer; it allocates a List(u8) error buffer on the stack, parses arguments via ArgParser (a main.argparse.Parser instantiated for Args with commandName '/perm'), and on failure sends a red message to source. The parser returns a union of two cases: one for action+list+playerIndex+permissionPath and another for playerIndex+permissionPath only. For the first case it resolves target via command.Target.fromPlayerIndex (catching early), then maps list enum to ListType (.white/.black) and dispatches on action: add calls target.user.permissions.addPermission, remove calls target.user.permissions.removePermission with a red error message if removal fails. The second case checks hasPermission and sends green/red messages accordingly. A Path struct holds a []const u8 path field; its parse method validates the first byte is '/' (erroring otherwise) and returns .{.path = arg}. All allocations use main.stackAllocator or NeverFailingAllocator from main.heap.

## Related Questions
- How does the execute function handle parsing failures for the /perm command?
- What are the two distinct argument patterns recognized by ArgParser in this chunk?
- Which enum values correspond to whitelist and blacklist when mapping ListType?
- How is a target player resolved from an index inside the execute switch case?
- What happens if removePermission returns false for a given permission path?
- Does Path.parse validate anything other than the leading slash character?
- Which allocator is used for temporary error message storage in execute?
- Is there any cleanup logic (defer) around target allocation in this chunk?
- How does the code differentiate between checking existence and modifying permissions?
- What type does Path.path hold after a successful parse?

*Source: unknown | chunk_id: codebase_src_server_command_permission_perm.zig_chunk_0*
