# [src/models.zig] - PR #2733 review diff

**Type:** review
**Keywords:** EntityModel, initFromQuads, OpenGL, VAO, VBO, EBO, quad processing, stack allocation, vertex attributes, pointer validity
**Symbols:** EntityModel, initFromQuads, QuadInfo, vao, vbo, ebo, size, EntityVertex, vertices, indices, lut
**Concepts:** OpenGL buffer management, vertex attribute setup, undefined behavior prevention

## Summary
Added a new `EntityModel` struct and its initialization function `initFromQuads` in `src/models.zig`. This function processes quad information to create vertex and index buffers for rendering.

## Explanation
The change introduces a new `EntityModel` struct designed to encapsulate the Vertex Array Object (VAO), Vertex Buffer Object (VBO), Element Buffer Object (EBO), and size of an entity model. The `initFromQuads` function initializes these components from quad information, allocating memory for vertices and indices on the stack using `main.stackAllocator`. It then populates these buffers with data derived from the quads, setting up vertex attributes and binding them to OpenGL buffers. The reviewer notes a critical architectural concern regarding pointer validity in OpenGL calls, suggesting potential undefined behavior if pointers are invalid.

## Related Questions
- What is the purpose of the `EntityModel` struct in Cubyz?
- How does the `initFromQuads` function process quad information to create vertex and index buffers?
- Why is stack allocation used for vertices and indices in the `initFromQuads` function?
- What are the potential consequences if pointers passed to OpenGL functions are invalid?
- How does the code handle memory deallocation of vertices and indices after buffer creation?
- What is the role of the lookup table (`lut`) in generating index data for the entity model?

*Source: unknown | chunk_id: github_pr_2733_comment_2967145926*
