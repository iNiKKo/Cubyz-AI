# [easy/codebase_src_server_command_gamemode.zig] - Chunk 0

**Type:** api
**Keywords:** argument parsing, gamemode setting, error handling, user communication, command execution
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command parsing, gamemode management, user messaging

## Summary
Handles the '/gamemode' command to get or set a player's gamemode.

## Explanation
The function `execute` parses the command arguments using an argument parser. If parsing fails, it sends an error message to the source user. If successful, it determines the target player and either sets their gamemode if provided or retrieves and sends their current gamemode.

## Related Questions
- What does the '/gamemode' command do?
- How is the 'Args' union defined?
- Where is the 'execute' function called?
- What happens if parsing fails in 'execute'?
- How is a target player determined?
- What method is used to set a player's gamemode?

*Source: unknown | chunk_id: codebase_src_server_command_gamemode.zig_chunk_0*
