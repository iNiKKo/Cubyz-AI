# [easy/codebase_src_server_command_time.zig] - Chunk 0

**Type:** api
**Keywords:** ArgParser, union enum, gameTime, doGameTimeCycle, dayStart, nightStart, parse error handling, defer cleanup, stackAllocator
**Symbols:** Args, ArgParser, execute
**Concepts:** command parsing, union enum cases, server time state, day-night cycle toggle, message formatting, stack allocator usage

## Summary
Implements the /time server command parser and execution logic, handling queries for current game time, setting specific times or phases (day/night), and toggling the day-night cycle.

## Explanation
The chunk defines a union enum Args with four cases: @/time <phase> mapping to an enum {day, night}, @/time <subcommand> mapping to an enum {start, stop}, @/time <number> mapping to i64, and @/time mapping to an empty struct. It instantiates ArgParser via main.argparse.Parser(Args, .{.commandName = "/time"}). The execute function receives raw args bytes and a source User pointer; it allocates a mutable errorMessage List(u8) on the stack allocator with defer cleanup. Parsing is performed by calling ArgParser.parse(main.stackAllocator, args, &errorMessage), which returns Result(Args, error.ArgparseError). On parse failure, the function sends an error message to source using #ff0000{s} format and returns early without modifying server state. On success, result contains one of the Args cases. For @/time (empty case), it reads main.server.world.?.gameTime, formats it with #ffff00{}, then assigns that value back to gameTime. For @/time <number>, it extracts params.number directly. For @/time <phase>, it switches on params.phase: day maps to main.game.World.DayTime.dayStart, night maps to main.game.World.DayTime.nightStart; both are formatted and assigned. For @/time <subcommand>, it switches on params.subcommand: start sets main.server.world.?.doGameTimeCycle = true and sends #ffff00Time started., stop sets doGameTimeCycle = false and sends #ffff00Time stopped.; each branch returns early after sending the message, so no further assignment occurs for those cases. Finally, gameTime is assigned to main.server.world.?.gameTime unconditionally (overwriting any previous value).

## Related Questions
- What are the four possible cases of the Args union enum and their corresponding data structures?
- How does the execute function handle a parse error returned by ArgParser.parse?
- Which server world fields are read or written when processing @/time <phase> versus @/time <subcommand>? 
- What is the exact format string used to send the current game time to the user, and what color code does it use?
- How does the chunk ensure that errorMessage is freed after execute returns, regardless of early exits?
- Does the execute function modify main.server.world.?.gameTime when processing @/time <subcommand> cases, or only for other cases?
- What enum values are allowed for the phase field inside Args.@/time <phase>, and what does each value map to in terms of game time constants?
- What enum values are allowed for the subcommand field inside Args.@/time <subcommand>, and how does each affect doGameTimeCycle?
- Is ArgParser instantiated with a custom commandName, and if so, what is that name set to?
- Does the execute function ever return early without assigning a new value to gameTime, and under which conditions?

*Source: unknown | chunk_id: codebase_src_server_command_time.zig_chunk_0*
