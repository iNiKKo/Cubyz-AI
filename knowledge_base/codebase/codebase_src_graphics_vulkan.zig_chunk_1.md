# [hard/codebase_src_graphics_vulkan.zig] - Chunk 1

**Type:** implementation
**Keywords:** Vulkan, instance creation, physical device, logical device, extension enumeration, queue family properties, surface formats, present modes
**Symbols:** enumerateDeviceExtensionProperties, getPhysicalDeviceQueueFamilyProperties, getPhysicalDeviceSurfaceFormatsKHR, getPhysicalDeviceSurfacePresentModesKHR, instance, surface, physicalDevice, device, graphicsQueue, presentQueue, version, interestingExtensions, init, deinit, validationLayers, checkValidationLayerSupport, createInstance, appInfo, glfwExtensionCount, glfwExtensions, availableExtensions, createFlags, extensions, createInfo
**Concepts:** Vulkan initialization, device enumeration, physical device selection, logical device creation

## Summary
This chunk handles Vulkan initialization and device enumeration in the Cubyz engine, including creating a Vulkan instance, physical device selection, and logical device creation.

## Explanation
The chunk defines several functions for enumerating Vulkan device properties such as extensions, queue families, surface formats, and present modes. It also manages global Vulkan objects like the instance, surface, physical device, and logical device. The `init` function initializes these Vulkan components, while `deinit` cleans them up. Key functions include `enumerateDeviceExtensionProperties`, `getPhysicalDeviceQueueFamilyProperties`, and `createInstance`. The chunk uses a stack allocator for temporary storage during initialization and checks for validation layers to ensure debugging support.

## Code Example
```zig
pub fn enumerateDeviceExtensionProperties(allocator: NeverFailingAllocator, dev: c.VkPhysicalDevice, layerName: ?[*:0]const u8) []c.VkExtensionProperties {
	return allocEnumerationGeneric(c.vkEnumerateDeviceExtensionProperties, allocator, .{dev, layerName});
}
```

## Related Questions
- How does the chunk enumerate Vulkan device extensions?
- What is the purpose of the `createInstance` function in this chunk?
- Which global Vulkan objects are managed by this chunk?
- How does the chunk handle validation layers during initialization?
- What is the role of the `deinit` function in this chunk?
- How does the chunk manage temporary storage during initialization?

*Source: unknown | chunk_id: codebase_src_graphics_vulkan.zig_chunk_1*
