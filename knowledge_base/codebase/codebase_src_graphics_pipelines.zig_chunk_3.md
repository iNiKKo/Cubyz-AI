# [hard/codebase_src_graphics_pipelines.zig] - Chunk 3

**Type:** api
**Keywords:** struct, enum, optional fields, Vulkan conversion, depth test, stencil test
**Symbols:** DepthStencilState, DepthStencilState.depthTest, DepthStencilState.depthWrite, DepthStencilState.depthCompare, DepthStencilState.depthBoundsTest, DepthStencilState.stencilTest, DepthStencilState.CompareOp, DepthStencilState.StencilTest, DepthStencilState.StencilTest.front, DepthStencilState.StencilTest.back, DepthStencilState.StencilTest.StencilOpState, DepthStencilState.StencilTest.StencilOpState.failOp, DepthStencilState.StencilTest.StencilOpState.passOp, DepthStencilState.StencilTest.StencilOpState.depthFailOp, DepthStencilState.StencilTest.StencilOpState.compareOp, DepthStencilState.StencilTest.StencilOpState.compareMask, DepthStencilState.StencilTest.StencilOpState.writeMask, DepthStencilState.StencilTest.StencilOpState.reference, DepthStencilState.StencilTest.StencilOpState.StencilOp, DepthStencilState.DepthBoundsTest, DepthStencilState.toVulkan
**Concepts:** Graphics pipeline configuration, Depth testing, Stencil testing

## Summary
Defines the DepthStencilState struct and its conversion to Vulkan format.

## Explanation
The chunk defines a `DepthStencilState` struct that encapsulates depth and stencil testing configurations for graphics pipelines. The struct includes several fields, with specific default values where applicable. The `depthTest` field is a boolean indicating whether depth testing is enabled. The `depthWrite` field, which defaults to true, indicates whether the depth buffer should be written during rendering. The `depthCompare` field specifies the comparison operation used for depth testing and defaults to `.less`. The possible values for `depthCompare` are: `.never`, `.less`, `.equal`, `.lessOrEqual`, `.greater`, `.notEqual`, `.greateOrEqual`, and `.always`. The `depthBoundsTest` field is an optional struct that allows setting a range of valid depths. The `stencilTest` field is also optional and contains settings for stencil operations, including front and back face configurations.

The nested `StencilTest` struct includes two `StencilOpState` structs for front and back faces. Each `StencilOpState` defines operations to perform based on the outcome of stencil tests (`failOp`, `passOp`, `depthFailOp`) and specifies a comparison operation (`compareOp`). It also includes masks (`compareMask`, `writeMask`) and a reference value (`reference`). The `StencilOp` enum lists possible operations such as keeping the current value, setting it to zero, replacing it with a new value, incrementing or decrementing it with clamping or wrapping. The possible values for `StencilOp` are: `.keep`, `.zero`, `.replace`, `.incrementAndClamp`, `.decrementAndClamp`, `.invert`, `.incrementAndWrap`, and `.decrementAndWrap`.

The `DepthBoundsTest` struct allows setting minimum and maximum depth bounds. The `toVulkan` method converts the `DepthStencilState` instance into a Vulkan-compatible structure (`VkPipelineDepthStencilStateCreateInfo`). It handles optional fields by checking if they are null and appropriately setting Vulkan flags and values.

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
