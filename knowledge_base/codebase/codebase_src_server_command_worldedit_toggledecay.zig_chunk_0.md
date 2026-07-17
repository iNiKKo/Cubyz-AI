# [easy/codebase_src_server_command_worldedit_toggledecay.zig] - Chunk 0

**Type:** api
**Keywords:** command execution, argument parsing, block state modification, blueprint usage, error handling
**Symbols:** description, usage, Target, State, Args, Args.parse, execute, toggledecay
**Concepts:** command processing, user input parsing, block manipulation, world editing

## Summary
This chunk defines a server command for toggling decay on selected or clipboard blocks.

## Explanation
The code defines a command `/toggledecay` that allows users to enable or disable decay on blocks within their selection or clipboard. It includes parsing logic for the command arguments, execution logic to apply the decay toggle, and a helper function `toggledecay` to modify block properties based on the decay state. The command uses a blueprint to capture and manipulate the selected area, handling errors and user feedback appropriately.

## Code Example
```zig
const Target = enum { selection, clipboard }
```

## Related Questions
- What is the purpose of the `toggledecay` function?
- How does the command handle invalid arguments from the user?
- What types of blocks can be affected by this command?
- How does the command capture and manipulate the selection area?
- What feedback does the command provide to the user after execution?
- How is the clipboard handled in this command?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_toggledecay.zig_chunk_0*
