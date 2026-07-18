# [hard/codebase_src_server_server.zig] - Chunk 3

**Type:** implementation
**Keywords:** chunk loading, thread pool, priority queue, network buffer, mutex locking
**Symbols:** loadNewChunk, loadUnloadChunks, getTaskFromJobQueue, addTask, clearJobQueue, isNetworkQueueFull, scheduleJobQueue, update
**Concepts:** chunk management, task scheduling, networking

## Summary
Handles chunk loading, unloading, and task management for a user in the server.

## Explanation
This chunk contains functions responsible for managing chunks that are loaded or unloaded based on the player's position and render distance. It includes logic to clear old chunks not within the new render box, load new chunks, and manage tasks using a thread pool. The `loadUnloadChunks` function checks if the player's position or render distance has changed and updates the chunks accordingly by calling `unloadOldChunk`, `loadNewChunk`, updating `lastRenderDistance`, and setting `lastPos`. Specifically, it calculates the bounding box for new chunks as follows:

```zig
const newPos: Vec3i = @as(Vec3i, @trunc(self.player().pos)) +% @as(Vec3i, @splat(chunk.chunkSize/2)) & ~@as(Vec3i, @splat(chunk.chunkMask));
const lastBoxStart = (self.lastPos -% @as(Vec3i, @splat(self.lastRenderDistance*chunk.chunkSize))) & ~@as(Vec3i, @splat(chunk.chunkMask));
const lastBoxEnd = (self.lastPos +% @as(Vec3i, @splat(self.lastRenderDistance*chunk.chunkSize))) +% @as(Vec3i, @splat(chunk.chunkSize - 1)) & ~@as(Vec3i, @splat(chunk.chunkMask));
const newBoxStart = (newPos -% @as(Vec3i, @splat(newRenderDistance*chunk.chunkSize))) & ~@as(Vec3i, @splat(chunk.chunkMask));
const newBoxEnd = (newPos +% @as(Vec3i, @splat(newRenderDistance*chunk.chunkSize))) +% @as(Vec3i, @splat(chunk.chunkSize - 1)) & ~@as(Vec3i, @splat(chunk.chunkMask));
```
The `getTaskFromJobQueue` function retrieves tasks from the job queue, prioritizing them based on a priority value calculated in `ResortTaskTask.getPriority`, handling network queue full conditions, and ensuring that tasks are still needed. If the network buffer exceeds 900000 bytes (`isNetworkQueueFull`), it prevents scheduling of the job queue. The exact conditions for scheduling the job queue are as follows:

```zig
fn scheduleJobQueue(self: *User) void {
    self.mutex.assertLocked();
    if (self.jobQueueScheduled) return;
    if (self.jobQueue.size == 0) return;
    if (self.isNetworkQueueFull()) return;
    self.jobQueueScheduled = true;
    main.threadPool.addPlayer(self);
}
```
The `addTask` function adds new tasks to the priority queue with a given priority value from the task's vtable. The `clearJobQueue` function clears all tasks in the job queue by cleaning each task using its vtable's clean method. The `isNetworkQueueFull` function checks if the network send buffer length is greater than 900000 bytes, and `scheduleJobQueue` schedules the job queue for processing if it's not already scheduled and there are tasks in the queue.

## Code Example
```zig
fn loadNewChunk(self: *User, newPos: Vec3i, newRenderDistance: u16) void {
		const lastBoxStart = (self.lastPos -% @as(Vec3i, @splat(self.lastRenderDistance*chunk.chunkSize))) & ~@as(Vec3i, @splat(chunk.chunkMask));
		const lastBoxEnd = (self.lastPos +% @as(Vec3i, @splat(self.lastRenderDistance*chunk.chunkSize))) +% @as(Vec3i, @splat(chunk.chunkSize - 1)) & ~@as(Vec3i, @splat(chunk.chunkMask));
		const newBoxStart = (newPos -% @as(Vec3i, @splat(newRenderDistance*chunk.chunkSize))) & ~@as(Vec3i, @splat(chunk.chunkMask));
		const newBoxEnd = (newPos +% @as(Vec3i, @splat(newRenderDistance*chunk.chunkSize))) +% @as(Vec3i, @splat(chunk.chunkSize - 1)) & ~@as(Vec3i, @splat(chunk.chunkMask));
		// Clear all chunks not inside the new box:
		var x: i32 = newBoxStart[0];
		while (x != newBoxEnd[0]) : (x +%= chunk.chunkSize) {
			const inXDistance = x -% lastBoxStart[0] >= 0 and x -% lastBoxEnd[0] < 0;
			var y: i32 = newBoxStart[1];
			while (y != newBoxEnd[1]) : (y +%= chunk.chunkSize) {
				const inYDistance = y -% lastBoxStart[1] >= 0 and y -% lastBoxEnd[1] < 0;
				var z: i32 = newBoxStart[2];
				while (z != newBoxEnd[2]) : (z +%= chunk.chunkSize) {
					const inZDistance = z -% lastBoxStart[2] >= 0 and z -% lastBoxEnd[2] < 0;
					if (!inXDistance or !inYDistance or !inZDistance) {
						self.loadedChunks[simArrIndex(x)][simArrIndex(y)][simArrIndex(z)] = world_zig.ChunkManager.getOrGenerateSimulationChunkAndIncreaseRefCount(.{.wx = x, .wy = y, .wz = z, .voxelSize = 1});
					}
				}
			}
		}
	}
```

## Related Questions
-  How does the `loadNewChunk` function calculate the bounding box for new chunks using `chunk.chunkSize` and `chunk.chunkMask`?
-  What is the purpose of the `ResortTaskTask` struct within `getTaskFromJobQueue`, including how it calculates task priorities?
-  How does the `addTask` function handle adding tasks to the job queue with specific priority values from the vtable?
-  What are the exact conditions that trigger the scheduling of the job queue in the `scheduleJobQueue` method?
-  How does the `isNetworkQueueFull` function determine if the network buffer is full, and what actions are taken when it exceeds 900000 bytes?
-  What role does the `mutex` play in ensuring thread safety within this chunk?

*Source: unknown | chunk_id: codebase_src_server_server.zig_chunk_3*
