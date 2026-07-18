# [src/graphics/vulkan.zig] - PR #1752 review diff

**Type:** review
**Keywords:** VkPhysicalDeviceFeatures, pNext, Vulkan 1.0, extension, feature management, refactoring, improvement, limitation
**Symbols:** VkPhysicalDeviceFeatures, c.VK_KHR_SWAPCHAIN_EXTENSION_NAME
**Concepts:** Vulkan API, Extension and Feature Management

## Summary
The review discusses the limitations of `VkPhysicalDeviceFeatures` in Vulkan and advises against adding unnecessary improvements to the code.

## Explanation
The reviewer points out that `VkPhysicalDeviceFeatures` does not include a `pNext` entry, which means it cannot be extended with additional structures or new features introduced after Vulkan 1.0. This limitation could lead to significant changes in the code if future Vulkan versions introduce necessary features. The reviewer advises against making substantial improvements to the current implementation to prevent potential future refactoring.

## Related Questions
- What are the implications of `VkPhysicalDeviceFeatures` not having a `pNext` entry?
- How might future Vulkan versions affect the current implementation?
- Why is it important to avoid unnecessary improvements in this code?
- Can additional features be added to `VkPhysicalDeviceFeatures` after Vulkan 1.0?
- What are the potential consequences of extending `VkPhysicalDeviceFeatures` with new structures?
- How should the code be structured to accommodate future Vulkan feature additions?

*Source: unknown | chunk_id: github_pr_1752_comment_2265350449*
