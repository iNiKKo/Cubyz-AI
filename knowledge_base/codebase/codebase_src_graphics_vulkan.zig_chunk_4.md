# [hard/codebase_src_graphics_vulkan.zig] - Chunk 4

**Type:** implementation
**Keywords:** swap chain creation, image views, device capabilities, resource management, Vulkan initialization
**Symbols:** createImageView, init, deinit
**Concepts:** Vulkan swap chain management

## Summary
Handles Vulkan swap chain creation and management.

## Explanation
This chunk manages the creation and destruction of a Vulkan swap chain. It initializes the swap chain by choosing appropriate formats, present modes, and image extents based on device capabilities. It also creates image views for each swap chain image. The `init` function sets up the swap chain with the desired properties, while the `deinit` function cleans up resources by destroying image views and the swap chain itself.

## Code Example
```zig
fn createImageView(image: c.VkImage) c.VkImageView {
	const createInfo: c.VkImageViewCreateInfo = .{
		.sType = c.VK_STRUCTURE_TYPE_IMAGE_VIEW_CREATE_INFO,
		.image = image,
		.viewType = c.VK_IMAGE_VIEW_TYPE_2D,
		.format = imageFormat,
		.components = .{
			.a = c.VK_COMPONENT_SWIZZLE_IDENTITY,
			.r = c.VK_COMPONENT_SWIZZLE_IDENTITY,
			.g = c.VK_COMPONENT_SWIZZLE_IDENTITY,
			.b = c.VK_COMPONENT_SWIZZLE_IDENTITY,
		},
		.subresourceRange = .{
			.aspectMask = c.VK_IMAGE_ASPECT_COLOR_BIT,
			.baseMipLevel = 0,
			.levelCount = 1,
			.baseArrayLayer = 0,
			.layerCount = 1,
		},
	};
	var result: c.VkImageView = undefined;
	checkResult(c.vkCreateImageView(device, &createInfo, null, &result));
	return result;
}
```

## Related Questions
- How does the `createImageView` function create an image view?
- What is the purpose of the `init` function in this chunk?
- How are image views managed during the swap chain initialization?
- What steps are taken to clean up resources in the `deinit` function?
- How does the code handle different queue family indices for graphics and present operations?
- What Vulkan structures are used to configure the swap chain creation?

*Source: unknown | chunk_id: codebase_src_graphics_vulkan.zig_chunk_4*
