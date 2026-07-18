# [medium/codebase_src_rotation.zig] - Chunk 1

**Type:** api
**Keywords:** block rotation, ray intersection, block data, neighbor dependency, model generation
**Symbols:** RotationMode, RotationMode.DefaultFunctions, RotationMode.DefaultFunctions.model, RotationMode.DefaultFunctions.rotateZ, RotationMode.DefaultFunctions.generateData, RotationMode.DefaultFunctions.createBlockModel, RotationMode.DefaultFunctions.updateData, RotationMode.DefaultFunctions.modifyBlock, RotationMode.DefaultFunctions.rayIntersection, RotationMode.DefaultFunctions.onBlockBreaking, RotationMode.DefaultFunctions.canBeChangedInto, RotationMode.DefaultFunctions.itemDropsOnChange, RotationMode.DefaultFunctions.getBlockTags, RotationMode.DefaultFunctions.formatBlockData, RotationMode.CanBeChangedInto, rotationModes
**Concepts:** block rotation, ray intersection, block interaction, block transformation

## Summary
Defines the RotationMode struct and its associated functions for handling block rotations and interactions in the Cubyz voxel engine.

## Explanation
The RotationMode struct in Cubyz defines how blocks can be rotated, interact with rays, change states, and handle various interactions. Each block gets 16 bits of additional storage accessed by the `RotationMode` interface. The struct includes fields such as `dependsOnNeighbors`, which indicates if a block's state depends on its neighbors; `naturalStandard`, which holds default rotation data for generation algorithms; and pointers to functions like `model`, `rotateZ`, `generateData`, `createBlockModel`, `updateData`, `modifyBlock`, `rayIntersection`, `onBlockBreaking`, `canBeChangedInto`, `itemDropsOnChange`, `getBlockTags`, and `formatBlockData`. The `DefaultFunctions` struct provides default implementations for these functions. For example, the `model` function retrieves a model index based on the block type; `rotateZ` rotates data counterclockwise around the Z-axis without changing it; `generateData` updates or places blocks in the world and returns success status; `createBlockModel` generates a block model from provided data; `updateData` updates block data if neighbors change; `modifyBlock` modifies block type based on new data; `rayIntersection` detects intersections with block models using ray-triangle intersection logic; `onBlockBreaking` handles block destruction behavior; `canBeChangedInto` determines conditions for changing a block into another, including durability costs and item drops; `itemDropsOnChange` specifies the number of items dropped when blocks change; `getBlockTags` retrieves tags associated with blocks; and `formatBlockData` formats block data. The exact functions are as follows:

- **model**: Returns the model index for a given block.
  ```zig
  pub fn model(block: Block) ModelIndex {
    return blocks.meshes.modelIndexStart(block);
  }
  ```
- **rotateZ**: Rotates data counterclockwise around the Z-axis without changing it.
  ```zig
  pub fn rotateZ(data: u16, angle: Degrees) u16 {
    return DefaultFunctions.rotateZ(data, angle);
  }
  ```
- **generateData**: Updates or places blocks in the world and returns success status.
  ```zig
  pub fn generateData(world: *main.game.World, pos: Vec3i, relativePlayerPos: Vec3f, playerDir: Vec3f, relativeDir: Vec3i, neighbor: ?Neighbor, currentData: *Block, neighborBlock: Block, blockPlacing: bool) bool {
    return DefaultFunctions.generateData(world, pos, relativePlayerPos, playerDir, relativeDir, neighbor, currentData, neighborBlock, blockPlacing);
  }
  ```
- **createBlockModel**: Generates a block model from provided data.
  ```zig
  pub fn createBlockModel(block: Block, modeData: *u16, zon: ZonElement) ModelIndex {
    return DefaultFunctions.createBlockModel(block, modeData, zon);
  }
  ```
- **updateData**: Updates block data if neighbors change.
  ```zig
  pub fn updateData(block: *Block, neighbor: Neighbor, neighborBlock: Block) bool {
    return DefaultFunctions.updateData(block, neighbor, neighborBlock);
  }
  ```
- **modifyBlock**: Modifies block type based on new data.
  ```zig
  pub fn modifyBlock(block: *Block, newData: u16) bool {
    return DefaultFunctions.modifyBlock(block, newData);
  }
  ```
- **rayIntersection**: Detects intersections with block models using ray-triangle intersection logic.
  ```zig
  pub fn rayIntersection(block: Block, item: main.items.Item, relativePlayerPos: Vec3f, playerDir: Vec3f) ?RayIntersectionResult {
    return DefaultFunctions.rayIntersection(block, item, relativePlayerPos, playerDir);
  }
  ```
- **onBlockBreaking**: Handles block destruction behavior.
  ```zig
  pub fn onBlockBreaking(item: main.items.Item, relativePlayerPos: Vec3f, playerDir: Vec3f, currentData: *Block) void {
    return DefaultFunctions.onBlockBreaking(item, relativePlayerPos, playerDir, currentData);
  }
  ```
- **canBeChangedInto**: Determines conditions for changing a block into another.
  ```zig
  pub fn canBeChangedInto(oldBlock: Block, newBlock: Block, item: main.items.ItemStack, shouldDropSourceBlockOnSuccess: *bool) RotationMode.CanBeChangedInto {
    return DefaultFunctions.canBeChangedInto(oldBlock, newBlock, item, shouldDropSourceBlockOnSuccess);
  }
  ```
- **itemDropsOnChange**: Specifies the number of items dropped when blocks change.
  ```zig
  pub fn itemDropsOnChange(oldBlock: Block, newBlock: Block) u16 {
    return DefaultFunctions.itemDropsOnChange(oldBlock, newBlock);
  }
  ```
- **getBlockTags**: Retrieves tags associated with blocks.
  ```zig
  pub fn getBlockTags() []const Tag {
    return DefaultFunctions.getBlockTags();
  }
  ```
- **formatBlockData**: Formats block data.
  ```zig
  pub fn formatBlockData(block: Block, _list: *main.ListManaged(u8)) void {
    return DefaultFunctions.formatBlockData(block, _list);
  }
  ```
A global StringHashMap named `rotationModes` is declared but not initialized in this chunk.

## Code Example
```zig
pub fn model(block: Block) ModelIndex {
	return blocks.meshes.modelIndexStart(block);
}
```

## Related Questions
-  What is the purpose of the RotationMode struct in Cubyz?
-  How does the rotateZ function work in the RotationMode struct?
-  What methods are available in the DefaultFunctions of RotationMode?
-  What is the role of the rotationModes variable in this chunk?
-  How does the rayIntersection method detect intersections with block models?
-  What conditions determine if a block can be changed into another block using the canBeChangedInto method?
-  How is block data formatted and what information does it include?
-  What is the significance of the dependsOnNeighbors field in RotationMode?
-  How are errors handled when retrieving model data for blocks?

*Source: unknown | chunk_id: codebase_src_rotation.zig_chunk_1*
