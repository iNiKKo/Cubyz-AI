# [hard/codebase_src_network_protocols.zig] - Chunk 7

**Type:** networking
**Keywords:** network protocols, light map transmission, inventory, thread pool, binary writer, compression, client-server communication
**Symbols:** lightMapTransmission, lightMapTransmission.id, lightMapTransmission.LightMapTask, lightMapTransmission.LightMapTask.wx, lightMapTransmission.LightMapTask.wy, lightMapTransmission.LightMapTask.voxelSizeShift, lightMapTransmission.LightMapTask.data, lightMapTransmission.LightMapTask.getPriority, lightMapTransmission.LightMapTask.isStillNeeded, lightMapTransmission.LightMapTask.run, lightMapTransmission.LightMapTask.clean, lightMapTransmission.clientReceive, lightMapTransmission.sendLightMap, inventory, inventory.id, inventory.clientReceive, inventory.serverReceive, inventory.sendCommand, inventory.sendConfirmation
**Concepts:** networking, thread pool, binary serialization, compression, inventory management

## Summary
This chunk defines network protocols for light map transmission and inventory management.

## Explanation
The chunk contains two main sections: `lightMapTransmission` and `inventory`. The `lightMapTransmission` section handles sending and receiving light map data. It includes functions to send requests, process tasks in a thread pool, and handle client reception of light map data. The `inventory` section manages inventory-related network communication, including handling client and server-side receptions, sending commands, and sending confirmations.

## Code Example
```zig
pub fn sendRequest(conn: *Connection, requests: []main.server.terrain.SurfaceMap.MapFragmentPosition) void {
	if (requests.len == 0) return;
	var writer = utils.BinaryWriter.initCapacity(main.stackAllocator, 9*requests.len);
	defer writer.deinit();
	for (requests) |req| {
		writer.writeInt(i32, req.wx);
		writer.writeInt(i32, req.wy);
		writer.writeInt(u8, req.voxelSizeShift);
	}
	conn.send(.secure, id, writer.data.items); // TODO: Can this use the slow channel?
}
```

## Related Questions
- What is the purpose of the `sendRequest` function in the `lightMapTransmission` section?
- How does the `LightMapTask` struct handle decompression and error checking for light map data?
- What role does the `clientReceive` function play in the `inventory` section?
- How are tasks managed in the thread pool within the `lightMapTransmission` section?
- What is the process for sending a confirmation message in the `inventory` section?
- How does the chunk handle invalid data received during light map transmission?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_7*
