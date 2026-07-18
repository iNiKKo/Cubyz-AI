# [hard/codebase_src_models.zig] - Chunk 5

**Type:** implementation
**Keywords:** model initialization, deinitialization, face retrieval, model merging, transformation function, quad appending, memory management
**Symbols:** Model, Model.init, Model.deinit, Model.getRawFaces, Model.mergeModels, Model.transformModel, Model.appendQuadsToList, Model.appendInternalQuadsToList, Model.appendNeighborFacingQuadsToList
**Concepts:** model data processing, quad management, memory allocation, face retrieval, model transformation

## Summary
Handles model data processing including initialization, deinitialization, face retrieval, merging, transformation, and appending quads to lists.

## Explanation
This chunk defines the `Model` struct with methods for managing its internal quad information. It includes functions for initializing (`init`) and deinitializing (`deinit`) models, retrieving raw faces (`getRawFaces`), merging multiple models into one (`mergeModels`), transforming a model using a provided function (`transformModel`), and appending quads to lists (`appendQuadsToList`, `appendInternalQuadsToList`, `appendNeighborFacingQuadsToList`). The chunk also contains utility functions for processing vertices, normals, UVs, and texture slots. It manages memory allocation and deallocation using the global allocator.

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
