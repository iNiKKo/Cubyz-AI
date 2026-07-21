# [hard/codebase_src_block_entity.zig] - Chunk 4

**Type:** api
**Keywords:** OpenGL, framebuffer, shader uniforms, mutex locking, client-server communication
**Symbols:** updateTextFromClient, renderAll
**Concepts:** block entity ECS, text rendering, networking protocol

## Summary
Handles block entity text updates and rendering.

## Explanation
This chunk contains functions for updating block entity text from a client and rendering all block entities. The `updateTextFromClient` function retrieves the mesh, locks it, and updates the block entity's text data if the block is a sign. It then sends an update to the server. The `renderAll` function sets up rendering context by saving the current framebuffer binding and viewport settings. It iterates over stored sign data, and for each sign that does not already have a rendered texture, it creates a new framebuffer with dimensions `textureWidth` and `textureHeight`, renders the text onto this framebuffer using OpenGL operations such as setting the color to black (`0x000000`) and aligning the text to the center. The process includes clearing the framebuffer, binding the resulting texture for rendering in the scene, and configuring shader uniforms such as ambient light, quad index, light data, chunk position, and block position. After rendering all signs, it restores the original framebuffer binding and viewport settings. It uses mutex locking to ensure thread safety when accessing shared resources and communicates with the server after updating a block entity's text.

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
