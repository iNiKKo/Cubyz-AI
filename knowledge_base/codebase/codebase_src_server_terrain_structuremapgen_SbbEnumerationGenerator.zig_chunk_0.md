# [medium/codebase_src_server_terrain_structuremapgen_SbbEnumerationGenerator.zig] - Chunk 0

**Type:** implementation
**Keywords:** structure building blocks, terrain generation, reachability, ID sorting, block initialization
**Symbols:** id, priority, generatorSeed, defaultState, sbbList, signBlock, init
**Concepts:** structure building blocks (SBBs), terrain generation, reachability checking, sorting by ID, block initialization

## Summary
The chunk initializes and manages the enumeration of structure building blocks (SBBs) for terrain generation.

## Explanation
This chunk is responsible for initializing a list of SBBs, marking them based on their parent-child relationships, ensuring all structures are reachable, sorting them by ID, and preparing them for generation. It also initializes a sign block used in the process. The `init` function handles most of this logic, including iterating over SBBs, checking reachability, and setting up structure data models.

## Code Example
```zig
pub fn init(parameters: ZonElement) void {
	_ = parameters;

	const Entry = struct { sbb: *const StructureBuildingBlock, hasParent: bool, reachable: bool };
	var localSbbList: main.List(Entry) = .empty;
	defer localSbbList.deinit(main.stackAllocator);
	for (terrain.sbb.list()) |*entry| {
		localSbbList.append(main.stackAllocator, .{.sbb = entry, .hasParent = false, .reachable = false});
	}

	{ // Mark all SBBs that are children of other SBBs.
		outer: for (localSbbList.items) |*candidate| {
			for (localSbbList.items) |other| {
				if (other.sbb == candidate.sbb) continue;
				for (other.sbb.children) |child| {
					if (child == candidate.sbb) {
						candidate.hasParent = true;
						continue :outer;
					}
				}
			}
		}
	}
	var rootSbbList: main.List(*const StructureBuildingBlock) = .initCapacity(main.stackAllocator, localSbbList.items.len);
	defer rootSbbList.deinit(main.stackAllocator);
	{ // Ensure that every structure was reachable (in case of recursion)
		var unreachables: main.List(*Entry) = .initCapacity(main.stackAllocator, localSbbList.items.len);
		defer unreachables.deinit(main.stackAllocator);

		for (localSbbList.items) |*candidate| {
			if (candidate.hasParent) {
				unreachables.appendAssumeCapacity(candidate);
			} else {
				candidate.reachable = true;
				rootSbbList.appendAssumeCapacity(candidate.sbb);
			}
		}

		while (unreachables.items.len != 0) {
			var lastLen: usize = 0;
			while (lastLen != unreachables.items.len) {
				lastLen = unreachables.items.len;
				var i: usize = 0;
				outer: while (i < unreachables.items.len) {
					const candidate = unreachables.items[i];
					for (localSbbList.items) |other| {
						if (!other.reachable) continue;
						for (other.sbb.children) |child| {
							if (child == candidate.sbb) {
								candidate.reachable = true;
								_ = unreachables.swapRemove(i);
								continue :outer;
							}
						}
					}
					i += 1;
				}
			}
			const recursiveOne = unreachables.popOrNull() orelse break;
			recursiveOne.reachable = true;
			rootSbbList.appendAssumeCapacity(recursiveOne.sbb);
		}
	}

	std.sort.insertion(*const StructureBuildingBlock, rootSbbList.items, {}, struct {
		fn lessThanFn(_: void, lhs: *const StructureBuildingBlock, rhs: *const StructureBuildingBlock) bool {
			return std.ascii.orderIgnoreCase(lhs.id, rhs.id) == .lt;
		}
	}.lessThanFn);

	sbbList = main.worldArena.alloc(main.server.terrain.biomes.SimpleStructureModel, rootSbbList.items.len);

	for (rootSbbList.items, 0..) |sbb, i| {
		const structureData = main.worldArena.create(SbbGen);
		structureData.* = .{
			.structureRef = sbb,
			.placeMode = .all,
			.rotation = .{.fixed = .@"0"},
		};
		sbbList[i] = .{
			.chance = undefined,
			.generationMode = .floor,
			.priority = 1.0,
			.vtable = .{
				.generate = main.meta.castFunctionSelfToAnyopaque(SbbGen.generate),
				.generationMode = .floor,
				.hashFunction = undefined,
				.loadModel = undefined,
			},
			.data = structureData,
		};
	}

	signBlock.typ = main.blocks.getBlockById("cubyz:sign/oak") catch |err| blk: {
		std.log.err("Could not find sign with id cubyz:sign/oak: {s}", .{@errorName(err)});
		break :blk 0;
	};
	signBlock.data = 6;
}
```

## Related Questions
- What is the purpose of the `init` function in this chunk?
- How does the chunk determine if an SBB has a parent?
- What happens to unreachable SBBs during initialization?
- How are SBBs sorted after initialization?
- What block ID is used for the sign block, and how is it handled if not found?
- Where is the `generatorSeed` defined and what is its value?

*Source: unknown | chunk_id: codebase_src_server_terrain_structuremapgen_SbbEnumerationGenerator.zig_chunk_0*
