# [hard/codebase_src_graphics_vulkan.zig] - Chunk 0

**Type:** api
**Keywords:** VkResultEnum, checkResult, allocEnumerationGeneric, Vulkan API calls, global variables
**Symbols:** VkResultEnum, checkResult, checkResultErr, allocEnumerationGeneric, enumerateInstanceLayerProperties, enumerateInstanceExtensionProperties, enumeratePhysicalDevices, enumerateDeviceExtensionProperties, getPhysicalDeviceQueueFamilyProperties, getPhysicalDeviceSurfaceFormatsKHR, getPhysicalDeviceSurfacePresentModesKHR, instance, surface, physicalDevice, device, graphicsQueue, presentQueue
**Concepts:** Vulkan error handling, Vulkan enumeration functions, dynamic memory allocation

## Summary
This chunk defines Vulkan error handling and enumeration functions for various Vulkan properties.

## Explanation
The chunk includes an enum `VkResultEnum` mapping Vulkan result codes to human-readable names. It provides two main functions, `checkResult` and `checkResultErr`, which convert Vulkan result codes to the corresponding enum values and log errors if necessary. The function `allocEnumerationGeneric` is a generic allocator for Vulkan enumeration functions, handling dynamic memory allocation and reallocation based on the number of items returned by Vulkan API calls. Several public functions like `enumerateInstanceLayerProperties`, `enumeratePhysicalDevices`, etc., use this generic allocator to enumerate various Vulkan properties. Global variables such as `instance`, `surface`, `physicalDevice`, `device`, `graphicsQueue`, and `presentQueue` are declared for storing Vulkan instance, surface, physical device, logical device, graphics queue, and present queue handles respectively.

## Code Example
```zig
pub fn checkResult(result: c.VkResult) void {
	const resultEnum = std.enums.fromInt(VkResultEnum, result) orelse {
		std.log.err("Encountered a vulkan error with unknown error code {}", .{result});
		return;
	};
	if (resultEnum == .VK_SUCCESS) return;
	std.log.err("Encountered a vulkan error: {s}", .{@tagName(resultEnum)});
}
```

## Related Questions
- What is the purpose of the `VkResultEnum` enum?
- How does the `checkResult` function handle Vulkan errors?
- What does the `allocEnumerationGeneric` function do?
- Which Vulkan properties can be enumerated using this chunk's functions?
- What are the global variables declared in this chunk and what do they represent?
- How is error handling implemented for Vulkan API calls in this chunk?

*Source: unknown | chunk_id: codebase_src_graphics_vulkan.zig_chunk_0*
