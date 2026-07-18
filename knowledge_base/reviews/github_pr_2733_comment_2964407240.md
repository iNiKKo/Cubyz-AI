# [src/models.zig] - PR #2733 review diff

**Type:** review
**Keywords:** EntityModel, EntityVertex, vao, vbo, ebo, position, normal, UV, texture slot, irrelevant for entities
**Symbols:** EntityModel, vao, vbo, ebo, size, EntityVertex, pos, normal, uv, textureSlot, opaqueInLod
**Concepts:** data structures, OpenGL bindings

## Summary
A new struct `EntityModel` and its nested `EntityVertex` are added to the `models.zig` file.

## Explanation
The review indicates that a new struct `EntityModel` is being introduced, which includes fields for vertex array object (vao), vertex buffer object (vbo), element buffer object (ebo), and size. Additionally, a nested struct `EntityVertex` is defined with fields for position, normal, UV coordinates, texture slot, and an optional opaque in LOD flag. The reviewer notes that this addition is irrelevant for entities as it is an optimization intended for blocks.

## Related Questions
- What is the purpose of the `EntityModel` struct in the context of Cubyz?
- Why are fields like `vao`, `vbo`, and `ebo` included in the `EntityModel` struct?
- How does the `EntityVertex` struct contribute to rendering entities in Cubyz?
- What is the significance of the `opaqueInLod` field in the `EntityVertex` struct?
- Why was this change marked as irrelevant for entities by the reviewer?
- How might this addition impact performance or memory usage in Cubyz?

*Source: unknown | chunk_id: github_pr_2733_comment_2964407240*
