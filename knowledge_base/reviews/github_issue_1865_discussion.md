# [issues/issue_1865.md] - Issue #1865 discussion

**Type:** review
**Keywords:** water to land, swimming, jumping, shore-side blocks, bilinear filtering, VK_LAYER_KHRONOS_validation, driver issue, missing configuration option, renderdoc, vulkan rendering
**Concepts:** player movement, bilinear filtering, Vulkan, validation layers

## Summary
Discussion about player movement from water to land in Cubyz, with a side note on bilinear filtering and Vulkan validation layers.

## Explanation
The issue revolves around the current requirement for players to stand on shore-side blocks and jump to transition from water to land. The discussion includes a user comment about bilinear filtering in a screenshot, which is believed to be related to driver issues or missing configuration options. A maintainer clarifies that Cubyz does not currently use Vulkan for rendering and that validation layers are merely debug tools, thus downplaying the significance of the Vulkan-related warning.

## Related Questions
- What is the current mechanism for transitioning from water to land in Cubyz?
- How can the player movement from water to land be improved?
- Is bilinear filtering a known issue in Cubyz, and if so, what causes it?
- Why are Vulkan validation layers mentioned in the discussion, and how do they relate to the game's rendering?
- What is the current status of Vulkan usage in Cubyz's rendering pipeline?
- How can driver issues or missing configuration options affect bilinear filtering in Cubyz?

*Source: unknown | chunk_id: github_issue_1865_discussion*
