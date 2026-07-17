# [medium/codebase_src_server_terrain_structures.zig] - Chunk 0

**Type:** implementation
**Keywords:** SimpleStructureModel, StructureTable, generation modes, ZonElement, registration process
**Symbols:** SimpleStructureModel, SimpleStructureModel.GenerationMode, SimpleStructureModel.VTable, SimpleStructureModel.initModel, SimpleStructureModel.generate, SimpleStructureModel.getHash, StructureTable, StructureTable.id, StructureTable.tags, StructureTable.structures, StructureTable.init, register, registerStructureTables, compareStructureTables, finishLoading, simple_structures
**Concepts:** terrain structures, structure generation, ZonElement configuration

## Summary
Defines the SimpleStructureModel and StructureTable for managing terrain structures in a server environment.

## Explanation
This chunk defines two main types: SimpleStructureModel and StructureTable. SimpleStructureModel represents a model for generating simple structures with various generation modes, including floor, ceiling, air, underground, and water surface. It includes methods for initialization, generation, and hash calculation. The StructureTable manages multiple SimpleStructureModels, allowing them to be registered and loaded from ZonElement configurations. The chunk also provides functions for registering structure tables and finishing the loading process.

## Code Example
```zig
pub fn initModel(parameters: ZonElement) ?SimpleStructureModel {
	const id = parameters.get([]const u8, "id") orelse "";
	const vtable = modelRegistry.get(id) orelse {
		std.log.err("Couldn't find structure model with id {s}", .{id});
		return null;
	};
	const vtableModel = vtable.loadModel(parameters) orelse {
		std.log.err("Error occurred while loading structure with id '{s}'. Dropping model from biome.", .{id});
		return null;
	};
	return SimpleStructureModel{
		.vtable = vtable,
		.data = vtableModel,
		.chance = parameters.get(f32, "chance") orelse 0.1,
		.priority = parameters.get(f32, "priority") orelse 1,
		.generationMode = std.meta.stringToEnum(GenerationMode, parameters.get([]const u8, "generationMode") orelse "") orelse vtable.generationMode,
	};
}
```

## Related Questions
- What are the different generation modes for SimpleStructureModel?
- How is a SimpleStructureModel initialized from ZonElement parameters?
- What does the StructureTable manage and how is it initialized?
- How are structure tables registered and what happens during registration?
- What is the purpose of the finishLoading function in this chunk?
- How does the code handle errors when loading structure models?

*Source: unknown | chunk_id: codebase_src_server_terrain_structures.zig_chunk_0*
