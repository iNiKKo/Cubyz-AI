# [hard/codebase_src_renderer.zig] - Chunk 3

**Type:** implementation
**Keywords:** frame buffer, pipeline, texture, shader, GPU performance, rendering passes, resource management
**Symbols:** Bloom, Bloom.buffer1, Bloom.buffer2, Bloom.emptyBuffer, Bloom.width, Bloom.height, Bloom.firstPassPipeline, Bloom.secondPassPipeline, Bloom.colorExtractAndDownsamplePipeline, Bloom.colorExtractUniforms, Bloom.init, Bloom.deinit, Bloom.extractImageDataAndDownsample, Bloom.firstPass, Bloom.secondPass, Bloom.render, Bloom.bindReplacementImage
**Concepts:** post-processing effect, frame buffer, pipeline, texture, shader, GPU performance measurement

## Summary
The Bloom struct manages the bloom post-processing effect, initializing and deinitializing resources, and rendering the effect in multiple passes.

## Explanation
The Bloom struct manages the bloom post-processing effect by handling frame buffers, pipelines, and textures. It initializes resources such as frame buffers and pipelines with specific shaders. The `init` method sets up the frame buffers and pipelines using the provided shader paths and configurations. The `render` method orchestrates the bloom effect by resizing buffers if necessary, executing three passes (extracting image data and downscaling, first pass, and second pass), and measuring GPU performance for each step. The `deinit` method cleans up all allocated resources. The struct also includes methods to bind replacement images and extract image data with downsampling.

**Initialization Process:**
The `init` method initializes the frame buffers (`buffer1` and `buffer2`) with linear filtering and clamp-to-edge wrapping. It generates an empty texture for `emptyBuffer`. It then initializes three pipelines: `firstPassPipeline`, `secondPassPipeline`, and `colorExtractAndDownsamplePipeline` using different shader paths and configurations.

**Buffer Resizing:**
The `render` method checks if the current width and height differ from the stored values. If they do, it updates the sizes of `buffer1` and `buffer2` to one-fourth of the current dimensions and validates them.

**GPU Performance Measurement:**
GPU performance is measured during each pass of the bloom effect using `gpu_performance_measuring.startQuery` and `gpu_performance_measuring.stopQuery` for `bloom_extract_downsample`, `bloom_first_pass`, and `bloom_second_pass`.

**Shaders Used:**
- **First Pass:** Shaders located at "assets/cubyz/shaders/bloom/first_pass.vert" and "assets/cubyz/shaders/bloom/first_pass.frag"
- **Second Pass:** Shaders located at "assets/cubyz/shaders/bloom/second_pass.vert" and "assets/cubyz/shaders/bloom/second_pass.frag"
- **Color Extract and Downsample:** Shaders located at "assets/cubyz/shaders/bloom/color_extractor_downsample.vert" and "assets/cubyz/shaders/bloom/color_extractor_downsample.frag"

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
- What are the steps involved in initializing the Bloom effect?
- How does the Bloom struct handle buffer resizing during rendering?
- Which shaders are used for each pass of the bloom effect?
- What is the purpose of the `bindReplacementImage` method?
- How is GPU performance measured during the bloom rendering process?
- What resources are cleaned up when the Bloom struct is deinitialized?

*Source: unknown | chunk_id: codebase_src_renderer.zig_chunk_3*
