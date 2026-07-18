# [issues/issue_102.md] - Issue #102 discussion

**Type:** review
**Keywords:** vulkan, opengl, vulkan-zig, glad, vk.xml, InstanceCreateInfo, AllocationCallbacks, Instance, Result, vkCreateInstance, type safety, driver reliability, platform support, error handling
**Symbols:** vulkan, opengl, vulkan-zig, glad, vk.xml, InstanceCreateInfo, AllocationCallbacks, Instance, Result, vkCreateInstance
**Concepts:** API transition, type safety, driver reliability, platform support, error handling

## Summary
The discussion revolves around transitioning Cubyz from OpenGL to Vulkan, highlighting advantages like better tooling, platform support, and error detection, but also noting potential development costs and bugs in existing Vulkan implementations.

## Explanation
The issue discusses the benefits of using Vulkan over OpenGL for Cubyz, including improved tooling, broader platform support (including macOS and mobile GPUs), more consistent performance, and larger buffer sizes. However, it acknowledges that this transition comes with significant development costs. The maintainer expresses concerns about the stability of Zig libraries compared to C libraries and the potential difficulty in maintaining abstraction layers. Users suggest using a Zig-based Vulkan binding library called 'vulkan-zig' for better type safety and error handling, but the maintainer is cautious due to the risk of diverging from official documentation and tutorials. The discussion also touches on the reliability of Vulkan drivers, citing examples of bugs in GTK4's Vulkan renderer and issues with Intel GPUs. Despite these concerns, there is a desire to use Vulkan for its wider support and better extension capabilities.

## Related Questions
- What are the main advantages of using Vulkan over OpenGL for Cubyz?
- Why is there a concern about maintaining Zig libraries compared to C libraries?
- How does 'vulkan-zig' improve upon traditional Vulkan bindings in Zig?
- What specific bugs have been encountered with Vulkan drivers, particularly on Intel GPUs?
- How does the maintainer view the future of Vulkan driver improvements?
- What are the potential performance gains from using Vulkan in Cubyz?
- Why is there a desire to use Vulkan for its wider support and better extension capabilities?

*Source: unknown | chunk_id: github_issue_102_discussion*
