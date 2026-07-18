# [medium/codebase_src_entityModel.zig] - Chunk 1

**Type:** api
**Keywords:** struct, initialization, deinitialization, cloning, memory allocation, error handling, vertex format
**Symbols:** EntityModel, EntityModel.height, EntityModel.texturePath, EntityModel.modelId, EntityModel.entityModelId, EntityModel.nodeIndexMap, EntityModel.nodes, EntityModel.nodeParents, EntityModel.nodePivots, EntityModel.vao, EntityModel.indexCount, EntityModel.defaultTexture, EntityModel.coordinateSystem, EntityModel.Node, EntityModel.Node.pos, EntityModel.Node.rot, EntityModel.Node.scale, EntityModel.Node.recalc, EntityModel.Vertex, EntityModel.Vertex.pos, EntityModel.Vertex.normal, EntityModel.Vertex.uv, EntityModel.Vertex.nodeId, EntityModel.Vertex.attributeDescriptions, EntityModel.init, EntityModel.deinit, EntityModel.cloneMetaData, EntityModel.loadModelAndTexture
**Concepts:** entity ECS, model loading, texture handling

## Summary
Defines the EntityModel struct and its associated methods for initialization, deinitialization, cloning metadata, and loading models and textures.

## Explanation
The EntityModel struct represents a model of an entity in the game, including properties like height, texture path, model ID, nodes, and coordinate system. It contains methods for initializing the model from a ZonElement, deinitializing resources, cloning metadata, and loading both the model and its associated texture. The Node struct within EntityModel handles transformations with position, rotation, and scale. The Vertex struct defines the vertex format used in rendering. The init function sets up the entity model based on data from a ZonElement, handling optional fields such as initializing `modelId`, `texturePath`, and other properties using the world arena allocator. If the 'defaultTexture' field exists in the ZonElement, it constructs the texture path based on the provided asset folder and module name. The deinit function releases resources like textures and vertex arrays. The cloneMetaData function creates a deep copy of the entity model's metadata. The loadModelAndTexture function loads the texture and model file, with error handling for missing model specifications.

## Code Example
```zig
pub fn init(assetFolder: []const u8, entityModelId: []const u8, index: EntityModelIndex, zon: ZonElement) EntityModel {
	var self: EntityModel = undefined;
	if (zon.get([]const u8, "model")) |modelId| {
		self.modelId = main.worldArena.dupe(u8, modelId);
	} else {
		self.modelId = null;
	}
	self.entityModelId = main.worldArena.dupe(u8, entityModelId);
	self.height = zon.get(f32, "height") orelse 1;
	self.defaultTexture = null;
	self.vao = null;
	self.indexCount = 0;
	self.coordinateSystem = zon.get(CoordinateSystem, "coordinateSystem") orelse .right_handed_z_up;

	self.nodeIndexMap = .init(main.worldArena.allocator);
	self.nodes = &.{};
	self.nodeParents = &.{};
	self.nodePivots = &.{};
	self.nodeCount = 0;

	var isPlayerModel = false;
	const tags = main.Tag.loadTagsFromZon(main.worldArena, zon.getChild("tags"));
	for (tags) |tag| {
		if (tag == .playerModel) {
			isPlayerModel = true;
		}
	}

	if (isPlayerModel) {
		playerEntityModels.append(main.worldArena, index);
	}

	// get TexturePath
	{
		self.texturePath = &.{};
		const fileEnding = ".png";
		if (zon.get([]const u8, "defaultTexture")) |texture| {
			var split = std.mem.splitScalar(u8, texture, ':');
			const mod = split.first();
			const textureName = split.next().?;
			self.texturePath = std.fmt.allocPrint(main.worldArena.allocator, "{s}/{s}/entity_models/textures/{s}{s}", .{assetFolder, mod, textureName, fileEnding}) catch unreachable;
			main.files.cubyzDir().dir.access(main.io, self.texturePath, .{}) catch {
				main.worldArena.free(self.texturePath);
				self.texturePath = std.fmt.allocPrint(main.worldArena.allocator, "assets/{s}/entity_models/textures/{s}{s}", .{mod, textureName, fileEnding}) catch unreachable;
			};
		}
	}
	return self;
}
```

## Related Questions
- What is the purpose of the EntityModel struct?
- How does the init function handle optional fields in the ZonElement?
- What resources are released by the deinit function?
- How is metadata cloned in the cloneMetaData function?
- What steps are involved in loading a model and texture in the loadModelAndTexture function?
- What transformations can be applied to nodes within an EntityModel?

*Source: unknown | chunk_id: codebase_src_entityModel.zig_chunk_1*
