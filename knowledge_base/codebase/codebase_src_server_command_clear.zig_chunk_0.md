# [easy/codebase_src_server_command_clear.zig] - Chunk 0

**Type:** api
**Keywords:** union enum, parser catch, switch target, defer deinit, sendMessage red
**Symbols:** Args, ArgParser, execute
**Concepts:** command parsing, inventory clearing, chat protocol update, error handling via message, stack allocation

## Summary
Implements the /clear server command that parses arguments to either clear a player's inventory or send a generic chat update.

## Explanation
The chunk defines an Args union with a single variant for the /clear command, containing a target enum (inventory|chat). It uses main.argparse.Parser to parse raw args into this struct, catching errors and sending a red message via source.sendMessage if parsing fails. On success it switches on result.target: inventory invokes main.items.Inventory.server.clearPlayerInventory(source) while chat calls main.network.protocols.genericUpdate.sendClear(source.conn, .chat). The function allocates an error list with main.stackAllocator, defers its deinit, and never returns a value.

## Related Questions
- What does the execute function return on successful parsing?
- Which enum values are valid for the target field in Args?
- How is a parse error communicated to the user?
- Where is the allocated error list freed?
- What function clears player inventory when target equals inventory?
- What network protocol handles chat clearing when target equals chat?
- Does execute perform any memory allocation itself?
- Is ArgParser constructed with a specific command name constant?
- What type does main.argparse.Parser expect as its first argument?
- Can the result of parsing be used directly without a switch statement?

*Source: unknown | chunk_id: codebase_src_server_command_clear.zig_chunk_0*
