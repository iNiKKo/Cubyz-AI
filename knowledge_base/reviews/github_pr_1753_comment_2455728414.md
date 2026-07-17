# [src/graphics/vulkan.zig] - PR #1753 review diff

**Type:** review
**Keywords:** VkSwapchainKHR, VkSurfaceFormatKHR, VkPresentModeKHR, VkExtent2D, image views, abstraction, Image struct
**Symbols:** SwapChain, SupportDetails, createImageView
**Concepts:** Vulkan API, swap chain management, abstraction

## Summary
Added SwapChain struct and related functions to handle Vulkan swap chain creation and management.

## Explanation
The change introduces a new SwapChain struct to encapsulate swap chain-related data and operations. This includes methods to initialize, deinitialize, choose format, present mode, and extent for the swap chain. The reviewer suggests considering future abstraction by wrapping VkImage in an Image struct with a view() method, which could simplify image view creation.

## Related Questions
- What is the purpose of the SwapChain struct in the Vulkan implementation?
- How does the SupportDetails struct assist in choosing swap chain parameters?
- Why is there a TODO comment about using MAILBOX present mode?
- What potential benefits could come from abstracting VkImage into an Image struct?
- How does the chooseSwapExtent function determine the extent of the swap chain images?
- What are the implications of not finding the BGRA8 format during swap chain creation?

*Source: unknown | chunk_id: github_pr_1753_comment_2455728414*
