# [hard/codebase_src_graphics_vulkan.zig] - Chunk 2

**Type:** implementation
**Keywords:** Vulkan, physical device, queue families, extensions, device score, logical device
**Symbols:** findQueueFamilies, checkDeviceExtensionSupport, getDeviceScore, pickPhysicalDevice, createLogicalDevice
**Concepts:** Vulkan device selection, queue family identification, extension support checking, device scoring, logical device creation

## Summary
Handles Vulkan physical device selection and logical device creation.

## Explanation
This chunk contains functions for selecting a suitable Vulkan physical device based on its capabilities and creating a logical device from it. The `findQueueFamilies` function identifies queue families that support both graphics and compute operations, as well as presentation to the surface. The `checkDeviceExtensionSupport` function verifies if all required extensions are supported by the device. The `getDeviceScore` function assigns a score to each device based on its type and features, helping in selecting the best device. The `pickPhysicalDevice` function iterates through available devices, scores them, and selects the one with the highest score that meets the necessary criteria. The `createLogicalDevice` function sets up the logical device using the selected physical device, configuring queues and enabling required extensions.

## Code Example
```zig
fn checkDeviceExtensionSupport(dev: c.VkPhysicalDevice) bool {
	const availableExtension = enumerateDeviceExtensionProperties(main.stackAllocator, dev, null);
	defer main.stackAllocator.free(availableExtension);
	for (deviceExtensions) |requiredName| continueOuter: {
		for (availableExtension) |available| {
			if (std.mem.eql(u8, std.mem.span(requiredName), std.mem.span(@as([*:0]const u8, @ptrCast(&available.extensionName))))) {
				break :continueOuter;
			}
		}
		std.log.warn("Rejecting device because extension {s} was not found", .{requiredName});
		return false;
	}
	return true;
}
```

## Related Questions
- How does the function `findQueueFamilies` determine suitable queue families?
- What is the purpose of the `checkDeviceExtensionSupport` function in Vulkan device selection?
- How is the score for a physical device calculated in this chunk?
- What steps are involved in selecting the best physical device using the `pickPhysicalDevice` function?
- Can you explain how the logical device is created in the `createLogicalDevice` function?
- What role do validation layers play in the creation of the Vulkan logical device?

*Source: unknown | chunk_id: codebase_src_graphics_vulkan.zig_chunk_2*
