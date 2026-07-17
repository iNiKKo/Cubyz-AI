# [easy/codebase_src_server_command_worldedit_paste.zig] - Chunk 0

**Type:** api
**Keywords:** paste, clipboard, void blocks, undo history, redo history, Blueprint capture, command line arguments, world edit data, player position, error handling
**Symbols:** description, usage, Args, ArgParser
**Concepts:** command parsing, clipboard paste, undo/redo history management, world edit operations, player position floored to integer coordinates

## Summary
Implements the /paste command for worldedit, parsing arguments and pasting clipboard contents at the player's floored position while managing undo/redo history via Blueprint.capture.

## Explanation
The chunk defines a public description and usage string for the /paste command. It declares an Args union with a single variant containing a void field that holds either @

## Related Questions
- What is the default behavior regarding void blocks when pasting clipboard content?
- How does the command parser handle missing or invalid arguments for /paste?
- Where in the source code is the undo history updated after a successful paste operation?
- Which function is responsible for capturing the selection before pasting, and what does it return?
- What happens if there is no clipboard content available when the /paste command is executed?
- How are errors communicated to the user during the paste operation?
- Is there any validation performed on the player position before pasting?
- Does the chunk provide a way to query whether a paste was successful or failed?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_paste.zig_chunk_0*
