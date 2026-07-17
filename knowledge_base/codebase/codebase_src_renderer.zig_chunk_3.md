# [hard/codebase_src_renderer.zig] - Chunk 3

**Type:** implementation
**Keywords:** pipeline, buffer, vertex array object, uniform, fog, downsample, query, render pass, texture swap, validation
**Symbols:** MenuBackGround, MenuBackGround.init
**Concepts:** bloom post-processing, multi-pass rendering, GPU performance profiling, viewport resizing, fog-aware color extraction, uniform binding, Vulkan pipeline creation

## Summary
Implements the bloom post-processing pipeline with multi-pass rendering, fog-aware color extraction and downsampling, GPU performance query instrumentation, viewport resizing logic, and a menu background shader setup.

## Explanation
The chunk defines several graphics pipelines: emptyBuffer (initialized to an empty image), firstPassPipeline and secondPassPipeline for the two bloom passes using SimpleVertex2D with no culling, depth testing or blending, and colorExtractAndDownsamplePipeline which binds uniforms including fog parameters. The deinit function releases all buffers and pipelines. extractImageDataAndDownsample configures uniform values: it checks blocks.meshes.hasFog to decide whether to use world dayTime.fog settings (fogColor, density, lower/higher) or block-specific fogColor/density with extreme fog bounds; it sets invViewMatrix transpose, player position integer/fraction uniforms, zNear/zFar, tanXY derived from the projection matrix rows, then draws a rectVao triangle strip. firstPass and secondPass swap buffer bindings (texture vs render target) for each pass. render handles width/height changes by updating buffer sizes with GL_R11F_G11F_B10F format and asserting validation; it starts GPU performance queries named bloom_extract_downsample, bloom_first_pass, bloom_second_pass, draws the extracted image to a quarter-size viewport, then draws the first pass result into buffer2 (bound as texture5) at full resolution. bindReplacementImage binds emptyBuffer to slot 5. MenuBackGround is a struct with pipeline, uniforms (viewMatrix, projectionMatrix), vao, texture, and angle; its init defines MenuBackgroundVertex with pos [3]f32 and uv [2]f32 fields and provides attributeDescriptions for Vulkan vertex input.

## Related Questions
- What are the exact shader file paths used for each bloom pipeline?
- How does extractImageDataAndDownsample decide between world fog and block-specific fog settings?
- Which uniform locations are configured in extractImageDataAndDownsample and what values do they receive?
- In what order are firstPass and secondPass executed relative to GPU performance queries?
- What happens when render is called with different width/height than the current stored dimensions?
- How does bindReplacementImage affect texture slot usage after bloom rendering?
- What vertex attribute layout is defined inside MenuBackGround.init for the menu background shader?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_3*
