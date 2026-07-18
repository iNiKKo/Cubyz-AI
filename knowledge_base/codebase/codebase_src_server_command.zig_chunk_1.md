# [medium/codebase_src_server_command.zig] - Chunk 1

**Type:** api
**Keywords:** reference counting, error handling, string parsing, resource management, user communication
**Symbols:** Target, Target.user, Target.increasedRefCount, Target.init, Target.fromPlayerIndex, Target.deinit, getCurrentSelection, PlayerIndex, PlayerIndex.index, PlayerIndex.parse, BiomeId, BiomeId.biome, BiomeId.parse, EntityModel, EntityModel.index, EntityModel.parse, MaskExpression, MaskExpression.mask, MaskExpression.parse, MaskExpression.deinit
**Concepts:** command parsing, user management, world edit selection, entity models, biome handling, mask expressions

## Summary
Defines data structures and parsing functions for command targets, selections, player indices, biomes, entity models, and mask expressions.

## Explanation
This chunk defines several structs and their associated methods to handle different types of command arguments in a server environment. The `Target` struct manages user references with reference counting. The `getCurrentSelection` function retrieves world edit selection positions from user data. The `PlayerIndex`, `BiomeId`, `EntityModel`, and `MaskExpression` structs each have a `parse` method to convert string inputs into their respective types, handling errors by sending messages to the user. The `MaskExpression` struct also includes a `deinit` method for proper resource management.

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
