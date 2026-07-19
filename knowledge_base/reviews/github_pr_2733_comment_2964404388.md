# [src/models.zig] - PR #2733 review diff

**Type:** review
**Keywords:** EntityModel, initFromQuads, OpenGL, vertex data, index data, vao, vbo, ebo
**Symbols:** EntityModel, initFromQuads, EntityVertex, quadInfos, vertices, indices, vao, vbo, ebo
**Concepts:** OpenGL rendering, vertex buffer objects (VBOs), element buffer objects (EBOs)

## Summary
Added a new `EntityModel` struct and its initialization function `initFromQuads` in `models.zig`. The function converts quad information into vertex and index data for OpenGL rendering.

## Explanation
The change introduces a new `EntityModel` struct to manage model data for entities. The `initFromQuads` function processes quad information, allocating memory for vertices and indices, populating them with data from the quads, and setting up OpenGL buffers. The `EntityVertex` struct contains fields such as position (`pos`), normal (`normal`), UV coordinates (`uv`), texture slot (`textureSlot`), and opaque in LOD (`opaqueInLod`). The function initializes these fields for each vertex based on the quad information provided. Memory allocation is handled using `main.stackAllocator`, and allocated memory is freed at the end of the function. OpenGL functions such as `glGenVertexArrays`, `glBindVertexArray`, `glGenBuffers`, `glBufferData`, and `glVertexAttribPointer` are used to set up vertex and element buffers. The reviewer suggests using `@fieldParentPtr` to avoid hardcoding offsets in vertex attribute pointers, which could help catch errors related to struct layout changes.

## Related Questions
- What is the purpose of the `EntityModel` struct?
- How does the `initFromQuads` function convert quad information into vertex and index data?
- Why is it suggested to use `@fieldParentPtr` instead of hardcoding offsets?
- What are the benefits of using `@fieldParentPtr` in this context?
- How does the code handle memory allocation for vertices and indices?
- What OpenGL functions are used to set up vertex and element buffers?
- How is the vertex attribute pointer configured in the code?
- What potential issues could arise from hardcoding offsets in vertex attribute pointers?
- How does the code ensure that allocated memory is properly freed?
- What is the role of `@sizeOf` in this context?

*Source: unknown | chunk_id: github_pr_2733_comment_2964404388*
