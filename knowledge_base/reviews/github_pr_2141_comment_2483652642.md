# [src/graphics/vulkan.zig] - PR #2141 review diff

**Type:** review
**Keywords:** macOS, Vulkan, extensions, instance creation, defer, memory leak, platform-specific, early return paths, stack allocator, extension names
**Symbols:** createInstance, glfwExtensions, glfwExtensionCount, main.stackAllocator, c.VK_KHR_PORTABILITY_ENUMERATION_EXTENSION_NAME, c.VK_KHR_GET_PHYSICAL_DEVICE_PROPERTIES_2_EXTENSION_NAME, c.VkInstanceCreateInfo, c.vkCreateInstance
**Concepts:** thread safety, memory management, platform-specific code, Vulkan API usage

## Summary
The code adds support for macOS-specific Vulkan extensions and adjusts the instance creation process to handle these extensions properly.

## Explanation
The change introduces conditional logic to handle macOS-specific Vulkan extensions by appending additional extension names to the existing list. It also modifies the `VkInstanceCreateInfo` structure to include these new extensions and sets appropriate flags. The reviewer notes that using `defer` for memory management is crucial to prevent leaks, especially in early return paths.

## Related Questions
- How does the code handle Vulkan extensions on macOS?
- What is the purpose of the `defer` statement in this context?
- Why are additional extensions added for macOS?
- How does the code ensure memory safety during instance creation?
- What are the implications of not using `defer` for memory management?
- How does the code handle different operating systems in Vulkan initialization?

*Source: unknown | chunk_id: github_pr_2141_comment_2483652642*
