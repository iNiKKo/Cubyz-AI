# [issues/issue_1981.md] - Issue #1981 discussion

**Type:** review
**Keywords:** Vulkan error, VK_ERROR_INCOMPATIBLE_DRIVER, Intel HD Graphics 5500, Broadwell GT2, Windows 10, Linux, MESA drivers, OpenGL 4.6
**Concepts:** Vulkan, OpenGL, driver compatibility, operating system

## Summary
The user reports encountering Vulkan errors on an old laptop with incompatible drivers. The maintainer suggests switching to Linux for compatibility.

## Explanation
The issue revolves around a user's attempt to run a game that requires Vulkan support on an older Intel HD Graphics 5500 GPU, which lacks proper Vulkan drivers for Windows. The maintainer points out that the game only supports OpenGL 4.6 and suggests switching to Linux as a solution, where open-source MESA drivers might provide the necessary Vulkan support.

## Related Questions
- What are the Vulkan extensions available on the user's system?
- Why is VK_LAYER_KHRONOS_validation not found?
- How can the game be made compatible with older GPUs without Vulkan support?
- Are there any alternative drivers that could resolve the Vulkan error?
- Can the game be modified to fall back to OpenGL if Vulkan fails?
- What are the implications of running the game on Linux instead of Windows?

*Source: unknown | chunk_id: github_issue_1981_discussion*
