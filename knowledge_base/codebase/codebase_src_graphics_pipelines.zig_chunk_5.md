# [hard/codebase_src_graphics_pipelines.zig] - Chunk 5

**Type:** implementation
**Keywords:** descriptor set layout, pipeline layout, shader stages, rasterization state, depth stencil state, color blend state, dynamic state, vulkan device, glEnable, glDisable
**Symbols:** Pipeline, Pipeline.shader, Pipeline.rasterState, Pipeline.multisampleState, Pipeline.depthStencilState, Pipeline.blendState, Pipeline.descriptorSetLayout, Pipeline.pipelineLayout, Pipeline.graphicsPipeline, Pipeline.vulkanCreationSuccessful, Pipeline.init, Pipeline.deinit, Pipeline.bind, Pipeline.initVulkan, conditionalEnable
**Concepts:** graphics pipeline, vulkan rendering, opengl settings

## Summary
Handles the creation and management of graphics pipelines in Vulkan.

## Explanation
This chunk defines the `Pipeline` struct responsible for managing graphics pipelines in Vulkan. It includes methods for initializing (`init`), deinitializing (`deinit`), and binding (`bind`) a pipeline. The `initVulkan` function sets up Vulkan-specific components like descriptor set layouts, pipeline layouts, and graphics pipelines. The `bind` method configures various OpenGL settings based on the pipeline's state, including depth testing, culling, blending, and more.

## Code Example
```zig
fn conditionalEnable(typ: c.GLenum, val: bool) void {
		if (val) {
			c.glEnable(typ);
		} else {
			c.glDisable(typ);
		}
	}
```

## Related Questions
- What is the purpose of the `initVulkan` function in the `Pipeline` struct?
- How does the `bind` method configure OpenGL settings based on the pipeline's state?
- What assertions are made in the `init` method to ensure compatibility with Vulkan features?
- What Vulkan components are created and managed by the `Pipeline` struct?
- How is error handling implemented during Vulkan pipeline creation?
- What is the role of the `conditionalEnable` function in the `Pipeline` struct?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_5*
