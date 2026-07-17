# [easy/codebase_src_server_command_help.zig] - Chunk 0

**Type:** api
**Keywords:** union enum, value iterator, catch error, defer deinit, append slice, trim newline
**Symbols:** Args, ArgParser, Cmd
**Concepts:** command parsing, argument union enumeration, error handling with defer cleanup, message formatting

## Summary
Implements the /help server command that parses arguments and lists all available commands or details a specific one.

## Explanation
The chunk defines an Args union with three cases: bare '/help', '/help <command>', and '/help <bobik>'. It uses ArgParser to parse incoming args into result, catching errors and sending a red error message if parsing fails. On success it builds a yellow message buffer (msg) by appending the prefix '#ffff00' then iterating over command.commands.valueIterator() for the bare case, or extracting params.command.cmd for the specific-case. For each matched command it appends '/name: description\n'. The '<bobik>' case hardcodes 'Even Bobik can't help you anymore '. After building msg it trims a trailing newline if present and sends the result via source.sendMessage.

## Related Questions
- How does the Args union differentiate between a bare /help and a specific command?
- What happens when ArgParser.parse fails in execute?
- Which iterator is used to traverse all commands in the bare /help case?
- How are command details formatted before being sent to the user?
- Where does the hardcoded Bobik message appear in the switch statement?
- Why is a trailing newline removed from msg.items before sending?

*Source: unknown | chunk_id: codebase_src_server_command_help.zig_chunk_0*
