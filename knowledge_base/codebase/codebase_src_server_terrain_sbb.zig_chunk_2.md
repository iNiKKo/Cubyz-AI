# [medium/codebase_src_server_terrain_sbb.zig] - Chunk 2

**Type:** implementation
**Keywords:** struct initialization, error handling, blueprint sampling, child structure retrieval, zon parsing
**Symbols:** StructureBuildingBlock, StructureBuildingBlock.id, StructureBuildingBlock.children, StructureBuildingBlock.blueprints, StructureBuildingBlock.rotation, StructureBuildingBlock.initFromZon, StructureBuildingBlock.postResolutionChecks, StructureBuildingBlock.getBlueprints, StructureBuildingBlock.getChildStructure
**Concepts:** world generation, blueprint system, structure configuration

## Summary
Defines the StructureBuildingBlock struct and its methods for initialization from Zon data, post-resolution checks, blueprint sampling, and child structure retrieval.

## Explanation
The chunk defines a `StructureBuildingBlock` struct with fields for an ID (`id`), children (`children`), blueprints (`blueprints`), and rotation (`rotation`). It includes methods for initializing from Zon data (`initFromZon`), performing post-resolution checks (`postResolutionChecks`), sampling blueprints based on a seed (`getBlueprints`), and retrieving child structures (`getChildStructure`). The `initFromZon` method handles parsing Zon elements to populate the struct, including detailed error handling for missing or invalid fields. Specifically, it logs errors if the 'blueprints' field is missing, not an array, empty, or contains non-object configurations. It also checks for valid blueprint IDs and ensures that rotation parameters are correctly parsed. The `postResolutionChecks` method ensures that all configured child blocks are used in at least one blueprint and vice versa by collecting unique child blocks from blueprints and verifying their presence in the configuration. Here are some specific error messages logged during Zon parsing:

- Missing 'blueprints' field: `std.log.err("['{s}'] Missing 'blueprints' field.", .{stringId});`
- Invalid type for 'blueprints': `std.log.err("['{s}'] 'blueprints' field must contain a list.", .{stringId});`
- Empty 'blueprints' list: `std.log.err("['{s}'] Empty 'blueprints' list not allowed.", .{stringId});`
- Invalid blueprint configuration (object expected, got {s}): `std.log.err("Invalid blueprint configuration (object expected, got {s}).", .{configType});`
- Blueprint entry must be an object: `std.log.err("Blueprint entry must be an object, found {s}.", .{entryType});`
- Child ID can not be null: `std.log.err("['{s}'] None of the blueprints contains a child '{s}' but configuration for it was specified.", .{self.id, @as(LocalBlockIndex, @enumFromInt(childBlockIndex)).name()});`

## Code Example
```zig
fn postResolutionChecks(self: StructureBuildingBlock) void {
	// Collect all unique child blocks used in blueprints of this SBB.
	var childBlocksInBlueprints: List(LocalBlockIndex) = .empty;
	defer childBlocksInBlueprints.deinit(main.stackAllocator);

	for (self.blueprints.items, 0..) |blueprints, blueprintIndex| {
		if (blueprints.items == null) continue;

		for (blueprints.items.?[0].childBlocks) |child| {
			if (std.mem.containsAtLeastScalar(LocalBlockIndex, childBlocksInBlueprints.items, 1, child.index)) continue;
			childBlocksInBlueprints.append(main.stackAllocator, child.index);
			// Check that all child blocks present in any of the blueprints have corresponding configurations.
			if (self.children[@intFromEnum(child.index)] != null) continue;
			std.log.err("['{s}'] Blueprint ({}) requires child block {s} but no configuration was specified for it.", .{self.id, blueprintIndex, child.id()});
		}
	}
	// Check that all configured child blocks are used somewhere in one of the blueprints.
	for (self.children, 0..) |child, childBlockIndex| {
		if (child == null) continue;
		if (std.mem.containsAtLeastScalar(LocalBlockIndex, childBlocksInBlueprints.items, 1, @enumFromInt(childBlockIndex))) continue;
		std.log.err("['{s}'] None of the blueprints contains a child '{s}' but configuration for it was specified.", .{self.id, @as(LocalBlockIndex, @enumFromInt(childBlockIndex)).name()});
	}
}
```

## Related Questions
-  What is the purpose of the `initFromZon` method in the `StructureBuildingBlock` struct?
-  How does the `postResolutionChecks` method ensure that all child blocks are correctly configured?
-  What error handling is implemented when parsing blueprints from Zon data?
-  How does the `getBlueprints` method sample blueprints based on a seed?
-  What is the role of the `getChildStructure` method in retrieving child structures?
-  What fields does the `StructureBuildingBlock` struct contain?
-  How are errors logged when parsing Zon elements for `StructureBuildingBlock` initialization?
-  What checks are performed to ensure that all configured child blocks are used in blueprints?
-  How is memory management handled within the `initFromZon` method?
-  What is the relationship between blueprints and child structures in the `StructureBuildingBlock`?

*Source: unknown | chunk_id: codebase_src_server_terrain_sbb.zig_chunk_2*
