# [src/models.zig] - PR #2733 review diff

**Type:** review
**Keywords:** EntityModel, EntityVertex, VAO, VBO, EBO, position, normal, UV, texture slot, LOD, optimization, irrelevant
**Symbols:** EntityModel, vao, vbo, ebo, size, EntityVertex, pos, normal, uv, textureSlot, opaqueInLod
**Concepts:** data structure design, graphics pipeline, vertex buffer management

## Summary
A new struct `EntityModel` and its nested `EntityVertex` are added to the `models.zig` file.

## Explanation
The addition of the `EntityModel` struct introduces a new data structure for managing entity models in the graphics pipeline. The struct includes fields for vertex array object (VAO), vertex buffer object (VBO), element buffer object (EBO), and model size. The nested `EntityVertex` struct defines the structure of individual vertices, including position, normal, UV coordinates, texture slot, and an opaque LOD flag. However, a critical architectural review comment suggests that this optimization is irrelevant for entities, as it was originally intended for blocks.

## Related Questions
- Why was the `EntityModel` struct added to the `models.zig` file?
- What is the purpose of the `EntityVertex` nested struct within `EntityModel`?
- How does the addition of `EntityModel` affect the existing graphics pipeline?
- Is there a specific reason why this optimization is considered irrelevant for entities?
- What potential performance implications might arise from adding these new structures?
- How could the `EntityModel` struct be modified to better suit entity needs?
- Are there any memory management considerations with the introduction of these new structs?
- How does the addition of `EntityModel` impact backwards compatibility with existing code?
- What architectural changes are necessary to integrate `EntityModel` into the current system?
- Is there a need for additional testing or validation after adding `EntityModel`?

*Source: unknown | chunk_id: github_pr_2733_comment_2964407240*
