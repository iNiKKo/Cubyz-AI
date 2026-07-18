# [hard/codebase_src_models.zig] - Chunk 7

**Type:** implementation
**Keywords:** model registration, quad generation, resource initialization, GPU buffer, deinitialization
**Symbols:** box, openBox, registerModel, init, reset, deinit, uploadModels
**Concepts:** model management, voxel models, quad generation, GPU buffer upload

## Summary
This chunk defines functions for creating and managing voxel models, including box and open box generation, model registration, initialization, reset, deinitialization, and uploading to GPU.

## Explanation
The chunk contains several functions related to voxel model management. The `box` function generates six quads representing a closed box with specified minimum and maximum corners and UV offset. The `openBox` function creates a box with one side removed based on the `openSide` parameter. The `registerModel` function loads a model from data, associates it with an ID, and stores it in a map. The `init`, `reset`, and `deinit` functions handle initialization, resetting to default state, and deinitialization of resources respectively. The `uploadModels` function uploads the quad information to a GPU buffer for rendering.

## Code Example
```zig
fn box(min: Vec3f, max: Vec3f, uvOffset: Vec2f) [6]QuadInfo {
	const corner000: Vec3f = .{min[0], min[1], min[2]};
	const corner001: Vec3f = .{min[0], min[1], max[2]};
	const corner010: Vec3f = .{min[0], max[1], min[2]};
	const corner011: Vec3f = .{min[0], max[1], max[2]};
	const corner100: Vec3f = .{max[0], min[1], min[2]};
	const corner101: Vec3f = .{max[0], min[1], max[2]};
	const corner110: Vec3f = .{max[0], max[1], min[2]};
	const corner111: Vec3f = .{max[0], max[1], max[2]};
	return .{
		.{
			.normal = .{-1, 0, 0},
			.corners = .{corner010, corner011, corner000, corner001},
			.cornerUV = .{uvOffset + Vec2f{1 - max[1], min[2]}, uvOffset + Vec2f{1 - max[1], max[2]}, uvOffset + Vec2f{1 - min[1], min[2]}, uvOffset + Vec2f{1 - min[1], max[2]}},
			.textureSlot = Neighbor.dirNegX.toInt(),
		},
		.{
			.normal = .{1, 0, 0},
			.corners = .{corner100, corner101, corner110, corner111},
			.cornerUV = .{uvOffset + Vec2f{min[1], min[2]}, uvOffset + Vec2f{min[1], max[2]}, uvOffset + Vec2f{max[1], min[2]}, uvOffset + Vec2f{max[1], max[2]}},
			.textureSlot = Neighbor.dirPosX.toInt(),
		},
		.{
			.normal = .{0, -1, 0},
			.corners = .{corner000, corner001, corner100, corner101},
			.cornerUV = .{uvOffset + Vec2f{min[0], min[2]}, uvOffset + Vec2f{min[0], max[2]}, uvOffset + Vec2f{max[0], min[2]}, uvOffset + Vec2f{max[0], max[2]}},
			.textureSlot = Neighbor.dirNegY.toInt(),
		},
		.{
			.normal = .{0, 1, 0},
			.corners = .{corner110, corner111, corner010, corner011},
			.cornerUV = .{uvOffset + Vec2f{1 - max[0], min[2]}, uvOffset + Vec2f{1 - max[0], max[2]}, uvOffset + Vec2f{1 - min[0], min[2]}, uvOffset + Vec2f{1 - min[0], max[2]}},
			.textureSlot = Neighbor.dirPosY.toInt(),
		},
		.{
			.normal = .{0, 0, -1},
			.corners = .{corner010, corner000, corner110, corner100},
			.cornerUV = .{uvOffset + Vec2f{min[0], 1 - max[1]}, uvOffset + Vec2f{min[0], 1 - min[1]}, uvOffset + Vec2f{max[0], 1 - max[1]}, uvOffset + Vec2f{max[0], 1 - min[1]}},
			.textureSlot = Neighbor.dirDown.toInt(),
		},
		.{
			.normal = .{0, 0, 1},
			.corners = .{corner111, corner101, corner011, corner001},
			.cornerUV = .{uvOffset + Vec2f{1 - max[0], 1 - max[1]}, uvOffset + Vec2f{1 - max[0], 1 - min[1]}, uvOffset + Vec2f{1 - min[0], 1 - max[1]}, uvOffset + Vec2f{1 - min[0], 1 - min[1]}},
			.textureSlot = Neighbor.dirUp.toInt(),
		},
	};
}
```

## Related Questions
- How does the `box` function generate quads for a closed box?
- What is the purpose of the `openBox` function and how does it differ from `box`?
- How are models registered in the system using the `registerModel` function?
- What steps are involved in initializing the model management system with `init`?
- How does the `reset` function restore the model system to its default state?
- What resources are deinitialized by the `deinit` function and how is it done?

*Source: unknown | chunk_id: codebase_src_models.zig_chunk_7*
