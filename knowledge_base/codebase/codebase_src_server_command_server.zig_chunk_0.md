# [easy/codebase_src_server_command_server.zig] - Chunk 0

**Type:** api
**Keywords:** union enum, ArgParser, StopType, stackAllocator, headlessServer, sendMessage, catch error, defer deinit, main.server.stop
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command parsing, argument handling, error reporting, server control, configuration checks

## Summary
Implements the /server command handler for stop/restart actions, parsing arguments and delegating to main.server.stop while handling headless configuration checks.

## Explanation
The chunk defines a public description and usage string for the /server command. It imports User from main.server and defines an Args union with one variant containing an action field of type main.server.StopType. An ArgParser is instantiated using main.argparse.Parser with the Args union and a command name of '/server'. The execute function takes raw args bytes and a source pointer to User, allocates a List(u8) for error messages on the stack allocator, parses the arguments via ArgParser.parse catching errors into errorMessage (which is then sent as a red message if parsing fails). After successful parse, it checks if the action equals .restart and main.settings.launchConfig.headlessServer is false; in that case it sends an error message about headfull restart not being supported yet. Finally it calls main.server.stop with the parsed action.

## Related Questions
- What is the exact usage string for the /server command?
- Which union variant does Args contain and what field does it hold?
- How are parsing errors communicated to the user source?
- Under what condition is a restart action rejected with an error message?
- Where is the main.server.stop function invoked within execute?
- What allocator is used for temporary buffers in execute?

*Source: unknown | chunk_id: codebase_src_server_command_server.zig_chunk_0*
