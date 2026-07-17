# [hard/codebase_src_blocks.zig] - Chunk 1

**Type:** api
**Keywords:** block registration, property initialization, zon configuration, drop processing, tag handling
**Symbols:** _collide, _id, _blockHealth, _blockResistance, _replaceable, _selectionCapabilities, _blockDrops, _degradable, _viewThrough, _alwaysViewThrough, _hasBackFace, _tags, _light, _absorption, _onInteract, _onBreak, _onUpdate, _mode, _modeData, _lodReplacement, _opaqueVariant, _friction, _bounciness, _density, _terminalVelocity, _mobility, _allowOres, _onTick, _onTouch, _blockEntity, reverseIndices, size, ores, register, loadBlockDrop
**Concepts:** block registration, block properties, resource drops, interaction callbacks

## Summary
This chunk manages the registration and properties of blocks in the Cubyz voxel engine, including their physical attributes, interactions, and resource drops.

## Explanation
The chunk defines several global arrays to store various properties of blocks, such as health, resistance, tags, and callbacks for interactions. The `register` function initializes these properties based on data provided in a ZonElement configuration. It also handles special cases like ore registration and block entity associations. The `loadBlockDrop` function processes the drop configurations for blocks, parsing item details and allowed tool tags.

## Code Example
```zig
pub fn register(_: []const u8, id: []const u8, zon: ZonElement) u16 {
	_id[size] = main.worldArena.dupe(u8, id);
	reverseIndices.put(main.worldArena.allocator, _id[size], @intCast(size)) catch unreachable;

	_mode[size] = rotation.getByID(zon.get([]const u8, "rotation") orelse "cubyz:no_rotation");
	_blockHealth[size] = zon.get(f32, "blockHealth") orelse 1;
	_blockResistance[size] = zon.get(f32, "blockResistance") orelse 0;
	const rotation_tags = _mode[size].getBlockTags();
	const block_tags = Tag.loadTagsFromZon(main.stackAllocator, zon.getChild("tags"));
	defer main.stackAllocator.free(block_tags);
	_tags[size] = std.mem.concat(main.worldArena.allocator, Tag, &.{rotation_tags, block_tags}) catch unreachable;

	if (_tags[size].len == 0) std.log.err("Block {s} is missing 'tags' field", .{id});
	for (_tags[size]) |tag| {
		if (tag == Tag.sbbChild) {
			sbb.registerChildBlock(@intCast(size), _id[size]);
			break;
		}
	}

	_light[size] = zon.get(u32, "emittedLight") orelse 0;
	_absorption[size] = zon.get(u32, "absorbedLight") orelse 0xffffff;
	_degradable[size] = zon.get(bool, "degradable") orelse false;

	if (zon.getChildOrNull("selectionCapabilities")) |capabilitiesZon| {
		_selectionCapabilities[size] = .loadFromZon(capabilitiesZon);
	} else {
		_selectionCapabilities[size] = .always;
	}

	_replaceable[size] = zon.get(bool, "replaceable") orelse false;
	_transparent[size] = zon.get(bool, "transparent") orelse false;
	_collide[size] = zon.get(bool, "collide") orelse true;
	_alwaysViewThrough[size] = zon.get(bool, "alwaysViewThrough") orelse false;
	_viewThrough[size] = (zon.get(bool, "viewThrough") orelse false) or _transparent[size] or _alwaysViewThrough[size];
	_hasBackFace[size] = zon.get(bool, "hasBackFace") orelse false;
	_friction[size] = zon.get(f32, "friction") orelse 20;
	_bounciness[size] = zon.get(f32, "bounciness") orelse 0.0;
	_density[size] = zon.get(f32, "density") orelse main.physics.airDensity;
	_terminalVelocity[size] = zon.get(f32, "terminalVelocity") orelse 90;
	_mobility[size] = zon.get(f32, "mobility") orelse 1.0;
	_allowOres[size] = zon.get(bool, "allowOres") orelse false;

	_blockEntity[size] = block_entity.getByID(zon.get([]const u8, "blockEntity"));

	const oreProperties = zon.getChild("ore");
	if (oreProperties != .null) blk: {
		if (!std.mem.eql(u8, zon.get([]const u8, "rotation") orelse "", "cubyz:ore")) {
			std.log.err("Ore must have rotation mode \"cubyz:ore\"!", .{});
			break :blk;
		}
		ores.append(main.worldArena, .{
			.veins = oreProperties.get(f32, "veins") orelse 0,
			.size = oreProperties.get(f32, "size") orelse 0,
			.maxHeight = oreProperties.get(i32, "maxHeight") orelse std.math.maxInt(i32),
			.minHeight = oreProperties.get(i32, "minHeight") orelse std.math.minInt(i32),
			.density = oreProperties.get(f32, "density") orelse 0.5,
			.blockType = @intCast(size),
			.seed = std.hash.Wyhash.hash(0, id),
		});
	}

	defer size += 1;
	std.log.debug("Registered block: {d: >5} '{s}'", .{size, id});
	return @intCast(size);
}
```

## Related Questions
- How does the `register` function handle the registration of a new block?
- What properties are initialized for each block during registration?
- How does the `loadBlockDrop` function process item drops for blocks?
- What is the purpose of the `reverseIndices` map in this chunk?
- How are ore-specific properties handled during block registration?
- synthetic_queries_response_1: The `register` function initializes various properties of a new block based on data provided in a ZonElement configuration. It sets up global arrays to store these properties and handles special cases like ore registration and block entity associations.
- synthetic_queries_response_2: During block registration, several properties are initialized, including health, resistance, tags, callbacks for interactions, and physical attributes such as friction, bounciness, density, terminal velocity, and mobility. These properties are stored in global arrays for easy access throughout the engine.
- synthetic_queries_response_3: The `loadBlockDrop` function processes item drops for blocks by parsing item details from a ZonElement configuration. It handles multiple items per drop, parses amounts, and associates allowed tool tags with each drop.
- synthetic_queries_response_4: The `reverseIndices` map is used to quickly look up block IDs based on their string representations. This allows for efficient access to block properties without needing to search through the global arrays.
- synthetic_queries_response_5: During block registration, ore-specific properties are handled by checking if the block has an 'ore' child in its ZonElement configuration. If it does, the function registers the block as an ore and initializes its ore-related properties such as vein density, size, height range, and seed.

*Source: unknown | chunk_id: codebase_src_blocks.zig_chunk_1*
