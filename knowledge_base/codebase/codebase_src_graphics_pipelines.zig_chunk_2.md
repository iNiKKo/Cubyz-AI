# [hard/codebase_src_graphics_pipelines.zig] - Chunk 2

**Type:** api
**Keywords:** Vulkan, pipeline state, rasterization, multisampling, enum, struct
**Symbols:** RasterizationState, RasterizationState.depthClamp, RasterizationState.rasterizerDiscard, RasterizationState.polygonMode, RasterizationState.cullMode, RasterizationState.frontFace, RasterizationState.depthBias, RasterizationState.lineWidth, RasterizationState.PolygonMode, RasterizationState.CullModeFlags, RasterizationState.FrontFace, RasterizationState.DepthBias, RasterizationState.toVulkan, MultisampleState, MultisampleState.rasterizationSamples, MultisampleState.sampleShading, MultisampleState.minSampleShading, MultisampleState.sampleMask, MultisampleState.alphaToCoverage, MultisampleState.alphaToOne, MultisampleState.Count, MultisampleState.toVulkan
**Concepts:** graphics pipeline configuration, rasterization settings, multisampling settings

## Summary
Defines Vulkan pipeline states for rasterization and multisampling.

## Explanation
This chunk defines two structs, `RasterizationState` and `MultisampleState`, which encapsulate the configuration for rasterization and multisampling in a Vulkan graphics pipeline. Each struct includes fields corresponding to various Vulkan pipeline state parameters, such as depth clamping, culling modes, polygon modes, and sample counts. The `toVulkan` methods convert these configurations into Vulkan's native structures (`VkPipelineRasterizationStateCreateInfo` and `VkPipelineMultisampleStateCreateInfo`) for use in creating graphics pipelines.

## Code Example
```zig
const DepthBias = struct {
	constantFactor: f32,
	clamp: f32,
	slopeFactor: f32,
};
```

## Related Questions
- What are the fields in the RasterizationState struct?
- How does the toVulkan method convert a RasterizationState to a Vulkan structure?
- What are the possible values for the polygonMode field in RasterizationState?
- What is the default value for rasterizationSamples in MultisampleState?
- How does the MultisampleState struct handle sampleMask?
- What Vulkan structure does the toVulkan method of MultisampleState return?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_2*
