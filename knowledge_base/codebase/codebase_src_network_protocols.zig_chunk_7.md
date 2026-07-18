# [hard/codebase_src_network_protocols.zig] - Chunk 7

**Type:** networking
**Keywords:** thread pool, binary serialization, error handling, compression, network protocols
**Symbols:** lightMapTransmission, lightMapTransmission.id, LightMapTask, LightMapTask.wx, LightMapTask.wy, LightMapTask.voxelSizeShift, LightMapTask.data, LightMapTask.getPriority, LightMapTask.isStillNeeded, LightMapTask.run, LightMapTask.clean, clientReceive, sendLightMap, inventory, inventory.id, serverReceive, sendCommand, sendConfirmation, sendFailure, sendSyncOperation
**Concepts:** networking, light map transmission, inventory operations

## Summary
Defines network protocols for light map transmission and inventory operations.

## Explanation
The chunk defines two main network protocols: `lightMapTransmission` and `inventory`. The `lightMapTransmission` protocol handles the sending and receiving of light map data, including decompression and updating the renderer's mesh storage. It uses a thread pool for task management and includes error handling for data integrity issues. The `inventory` protocol manages inventory-related network operations, such as sending commands, confirmations, failures, and synchronization operations. Both protocols use binary readers and writers for data serialization and deserialization.

## Code Example
```zig
pub fn getPriority(_: *LightMapTask) f32 {
	return std.math.floatMax(f32);
}
```

## Related Questions
- What is the ID for light map transmission?
- How does the `LightMapTask` handle decompression errors?
- What are the possible types of inventory operations defined in this chunk?
- How is data serialized and deserialized in the inventory protocol?
- What role does the thread pool play in handling light map tasks?
- How is a confirmation message sent in the inventory protocol?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_7*
