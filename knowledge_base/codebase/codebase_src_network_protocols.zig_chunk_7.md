# [hard/codebase_src_network_protocols.zig] - Chunk 7

**Type:** networking
**Keywords:** thread pool, binary serialization, error handling, compression, network protocols
**Symbols:** lightMapTransmission, lightMapTransmission.id, LightMapTask, LightMapTask.wx, LightMapTask.wy, LightMapTask.voxelSizeShift, LightMapTask.data, LightMapTask.getPriority, LightMapTask.isStillNeeded, LightMapTask.run, LightMapTask.clean, clientReceive, sendLightMap, inventory, inventory.id, serverReceive, sendCommand, sendConfirmation, sendFailure, sendSyncOperation
**Concepts:** networking, light map transmission, inventory operations

## Summary
Defines network protocols for light map transmission and inventory operations.

## Explanation
The chunk defines two main network protocols: `lightMapTransmission` and `inventory`. The `lightMapTransmission` protocol handles the sending and receiving of light map data, including decompression and updating the renderer's mesh storage. It uses a thread pool for task management and includes error handling for data integrity issues. The `inventory` protocol manages inventory-related network operations, such as sending commands, confirmations, failures, and synchronization operations. Both protocols use binary readers and writers for data serialization and deserialization.

The `lightMapTransmission` protocol has an ID of 12. It includes a struct `LightMapTask` with fields `wx`, `wy`, `voxelSizeShift`, and `data`. The `getPriority` function returns the maximum float value, indicating high priority. The `isStillNeeded` function checks if the game world is not null or paused. The `run` function decompresses light map data, reads it into a binary reader, initializes a light map fragment, and updates the renderer's mesh storage. The `clean` function frees allocated memory.

The `clientReceive` function in `lightMapTransmission` creates a `LightMapTask`, initializes it with received data, and adds it to the thread pool. The `sendLightMap` function compresses light map data, writes it to a binary writer, and sends it over the network.

The `inventory` protocol has an ID of 13. It includes functions for client and server reception of inventory operations, sending commands, confirmations, failures, and synchronization operations. The `clientReceive` function processes different types of inventory operations based on the received type. The `serverReceive` function receives commands from the server. The `sendCommand`, `sendConfirmation`, `sendFailure`, and `sendSyncOperation` functions send specific types of inventory messages over the network.

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
