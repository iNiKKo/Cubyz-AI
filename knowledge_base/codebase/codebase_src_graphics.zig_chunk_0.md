# [hard/codebase_src_graphics.zig] - Chunk 0

**Type:** api
**Keywords:** vector types, window handling, allocator utilities, C bindings, graphics pipelines, Vulkan
**Symbols:** Mat4f, Vec4i, Vec4f, Vec2f, Vec2i, Vec3f, Window, NeverFailingAllocator, ComputePipeline, Pipeline, vulkan
**Concepts:** OpenGL utilities, vector math, window management, Vulkan integration

## Summary
This chunk imports necessary modules and types for graphics handling, including OpenGL utilities, vector math, window management, and Vulkan integration.

## Explanation
The chunk begins by importing standard library (`std`) and built-in Zig features. It then imports various vector types from `vec.zig` such as matrices (`Mat4f`), integer vectors (`Vec4i`, `Vec2i`), and floating-point vectors (`Vec4f`, `Vec2f`, `Vec3f`). The `main` module is imported for window management (`Window`) and allocator utilities (`NeverFailingAllocator`). External C bindings are also imported. Additionally, it imports graphics pipelines from `graphics/pipelines.zig` and re-exports `ComputePipeline` and `Pipeline`. Finally, it imports Vulkan-specific graphics handling from `graphics/vulkan.zig`.

## Related Questions
- What vector types are imported from vec.zig?
- Which modules are imported for window management and allocation?
- How is Vulkan integration handled in this chunk?
- What external C bindings are used?
- Which graphics pipelines are re-exported?
- What standard library features are utilized?

*Source: unknown | chunk_id: codebase_src_graphics.zig_chunk_0*
