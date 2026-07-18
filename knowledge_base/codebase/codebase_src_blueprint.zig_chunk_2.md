# [hard/codebase_src_blueprint.zig] - Chunk 2

**Type:** serialization
**Keywords:** blueprint loading, block mapping, compression, palette handling, world update
**Symbols:** Blueprint, Blueprint.PasteFlags, Blueprint.paste, Blueprint.load, Blueprint.store, makeBlueprintIdToGameIdMap, makeGameIdToBlueprintIdMap, loadBlockPalette, storeBlockPalette
**Concepts:** blueprint management, block serialization, world interaction

## Summary
Handles blueprint loading, storing, and pasting operations in the Cubyz voxel engine.

## Explanation
This chunk defines the Blueprint struct and its associated methods for loading, storing, and pasting blueprints. The `load` method reads a compressed blueprint from a buffer, decompresses it, and reconstructs the blueprint's blocks using a block palette. The `store` method converts the blueprint's blocks into a compressed format suitable for storage or transmission. The `paste` method places the blueprint's blocks into the world at a specified position, optionally preserving void blocks. Helper functions like `makeBlueprintIdToGameIdMap`, `makeGameIdToBlueprintIdMap`, `loadBlockPalette`, and `storeBlockPalette` manage block mappings and palette serialization.

## Code Example
```zig
pub fn paste(self: Blueprint, pos: Vec3i, flags: PasteFlags) void {
	const startX = pos[0];
	const startY = pos[1];
	const startZ = pos[2];

	for (0..self.blocks.width) |x| {
		const worldX = startX +% @as(i32, @intCast(x));

		for (0..self.blocks.depth) |y| {
			const worldY = startY +% @as(i32, @intCast(y));

			for (0..self.blocks.height) |z| {
				const worldZ = startZ +% @as(i32, @intCast(z));

				const block = self.blocks.get(x, y, z);
				if (block.typ != voidType or flags.preserveVoid) {
					_ = main.server.world.?.updateBlock(worldX, worldY, worldZ, block);
				}
			}
		}
	}
}
```

## Related Questions
- How does the Blueprint struct handle different modes of block updating?
- What is the purpose of the PasteFlags struct in the Blueprint module?
- Can you explain how the `load` method decompresses and reconstructs a blueprint?
- Describe the process of converting blocks to a compressed format in the `store` method.
- How does the `paste` method interact with the world to place blueprint blocks?
- What role do block mappings play in the serialization and deserialization processes?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_2*
