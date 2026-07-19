# [src/renderer/chunk_meshing.zig] - PR #1760 review diff

**Type:** review
**Keywords:** block entity, client data update, uninitialized state, design choices, architecture
**Symbols:** ChunkMesh, mutex, chunk.data.setValue, blockEntity, BinaryReader, updateClientData
**Concepts:** thread safety, architectural design, state management

## Summary
Added logic to update client data for block entities when setting new blocks.

## Explanation
The change introduces a mechanism to handle uninitialized block entities by updating their client data after setting a new block. This addresses an architectural issue where the previous design relied on everything being initialized correctly upfront, which was not always the case. The reviewer emphasizes the need for a robust system that can manage block entities in any state, promoting better design choices and preventing potential issues related to uninitialized states.

Specifically, when a new block is set, the code checks if it has a block entity associated with it. If so, it initializes a `BinaryReader` with the provided `blockEntityData` and calls `blockEntity.updateClientData(.{_x, _y, _z}, self.chunk, .{.update = &reader})`. This method updates the client data for the block entity using the binary reader.

The reviewer also notes that they deliberately removed the 'update on create' event in #1739 because it promotes the wrong design choices. Instead of relying on everything being initialized correctly upfront, the new system should be able to handle uninitialized block entities in any state.

## Related Questions
- What is the purpose of the `updateClientData` method in this context?
- How does the addition of `blockEntity.updateClientData` affect the performance of chunk meshing?
- Why was the 'update on create' event removed in #1739?
- What are the potential implications of handling uninitialized block entities?
- How does this change ensure thread safety in the chunk meshing process?
- Can you explain the role of `BinaryReader` in updating block entity data?

*Source: unknown | chunk_id: github_pr_1760_comment_2277213297*
