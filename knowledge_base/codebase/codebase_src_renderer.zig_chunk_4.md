# [hard/codebase_src_renderer.zig] - Chunk 4

**Type:** implementation
**Keywords:** graphics pipeline, vertex shader, fragment shader, texture loading, random selection, version check, render loop, uniform matrices
**Symbols:** MenuBackGround, MenuBackgroundVertex, chooseBackgroundImagePath
**Concepts:** background rendering, texture management, pipeline initialization, vertex array construction, uniform binding, viewport configuration

## Summary
This chunk defines the MenuBackGround struct that manages a rotating background mesh with panorama textures, including initialization of graphics pipelines, vertex arrays, texture loading from configurable paths, and rendering logic.

## Explanation
The MenuBackGround struct contains fields for pipeline (graphics.Pipeline), uniforms (viewMatrix and projectionMatrix as c_int), vao (graphics.VertexArray), texture (graphics.Texture), and angle (f32). The init() function sets up a vertex shader and fragment shader from assets, defines a MenuBackgroundVertex struct with pos [3]f32 and uv [2]f32 fields, constructs attribute descriptions for VkVertexInputAttributeDescription, initializes the pipeline using graphics.Pipeline.init with specified shaders, uniforms, vertex type, empty attachments, and depth settings. It then builds rawData as an array of 10 MenuBackgroundVertex entries representing cube corners with positions in normalized device space and UV coordinates mapping to a panorama texture, defines indices as an array of u32 for triangle drawing (24 vertices), creates the vao via .init(MenuBackgroundVertex, &rawData, &indices). The chooseBackgroundImagePath function takes a NeverFailingAllocator, opens the cubyzDir backgrounds directory iterably, checks if settings.lastVersionString differs from settings.version.version to decide whether to copy default_background.png into the directory (reading from assets/cubyz/default_background.png and writing via dir.write), otherwise walks the directory collecting PNG files into a main.List ([]const u8) using fileList.append with dupe'd paths, returns error.NoBackgroundImagesFound if none found, then picks a random index using main.random.nextIntBounded and constructs the path string. The deinit() function calls pipeline.deinit() and vao.deinit(). hasImage() returns true if texture.textureID != 0. render(deltaTime) sets glViewport to window size, skips rendering if texture is missing, increments angle by deltaTime/20.0, computes viewMatrix as Mat4f.rotationZ(angle), binds the pipeline with null (no shader state override), uploads uniforms via glUniformMatrix4fv for view and projection matrices, binds texture at slot 0, calls vao.bind(), and draws elements with glDrawElements(GL_TRIANGLES, 24, GL_UNSIGNED_INT, null). takeBackgroundImage begins by allocating a size*size array of u32 pixels on main.stackAllocator (size=1024), saves old resolutionScale from settings, sets resolutionScale to 1, calls updateViewport(size, size) and updateFov(90.0) — these functions are not defined in this chunk but are called here.

## Related Questions
- What vertex attributes are defined for the MenuBackgroundVertex struct and how are they mapped to Vulkan input locations?
- How does chooseBackgroundImagePath decide whether to copy a default background image or select a random one from the backgrounds directory?
- What error is returned if no PNG files are found in the backgrounds folder during texture selection?
- Which graphics API calls are used to bind uniforms and draw elements in the render function of MenuBackGround?
- How is the rotation angle updated each frame and what matrix operation is applied for the view transformation?
- What happens to the pipeline and vertex array when deinit() is called on a MenuBackGround instance?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_4*
