# [hard/codebase_src_renderer.zig] - Chunk 3

**Type:** implementation
**Keywords:** frame buffer, pipeline, texture, shader, GPU performance, rendering passes, resource management
**Symbols:** Bloom, Bloom.buffer1, Bloom.buffer2, Bloom.emptyBuffer, Bloom.width, Bloom.height, Bloom.firstPassPipeline, Bloom.secondPassPipeline, Bloom.colorExtractAndDownsamplePipeline, Bloom.colorExtractUniforms, Bloom.init, Bloom.deinit, Bloom.extractImageDataAndDownsample, Bloom.firstPass, Bloom.secondPass, Bloom.render, Bloom.bindReplacementImage
**Concepts:** post-processing effect, frame buffer, pipeline, texture, shader, GPU performance measurement

## Summary
The Bloom struct manages the bloom post-processing effect, initializing and deinitializing resources, and rendering the effect in multiple passes.

## Explanation
The Bloom struct manages the bloom post-processing effect by handling frame buffers, pipelines, and textures. It initializes resources such as frame buffers (`buffer1` and `buffer2`) with linear filtering and clamp-to-edge wrapping. It generates an empty texture for `emptyBuffer`. It then initializes three pipelines: `firstPassPipeline`, `secondPassPipeline`, and `colorExtractAndDownsamplePipeline` using specific shader paths and configurations.

**Initialization Process:**
The `init` method sets up the frame buffers (`buffer1` and `buffer2`) with linear filtering and clamp-to-edge wrapping. It generates an empty texture for `emptyBuffer`. It then initializes three pipelines: `firstPassPipeline`, `secondPassPipeline`, and `colorExtractAndDownsamplePipeline` using different shader paths and configurations.

**Buffer Resizing:**
The `render` method checks if the current width and height differ from the stored values. If they do, it updates the sizes of `buffer1` and `buffer2` to one-fourth of the current dimensions and validates them.

**GPU Performance Measurement:**
GPU performance is measured during each pass of the bloom effect using `gpu_performance_measuring.startQuery` and `gpu_performance_measuring.stopQuery` for `bloom_extract_downsample`, `bloom_first_pass`, and `bloom_second_pass`.

**Shaders Used:*
- **First Pass:** Shaders located at "assets/cubyz/shaders/bloom/first_pass.vert" and "assets/cubyz/shaders/bloom/first_pass.frag"
- **Second Pass:** Shaders located at "assets/cubyz/shaders/bloom/second_pass.vert" and "assets/cubyz/shaders/bloom/second_pass.frag"
- **Color Extract and Downsample:** Shaders located at "assets/cubyz/shaders/bloom/color_extractor_downsample.vert" and "assets/cubyz/shaders/bloom/color_extractor_downsample.frag"

**Uniform Variables in Color Extraction Pipeline:*
The `colorExtractAndDownsamplePipeline` uses several uniform variables, including:
- `zNear`: Type `c_int`
- `zFar`: Type `c_int`
- `tanXY`: Type `c_int`
- `fog.color`: Type `c_int`
- `fog.density`: Type `c_int`
- `fog.fogLower`: Type `c_int`
- `fog.fogHigher`: Type `c_int`
- `invViewMatrix`: Type `c_int`

These uniform variables are set in the `extractImageDataAndDownsample` method based on various conditions and inputs, such as player position, view matrix, and fog settings.

**Concrete Values:*
- `buffer1`, `buffer2`: Frame buffers with linear filtering and clamp-to-edge wrapping
- `emptyBuffer`: Empty texture
- `firstPassPipeline`, `secondPassPipeline`, `colorExtractAndDownsamplePipeline`: Pipelines initialized with specific shader paths
- `zNear`, `zFar`, `tanXY`: Uniform variables of type `c_int`
- `fog.color`, `fog.density`, `fog.fogLower`, `fog.fogHigher`: Uniform variables of type `c_int`
- `invViewMatrix`: Uniform variable of type `c_int`

## Code Example
```zig
pub fn deinit() void {
	buffer1.deinit();
	buffer2.deinit();
	firstPassPipeline.deinit();
	secondPassPipeline.deinit();
	colorExtractAndDownsamplePipeline.deinit();
}
```

## Related Questions
- What are the specific shader paths used for each pass of the bloom effect?
- What are the concrete values and types of the uniform variables in the color extraction pipeline?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_3*
