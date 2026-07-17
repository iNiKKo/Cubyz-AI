# [src/models.zig] - PR #2733 review diff

**Type:** review
**Keywords:** EntityModel, initFromObj, OBJ file, local allocations, stackAllocator, allocator, memory management, resource allocation, thread safety, backwards compatibility
**Symbols:** EntityModel, vao, vbo, ebo, size, texture, EntityVertex, initFromObj, allocator, path, modelFile
**Concepts:** memory management, resource allocation, stack allocator, heap allocator

## Summary
Added a new struct `EntityModel` for handling entity models and an initialization function `initFromObj` that reads model data from an OBJ file.

## Explanation
The change introduces a new struct `EntityModel` to encapsulate the properties of an entity model, including vertex array object (VAO), vertex buffer object (VBO), element buffer object (EBO), size, and texture. The function `initFromObj` is designed to initialize an `EntityModel` from an OBJ file. However, the reviewer points out a critical architectural issue: local allocations should use the stack allocator instead of passing an allocator into the function unless necessary. This concern highlights the importance of memory management practices in ensuring efficient and safe resource allocation.

## Related Questions
- What is the purpose of the `EntityModel` struct?
- How does the `initFromObj` function read model data from an OBJ file?
- Why should local allocations use the stack allocator instead of passing an allocator into the function?
- What are the implications of using a heap allocator for local allocations in this context?
- How can we ensure that the memory management practices in this code prevent memory leaks?
- What is the role of the `EntityVertex` struct within the `EntityModel` struct?

*Source: unknown | chunk_id: github_pr_2733_comment_2971527199*
