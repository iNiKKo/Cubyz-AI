# [hard/codebase_src_graphics_pipelines.zig] - Chunk 3

**Type:** api
**Keywords:** struct, enum, optional fields, Vulkan conversion, depth test, stencil test
**Symbols:** DepthStencilState, DepthStencilState.depthTest, DepthStencilState.depthWrite, DepthStencilState.depthCompare, DepthStencilState.depthBoundsTest, DepthStencilState.stencilTest, DepthStencilState.CompareOp, DepthStencilState.StencilTest, DepthStencilState.StencilTest.front, DepthStencilState.StencilTest.back, DepthStencilState.StencilTest.StencilOpState, DepthStencilState.StencilTest.StencilOpState.failOp, DepthStencilState.StencilTest.StencilOpState.passOp, DepthStencilState.StencilTest.StencilOpState.depthFailOp, DepthStencilState.StencilTest.StencilOpState.compareOp, DepthStencilState.StencilTest.StencilOpState.compareMask, DepthStencilState.StencilTest.StencilOpState.writeMask, DepthStencilState.StencilTest.StencilOpState.reference, DepthStencilState.StencilTest.StencilOpState.StencilOp, DepthStencilState.DepthBoundsTest, DepthStencilState.toVulkan
**Concepts:** Graphics pipeline configuration, Depth testing, Stencil testing

## Summary
Defines the DepthStencilState struct and its conversion to Vulkan format.

## Explanation
The chunk defines a `DepthStencilState` struct that encapsulates depth and stencil testing configurations for graphics pipelines. It includes nested structs like `StencilTest`, `StencilOpState`, and `DepthBoundsTest`. The `toVulkan` method converts the `DepthStencilState` instance into a Vulkan-compatible structure, handling optional fields appropriately.

## Code Example
```zig
fn toVulkan(self: StencilOpState) c.VkStencilOpState {
	return .{
		.failOp = @intFromEnum(self.failOp),
		.passOp = @intFromEnum(self.passOp),
		.depthFailOp = @intFromEnum(self.depthFailOp),
		.compareOp = @intFromEnum(self.compareOp),
		.compareMask = self.compareMask,
		.writeMask = self.writeMask,
		.reference = self.reference,
	};
}
```

## Related Questions
- What is the purpose of the DepthStencilState struct?
- How does the toVulkan method convert a DepthStencilState instance?
- What are the possible values for depthCompare in DepthStencilState?
- How is the StencilOpState converted to Vulkan format?
- What fields are optional in the DepthStencilState struct?
- How does the chunk handle optional fields like depthBoundsTest and stencilTest?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_3*
