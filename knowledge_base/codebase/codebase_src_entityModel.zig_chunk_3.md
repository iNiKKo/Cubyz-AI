# [medium/codebase_src_entityModel.zig] - Chunk 3

**Type:** api
**Keywords:** entity models, initialization, resetting, retrieval by ID, loading textures
**Symbols:** entityModels, reverseIndices, playerEntityModels
**Concepts:** entity ECS, model management

## Summary
Handles entity models, including initialization, resetting, retrieval by ID, and loading of models and textures.

## Explanation
This chunk manages the lifecycle of entity models within the Cubyz engine. It includes functions to append new models, reset all models, retrieve a model index by its ID, provide a default model if none is available, and load both models and their associated textures. The `reset` function deinitializes all models and clears internal data structures. The `getById` function searches for an entity model by its ID using a reverse index map. The `default` function ensures that there is always a fallback model available. The `loadModelsAndTexture` function attempts to load each model's texture, and if it fails, it replaces the model with a default one and retries loading.

## Code Example
```zig
pub fn reset() void {
	for (entityModels.items) |*model| {
		model.deinit();
	}
	entityModels = .empty;
	reverseIndices = .{};
	playerEntityModels = .empty;
}
```

## Related Questions
- How do you append a new entity model?
- What does the reset function do in this chunk?
- How is an entity model retrieved by its ID?
- What happens if a default entity model cannot be found?
- How are models and textures loaded for each entity?
- What data structures are used to manage entity models?

*Source: unknown | chunk_id: codebase_src_entityModel.zig_chunk_3*
