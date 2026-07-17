# [hard/codebase_src_blueprint.zig] - Chunk 0

**Type:** implementation
**Keywords:** 3D array, block rotation, selection capture, chunk pasting, voxel blueprint
**Symbols:** blueprintVersion, BlueprintCompression, Blueprint, Blueprint.blocks, Blueprint.init, Blueprint.deinit, Blueprint.extent, Blueprint.clone, Blueprint.rotateZ, Blueprint.CaptureResult, Blueprint.Selection, Blueprint.Selection.minPos, Blueprint.Selection.maxPos, Blueprint.Selection.initFromInclusive, Blueprint.Selection.initFromExtent, Blueprint.Selection.size, Blueprint.Selection.format, Blueprint.capture, Blueprint.PasteMode, Blueprint.pasteInGeneration, _pasteInGeneration
**Concepts:** blueprint management, block manipulation, world interaction, chunk operations

## Summary
The Blueprint module defines a data structure for storing and manipulating voxel blueprints in the Cubyz engine.

## Explanation
This chunk contains the definition of the `Blueprint` struct, which represents a 3D array of blocks. It includes methods for initialization, deinitialization, cloning, rotating, capturing from the world, and pasting into chunks. The module also defines related types such as `Selection`, `CaptureResult`, and `PasteMode`. Key functionalities include handling block rotations, capturing selections from the game world, and pasting blueprints into server chunks with different modes.

## Code Example
```zig
pub fn init(allocator: NeverFailingAllocator) Blueprint {
	return .{.blocks = .init(allocator, 0, 0, 0)};
}
```

## Related Questions
- What is the version of the blueprint format?
- How does a blueprint initialize its block array?
- What methods are available for rotating a blueprint?
- How is a selection defined and initialized?
- What happens if a chunk containing a block is not loaded during capture?
- How does the blueprint paste into a server chunk with different modes?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_0*
