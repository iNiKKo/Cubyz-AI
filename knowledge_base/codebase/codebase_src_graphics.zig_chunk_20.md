# [hard/codebase_src_graphics.zig] - Chunk 20

**Type:** implementation
**Keywords:** framebuffer, OpenGL, mesh rendering, texture binding, shader uniforms
**Symbols:** generateBlockTexture, block_texture.textureSize, FrameBuffer.init, FrameBuffer.deinit, FrameBuffer.updateSize, FrameBuffer.bind, FrameBuffer.clear, Mat4f.perspective, main.game.camera.viewMatrix, Mat4f.identity, Mat4f.rotationX, Mat4f.rotationZ, main.renderer.chunk_meshing.transparentUniforms, main.renderer.chunk_meshing.uniforms, main.ListManaged.init, main.ListManaged.deinit, main.blocks.meshes.model, main.chunk.BlockPos.fromCoords, model.appendInternalQuadsToList, main.chunk.Neighbor.iterable, model.appendNeighborFacingQuadsToList, SubAllocation, main.renderer.chunk_meshing.faceBuffers.uploadData, main.renderer.chunk_meshing.faceBuffers.free, main.renderer.chunk_meshing.lightBuffers.uploadData, main.renderer.chunk_meshing.lightBuffers.free, c.glBlendEquation, c.glBlendFunc, main.renderer.chunk_meshing.bindTransparentShaderAndUniforms, main.renderer.chunk_meshing.bindShaderAndUniforms, c.glUniform1f, c.glActiveTexture, main.blocks.meshes.blockTextureArray.bind, main.blocks.meshes.emissionTextureArray.bind, main.blocks.meshes.reflectivityAndAbsorptionTextureArray.bind, block_texture.depthTexture.bindTo, c.glDrawElementsInstancedBaseVertexBaseInstance, c.glDisable, FrameBuffer.texture, block_texture.pipeline.bind, c.glUniform1i, frameBuffer.bindTexture, draw.rectVao.bind, c.glDrawArrays, c.glBindFramebuffer, main.Window.width, main.Window.height
**Concepts:** chunk meshing, texture generation, OpenGL rendering, framebuffer operations

## Summary
Generates a texture for a block by rendering its mesh into a framebuffer and then copying it to a final texture.

## Explanation
The `generateBlockTexture` function creates a texture for a given block type. It initializes a framebuffer, sets up the viewport, and configures the camera view matrix for rendering. The block's mesh is prepared by appending quads for internal and neighboring faces. Face data is uploaded to buffers, and shaders are bound with appropriate uniforms. The block is rendered into the framebuffer using OpenGL calls, including texture binding and drawing commands. Finally, the rendered image is copied from the framebuffer to a final texture, which is returned.

## Code Example
```zig
pub fn generateBlockTexture(blockType: u16) Texture {
	const block = main.blocks.Block{.typ = blockType, .data = 0}; // TODO: Use natural standard data.
	const textureSize = block_texture.textureSize;
	c.glViewport(0, 0, textureSize, textureSize);

	var frameBuffer: FrameBuffer = undefined;

	frameBuffer.init(false, c.GL_NEAREST, c.GL_REPEAT);
	defer frameBuffer.deinit();
	frameBuffer.updateSize(textureSize, textureSize, c.GL_RGBA16F);
	frameBuffer.bind();
	if (block.transparent()) {
		frameBuffer.clear(.{0.683421, 0.6854237, 0.685426, 1});
	} else {
		frameBuffer.clear(.{0, 0, 0, 0});
	}

	const projMatrix = Mat4f.perspective(0.013, 1, 64, 256);
	const oldViewMatrix = main.game.camera.viewMatrix;
	main.game.camera.viewMatrix = Mat4f.identity().mul(Mat4f.rotationX(std.math.pi/4.0)).mul(Mat4f.rotationZ(1.0*std.math.pi/4.0));
	defer main.game.camera.viewMatrix = oldViewMatrix;
	const uniforms = if (block.transparent()) &main.renderer.chunk_meshing.transparentUniforms else &main.renderer.chunk_meshing.uniforms;

	var faceData: main.ListManaged(main.renderer.chunk_meshing.FaceData) = .init(main.stackAllocator);
	defer faceData.deinit();
	const model = main.blocks.meshes.model(block).model();
	const pos: main.chunk.BlockPos = .fromCoords(1, 1, 1);
	if (block.hasBackFace()) {
		model.appendInternalQuadsToList(&faceData, block, pos, true);
		for (main.chunk.Neighbor.iterable) |neighbor| {
			model.appendNeighborFacingQuadsToList(&faceData, block, neighbor, pos, true);
		}
	}
	model.appendInternalQuadsToList(&faceData, block, pos, false);
	for (main.chunk.Neighbor.iterable) |neighbor| {
		model.appendNeighborFacingQuadsToList(&faceData, block, neighbor, pos.neighbor(neighbor)[0], false);
	}

	for (faceData.items) |*face| {
		face.position.lightIndex = 0;
	}
	var allocation: SubAllocation = .{.start = 0, .len = 0};
	main.renderer.chunk_meshing.faceBuffers[0].uploadData(faceData.items, &allocation);
	defer main.renderer.chunk_meshing.faceBuffers[0].free(allocation);
	var lightAllocation: SubAllocation = .{.start = 0, .len = 0};
	main.renderer.chunk_meshing.lightBuffers[0].uploadData(&.{0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff}, &lightAllocation);
	defer main.renderer.chunk_meshing.lightBuffers[0].free(lightAllocation);

	{
		const i = 4; // Easily switch between the 8 diagonal coordinates.
		var x: f64 = -65.5 + 1.5;
		var y: f64 = -65.5 + 1.5;
		var z: f64 = -92.631 + 1.5;
		if (i & 1 != 0) x = -x + 3;
		if (i & 2 != 0) y = -y + 3;
		if (i & 4 != 0) z = -z + 3;
		var chunkAllocation: SubAllocation = .{.start = 0, .len = 0};
		main.renderer.chunk_meshing.chunkBuffer.uploadData(&.{.{
			.position = .{0, 0, 0},
			.min = undefined,
			.max = undefined,
			.voxelSize = 1,
			.lightStart = lightAllocation.start,
			.vertexStartOpaque = undefined,
			.faceCountsByNormalOpaque = undefined,
			.vertexStartTransparent = undefined,
			.vertexCountTransparent = undefined,
			.visibilityState = 0,
			.oldVisibilityState = 0,
		}}, &chunkAllocation);
		defer main.renderer.chunk_meshing.chunkBuffer.free(chunkAllocation);
		if (block.transparent()) {
			c.glBlendEquation(c.GL_FUNC_ADD);
			c.glBlendFunc(c.GL_ONE, c.GL_SRC1_COLOR);
			main.renderer.chunk_meshing.bindTransparentShaderAndUniforms(projMatrix, .{1, 1, 1}, .{x, y, z});
		} else {
			main.renderer.chunk_meshing.bindShaderAndUniforms(projMatrix, .{1, 1, 1}, .{x, y, z});
		}
		c.glUniform1f(uniforms.contrast, 0.25);
		c.glActiveTexture(c.GL_TEXTURE0);
		main.blocks.meshes.blockTextureArray.bind();
		c.glActiveTexture(c.GL_TEXTURE1);
		main.blocks.meshes.emissionTextureArray.bind();
		c.glActiveTexture(c.GL_TEXTURE2);
		main.blocks.meshes.reflectivityAndAbsorptionTextureArray.bind();
		block_texture.depthTexture.bindTo(5);
		c.glDrawElementsInstancedBaseVertexBaseInstance(c.GL_TRIANGLES, @intCast(6*faceData.items.len), c.GL_UNSIGNED_INT, null, 1, allocation.start*4, chunkAllocation.start);
	}

	c.glDisable(c.GL_CULL_FACE);
	var finalFrameBuffer: FrameBuffer = undefined;
	finalFrameBuffer.init(false, c.GL_NEAREST, c.GL_REPEAT);
	finalFrameBuffer.updateSize(textureSize, textureSize, c.GL_RGBA8);
	finalFrameBuffer.bind();
	const texture = Texture{.textureID = finalFrameBuffer.texture};
	defer c.glDeleteFramebuffers(1, &finalFrameBuffer.frameBuffer);
	block_texture.pipeline.bind(null);
	c.glUniform1i(block_texture.uniforms.transparent, if (block.transparent()) c.GL_TRUE else c.GL_FALSE);
	frameBuffer.bindTexture(c.GL_TEXTURE3);

	draw.rectVao.bind();
	c.glDrawArrays(c.GL_TRIANGLE_STRIP, 0, 4);

	c.glBindFramebuffer(c.GL_FRAMEBUFFER, 0);

	c.glViewport(0, 0, main.Window.width, main.Window.height);
	c.glBlendFunc(c.GL_SRC_ALPHA, c.GL_ONE_MINUS_SRC_ALPHA);
	return texture;
}
```

## Related Questions
- What is the purpose of the `generateBlockTexture` function?
- How does the function initialize and configure the framebuffer?
- What steps are taken to prepare the block's mesh for rendering?
- How are shaders bound and uniforms set in the function?
- What OpenGL commands are used to draw the block into the framebuffer?
- How is the final texture generated from the rendered image?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_20*
