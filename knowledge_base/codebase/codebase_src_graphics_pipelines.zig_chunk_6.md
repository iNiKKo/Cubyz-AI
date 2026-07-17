# [hard/codebase_src_graphics_pipelines.zig] - Chunk 6

**Type:** implementation
**Keywords:** depth testing, color write masks, blending operations, stencil tests, GLSLang initialization, shader binding
**Symbols:** GraphicsPipeline, GraphicsPipeline.depthState, GraphicsPipeline.blendState, GraphicsPipeline.init, ComputePipeline, ComputePipeline.shader, ComputePipeline.init, ComputePipeline.deinit, ComputePipeline.bind, init, deinit
**Concepts:** graphics pipeline configuration, compute shader handling, OpenGL state management

## Summary
This chunk defines graphics pipeline configurations and initialization functions for both rendering and compute shaders.

## Explanation
The chunk primarily deals with setting up OpenGL state for graphics pipelines, including depth testing, color write masks, blending operations, and stencil tests. It also defines a `ComputePipeline` struct for handling compute shaders, providing methods to initialize, deinitialize, and bind compute shaders. The `init` function initializes the GLSLang process, while the `deinit` function finalizes it.

## Code Example
```zig
pub fn init(computePath: []const u8, defines: []const u8, uniformStruct: anytype) ComputePipeline {
	return .{
		.shader = .initCompute(computePath, defines, uniformStruct),
	};
}
```

## Related Questions
- How does the GraphicsPipeline struct initialize depth testing?
- What methods are available for managing compute shaders in the ComputePipeline struct?
- What is the purpose of the init function in this chunk?
- How does the code handle color write masks for different attachments?
- What steps are taken to ensure proper cleanup with the deinit function?
- How are blending operations configured for each attachment in the GraphicsPipeline?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_6*
