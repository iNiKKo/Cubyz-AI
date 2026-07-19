# [hard/codebase_src_blueprint.zig] - Chunk 1

**Type:** implementation
**Keywords:** Array3D, NeverFailingAllocator, Vec3i, rotation, capture, paste, ServerChunk
**Symbols:** Blueprint, Blueprint.blocks, Blueprint.init, Blueprint.deinit, Blueprint.extent, Blueprint.clone, Blueprint.rotateZ, Blueprint.CaptureResult, Blueprint.Selection, Blueprint.Selection.minPos, Blueprint.Selection.maxPos, Blueprint.Selection.initFromInclusive, Blueprint.Selection.initFromExtent, Blueprint.Selection.size, Blueprint.Selection.format, Blueprint.capture, Blueprint.PasteMode, Blueprint.pasteInGeneration, _pasteInGeneration, Blueprint.PasteFlags, Blueprint.paste
**Concepts:** blueprint management, block manipulation, world interaction, 3D array operations

## Summary
The Blueprint struct manages a 3D array of blocks and provides methods for initialization, deinitialization, cloning, rotation, capturing from the world, and pasting into the world.

## Explanation
The Blueprint struct manages a 3D array of blocks using an Array3D type. It includes methods for initializing and deinitializing the blueprint, getting its extent, cloning itself, rotating around the Z-axis, capturing a selection from the world, and pasting into the world. The rotateZ method rotates the blueprint around the Z-axis by specified angles (0, 90, 180, 270 degrees) and adjusts the block positions accordingly. Specifically, for a 90-degree rotation, the new x-coordinate is calculated as `new.blocks.width - yOld - 1` and the new y-coordinate is `xOld`. Similarly, for a 180-degree rotation, the new x-coordinate is `new.blocks.width - xOld - 1` and the new y-coordinate is `new.blocks.depth - yOld - 1`. For a 270-degree rotation, the new x-coordinate is `yOld` and the new y-coordinate is `new.blocks.depth - xOld - 1`. The capture method attempts to copy blocks from the main server's world into a new Blueprint instance. If a chunk containing a block is not loaded, it returns a failure message with the position of the unhandled block. The paste method allows pasting the blueprint's blocks into the world at a specified position with optional flags for preserving void blocks. The pasteInGeneration method is used internally to handle different modes of pasting (all or degradable) and interacts with ServerChunk instances by updating blocks in the chunk based on the mode.

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
