# [easy/codebase_src_server_command_worldedit_toggledecay.zig] - Chunk 0

**Type:** api
**Keywords:** command processing, argument parsing, enum usage, struct definition, error handling, blueprint capture, block data modification
**Symbols:** description, usage, Target, State, Args, Args.parse, execute, toggledecay
**Concepts:** world editor, command parsing, blueprint manipulation, block modification

## Summary
This chunk implements the /toggledecay command for enabling or disabling decay on selected blocks in a world editor context.

## Explanation
The chunk defines a command that allows users to toggle decay on either their current selection or clipboard. It includes parsing logic for command arguments, capturing and modifying blueprints based on the target (selection or clipboard), and applying changes to blocks. The `toggledecay` function specifically handles the modification of block data to enable or disable decay.

## Code Example
```zig
const Target = enum { selection, clipboard }
```

## Related Questions
- What is the purpose of the /toggledecay command?
- How are arguments parsed in the /toggledecay command?
- What happens if there are too many arguments provided for /toggledecay?
- How does the chunk handle errors during argument parsing?
- What data structures are used to store and modify blueprints?
- How is block decay toggled in the world editor?
- What types of blocks can be modified by the /toggledecay command?
- How is user feedback provided for successful or failed commands?
- What role does the Blueprint struct play in this chunk?
- How are selections and clipboards managed within the command?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_toggledecay.zig_chunk_0*
