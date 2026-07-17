# [hard/codebase_src_graphics_pipelines.zig] - Chunk 2

**Type:** serialization
**Keywords:** VkSampleCountFlags, rasterizationSamples, sampleShadingEnable, alphaToCoverageEnable, depthTestEnable, stencilTestEnable, blendFactor, colorBlendOp, VK_COMPARE_OP_LESS, VK_STENCIL_OP_KEEP
**Symbols:** Count, MultisampleState.toVulkan, DepthStencilState, CompareOp, StencilTest, StencilOpState, StencilOp, DepthBoundsTest, ColorBlendAttachmentState
**Concepts:** pipeline state creation, multisampling configuration, depth-stencil testing, blending factors, Vulkan API mapping

## Summary
Defines Vulkan pipeline state structures for multisampling and depth-stencil blending.

## Explanation
This chunk declares a public enum Count mapping to VkSampleCountFlags values (@

## Related Questions
- What VkSampleCountFlags values are exposed by the Count enum?
- How does MultisampleState.toVulkan map rasterizationSamples to a Vulkan integer?
- Which fields in DepthStencilState control depth testing and stencil enabling?
- What is the default value for depthWrite in DepthStencilState?
- How are StencilOpState front/back converted to VkStencilOpState?
- Where are the blend factor enums defined relative to ColorBlendAttachmentState?
- Does this chunk define any public constants for blending presets?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_2*
