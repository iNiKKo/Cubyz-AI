# [medium/codebase_mods_cubyz_rotations_stairs.zig] - Chunk 2

**Type:** implementation
**Keywords:** bitwise operations, ray casting, block data manipulation, state management, interaction logic
**Symbols:** model, generateData, closestRay, rayIntersection, onBlockBreaking, canBeChangedInto, getBlockTags
**Concepts:** block interaction, ray intersection, block breaking, block transformation

## Summary
Handles block rotation and interaction logic for stairs in the Cubyz voxel engine.

## Explanation
This chunk defines functions related to block interactions, specifically for handling stairs with chiselable properties. The bitwise operations on `block.data` manage different states of the stairs, including which corners are chiseled or broken. Here are detailed explanations and specific values used in each function:

- **model(block: Block) ModelIndex**: This function calculates the model index based on the block's data using bitwise AND operation with 255.

- **generateData(_: *main.game.World, _: Vec3i, _: Vec3f, _: Vec3f, _: Vec3i, _: ?Neighbor, currentData: *Block, _: Block, blockPlacing: bool) bool**: This function sets the `currentData.data` to 0 when a new block is being placed (`blockPlacing == true`).

- **closestRay(comptime typ: enum { bit, intersection }, block: Block, relativePlayerPos: Vec3f, playerDir: Vec3f)**: This function iterates over bits (1, 2, 4, 8, 16, 32, 64, 128) and checks if the corresponding bit in `block.data` is unset. It calculates a model index for each corner using bitwise operations and determines intersections with rays. If `typ == .bit`, it returns the bit that was checked; otherwise, it returns the closest intersection result.

- **rayIntersection(block: Block, item: main.items.Item, relativePlayerPos: Vec3f, playerDir: Vec3f) ?RayIntersectionResult**: This function checks if the item is a procedural item with chiselable tags. If so, it calls `closestRay` to find intersections and returns the result.

- **onBlockBreaking(item: main.items.Item, relativePlayerPos: Vec3f, playerDir: Vec3f, currentData: *Block)**: This function modifies `currentData.data` by setting bits corresponding to chiseled corners using bitwise OR. If all bits are set (255), it resets the block data.

- **canBeChangedInto(oldBlock: Block, newBlock: Block, item: main.items.ItemStack, shouldDropSourceBlockOnSuccess: *bool) RotationMode.CanBeChangedInto**: This function checks if `oldBlock.typ` matches `newBlock.typ`. If so and `item.item == .proceduralItem`, it returns `.yes_costsDurability = 1`; otherwise, it returns `.no`.

- **getBlockTags() []const Tag**: This function returns the tag array containing `.chiselable`.

## Code Example
```zig
pub fn model(block: Block) ModelIndex {
	return blocks.meshes.modelIndexStart(block).add(block.data & 255);
}
```

## Related Questions
- How does the `model` function determine the model index for a block?
- What is the purpose of the `generateData` function in this chunk?
- How does the `closestRay` function work and what does it return?
- What conditions trigger the `onBlockBreaking` function to modify block data?
- How does the `canBeChangedInto` function decide if a block can be transformed into another?
- What tags are associated with blocks handled by this chunk?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_stairs.zig_chunk_2*
