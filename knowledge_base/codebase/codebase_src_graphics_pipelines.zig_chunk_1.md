# [hard/codebase_src_graphics_pipelines.zig] - Chunk 1

**Type:** implementation
**Keywords:** shader initialization, pipeline state creation, SPIR-V compilation, uniform binding, rasterization settings, multisampling, depth stencil testing
**Symbols:** init, initCompute, createShaderModule, bind, deinit, RasterizationState, RasterizationState.depthClamp, RasterizationState.rasterizerDiscard, RasterizationState.polygonMode, RasterizationState.cullMode, RasterizationState.frontFace, RasterizationState.depthBias, RasterizationState.lineWidth, RasterizationState.PolygonMode, RasterizationState.CullModeFlags, RasterizationState.FrontFace, RasterizationState.DepthBias, RasterizationState.toVulkan, MultisampleState, MultisampleState.rasterizationSamples, MultisampleState.sampleShading, MultisampleState.minSampleShading, MultisampleState.sampleMask, MultisampleState.alphaToCoverage, MultisampleState.alphaToOne, MultisampleState.Count, MultisampleState.toVulkan, DepthStencilState, DepthStencilState.depthTest, DepthStencilState.depthWrite, DepthStencilState.depthCompare, DepthStencilState.depthBoundsTest, DepthStencilState.stencilTest
**Concepts:** shader management, graphics pipeline configuration, Vulkan API interaction

## Summary
This chunk defines shader initialization, binding, and deinitialization functions, as well as structures for rasterization, multisample, and depth stencil states in the graphics pipeline.

## Explanation
The chunk contains several functions related to shader management: `init`, `initCompute`, and `createShaderModule`. The `init` function initializes a shader program with vertex and fragment shaders, while `initCompute` does the same for compute shaders. Both functions handle adding shaders, linking them, and setting up uniform locations if provided. The `createShaderModule` function reads a shader file, compiles it to SPIR-V, and creates a Vulkan shader module.

Structures like `RasterizationState`, `MultisampleState`, and `DepthStencilState` are defined with methods to convert their settings into Vulkan-compatible structures (`toVulkan`). These structs manage various aspects of the graphics pipeline such as rasterization parameters, multisampling, and depth/stencil testing.

## Code Example
```zig
fn bind(self: *const Shader) void {
	c.glUseProgram(self.id);
}
```

## Related Questions
- How do you initialize a shader program with vertex and fragment shaders?
- What does the `createShaderModule` function do?
- How is the rasterization state converted to Vulkan format?
- What are the possible values for `RasterizationState.polygonMode`?
- How is depth bias handled in the shader initialization process?
- What settings can be configured in the multisample state?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_1*
