# [easy/codebase_src_server_command_worldedit_set.zig] - Chunk 0

**Type:** gameplay
**Keywords:** worldedit, selection capture, blueprint replace, undo history push, redo clear, mask region, preserve void, error message, defer cleanup, parse pattern string
**Symbols:** execute, description, usage, Pattern, Block, Blueprint, Vec3i, User, main.server.command, main.blocks.Block, main.blueprint.Blueprint, main.blueprint.Pattern, main.stackAllocator, main.globalAllocator
**Concepts:** worldedit command parsing, selection capture into blueprint, undo/redo history management, pattern replacement within mask, void preservation on paste

## Summary
Implements the /set worldedit command that parses a pattern string, captures the current selection into a blueprint, applies an undo history entry, and pastes the modified blueprint back to the world.

## Explanation
The execute function first validates args.len > 0 and sends a red error message if missing. It obtains the current selection via command.getCurrentSelection(source) catch return; on failure it exits immediately. The pattern string is parsed with Pattern.initFromString(main.stackAllocator, args); any parse error triggers a red message containing @errorName(err). A defer ensures pattern.deinit(main.stackAllocator) runs regardless of success or failure. Blueprint.capture(main.globalAllocator, selection) returns a union { .success => |blueprint|, .failure => err }. On .success the code pushes an undoHistory entry initialized with the captured blueprint, selection.minPos, and action "set"; it clears redoHistory to maintain undo/redo invariants. A clone of the blueprint is created into main.stackAllocator (deferred deinit) so modifications do not affect the original capture result. The modifiedBlueprint.replace(null, source.worldEditData.mask, pattern) applies the pattern within the mask region, and modifiedBlueprint.paste(selection.minPos, .{.preserveVoid = true}) writes it back to the world at the selection's minimum position while preserving void blocks.

## Related Questions
- What happens if the user provides an empty argument list to /set?
- How does the function handle a failed Blueprint.capture result?
- Why is redoHistory cleared after a successful set operation?
- Where are the allocated buffers for the pattern and blueprint stored?
- What does replace(null, source.worldEditData.mask, pattern) accomplish?
- Does paste modify blocks outside the selection bounds?
- Is the original captured blueprint retained after execution?

*Source: unknown | chunk_id: codebase_src_server_command_worldedit_set.zig_chunk_0*
