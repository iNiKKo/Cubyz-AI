# [easy/codebase_src_server_command_worldedit_mask.zig] - Chunk 0

**Type:** api
**Keywords:** ArgParser, deinit, MaskExpression, clone, switch, stackAllocator, globalAllocator, union enum, deferred cleanup, world edit mask
**Symbols:** Args, ArgParser, execute
**Concepts:** command parsing, union enum variants, deferred cleanup, world edit mask management, error reporting to user

## Summary
Implements the /mask server command for setting or clearing a world edit mask, parsing arguments via ArgParser and managing lifecycle of MaskExpression through deinit callbacks.

## Explanation
The chunk defines an Args union with two variants: @/mask (no-mask) and @/mask <mask> (with-mask). Each variant contains a struct holding optional fields; the no-mask variant has only a deinit stub, while the with-mask variant holds a mask field of type command.MaskExpression and implements deinit to call self.mask.deinit(allocator). A top-level deinit function on Args uses an inline switch to delegate cleanup based on which variant is active. ArgParser is instantiated as main.argparse.Parser(Args, .{.commandName = "/mask"}) to handle parsing of the command string into Args. The execute function receives raw args and a source User pointer; it allocates a List(u8) for error messages with stackAllocator, defers its deinit, then calls ArgParser.parse(main.stackAllocator, args, &errorMessage). On parse failure, it sends an error message to the user via source.sendMessage using color #ff0000 and returns early. After parsing succeeds, result is deferred-deinited. Before processing the command, if source.worldEditData.mask is non-null, its deinit is called on main.globalAllocator to free any previously allocated mask expression. The switch on result handles two cases: @/mask <mask> clones cmd.mask.mask onto main.globalAllocator and assigns it to source.worldEditData.mask, then sends a success message; @/mask sets source.worldEditData.mask to null and sends a clear message.

## Code Example
```zig
fn deinit(self: Args, allocator: NeverFailingAllocator) void {
	switch (self) {
		inline else => |object| object.deinit(allocator),
	}
}
```

## Related Questions
- What happens if ArgParser.parse fails during /mask execution?
- How is the previously allocated mask expression freed before setting a new one?
- Which allocator is used for cloning the mask in the with-mask variant?
- Does the no-mask variant of Args perform any cleanup beyond its stub deinit?
- What message color is sent when the mask is cleared versus set?
- How does the inline switch delegate deinit to the active union variant?
- Is there any validation performed on the mask string before cloning it?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_mask.zig_chunk_0*
