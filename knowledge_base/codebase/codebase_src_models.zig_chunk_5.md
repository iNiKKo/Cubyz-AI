# [hard/codebase_src_models.zig] - Chunk 5

**Type:** implementation
**Keywords:** memory management, quad deduplication, model transformation, face data, light sampling
**Symbols:** Model, QuadInfo, ExtraQuadInfo, FaceData, ModelIndex, getModelIndex, quads, extraQuadInfos, models, quadDeduplication
**Concepts:** model management, quad handling, memory allocation, lighting calculations

## Summary
Handles model creation, transformation, and face data management.

## Explanation
This chunk defines the `Model` struct with methods for initialization, deinitialization, retrieving raw faces, merging models, transforming models, and appending quads to a list. It also includes functions for managing quad deduplication and retrieving model indices by name. The code handles memory allocation and deallocation using `main.globalAllocator`, manages lists of quads and extra quad information, and performs operations like checking for degenerate quads and calculating light samples.

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
- How does the `Model` struct handle memory deallocation?
- What is the purpose of the `addQuad` function?
- How are degenerate quads detected in this code?
- What operations does the `transformModel` function perform?
- How are face data appended to a list in this chunk?
- What is the role of the `quadDeduplication` map?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_5*
