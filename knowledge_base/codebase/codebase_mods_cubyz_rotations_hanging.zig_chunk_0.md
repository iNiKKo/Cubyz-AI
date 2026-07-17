# [easy/codebase_mods_cubyz_rotations_hanging.zig] - Chunk 0

**Type:** gameplay
**Keywords:** hanging blocks, neighbor direction, replaceable check, top bottom models, data state update, transform model, mesh start index, block typ match, dirUp dirDown, support validation, model index add, zon get default, quads neighbor facing, replaceable blocks, hanging block logic
**Symbols:** dependsOnNeighbors, transform, init, deinit, reset, createBlockModel, model, generateData, updateData
**Concepts:** hanging blocks, neighbor support validation, rotation mode data state updates

## Summary
Chunk implementing hanging-block rotation mechanics, including neighbor support validation and data state updates.

## Explanation
This chunk defines a public API for handling blocks that hang from above. It imports main modules (blocks, models, vec) and defines a dependency flag dependsOnNeighbors = true indicating it interacts with adjacent blocks. The transform function is declared but empty; createBlockModel uses zon.get to retrieve top/bottom model names defaulting to cubyz:cube, then applies the empty transform via getModelIndex.model().transformModel. model returns a ModelIndex by adding block.data%2 to the mesh start index for this rotation mode. generateData takes neighbor info and current/neighbor blocks; when blockPlacing is true it checks that the neighbor direction is dirUp (otherwise false), verifies sameBlock typ, then computes support: if the neighbor block is not replaceable and its model's neighborFacingQuads[Neighbor.dirDown.toInt()] has non-zero length, support is true. If not supported it returns false; otherwise it sets currentData.data = 1 and returns true. updateData only acts when neighbor == .dirDown; it computes newData as 0 if typs match else 1, compares to block.data (returns false if equal), assigns block.data = newData, then returns true.

## Code Example
```zig
pub fn model(block: Block) ModelIndex {
	return blocks.meshes.modelIndexStart(block).add(block.data%2);
}
```

## Related Questions
- How does createBlockModel determine which models to use for a hanging block?
- What conditions cause generateData to reject placing a block on top of another?
- How is the support check computed using neighborFacingQuads in generateData?
- Why does updateData only process neighbors when they are dirDown?
- Does this chunk modify any global state besides block.data?
- What happens if the sameBlock typ check fails during placement validation?
- How does model use block.data to compute a ModelIndex for rotation modes?
- Is the transform function ever called with non-empty parameters in this chunk?
- Why is dependsOnNeighbors set to true and what does it imply about execution order?
- Can generateData return false without modifying currentData.data when blockPlacing is true?

*Source: unknown | chunk_id: codebase_mods_cubyz_rotations_hanging.zig_chunk_0*
