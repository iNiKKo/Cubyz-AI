# [easy/codebase_src_server_command_worldedit_copy.zig] - Chunk 0

**Type:** implementation
**Keywords:** worldedit, command, copy, selection, clipboard
**Symbols:** command, User, Block, Blueprint, description, usage, Args, ArgParser, execute, errorMessage, selection, result
**Concepts:** WorldEdit, copy command, selection capture, clipboard management

## Summary
WorldEdit copy command implementation

## Explanation
This chunk defines the 'copy' command for WorldEdit in the Cubyz voxel engine. It captures the current selection and copies it to the clipboard, handling errors if the capture fails.

## Code Example
```zig
const Args = union(enum) {
	@"/copy": struct {},
}
```

## Related Questions
- What is the purpose of the 'copy' command in WorldEdit?
- How does the 'execute' function handle errors during block capture?
- What data structures are used to manage clipboard contents?
- Where is the error message displayed to the user?
- What happens if the clipboard already contains a block?
- How is the captured selection stored in the worldEditData structure?
- What is the format of the error messages logged by this code?
- How does the 'execute' function interact with the globalAllocator?
- What are the possible outcomes of the Blueprint.capture function call?
- Where is the current selection retrieved from the command system?
- What is the role of the ArgParser in parsing command arguments?
- How is the usage string for the 'copy' command defined?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_copy.zig_chunk_0*
