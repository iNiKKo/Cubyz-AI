# [medium/codebase_src_server_terrain_simple_structures_SimpleTreeModel.zig] - Chunk 0

**Type:** world_generation
**Keywords:** block generation, tree structure, voxel world, randomization, chunk update
**Symbols:** SimpleTreeModel, SimpleTreeModel.typ, SimpleTreeModel.leavesBlock, SimpleTreeModel.woodBlock, SimpleTreeModel.woodRotationModeType, SimpleTreeModel.topWoodBlock, SimpleTreeModel.topRotationModeType, SimpleTreeModel.height0, SimpleTreeModel.deltaHeight, SimpleTreeModel.leafRadius, SimpleTreeModel.deltaLeafRadius, SimpleTreeModel.leafElongation, SimpleTreeModel.deltaLeafElongation, SimpleTreeModel.branched, loadModel, initalOrientation, addNeighbor, generateStem, generateBranch
**Concepts:** chunk meshing, entity ECS, world generation, networking protocol

## Summary
Defines the SimpleTreeModel for generating simple tree structures in the Cubyz voxel engine.

## Explanation
The SimpleTreeModel struct is responsible for defining and generating simple tree structures within the game world. It includes various parameters such as type (pyramid or round), leavesBlock, woodBlock, topWoodBlock, height0, deltaHeight, leafRadius, deltaLeafRadius, leafElongation, deltaLeafElongation, branched, woodRotationModeType, and topRotationModeType.

The loadModel function initializes a SimpleTreeModel from configuration parameters with default values for missing fields: height = 6, deltaHeight = 3, leafRadius = ((1 + height) / 2), deltaLeafRadius = (deltaHeight / 2), leafElongation = 1, and deltaLeafElongation = 0. The initalOrientation function adjusts block orientations based on rotation modes (log, branch, direction), while the addNeighbor function adds neighbors to blocks if they are branched.

The generateStem function generates the main trunk of the tree with optional branches added probabilistically, and the generateBranch function adds side branches to the tree. Specifically, leafRadius is calculated as ((1 + height) / 2) when no specific value is provided, and deltaLeafRadius is calculated based on the default or provided deltaHeight value. Similarly, leafElongation defaults to 1 if not specified.

The orientation of blocks is determined by the initalOrientation function, which sets the block's data field based on the rotation mode (log, branch, direction). The generateStem and generateBranch functions ensure that generated trees fit within the game's voxel chunks by checking if the coordinates lie within the chunk bounds before updating the blocks.

The SimpleTreeModel also includes a generation algorithm for branches. Branches are added probabilistically based on the height of the tree. The probability decreases as the branch is higher up in the tree. The direction of the branch is randomly chosen from four possible directions (up, down, left, right).

In addition to these parameters and functions, the SimpleTreeModel also includes a method for updating blocks if they are degradable. This ensures that trees can be destroyed by players or other entities without causing issues with the game world.

Overall, the SimpleTreeModel is a powerful tool for generating complex tree structures in the Cubyz voxel engine. It provides a wide range of parameters and functions to customize the appearance and behavior of trees, making it easy to create a variety of different environments within the game.

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
- How does the SimpleTreeModel generate branches?
- What parameters are used to define a tree in the SimpleTreeModel?
- How is the orientation of blocks determined in the SimpleTreeModel?
- Can you explain the role of randomization in generating trees with the SimpleTreeModel?
- How does the SimpleTreeModel ensure that generated trees fit within the game's voxel chunks?
- What are the different types of tree structures that can be generated using the SimpleTreeModel?

*Source: unknown | chunk_id: codebase_src_server_terrain_simple_structures_SimpleTreeModel.zig_chunk_0*
