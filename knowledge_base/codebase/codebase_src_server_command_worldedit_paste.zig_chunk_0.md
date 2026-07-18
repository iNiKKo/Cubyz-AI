# [easy/codebase_src_server_command_worldedit_paste.zig] - Chunk 0

**Type:** implementation
**Keywords:** paste, worldedit, command-line, arguments, clipboard, undo
**Symbols:** User, vec, Vec3i, Blueprint, description, usage, Args, ArgParser, execute
**Concepts:** WorldEdit, command-line arguments, clipboard content, undo history, void blocks

## Summary
Handles the '/paste' command in WorldEdit, pasting clipboard content to the current player's position.

## Explanation
The 'execute' function parses command-line arguments for the '/paste' command. It checks if there is a clipboard available and captures its undo history before pasting it to the player's position. The 'preserveVoid' flag is used to determine whether void blocks should be preserved during the paste operation.

## Code Example
```zig
{
	@"/paste [-v|--keep-void]": struct { void: ?enum { @"-v", @"--keep-void" } },
}
```

## Related Questions
- What is the purpose of the 'execute' function in this chunk?
- How does the 'execute' function handle clipboard availability and undo history?
- What are the parameters of the 'paste' method called by 'clipboard.paste(pos, .{.preserveVoid = result.@"/paste [-v|--keep-void]".void != null});'?
- What is the role of the 'ArgParser.parse' function in this chunk?
- How does the 'execute' function handle errors related to clipboard content or undo history capture?
- What are the possible outcomes of the 'undo.capture' function call within the 'execute' function?
- What data structures are used to store and manage undo history in this chunk?
- How is void block preservation determined in the 'paste' operation?
- What is the purpose of the 'Vec3i' type in this chunk?
- What is the role of the 'Blueprint.Selection' type in this chunk?
- What are the possible errors that can occur during the undo history capture process?
- How does the 'execute' function communicate error messages to the player?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_paste.zig_chunk_0*
