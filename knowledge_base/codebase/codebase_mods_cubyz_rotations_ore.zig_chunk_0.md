# [easy/codebase_mods_cubyz_rotations_ore.zig] - Chunk 0

**Type:** implementation
**Keywords:** block models, ore blocks, model caching, block data formatting, rotation logic
**Symbols:** modelCache, init, deinit, reset, createBlockModel, generateData, modifyBlock, canBeChangedInto, onBlockBreaking, formatBlockData
**Concepts:** block model creation, block modification, rotation and ore handling

## Summary
Rotations and ore block model creation

## Explanation
This chunk defines functions for creating block models based on ore data, handling block modification, checking if a block can be changed into another type, and formatting block data. It also includes initialization and deinitialization functions.

## Code Example
```zig
pub fn createBlockModel(block: Block, _: *u16, zon: ZonElement) ModelIndex {
	const modelId = zon.as([]const u8) orelse blk: {
		std.log.err("Invalid model data for block {s} found {s}, expected string", .{block.id(), @tagName(zon)});
		break :blk "cubyz:cube";
	};
	if (!std.mem.eql(u8, modelId, "cubyz:cube")) {
		std.log.err("Ores can only be use on cube models, found '{s}'", .{modelId});
	}
	if (modelCache) |modelIndex| return modelIndex;

	const baseModel = main.models.getModelIndex("cubyz:cube").model();
	var quadList = main.ListManaged(main.models.QuadInfo).init(main.stackAllocator);
	defer quadList.deinit();
	baseModel.getRawFaces(&quadList);
	const len = quadList.items.len;
	for (0..len) |i| {
		quadList.append(quadList.items[i]);
		quadList.items[i + len].textureSlot += 16;
		quadList.items[i].opaqueInLod = 2;
	}
	const modelIndex = main.models.Model.init(quadList.items);
	modelCache = modelIndex;
	return modelIndex;
}
```

## Related Questions
- What is the purpose of the `modelCache` variable?
- How does the `createBlockModel` function handle invalid model data for blocks?
- Can you explain how the `modifyBlock` function checks if a block can be changed into another type?
- What is the logic behind the `onBlockBreaking` function?
- How does the `formatBlockData` function format block data?
- What are the conditions under which the `canBeChangedInto` function returns `.yes_costsItems = 1`?
- What happens if a block's data is not zero when it is modified?
- How does the `generateData` function handle block generation?
- What is the purpose of the `reset` function?
- Can you explain how the `createBlockModel` function handles cube models specifically?
- What are the conditions under which the `modifyBlock` function returns false?
- What is the logic behind the `onBlockBreaking` function when a block's data is set to zero?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_ore.zig_chunk_0*
