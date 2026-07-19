# [hard/codebase_src_graphics_pipelines.zig] - Chunk 4

**Type:** api
**Keywords:** blend factor, blend operation, color write mask, vulkan conversion, packed struct
**Symbols:** ColorBlendAttachmentState, ColorBlendAttachmentState.enabled, ColorBlendAttachmentState.srcColorBlendFactor, ColorBlendAttachmentState.dstColorBlendFactor, ColorBlendAttachmentState.colorBlendOp, ColorBlendAttachmentState.srcAlphaBlendFactor, ColorBlendAttachmentState.dstAlphaBlendFactor, ColorBlendAttachmentState.alphaBlendOp, ColorBlendAttachmentState.colorWriteMask, ColorBlendAttachmentState.alphaBlending, ColorBlendAttachmentState.noBlending, BlendFactor, BlendFactor.zero, BlendFactor.one, BlendFactor.srcColor, BlendFactor.oneMinusSrcColor, BlendFactor.dstColor, BlendFactor.oneMinusDstColor, BlendFactor.srcAlpha, BlendFactor.oneMinusSrcAlpha, BlendFactor.dstAlpha, BlendFactor.oneMinusDstAlpha, BlendFactor.constantColor, BlendFactor.oneMinusConstantColor, BlendFactor.constantAlpha, BlendFactor.oneMinusConstantAlpha, BlendFactor.srcAlphaSaturate, BlendFactor.src1Color, BlendFactor.oneMinusSrc1Color, BlendFactor.src1Alpha, BlendFactor.oneMinusSrc1Alpha, BlendFactor.toGl, BlendOp, BlendOp.add, BlendOp.subtract, BlendOp.reverseSubtract, BlendOp.min, BlendOp.max, BlendOp.toGl, ColorComponentFlags, ColorComponentFlags.r, ColorComponentFlags.g, ColorComponentFlags.b, ColorComponentFlags.a, ColorComponentFlags.all, ColorComponentFlags.none, ColorBlendAttachmentState.toVulkan
**Concepts:** color blending, graphics pipeline, vulkan API

## Summary
Defines structures and enums for color blending states in graphics pipelines.

## Explanation
This chunk defines several structures and enumerations related to color blending in Vulkan graphics pipelines. The `ColorBlendAttachmentState` struct represents the state of a single attachment's blend settings, including factors and operations for both color and alpha channels, as well as a color write mask. It includes two static instances: `alphaBlending` and `noBlending`, which provide predefined configurations for blending and no blending, respectively.

The `alphaBlending` instance is defined as follows:
```zig
pub const alphaBlending: ColorBlendAttachmentState = .{
    .srcColorBlendFactor = .srcAlpha,
    .dstColorBlendFactor = .oneMinusSrcAlpha,
    .colorBlendOp = .add,
    .srcAlphaBlendFactor = .srcAlpha,
    .dstAlphaBlendFactor = .oneMinusSrcAlpha,
    .alphaBlendOp = .add,
};
```

The `noBlending` instance is defined as follows:
```zig
pub const noBlending: ColorBlendAttachmentState = .{
    .enabled = false,
    .srcColorBlendFactor = .zero,
    .dstColorBlendFactor = .zero,
    .colorBlendOp = .add,
    .srcAlphaBlendFactor = .zero,
    .dstAlphaBlendFactor = .zero,
    .alphaBlendOp = .add,
};
```

The `BlendFactor` enum maps Vulkan blend factor constants to their GL equivalents, and includes the following values:
- zero
- one
- srcColor
- oneMinusSrcColor
- dstColor
- oneMinusDstColor
- srcAlpha
- oneMinusSrcAlpha
- dstAlpha
- oneMinusDstAlpha
- constantColor
- oneMinusConstantColor
- constantAlpha
- oneMinusConstantAlpha
- srcAlphaSaturate
- src1Color
- oneMinusSrc1Color
- src1Alpha
- oneMinusSrc1Alpha

The `BlendOp` enum does the same for blend operations, and includes the following values:
- add
- subtract
- reverseSubtract
- min
- max

The `ColorComponentFlags` struct uses packed boolean fields to represent write masks for each color component (R, G, B, A). The `toVulkan` method converts a `ColorBlendAttachmentState` instance into its Vulkan counterpart.

## Code Example
```zig
pub fn toVulkan(self: ColorBlendAttachmentState) c.VkPipelineColorBlendAttachmentState {
	return .{
		.blendEnable = @intFromBool(self.enabled),
		.srcColorBlendFactor = @intFromEnum(self.srcColorBlendFactor),
		.dstColorBlendFactor = @intFromEnum(self.dstColorBlendFactor),
		.colorBlendOp = @intFromEnum(self.colorBlendOp),
		.srcAlphaBlendFactor = @intFromEnum(self.srcAlphaBlendFactor),
		.dstAlphaBlendFactor = @intFromEnum(self.dstAlphaBlendFactor),
		.alphaBlendOp = @intFromEnum(self.alphaBlendOp),
		.colorWriteMask = @as(u4, @bitCast(self.colorWriteMask)),
	};
}
```

## Related Questions
- What are the predefined blending states provided by `ColorBlendAttachmentState`?
- How does the `toVulkan` method convert a blend state to Vulkan format?
- What is the purpose of the `BlendFactor` enum in this context?
- What operations are supported by the `BlendOp` enum?
- How are color component flags represented in this code?
- What is the function of the `toGl` method in the `BlendFactor` and `BlendOp` enums?

*Source: unknown | chunk_id: codebase_src_graphics_pipelines.zig_chunk_4*
