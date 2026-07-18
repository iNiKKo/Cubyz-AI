# [medium/codebase_mods_cubyz_rotations_torch.zig] - Chunk 1

**Type:** implementation
**Keywords:** ray intersection, block data, bit manipulation, item usage, state update
**Symbols:** closestRay, rayIntersection, onBlockBreaking, canBeChangedInto, itemDropsOnChange, updateBlockFromNeighborConnectivity
**Concepts:** block interactions, ray intersection, torch block breaking, block transformation, item drops, neighbor connectivity

## Summary
Handles torch block interactions including ray intersection and breaking logic.

## Explanation
This chunk defines functions for handling torch block interactions including ray intersection and breaking logic. The `closestRay` function iterates over specific bits (1, 2, 4, 8, 16) of a block's data to find intersections or relevant bits for interactions. It returns the bit index if requested with `.bit`, otherwise it provides detailed intersection results using `.intersection`. The `rayIntersection` function uses `closestRay` with `.intersection` to return intersection results. The `onBlockBreaking` function updates the block's data by clearing the specific bit identified by `closestRay` when broken, and sets the block type to air if all bits are cleared. The `canBeChangedInto` function checks if a block can be transformed into another based on item usage and block data, considering torch amount changes and item requirements. It returns `.yes_costsItems` with the number of items needed for transformation. The `itemDropsOnChange` calculates how many items should drop when a block changes type by comparing bit counts before and after transformation. The `updateBlockFromNeighborConnectivity` function adjusts the torch block's state based on its neighbors' support, setting specific bits (center, negX, posX, negY, posY) to false if corresponding neighbor blocks do not provide support.

## Code Example
```zig
pub fn rayIntersection(block: Block, item: main.items.Item, relativePlayerPos: Vec3f, playerDir: Vec3f) ?RayIntersectionResult {
	return closestRay(.intersection, block, item, relativePlayerPos, playerDir);
}
```

## Related Questions
- How does the `closestRay` function determine the closest intersection with a torch block?
- What is the purpose of the `rayIntersection` function in this chunk?
- How does the `onBlockBreaking` function update the block's data when it is broken?
- What conditions must be met for one block to be changed into another according to the `canBeChangedInto` function?
- How are item drops calculated when a block changes type using the `itemDropsOnChange` function?
- What does the `updateBlockFromNeighborConnectivity` function do and how is it used?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_torch.zig_chunk_1*
