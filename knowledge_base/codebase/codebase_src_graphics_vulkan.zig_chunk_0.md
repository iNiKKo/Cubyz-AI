# [hard/codebase_src_graphics_vulkan.zig] - Chunk 0

**Type:** api
**Keywords:** VkResultEnum, error handling, enumeration, Vulkan properties, global variables
**Symbols:** VkResultEnum, checkResult, checkResultErr, allocEnumerationGeneric, enumerateInstanceLayerProperties, enumerateInstanceExtensionProperties, enumeratePhysicalDevices, enumerateDeviceExtensionProperties, getPhysicalDeviceQueueFamilyProperties, getPhysicalDeviceSurfaceFormatsKHR, getPhysicalDeviceSurfacePresentModesKHR, instance, surface, physicalDevice, device, graphicsQueue, presentQueue
**Concepts:** Vulkan error handling, Vulkan property enumeration

## Summary
This chunk defines Vulkan error handling functions and enumerators for various Vulkan properties.

## Explanation
The chunk includes an enumeration of Vulkan result codes in `VkResultEnum` and several functions to handle these results, such as `checkResult`, `checkResultErr`, and `allocEnumerationGeneric`. It also provides enumerators for instance layers, extensions, physical devices, device extensions, queue family properties, surface formats, and present modes. Global variables for Vulkan instance, surface, physical device, device, graphics queue, and present queue are declared.

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
- What are the global variables declared in this chunk?
- How is error handling implemented for Vulkan results in this code?

*Source: unknown | chunk_id: codebase_src_graphics_vulkan.zig_chunk_0*
