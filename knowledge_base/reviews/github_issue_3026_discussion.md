# [issues/issue_3026.md] - Issue #3026 discussion

**Type:** review
**Keywords:** max texture array size, 2048 layers, GL_ARB_sparse_texture, bindless textures, software emulation, texture atlas, multiple texture arrays
**Concepts:** texture array size, bindless textures, sparse textures

## Summary
Discussion on increasing the maximum texture array size in Cubyz, exploring options like bindless textures and sparse textures.

## Explanation
The issue revolves around the limitation of the maximum texture array size being only **2048** layers, which is insufficient for certain use cases. The maintainers and users discuss various potential solutions including using a texture atlas, multiple texture arrays, bindless textures, and software emulation. They explore the feasibility of sparse textures but find that they do not increase the layer limit significantly (`MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB` also has a limit of 2048 layers). The discussion highlights the need to find a solution that supports larger textures without introducing significant complexity or performance overhead.

## Related Questions
- What is the current maximum number of layers for a texture array in Cubyz?
- How does bindless textures compare to other solutions for increasing texture array size?
- Can sparse textures be used to increase the layer limit beyond 2048?
- What are the potential performance implications of using multiple texture arrays?
- Why is software emulation not considered a viable solution for this issue?
- How does the use of bindless textures align with the planned Vulkan survey?

*Source: unknown | chunk_id: github_issue_3026_discussion*
