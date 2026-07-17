# [src/graphics/vulkan.zig] - PR #1752 review diff

**Type:** review
**Keywords:** VkPhysicalDeviceFeatures, pNext, Vulkan1.2, Extensions, Feature Support, Future-Proofing, Code Refactoring, Architectural Design, Documentation, Technical Requirements
**Symbols:** VkPhysicalDeviceFeatures, VK_KHR_SWAPCHAIN_EXTENSION_NAME
**Concepts:** Extensibility, Backwards Compatibility

## Summary
The review highlights that `VkPhysicalDeviceFeatures` lacks a `pNext` entry, preventing the addition of new features introduced after Vulkan 1.0. This could necessitate significant changes in the future if such features are required.

## Explanation
The reviewer points out that the current implementation using `VkPhysicalDeviceFeatures` cannot be extended with additional structures or newer features from later Vulkan versions (e.g., VK1.2). This limitation means that any future need for these new features would require a major overhaul of the code, potentially introducing bugs or breaking existing functionality. The reviewer advises against making substantial improvements to this part of the code until such extensions are supported.

## Related Questions
- What are the implications of not supporting `pNext` in `VkPhysicalDeviceFeatures`?
- How can we extend support for newer Vulkan features without significant code changes?
- Are there any plans to update the Vulkan implementation to support future extensions?
- What are the potential risks of delaying improvements until extensibility is addressed?
- How does this limitation affect compatibility with different Vulkan versions?
- Can we identify a pattern or strategy to handle similar limitations in the future?

*Source: unknown | chunk_id: github_pr_1752_comment_2265350449*
