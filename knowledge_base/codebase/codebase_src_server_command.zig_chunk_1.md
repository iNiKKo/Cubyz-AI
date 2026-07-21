# [medium/codebase_src_server_command.zig] - Chunk 1

**Type:** api
**Keywords:** reference counting, error handling, string parsing, resource management, user communication
**Symbols:** Target, Target.user, Target.increasedRefCount, Target.init, Target.fromPlayerIndex, Target.deinit, getCurrentSelection, PlayerIndex, PlayerIndex.index, PlayerIndex.parse, BiomeId, BiomeId.biome, BiomeId.parse, EntityModel, EntityModel.index, EntityModel.parse, MaskExpression, MaskExpression.mask, MaskExpression.parse, MaskExpression.deinit
**Concepts:** command parsing, user management, world edit selection, entity models, biome handling, mask expressions

## Summary
Defines data structures and parsing functions for command targets, selections, player indices, biomes, entity models, and mask expressions.

## Explanation
This chunk defines several structs and their associated methods to handle different types of command arguments in a server environment. The `Target` struct manages user references with reference counting. If the `increasedRefCount` field is true, it decreases the reference count when deinitialized. The `getCurrentSelection` function retrieves world edit selection positions from user data; if either position is not set, it sends an error message to the user and returns an appropriate error code (`error.SelectionPartiallyUnset`). The `PlayerIndex.parse` method parses a player index string starting with '@' followed by an integer. If the format is incorrect or the player does not exist, it sends an error message in the form of `errorMessage.print("Expected to start with @ for <{s}>, found \"{s}\"", .{name, arg})` and returns `error.ParseError`. The `BiomeId.parse` method retrieves a biome based on its ID. If the biome cannot be found, it sends an error message in the form of `errorMessage.print("Couldn't find biome for <{s}> with id \"{s}\"", .{name, args})` and returns `error.ParseError`. The `EntityModel.parse` method retrieves an entity model based on its ID. If the entity model cannot be found, it sends an error message in the form of `errorMessage.print("Couldn't find EntityModel for <{s}> with id \"{s}\"", .{name, args})` and returns `error.ParseError`. The `MaskExpression.parse` method parses a mask string and initializes a `MaskExpression` struct. If parsing fails, it sends an error message in the form of `errorMessage.print("Couldn't parse mask: {s}", .{@errorName(err)})` and returns `error.ParseError`. Additionally, the `MaskExpression.deinit` method deinitializes the mask expression to manage resources properly.

## Code Example
```zig
pub fn deinit(self: Target) void {
	if (self.increasedRefCount) self.user.decreaseRefCount();
}
```

## Related Questions
- How does the `Target` struct manage user references?
- What error message is sent if a player index is not found?
- How does the `getCurrentSelection` function handle unset positions?
- What types of arguments can be parsed by `PlayerIndex.parse`?
- How does the `BiomeId` struct parse biome identifiers?
- What happens if an invalid entity model ID is provided?
- How is a mask expression parsed and what resources are managed?
- What methods are available for the `MaskExpression` struct?
- How does the `Target.init` function handle insufficient arguments?
- What is the purpose of the `increasedRefCount` field in the `Target` struct?

*Source: unknown | chunk_id: codebase_src_server_command.zig_chunk_1*
