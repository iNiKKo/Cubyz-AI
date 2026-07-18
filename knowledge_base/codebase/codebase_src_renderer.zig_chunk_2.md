# [hard/codebase_src_renderer.zig] - Chunk 2

**Type:** implementation
**Keywords:** frustum culling, indirect rendering, texture binding, shader uniforms, deferred rendering
**Symbols:** renderWorld, worldFrameBuffer, c.glViewport, gpu_performance_measuring.startQuery, gpu_performance_measuring.stopQuery, game.camera.updateViewMatrix, Frustum.init, blocks.meshes.preProcessAnimationData, chunk_meshing.bindShaderAndUniforms, c.glActiveTexture, blocks.meshes.blockTextureArray.bind, blocks.meshes.emissionTextureArray.bind, blocks.meshes.reflectivityAndAbsorptionTextureArray.bind, blocks.meshes.ditherTexture.bind, reflectionCubeMap.bindTo, chunk_meshing.beginRender, main.ListManaged(u32).init, mesh_storage.updateAndGetRenderChunks, crosshairDirection, MeshSelection.select, chunk_meshing.drawChunksIndirect, main.entity.client.render, itemdrop.ItemDropRenderer.renderItemDrops, main.block_entity.renderAll, particles.ParticleSystem.render, MeshSelection.render, c.glTextureBarrier, itemdrop.ItemDropRenderer.renderDisplayItems, chunk_meshing.endRender, Bloom.render, Bloom.bindReplacementImage, deferredRenderPassPipeline.bind, blocks.meshes.hasFog, c.glUniform3fv, c.glUniform1f, game.world.?.dayTime.fog.fogColor, game.world.?.dayTime.fog.density, game.world.?.dayTime.fog.fogLower, game.world.?.dayTime.fog.fogHigher, blocks.meshes.fogColor, blocks.meshes.fogDensity, c.glUniformMatrix4fv, c.glUniform3i, c.glUniform3f, c.glBindFramebuffer, graphics.draw.rectVao.bind, c.glDrawArrays
**Concepts:** chunk meshing, entity ECS, world rendering, post-processing effects

## Summary
The `renderWorld` function handles the rendering of the game world, including skybox, chunk meshing, entity rendering, and post-processing effects.

## Explanation
The `renderWorld` function orchestrates the rendering process for the entire game world. It begins by binding the world framebuffer and setting up the viewport. It then clears the framebuffer with the sky color and updates the camera's view matrix. Frustum culling is applied to determine which chunks are visible, and the skybox is rendered next. The function proceeds to preprocess animation data for blocks, bind necessary shaders and textures, and prepare rendering lists for opaque and transparent meshes. Chunks are drawn using indirect rendering, followed by entity, block entity, and particle rendering. Transparent meshes are rendered separately after a texture barrier. Bloom effects are applied if enabled, and finally, the deferred render pass is executed to combine all rendered elements into the final image.

## Code Example
```zig
pub fn renderWorld(world: *World, ambientLight: Vec3f, skyColor: Vec3f, playerPos: Vec3d) void { // MARK: renderWorld()
	worldFrameBuffer.bind();
	c.glViewport(0, 0, lastWidth, lastHeight);
	gpu_performance_measuring.startQuery(.clear);
	worldFrameBuffer.clear(Vec4f{skyColor[0], skyColor[1], skyColor[2], 1});
	gpu_performance_measuring.stopQuery();
	game.camera.updateViewMatrix();

	// Uses FrustumCulling on the chunks.
	const frustum = Frustum.init(Vec3f{0, 0, 0}, game.camera.viewMatrix, lastFov, lastWidth, lastHeight);

	const time: u32 = @intCast(main.timestamp().toMilliseconds() & std.math.maxInt(u32));

	gpu_performance_measuring.startQuery(.skybox);
	Skybox.render();
	gpu_performance_measuring.stopQuery();

	gpu_performance_measuring.startQuery(.animation);
	blocks.meshes.preProcessAnimationData(time);
	gpu_performance_measuring.stopQuery();

	// Update the uniforms. The uniforms are needed to render the replacement meshes.
	chunk_meshing.bindShaderAndUniforms(game.projectionMatrix, ambientLight, playerPos);

	c.glActiveTexture(c.GL_TEXTURE0);
	blocks.meshes.blockTextureArray.bind();
	c.glActiveTexture(c.GL_TEXTURE1);
	blocks.meshes.emissionTextureArray.bind();
	c.glActiveTexture(c.GL_TEXTURE2);
	blocks.meshes.reflectivityAndAbsorptionTextureArray.bind();
	c.glActiveTexture(c.GL_TEXTURE5);
	blocks.meshes.ditherTexture.bind();
	reflectionCubeMap.bindTo(4);

	chunk_meshing.quadsDrawn = 0;
	chunk_meshing.transparentQuadsDrawn = 0;
	const meshes = mesh_storage.updateAndGetRenderChunks(world.conn, &frustum, playerPos, settings.renderDistance);

	gpu_performance_measuring.startQuery(.chunk_rendering_preparation);
	const direction = crosshairDirection(game.camera.viewMatrix, lastFov, lastWidth, lastHeight);
	MeshSelection.select(playerPos, direction, game.Player.inventory.getItem(game.Player.selectedSlot));

	chunk_meshing.beginRender();

	var chunkLists: [main.settings.highestSupportedLod + 1]main.ListManaged(u32) = @splat(main.ListManaged(u32).init(main.stackAllocator));
	defer for (chunkLists) |list| list.deinit();
	for (meshes) |mesh| {
		mesh.prepareRendering(&chunkLists);
	}
	gpu_performance_measuring.stopQuery();
	gpu_performance_measuring.startQuery(.chunk_rendering);
	chunk_meshing.drawChunksIndirect(&chunkLists, game.projectionMatrix, ambientLight, playerPos, false);
	gpu_performance_measuring.stopQuery();

	gpu_performance_measuring.startQuery(.entity_rendering);
	main.entity.client.render(game.projectionMatrix, ambientLight, playerPos, main.lastDeltaTime.load(.monotonic));

	itemdrop.ItemDropRenderer.renderItemDrops(game.projectionMatrix, ambientLight, playerPos);
	gpu_performance_measuring.stopQuery();

	gpu_performance_measuring.startQuery(.block_entity_rendering);
	main.block_entity.renderAll(game.projectionMatrix, ambientLight, playerPos);
	gpu_performance_measuring.stopQuery();

	gpu_performance_measuring.startQuery(.particle_rendering);
	particles.ParticleSystem.render(game.projectionMatrix, game.camera.viewMatrix, ambientLight);
	gpu_performance_measuring.stopQuery();

	// Rebind block textures back to their original slots
	c.glActiveTexture(c.GL_TEXTURE0);
	blocks.meshes.blockTextureArray.bind();
	c.glActiveTexture(c.GL_TEXTURE1);
	blocks.meshes.emissionTextureArray.bind();

	MeshSelection.render(game.projectionMatrix, game.camera.viewMatrix, playerPos);

	// Render transparent chunk meshes:
	worldFrameBuffer.bindDepthTexture(c.GL_TEXTURE5);

	gpu_performance_measuring.startQuery(.transparent_rendering_preparation);
	c.glTextureBarrier();

	{
		for (&chunkLists) |*list| list.clearRetainingCapacity();
		var i: usize = meshes.len;
		while (true) {
			if (i == 0) break;
			i -= 1;
			meshes[i].prepareTransparentRendering(playerPos, &chunkLists);
		}
		gpu_performance_measuring.stopQuery();
		gpu_performance_measuring.startQuery(.transparent_rendering);
		chunk_meshing.drawChunksIndirect(&chunkLists, game.projectionMatrix, ambientLight, playerPos, true);
		gpu_performance_measuring.stopQuery();
	}

	c.glDepthRange(0, 0.001);
	itemdrop.ItemDropRenderer.renderDisplayItems(ambientLight, playerPos);
	c.glDepthRange(0.001, 1);

	chunk_meshing.endRender();

	worldFrameBuffer.bindTexture(c.GL_TEXTURE3);

	const playerBlock = mesh_storage.getBlockFromAnyLodFromRenderThread(@floor(playerPos[0]), @floor(playerPos[1]), @floor(playerPos[2]));

	if (settings.bloom) {
		Bloom.render(lastWidth, lastHeight, playerBlock, playerPos, game.camera.viewMatrix);
	} else {
		Bloom.bindReplacementImage();
	}
	gpu_performance_measuring.startQuery(.final_copy);
	if (activeFrameBuffer == 0) c.glViewport(0, 0, main.Window.width, main.Window.height);
	worldFrameBuffer.bindTexture(c.GL_TEXTURE3);
	worldFrameBuffer.bindDepthTexture(c.GL_TEXTURE4);
	worldFrameBuffer.unbind();
	deferredRenderPassPipeline.bind(null);
	if (!blocks.meshes.hasFog(playerBlock)) {
		c.glUniform3fv(deferredUniforms.@"fog.color", 1, @ptrCast(&game.world.?.dayTime.fog.fogColor));
		c.glUniform1f(deferredUniforms.@"fog.density", game.world.?.dayTime.fog.density);
		c.glUniform1f(deferredUniforms.@"fog.fogLower", game.world.?.dayTime.fog.fogLower);
		c.glUniform1f(deferredUniforms.@"fog.fogHigher", game.world.?.dayTime.fog.fogHigher);
	} else {
		const fogColor = blocks.meshes.fogColor(playerBlock);
		c.glUniform3f(deferredUniforms.@"fog.color", @as(f32, @floatFromInt(fogColor >> 16 & 255))/255.0, @as(f32, @floatFromInt(fogColor >> 8 & 255))/255.0, @as(f32, @floatFromInt(fogColor >> 0 & 255))/255.0);
		c.glUniform1f(deferredUniforms.@"fog.density", blocks.meshes.fogDensity(playerBlock));
		c.glUniform1f(deferredUniforms.@"fog.fogLower", 1e10);
		c.glUniform1f(deferredUniforms.@"fog.fogHigher", 1e10);
	}
	c.glUniformMatrix4fv(deferredUniforms.invViewMatrix, 1, c.GL_TRUE, @ptrCast(&game.camera.viewMatrix.transpose()));
	c.glUniform3i(deferredUniforms.playerPositionInteger, @floor(playerPos[0]), @floor(playerPos[1]), @floor(playerPos[2]));
	c.glUniform3f(deferredUniforms.playerPositionFraction, @floatCast(@mod(playerPos[0], 1)), @floatCast(@mod(playerPos[1], 1)), @floatCast(@mod(playerPos[2], 1)));
	c.glUniform1f(deferredUniforms.zNear, zNear);
	c.glUniform1f(deferredUniforms.zFar, zFar);
	c.glUniform2f(deferredUniforms.tanXY, 1.0/game.projectionMatrix.rows[0][0], 1.0/game.projectionMatrix.rows[1][2]);

	c.glBindFramebuffer(c.GL_FRAMEBUFFER, activeFrameBuffer);

	graphics.draw.rectVao.bind();
	c.glDrawArrays(c.GL_TRIANGLE_STRIP, 0, 4);

	c.glBindFramebuffer(c.GL_FRAMEBUFFER, 0);

	if (!main.gui.hideGui) main.entity.client.renderHud(game.projectionMatrix, ambientLight, playerPos);
	gpu_performance_measuring.stopQuery();
}
```

## Related Questions
- What is the first step in rendering the world?
- How does the function handle frustum culling?
- Which textures are bound before drawing chunks?
- What method is used to draw opaque and transparent meshes?
- How is bloom effect applied if enabled?
- What is the final step in the rendering process?
- How are shader uniforms set for deferred rendering?
- What function updates the camera's view matrix?
- Which function handles the preparation of animation data for blocks?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_2*
