# [hard/codebase_src_blueprint.zig] - Chunk 1

**Type:** implementation
**Keywords:** Array3D, NeverFailingAllocator, Vec3i, rotation, capture, paste, ServerChunk
**Symbols:** Blueprint, Blueprint.blocks, Blueprint.init, Blueprint.deinit, Blueprint.extent, Blueprint.clone, Blueprint.rotateZ, Blueprint.CaptureResult, Blueprint.Selection, Blueprint.Selection.minPos, Blueprint.Selection.maxPos, Blueprint.Selection.initFromInclusive, Blueprint.Selection.initFromExtent, Blueprint.Selection.size, Blueprint.Selection.format, Blueprint.capture, Blueprint.PasteMode, Blueprint.pasteInGeneration, _pasteInGeneration, Blueprint.PasteFlags, Blueprint.paste
**Concepts:** blueprint management, block manipulation, world interaction, 3D array operations

## Summary
The Blueprint struct manages a 3D array of blocks and provides methods for initialization, deinitialization, cloning, rotation, capturing from the world, and pasting into the world.

## Explanation
The Blueprint struct encapsulates a 3D array of blocks using an Array3D type. It includes methods for initializing and deinitializing the blueprint, getting its extent, cloning itself, rotating around the Z-axis, and capturing a selection from the world. The capture method attempts to copy blocks from the main server's world into a new Blueprint instance, handling cases where chunks are not loaded. The paste method allows pasting the blueprint's blocks into the world at a specified position with optional flags for preserving void blocks. The pasteInGeneration method is used internally to handle different modes of pasting (all or degradable) and interacts with ServerChunk instances.

## Code Example
```zig
pub fn init(allocator: NeverFailingAllocator) Blueprint {
	return .{.blocks = .init(allocator, 0, 0, 0)};
}
```

## Related Questions
- How does the Blueprint struct initialize its blocks?
- What is the purpose of the rotateZ method in the Blueprint struct?
- How does the capture method handle cases where chunks are not loaded?
- What are the different modes available for pasting a blueprint into the world?
- How does the pasteInGeneration method interact with ServerChunk instances?
- What is the role of the PasteFlags struct in the paste method?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_1*
