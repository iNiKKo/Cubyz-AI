# [hard/codebase_src_network_protocols.zig] - Chunk 2

**Type:** networking
**Keywords:** networking, chunk request, mesh generation, thread pool, binary reader, binary writer
**Symbols:** chunkRequest, chunkRequest.id, chunkRequest.serverReceive, chunkRequest.sendRequest, chunkTransmission, chunkTransmission.id, chunkTransmission.MeshGenerationTask, chunkTransmission.MeshGenerationTask.pos, chunkTransmission.MeshGenerationTask.data, chunkTransmission.MeshGenerationTask.vtable, chunkTransmission.MeshGenerationTask.schedule, chunkTransmission.MeshGenerationTask.getPriority, chunkTransmission.MeshGenerationTask.isStillNeeded, chunkTransmission.MeshGenerationTask.run, chunkTransmission.MeshGenerationTask.clean, chunkTransmission.clientReceive, chunkTransmission.sendChunkOverTheNetwork, chunkTransmission.sendChunk
**Concepts:** networking protocol, chunk meshing, thread pool, binary serialization

## Summary
Handles chunk request and transmission protocols in the Cubyz engine.

## Explanation
This section describes the networking protocols for handling chunk requests and transmissions in the Cubyz engine. The `chunkRequest` struct manages client requests for specific chunks, including reading these requests from a connection and sending them over the network. It uses a binary reader to decode position and size data, then processes each chunk request by calculating its world position and scheduling it for rendering. The ID of the chunk request protocol is 2.

The server receives a chunk request from a client by reading the base position and render distance using a binary reader, then processing each chunk request by calculating its world position and scheduling it for rendering. The `chunkTransmission` struct handles the transmission of chunk data from the server to the client. It includes a nested `MeshGenerationTask` struct that defines how to generate mesh data for chunks in a thread pool environment. This task structure manages priority, checks if the task is still needed, runs the actual mesh generation and lighting calculation, and cleans up resources afterward.

The `chunkTransmission` also provides functions to receive chunk data from the network and send it over the network securely. The steps involved in sending a chunk over the network securely include compressing the chunk data, writing the position and size data using a binary writer, and sending the data over the network using a secure connection.

The `chunkRequest` struct has the following methods:
- `serverReceive`: Reads the base position and render distance from the reader, updates the client's position and render distance, and processes each chunk request by calculating its world position and scheduling it for rendering.
- `sendRequest`: Sends a chunk request over the network using a binary writer. It writes the base position, render distance, and each chunk request's position and size data to the writer, then sends the data over the network using a secure connection.

The `chunkTransmission` struct has the following methods:
- `clientReceive`: Reads the chunk position and data from the reader, creates a new `MeshGenerationTask`, and adds it to the thread pool for processing.
- `sendChunkOverTheNetwork`: Compresses the chunk data, writes the position and size data using a binary writer, and sends the data over the network using a secure connection.
- `sendChunk`: Calls `sendChunkOverTheNetwork` to send the chunk data over the network.

## Code Example
```zig
fn sendRequest(conn: *Connection, requests: []chunk.ChunkPosition, basePosition: Vec3i, renderDistance: u16) void {
	if (requests.len == 0) return;
	var writer = utils.BinaryWriter.initCapacity(main.stackAllocator, 14 + 4*requests.len);
	defer writer.deinit();
	writer.writeVec(Vec3i, basePosition);
	writer.writeInt(u16, renderDistance);
	for (requests) |req| {
		const voxelSizeShift: u5 = std.math.log2_int(u31, req.voxelSize);
		const positionMask = ~((@as(i32, 1) << voxelSizeShift + chunk.chunkShift) - 1);
		writer.writeInt(i8, @intCast((req.wx -% (basePosition[0] & positionMask)) >> voxelSizeShift + chunk.chunkShift));
		writer.writeInt(i8, @intCast((req.wy -% (basePosition[1] & positionMask)) >> voxelSizeShift + chunk.chunkShift));
		writer.writeInt(i8, @intCast((req.wz -% (basePosition[2] & positionMask)) >> voxelSizeShift + chunk.chunkShift));
		writer.writeInt(u5, voxelSizeShift);
	}
	conn.send(.secure, id, writer.data.items); // TODO: Can this use the slow channel?
}
```

## Related Questions
- What is the ID of the chunk request protocol?
- How does the server receive a chunk request from a client?
- What function sends a chunk request over the network?
- What is the purpose of the MeshGenerationTask struct in chunk transmission?
- How does the client handle incoming chunk data?
- What steps are involved in sending a chunk over the network securely?

*Source: unknown | chunk_id: codebase_src_network_protocols.zig_chunk_2*
