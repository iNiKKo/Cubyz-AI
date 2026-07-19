# [issues/issue_1981.md] - Issue #1981 discussion

**Type:** review
**Keywords:** Vulkan error, VK_ERROR_INCOMPATIBLE_DRIVER, Intel HD Graphics 5500, Broadwell GT2, Windows 10, Linux, MESA drivers, OpenGL 4.6
**Concepts:** Vulkan, OpenGL, driver compatibility, operating system

## Summary
The user reports encountering Vulkan errors on an old laptop with incompatible drivers. The maintainer suggests switching to Linux for compatibility.

## Explanation
The issue revolves around a user attempting to run a game that requires Vulkan support on an older Intel HD Graphics 5500 GPU, which lacks proper Vulkan drivers for Windows. The log indicates several Vulkan-related errors, including `VK_ERROR_INCOMPATIBLE_DRIVER` and `VK_ERROR_EXTENSION_NOT_PRESENT`. The available Vulkan instance extensions are listed as VK_EXT_debug_report, VK_EXT_debug_utils, VK_KHR_portability_enumeration, and VK_LUNARG_direct_driver_loading. The user's laptop is running Windows 10 with an Intel Core i3-5005U CPU and Intel HD Graphics 5500 GPU, which supports OpenGL 4.4 but not Vulkan 1.1 on Windows. The maintainer suggests switching to Linux, where open-source MESA drivers might provide the necessary Vulkan support.

## Related Questions
- What are the Vulkan extensions available on the user's system?
- Why is VK_LAYER_KHRONOS_validation not found?
- How can the game be made compatible with older GPUs without Vulkan support?
- Are there any alternative drivers that could resolve the Vulkan error?
- Can the game be modified to fall back to OpenGL if Vulkan fails?
- What are the implications of running the game on Linux instead of Windows?

*Source: unknown | chunk_id: github_issue_1981_discussion*
