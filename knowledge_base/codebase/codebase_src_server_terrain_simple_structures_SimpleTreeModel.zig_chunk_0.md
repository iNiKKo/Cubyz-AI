# [medium/codebase_src_server_terrain_simple_structures_SimpleTreeModel.zig] - Chunk 0

**Type:** world_generation
**Keywords:** reference counting, binary serialization, mutex locking, tree generation, block placement, randomization
**Symbols:** SimpleTreeModel, SimpleTreeModel.typ, SimpleTreeModel.leavesBlock, SimpleTreeModel.woodBlock, SimpleTreeModel.woodRotationModeType, SimpleTreeModel.topWoodBlock, SimpleTreeModel.topRotationModeType, SimpleTreeModel.height0, SimpleTreeModel.deltaHeight, SimpleTreeModel.leafRadius, SimpleTreeModel.deltaLeafRadius, SimpleTreeModel.leafElongation, SimpleTreeModel.deltaLeafElongation, SimpleTreeModel.branched, loadModel, initalOrientation, addNeighbor, generateStem, generateBranch, generate
**Concepts:** chunk meshing, entity ECS, world generation, networking protocol

## Summary
The SimpleTreeModel struct defines a simple tree generation model for the Cubyz voxel engine, handling tree parameters, orientation, and generation logic.

## Explanation
The SimpleTreeModel struct encapsulates the logic for generating simple trees in the Cubyz voxel engine. It includes fields for defining the type of tree (pyramid or round), block types for leaves and wood, rotation modes, and various dimensions like height and leaf radius. The `loadModel` function initializes a SimpleTreeModel instance from configuration parameters. Methods like `initalOrientation`, `addNeighbor`, `generateStem`, and `generateBranch` handle the orientation and placement of tree blocks within chunks. The `generate` method orchestrates the overall tree generation process, considering factors such as height variation, leaf elongation, and branching probabilities.

## Code Example
```zig
pub fn loadModel(parameters: ZonElement) ?*SimpleTreeModel {
	const self = main.worldArena.create(SimpleTreeModel);
	const woodBlock = main.blocks.parseBlock(parameters.get([]const u8, "log") orelse {
		std.log.err("Missing required 'log' field for cubyz:simple_tree rotation", .{});
		return null;
	});
	self.* = .{
		.typ = std.meta.stringToEnum(Type, parameters.get([]const u8, "type") orelse "") orelse blk: {
			if (parameters.get([]const u8, "type")) |typ| std.log.err("Unknown tree type \"{s}\"", .{typ});
			break :blk .round;
		},
		.leavesBlock = main.blocks.parseBlock(parameters.get([]const u8, "leaves") orelse {
			std.log.err("Missing required 'leaves' field for cubyz:simple_tree rotation", .{});
			return null;
		}),
		.woodBlock = woodBlock,
		.topWoodBlock = blk: {
			break :blk main.blocks.parseBlock(parameters.get([]const u8, "top") orelse break :blk woodBlock);
		},
		.height0 = parameters.get(i32, "height") orelse 6,
		.deltaHeight = parameters.get(u31, "height_variation") orelse 3,
		.leafRadius = parameters.get(f32, "leafRadius") orelse ((1 + (parameters.get(f32, "height") orelse 6))/2),
		.deltaLeafRadius = parameters.get(f32, "leafRadius_variation") orelse ((parameters.get(f32, "height_variation") orelse 3)/2),
		.leafElongation = parameters.get(f32, "leafElongation") orelse 1,
		.deltaLeafElongation = parameters.get(f32, "deltaLeafElongation") orelse 0,
		.branched = parameters.get(bool, "branched") orelse true,
	};
	if (self.woodBlock.mode() == main.rotation.getByID("cubyz:branch")) self.woodRotationModeType = .branch;
	if (self.woodBlock.mode() == main.rotation.getByID("cubyz:log")) self.woodRotationModeType = .log;
	if (self.woodBlock.mode() == main.rotation.getByID("cubyz:direction")) self.woodRotationModeType = .direction;
	if (self.topWoodBlock.mode() == main.rotation.getByID("cubyz:branch")) self.topRotationModeType = .branch;
	if (self.topWoodBlock.mode() == main.rotation.getByID("cubyz:log")) self.topRotationModeType = .log;
	if (self.topWoodBlock.mode() == main.rotation.getByID("cubyz:direction")) self.topRotationModeType = .direction;
	return self;
}
```

## Related Questions
- How does the SimpleTreeModel handle tree orientation?
- What parameters are used to generate a simple tree in Cubyz?
- Can you explain the branching logic in the SimpleTreeModel?
- How is the height of the tree determined during generation?
- What role do randomization play in the tree generation process?
- How does the SimpleTreeModel ensure that trees fit within the available space?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_SimpleTreeModel.zig_chunk_0*
