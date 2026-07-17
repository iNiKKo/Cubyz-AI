# [src/graphics/vulkan.zig] - PR #2141 review diff

**Type:** review
**Keywords:** Vulkan, macOS, extensions, stackAllocator, initCapacity, performance, optimization
**Symbols:** createInstance, glfwExtensions, glfwExtensionCount, VK_KHR_PORTABILITY_ENUMERATION_EXTENSION_NAME, VK_KHR_GET_PHYSICAL_DEVICE_PROPERTIES_2_EXTENSION_NAME
**Concepts:** thread safety, backwards compatibility, memory allocation optimization

## Summary
Refactored Vulkan instance creation by adding macOS-specific extensions and optimizing extension handling.

## Explanation
The change involves modifying the Vulkan instance creation process to include additional extensions specific to macOS. The reviewer notes that precomputing the count and using `initCapacity` does not provide any performance benefit, as the stack allocator will only perform one allocation regardless of whether `initCapacity` is used or not.

## Related Questions
- What are the specific Vulkan extensions added for macOS?
- Why was it decided to use a stack allocator instead of precomputing the count?
- How does this change affect the compatibility with other operating systems?
- Is there any potential impact on memory usage with this refactoring?
- Can you explain the purpose of the `VK_KHR_PORTABILITY_ENUMERATION_EXTENSION_NAME` extension?
- What is the significance of the `VK_KHR_GET_PHYSICAL_DEVICE_PROPERTIES_2_EXTENSION_NAME` extension in this context?

*Source: unknown | chunk_id: github_pr_2141_comment_2491328566*
