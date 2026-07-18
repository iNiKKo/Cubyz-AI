# [easy/codebase_src_server_command_worldedit_mask.zig] - Chunk 0

**Type:** api
**Keywords:** command handling, union enum, deinitialization, message sending, argument parsing
**Symbols:** description, usage, Args, ArgParser, execute
**Concepts:** command processing, world edit mask, argument parsing

## Summary
Handles the '/mask' command for setting or clearing a world edit mask.

## Explanation
This chunk defines the logic for processing the '/mask' command in the server's command system. It uses an argument parser to handle two forms of the command: one that sets a mask with an expression (`/mask <mask>`) and another that clears the current mask (`/mask`). The `Args` union enum manages different argument structures, each with its own deinitialization method. The `execute` function parses the input arguments using the defined usage syntax. If parsing fails, an error message is sent to the user in a custom format with color codes (e.g., `#ff0000{s}` for errors and `#00ff00Mask set/cleared.` for success messages). When setting a mask, it clones the provided mask expression into the global allocator; when clearing the mask, it sets `source.worldEditData.mask` to null.

## Code Example
```zig
fn deinit(_: @This(), _: NeverFailingAllocator) void {}
```

## Related Questions
- What is the description of the '/mask' command?
- How does the chunk handle different forms of the '/mask' command?
- What is the purpose of the `Args` union enum in this chunk?
- How does the `execute` function parse and process the input arguments?
- What happens if the argument parsing fails in the `execute` function?
- How is the world edit mask updated based on the parsed arguments?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_mask.zig_chunk_0*
