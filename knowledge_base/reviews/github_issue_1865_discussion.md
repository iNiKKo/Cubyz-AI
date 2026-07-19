# [issues/issue_1865.md] - Issue #1865 discussion

**Type:** review
**Keywords:** water to land, swimming, jumping, shore-side blocks, bilinear filtering, VK_LAYER_KHRONOS_validation, driver issue, missing configuration option, renderdoc, vulkan rendering
**Concepts:** player movement, bilinear filtering, Vulkan, validation layers

## Summary
Discussion about player movement from water to land in Cubyz, with a side note on bilinear filtering and Vulkan validation layers.

## Explanation
The discussion centers around an issue where players must stand on shore-side blocks and jump to transition from water to land. A user comment mentions bilinear filtering in a screenshot, which is believed to be related to driver issues or missing configuration options. However, the maintainer clarifies that Cubyz does not currently use Vulkan for rendering and that validation layers are merely debug tools, thus downplaying their significance. The current mechanism requires players to manually jump from water onto land, and there are no specific suggestions provided on how this can be improved.

## Related Questions
- What is the current mechanism for transitioning from water to land in Cubyz?
- How can the player movement from water to land be improved?
- Is bilinear filtering a known issue in Cubyz, and if so, what causes it?
- Why are Vulkan validation layers mentioned in the discussion, and how do they relate to the game's rendering?

*Source: unknown | chunk_id: github_issue_1865_discussion*
