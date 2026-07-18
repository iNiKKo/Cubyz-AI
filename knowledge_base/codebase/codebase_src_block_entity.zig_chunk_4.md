# [hard/codebase_src_block_entity.zig] - Chunk 4

**Type:** api
**Keywords:** OpenGL, framebuffer, shader uniforms, mutex locking, client-server communication
**Symbols:** updateTextFromClient, renderAll
**Concepts:** block entity ECS, text rendering, networking protocol

## Summary
Handles block entity text updates and rendering.

## Explanation
This chunk contains functions for updating block entity text from a client and rendering all block entities. The `updateTextFromClient` function retrieves the mesh, locks it, and updates the block entity's text data if the block is a sign. It then sends an update to the server. The `renderAll` function sets up rendering context, iterates over stored sign data, renders text onto textures, and binds these textures for rendering in the scene. It uses OpenGL for framebuffer operations and shader uniform updates.

## Code Example
```zig
pub fn updateTextFromClient(pos: Vec3i, newText: []const u8) void {
			{
				const mesh = main.renderer.mesh_storage.getMesh(.initFromWorldPos(pos, 1)) orelse return;
				mesh.mutex.lock();
				defer mesh.mutex.unlock();
				const localPos = mesh.chunk.getLocalBlockPos(pos);
				const block = mesh.chunk.data.getValue(localPos.toIndex());
				const blockEntity = block.blockEntity() orelse return;
				if (!std.mem.eql(u8, blockEntity.id, "cubyz:sign")) return;

				StorageClient.mutex.lock();
				defer StorageClient.mutex.unlock();

				const data = StorageClient.getOrPut(pos, mesh.chunk);
				if (data.foundExisting) {
					data.valuePtr.deinit();
				}
				data.valuePtr.* = .{
					.blockPos = pos,
					.block = mesh.chunk.data.getValue(localPos.toIndex()),
					.renderedTexture = null,
					.text = main.globalAllocator.dupe(u8, newText),
				};
			}

			main.network.protocols.blockEntityUpdate.sendClientDataUpdateToServer(main.game.world.?.conn, pos);
		}
```

## Related Questions
- How does the `updateTextFromClient` function handle block entity text updates?
- What is the purpose of the `renderAll` function in this chunk?
- How does the chunk ensure thread safety when accessing shared resources?
- What OpenGL operations are performed during the rendering process?
- How does the chunk communicate with the server after updating a block entity's text?
- What steps are taken to render text onto textures for block entities?

*Source: unknown | chunk_id: codebase_src_block_entity.zig_chunk_4*
