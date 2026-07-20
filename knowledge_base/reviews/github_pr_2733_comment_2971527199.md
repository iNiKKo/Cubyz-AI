# [src/models.zig] - PR #2733 review diff

**Type:** review
**Keywords:** EntityModel, OBJ file, stackAllocator, heap allocation, VAO, VBO, EBO
**Symbols:** EntityModel, vao, vbo, ebo, size, texture, EntityVertex, initFromObj
**Concepts:** memory management, resource initialization

## Summary
Added a new `EntityModel` struct and its initialization method from OBJ files.

## Explanation
The change introduces a new `EntityModel` struct with fields for vertex array object (VAO), vertex buffer object (VBO), element buffer object (EBO), size, and texture. The `initFromObj` function is added to initialize an `EntityModel` from an OBJ file. This function reads the OBJ file using the provided allocator and initializes the `EntityModel` with the parsed data. If there's an error during file reading, it returns an error value. The reviewer notes that local allocations should use the stack allocator unless there's a specific need for heap allocation, suggesting potential improvements in memory management.

The `EntityVertex` struct contains fields for position (`pos`), normal (`normal`), and UV coordinates (`uv`). Each field is of type `[3]f32` for `pos` and `normal`, and `[2]f32` for `uv`. The `initFromObj` function processes the OBJ file to populate these fields accordingly.

The error handling mechanism in the `initFromObj` function is implemented using a `catch |err|` block, which returns an error value if there's an issue reading the OBJ file.

## Related Questions
- What is the purpose of the `EntityModel` struct?
- How does the `initFromObj` function initialize an `EntityModel`?
- Why should local allocations use the stack allocator?
- What are the fields in the `EntityVertex` struct?
- Is there a specific reason to pass an allocator into the `initFromObj` function?
- How is memory management handled for the `EntityModel` struct?

*Source: unknown | chunk_id: github_pr_2733_comment_2971527199*
