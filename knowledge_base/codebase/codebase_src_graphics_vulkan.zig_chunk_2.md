# [hard/codebase_src_graphics_vulkan.zig] - Chunk 2

**Type:** implementation
**Keywords:** Vulkan, physical device, queue families, extensions, device score, logical device
**Symbols:** findQueueFamilies, checkDeviceExtensionSupport, getDeviceScore, pickPhysicalDevice, createLogicalDevice
**Concepts:** Vulkan device selection, queue family identification, extension support checking, device scoring, logical device creation

## Summary
Handles Vulkan physical device selection and logical device creation.

## Explanation
This chunk contains functions for selecting a suitable Vulkan physical device based on its capabilities and creating a logical device from it. The `findQueueFamilies` function identifies queue families that support both graphics and compute operations (VK_QUEUE_GRAPHICS_BIT and VK_QUEUE_COMPUTE_BIT) as well as presentation to the surface. It iterates through all available queue families and checks if they have the required flags. If a family supports both graphics and compute, it is assigned as the graphics family. Additionally, it checks for present support by calling `vkGetPhysicalDeviceSurfaceSupportKHR` and assigns the first family with present support as the present family.

The `checkDeviceExtensionSupport` function verifies if all required extensions are supported by the device by comparing each required extension name with available extensions. It enumerates all available extensions using `enumerateDeviceExtensionProperties`, then iterates through the required extensions and checks if they exist in the list of available extensions. If any required extension is not found, it logs a warning and returns false.

The `getDeviceScore` function assigns a score to each device based on its type (CPU, discrete GPU, integrated GPU, other) and features. It first retrieves the device properties and features using `vkGetPhysicalDeviceProperties` and `vkGetPhysicalDeviceFeatures`. The base score is determined by the device type: CPU devices get a very low score, discrete GPUs get a high score, integrated GPUs get a moderate score, and other types get a slightly higher score. It then checks for available extensions and logs them. If the queue families are not complete or if any required feature is not supported, it returns 0. Otherwise, it returns the base score.

The `pickPhysicalDevice` function iterates through all available physical devices, scores them using `getDeviceScore`, and selects the one with the highest score that meets the necessary criteria. If no capable device is found, it returns an error.

The `createLogicalDevice` function sets up the logical device using the selected physical device. It first identifies unique queue families by adding the graphics and present family indices to a hash map. Then, it creates `VkDeviceQueueCreateInfo` structures for each unique family, setting the queue count to 1 and the priority to 1.0. The `VkDeviceCreateInfo` structure is then populated with the queue create infos, enabled features, validation layers (if supported), and device extensions. Finally, it calls `vkCreateDevice` to create the logical device and retrieves the graphics and present queues using `vkGetDeviceQueue`.

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
