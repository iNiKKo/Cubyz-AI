# [hard/codebase_src_graphics_pipelines.zig] - Chunk 2

**Type:** api
**Keywords:** Vulkan, pipeline state, rasterization, multisampling, enum, struct
**Symbols:** RasterizationState, RasterizationState.depthClamp, RasterizationState.rasterizerDiscard, RasterizationState.polygonMode, RasterizationState.cullMode, RasterizationState.frontFace, RasterizationState.depthBias, RasterizationState.lineWidth, RasterizationState.PolygonMode, RasterizationState.CullModeFlags, RasterizationState.FrontFace, RasterizationState.DepthBias, RasterizationState.toVulkan, MultisampleState, MultisampleState.rasterizationSamples, MultisampleState.sampleShading, MultisampleState.minSampleShading, MultisampleState.sampleMask, MultisampleState.alphaToCoverage, MultisampleState.alphaToOne, MultisampleState.Count, MultisampleState.toVulkan
**Concepts:** graphics pipeline configuration, rasterization settings, multisampling settings

## Summary
Defines Vulkan pipeline states for rasterization and multisampling.

## Explanation
This chunk defines two structs, `RasterizationState` and `MultisampleState`, which encapsulate the configuration for rasterization and multisampling in a Vulkan graphics pipeline. Each struct includes fields corresponding to various Vulkan pipeline state parameters.

### RasterizationState
- **depthClamp**: A boolean indicating whether depth clamping is enabled (default: true).
- **rasterizerDiscard**: A boolean indicating whether the rasterizer should discard primitives (default: false).
- **polygonMode**: An enum specifying the polygon mode (`fill`, `line`, or `point`) (default: `fill`).
- **cullMode**: An enum specifying the culling mode (`none`, `front`, `back`, or `frontAndBack`) (default: `back`).
- **frontFace**: An enum specifying the front face orientation (`counterClockwise` or `clockwise`) (default: `counterClockwise`).
- **depthBias**: A struct containing depth bias settings (`constantFactor`, `clamp`, and `slopeFactor`) (default: null).
- **lineWidth**: A float specifying the line width (default: 1).

### MultisampleState
- **rasterizationSamples**: An enum specifying the number of rasterization samples (`1`, `2`, `4`, `8`, `16`, `32`, or `64`) (default: `1`).
- **sampleShading**: A boolean indicating whether sample shading is enabled (default: false).
- **minSampleShading**: A float specifying the minimum fraction of sample shading (default: undefined).
- **sampleMask**: An array of two unsigned integers representing the sample mask (default: `[0, 0]`).
- **alphaToCoverage**: A boolean indicating whether alpha to coverage is enabled (default: false).
- **alphaToOne**: A boolean indicating whether alpha to one is enabled (default: false).

The `toVulkan` methods convert these configurations into Vulkan's native structures (`VkPipelineRasterizationStateCreateInfo` and `VkPipelineMultisampleStateCreateInfo`) for use in creating graphics pipelines.

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
