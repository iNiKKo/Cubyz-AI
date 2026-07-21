# [easy/codebase_src_server_command_worldedit_paste.zig] - Chunk 0

**Type:** implementation
**Keywords:** paste, worldedit, command-line, arguments, clipboard, undo
**Symbols:** User, vec, Vec3i, Blueprint, description, usage, Args, ArgParser, execute
**Concepts:** WorldEdit, command-line arguments, clipboard content, undo history, void blocks

## Summary
Handles the '/paste' command in WorldEdit, pasting clipboard content to the current player's position.

## Explanation
Handles the '/paste' command in WorldEdit, pasting clipboard content to the current player's position. The command accepts optional arguments `-v` or `--keep-void` to preserve void blocks during the paste operation.

The `/paste` command is implemented in Zig and handled by the `execute` function within the `WorldEdit` module. The command syntax is defined as `/paste [-v|--keep-void]`, where `-v` or `--keep-void` are optional flags to preserve void blocks.

### Command-Line Arguments
The command-line arguments for the `/paste` command are parsed using a union enum named `Args`. The structure of this union is as follows:
```zig
pub const Args = union(enum) {
    @"/paste [-v|--keep-void]": struct { void: ?enum { @"-v", @"--keep-void" } },
};
```
The `Args` union contains a single variant, which is a struct with an optional field `void`. This field can hold either the value `-v` or `--keep-void`, indicating whether the preserve void blocks option was provided.

### Clipboard Handling
The `execute` function first checks if there is clipboard content available. If no clipboard content is found, it sends an error message to the player:
```zig
if (source.worldEditData.clipboard) |clipboard| {
    // Clipboard content is available
} else {
    source.sendMessage("#ff0000Error: No clipboard content to paste.", .{});
}
```
If clipboard content is available, the function proceeds to paste it at the player's current position. The position is calculated by flooring the player's coordinates:
```zig
const pos: Vec3i = @floor(source.player().pos);
source.sendMessage("Pasting: {}", .{pos});
```

### Undo History
Before pasting the clipboard content, the function captures the current state of the world at the selected area using `Blueprint.capture`. This captured state is used to create an undo history entry:
```zig
const selection: Blueprint.Selection = .initFromExtent(pos, clipboard.extent());
const undo = Blueprint.capture(main.globalAllocator, selection);
switch (undo) {
    .success => |blueprint| {
        source.worldEditData.undoHistory.push(.init(blueprint, pos, "paste"));
        source.worldEditData.redoHistory.clear();
    },
    .failure => {
        source.sendMessage("#ff0000Error: Could not capture undo history.", .{});
    },
}
```
If the capture operation fails, an error message is sent to the player.

### Void Block Preservation
The `clipboard.paste` method is called with a parameter that determines whether void blocks should be preserved. This parameter is set based on the presence of the `-v` or `--keep-void` argument:
```zig
clipboard.paste(pos, .{.preserveVoid = args.@"/paste [-v|--keep-void]".void != null});
```
If either `-v` or `--keep-void` is provided, the `preserveVoid` flag is set to true; otherwise, it defaults to false.

### Description and Usage
The command's description and usage are defined as follows:
```zig
pub const description =
    \\Paste clipboard content to current player position.
    \\-v|--keep-void - Preserve void blocks. By default, void blocks are not preserved.
;
pub const usage = "/paste [-v|--keep-void]";
```
The `description` string provides a brief explanation of the command and its options, while the `usage` string specifies the correct syntax for using the command.

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
