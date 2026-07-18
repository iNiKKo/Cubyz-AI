# [issues/issue_2962.md] - Issue #2962 discussion

**Type:** review
**Keywords:** Vulkan Validation Error, VkRenderPass, vkDestroyDevice, resource cleanup, mid-migration, testing mode
**Symbols:** VkRenderPass, vkDestroyDevice
**Concepts:** Vulkan API, Resource Management, Validation Layers

## Summary
A Vulkan validation error occurs when exiting Cubyz due to a VkRenderPass not being destroyed before the device is destroyed.

## Explanation
The issue arises from the mid-migration state of Vulkan support in the codebase. The Vulkan specification requires that all child objects created on a device, such as VkRenderPass, must be destroyed or freed before the device itself is destroyed. This error indicates that a VkRenderPass object has not been properly cleaned up, leading to a validation failure when the device is being destroyed. The maintainer suggests that these objects should not be created outside of Vulkan testing mode to prevent such issues.

## Related Questions
- What is the current state of Vulkan support in Cubyz?
- How can we ensure that all Vulkan objects are properly destroyed before the device is destroyed?
- Is there a plan to complete the Vulkan migration in the near future?
- What are the implications of not destroying Vulkan objects on application exit?
- Are there any other similar validation errors related to Vulkan object management?
- How can we prevent such issues from occurring during development?

*Source: unknown | chunk_id: github_issue_2962_discussion*
