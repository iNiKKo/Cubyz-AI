# [hard/codebase_src_server_terrain_biomes.zig] - Chunk 3

**Type:** world_generation
**Keywords:** block parsing, memory allocation, terrain addition, depth calculation, random number generation
**Symbols:** BlockStructure, BlockStructure.BlockStack, BlockStructure.BlockStack.block, BlockStructure.BlockStack.min, BlockStructure.BlockStack.max, BlockStructure.BlockStack.init, BlockStructure.structure, BlockStructure.init, BlockStructure.deinit, BlockStructure.addSubTerranian
**Concepts:** terrain generation, biome structure

## Summary
Defines the structure of a biome's vertical ground, including parsing from configuration and adding terrain to chunks.

## Explanation
The `BlockStructure` struct represents the vertical layers of blocks in a biome. It contains an array of `BlockStack`, each specifying a block type and its depth range. The `init` function parses a ZonElement into a BlockStructure, allocating memory for the structure array and initializing each BlockStack from string descriptions. The `deinit` function frees the allocated memory. The `addSubTerranian` method adds terrain to a chunk based on the biome's block structure, considering depth, slope, and soil creep.

## Code Example
```zig
fn init(self: *BlockStack, string: []const u8) !void {
			var tokenIt = std.mem.tokenizeAny(u8, string, &std.ascii.whitespace);
			const first = tokenIt.next() orelse return error.@"String is empty.";
			var blockId: []const u8 = first;
			if (tokenIt.next()) |second| {
				self.min = try std.fmt.parseInt(u31, first, 0);
				if (tokenIt.next()) |third| {
					const fourth = tokenIt.next() orelse return error.@"Expected 1, 2 or 4 parameters, found 3.";
					if (!std.mem.eql(u8, second, "to")) return error.@"Expected layout '<min> to <max> <block>'. Missing 'to'.";
					self.max = try std.fmt.parseInt(u31, third, 0);
					blockId = fourth;
					if (tokenIt.next() != null) return error.@"Found too many parameters. Expected 1, 2 or 4.";
					if (self.max < self.min) return error.@"The max value must be bigger than the min value.";
				} else {
					self.max = self.min;
					blockId = second;
				}
			} else {
				self.min = 1;
				self.max = 1;
			}
			self.block = blocks.parseBlock(blockId);
		}
```

## Related Questions
- How is a BlockStructure initialized from a ZonElement?
- What does the `addSubTerranian` method do in detail?
- How are errors handled during the initialization of a BlockStack?
- What is the purpose of the `remainingSkippedBlocks` variable in `addSubTerranian`?
- How does the `BlockStructure` handle memory allocation and deallocation?
- What types of parameters does the `init` method for BlockStack expect?

*Source: unknown | chunk_id: codebase_src_server_terrain_biomes.zig_chunk_3*
