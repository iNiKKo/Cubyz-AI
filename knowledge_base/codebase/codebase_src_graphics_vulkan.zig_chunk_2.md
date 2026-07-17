# [hard/codebase_src_graphics_vulkan.zig] - Chunk 2

**Type:** implementation
**Keywords:** Vulkan instance creation, physical devices, queue families, extensions, validation layers
**Symbols:** extensions, QueueFamilyIndidices, findQueueFamilies, checkDeviceExtensionSupport, getDeviceScore, pickPhysicalDevice
**Concepts:** Vulkan initialization, physical device selection, queue family management, extension handling

## Summary
Handles Vulkan instance creation and physical device selection.

## Explanation
This chunk manages the initialization of a Vulkan instance and selects an appropriate physical device. It appends necessary extensions to the instance, checks for validation layers, and creates the Vulkan instance using these settings. The code also defines structures and functions to find suitable queue families, check device extension support, score devices based on their properties, and pick the best physical device among available options.

## Code Example
```zig
fn isComplete(self: QueueFamilyIndidices) bool {
	return self.graphicsFamily != null and self.presentFamily != null;
}
```

## Related Questions
- What are the necessary Vulkan extensions for instance creation?
- How does the code check for validation layer support?
- What is the process for scoring physical devices?
- How are queue families identified in this chunk?
- What error handling is implemented for device selection?
- How does the code handle macOS-specific Vulkan extensions?

*Source: unknown | chunk_id: codebase_src_graphics_vulkan.zig_chunk_2*
