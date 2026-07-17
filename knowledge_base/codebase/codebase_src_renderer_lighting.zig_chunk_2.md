# [hard/codebase_src_renderer_lighting.zig] - Chunk 2

**Type:** implementation
**Keywords:** lightingData, CircularBufferQueue, ListManaged, ChunkPosition, BlockPos, Entry, mesh_storage, calculateIncomingOcclusion, calculateOutgoingOcclusion
**Symbols:** ChannelChunk, ChannelChunk.entries, ChannelChunk.isSun, ChannelChunk.ch, ChannelChunk.propagateFromNeighbor, ChannelChunk.propagateDestructiveFromNeighbor, ChannelChunk.propagateLights, ChannelChunk.propagateUniformSun, ChannelChunk.propagateLightsDestructive, main.utils.CircularBufferQueue, main.ListManaged, chunk.ChunkPosition, BlockPos, Entry, mesh_storage.getNeighbor, calculateIncomingOcclusion, calculateOutgoingOcclusion
**Concepts:** lighting propagation, neighbor interactions, uniform sunlight handling, destructive light updates

## Summary
Handles lighting propagation within a chunk, including destructive and non-destructive light updates from neighbors.

## Explanation
The code defines functions for propagating lighting data within a chunk. It includes methods to propagate lights from neighboring chunks, handle uniform sunlight, and perform destructive light propagation. The `propagateLights` function initializes a queue of light entries and processes them, updating the lighting state based on neighbor interactions. The `propagateUniformSun` method sets all voxels in the chunk to full brightness under sunlight conditions. The `propagateDestructiveFromNeighbor` and `propagateFromNeighbor` functions manage how light propagates from neighboring chunks, considering occlusions and directional sources.

## Code Example
```zig
fn propagateFromNeighbor(self: *ChannelChunk, lightQueue: *main.utils.CircularBufferQueue(Entry), lights: []const Entry, lightRefreshList: *main.ListManaged(chunk.ChunkPosition)) void {
    std.debug.assert(lightQueue.isEmpty());
    for (lights) |entry| {
        var result = entry;
        calculateIncomingOcclusion(&result.value, self.ch.data.getValue(entry.pos.toIndex()), self.ch.pos.voxelSize, @enumFromInt(entry.sourceDir));
        if (result.value[0] != 0 or result.value[1] != 0 or result.value[2] != 0) lightQueue.pushBack(result);
    }
    self.propagateDirect(lightQueue, lightRefreshList);
}
```

## Related Questions
- What is the purpose of the `propagateFromNeighbor` function?
- How does the `propagateLights` function handle sunlight propagation?
- What data structure is used to manage the queue of light entries in `propagateLights`?
- Describe the role of `calculateIncomingOcclusion` and `calculateOutgoingOcclusion` in the lighting propagation process.
- How does the `propagateUniformSun` function set the lighting state for a chunk under sunlight?
- What is the difference between `propagateFromNeighbor` and `propagateDestructiveFromNeighbor` methods?
- Explain how neighbor interactions are handled during light propagation in this code.

*Source: unknown | chunk_id: codebase_src_renderer_lighting.zig_chunk_2*
