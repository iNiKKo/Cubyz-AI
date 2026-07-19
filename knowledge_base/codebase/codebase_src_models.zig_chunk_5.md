# [hard/codebase_src_models.zig] - Chunk 5

**Type:** implementation
**Keywords:** model initialization, deinitialization, face retrieval, model merging, transformation function, quad appending, memory management
**Symbols:** Model, Model.init, Model.deinit, Model.getRawFaces, Model.mergeModels, Model.transformModel, Model.appendQuadsToList, Model.appendInternalQuadsToList, Model.appendNeighborFacingQuadsToList
**Concepts:** model data processing, quad management, memory allocation, face retrieval, model transformation

## Summary
Handles model data processing including initialization, deinitialization, face retrieval, merging, transformation, and appending quads to lists.

## Explanation
This chunk defines the `Model` struct with methods for managing its internal quad information. It includes functions for initializing (`init`) and deinitializing (`deinit`) models, retrieving raw faces (`getRawFaces`), merging multiple models into one (`mergeModels`), transforming a model using a provided function (`transformModel`), and appending quads to lists (`appendQuadsToList`, `appendInternalQuadsToList`, `appendNeighborFacingQuadsToList`). The chunk also contains utility functions for processing vertices, normals, UVs, and texture slots. It manages memory allocation and deallocation using the global allocator.

The `init` function initializes the `Model` struct by setting up its internal quad information based on the provided vertices, normals, uvs, and faces. Specifically, it appends `QuadInfo` structs to the `quadInfos` list with details such as normal vectors, corner positions, UV coordinates, and texture slots.

The `deinit` function frees all allocated memory for the model's quads and collision data by iterating over arrays of quad indices and freeing each one using the global allocator.

The `getRawFaces` function retrieves raw face data from the model, including both internal and neighbor-facing quads. It appends these faces to a provided list, adjusting corner positions for neighbor-facing quads by adding the normal vector.

The `mergeModels` function combines multiple models into a single model by appending their quad information to a list. This is done using the `getRawFaces` method of each model in the input list.

The `transformModel` function applies a transformation function to each quad in the model. It uses Zig's `@call` function to dynamically call the provided transformation function with parameters including the quad and any additional transform function parameters.

The `appendQuadsToList`, `appendInternalQuadsToList`, and `appendNeighborFacingQuadsToList` functions append quads to a list, with specific handling for internal and neighbor-facing quads. The `appendQuadsToList` function appends `QuadInfo` structs to the provided list, adjusting corner positions if necessary.

## Code Example
```zig
fn deinit(self: *const Model) void {
	for (0..6) |i| {
		main.globalAllocator.free(self.neighborFacingQuads[i]);
	}
	main.globalAllocator.free(self.internalQuads);
	main.globalAllocator.free(self.collision);
}
```

## Related Questions
- How does the `Model` struct initialize its quad information?
- What is the purpose of the `deinit` function in the `Model` struct?
- How are raw faces retrieved from a model instance?
- How do multiple models get merged into one using the `mergeModels` function?
- What is the role of the `transformModel` function in modifying a model?
- How are quads appended to a list using the `appendQuadsToList` function?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_5*
