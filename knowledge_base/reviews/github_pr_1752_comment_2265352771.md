# [src/graphics/vulkan.zig] - PR #1752 review diff

**Type:** review
**Keywords:** Vulkan, device features, VkPhysicalDeviceFeatures2, vkGetPhysicalDeviceFeatures2, Vulkan 1.2, extension chaining, API compatibility, feature support, physical device, graphics programming
**Symbols:** deviceExtensions, c.VK_KHR_SWAPCHAIN_EXTENSION_NAME, deviceFeatures, c.VkPhysicalDeviceFeatures, vkGetPhysicalDeviceFeatures2, VkPhysicalDeviceVulkan12Features
**Concepts:** Vulkan API, Feature querying, Extension handling

## Summary
The review suggests using `VkPhysicalDeviceFeatures2` and chaining Vulkan 1.2 features instead of directly accessing Vulkan 1.2 functions.

## Explanation
The reviewer points out that the current implementation does not utilize Vulkan 1.2 functions, which is incorrect for modern Vulkan applications. Instead, it should use the `VkPhysicalDeviceFeatures2` struct along with the `vkGetPhysicalDeviceFeatures2` function to access Vulkan 1.2 features through chaining. This approach ensures compatibility and proper feature querying as specified in the Vulkan specification.

## Related Questions
- What is the purpose of using `VkPhysicalDeviceFeatures2` in Vulkan?
- How does chaining work with `VkPhysicalDeviceFeatures2` to access Vulkan 1.2 features?
- Why is it important to use `vkGetPhysicalDeviceFeatures2` instead of direct Vulkan 1.2 functions?
- Can you explain the structure of `VkPhysicalDeviceVulkan12Features` and its role in feature querying?
- What are the benefits of using the `VkPhysicalDeviceFeatures2` approach for feature querying?
- How does this change ensure compatibility with different Vulkan implementations?

*Source: unknown | chunk_id: github_pr_1752_comment_2265352771*
