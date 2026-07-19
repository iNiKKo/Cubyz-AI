# [issues/issue_3026.md] - Issue #3026 discussion

**Type:** review
**Keywords:** max texture array size, 2048 layers, GL_ARB_sparse_texture, bindless textures, software emulation, texture atlas, multiple texture arrays
**Concepts:** texture array size, bindless textures, sparse textures

## Summary
Discussion on increasing the maximum texture array size in Cubyz, exploring options like bindless textures and sparse textures.

## Explanation
Discussion on increasing the maximum texture array size in Cubyz, exploring options like bindless textures and sparse textures. The issue revolves around the limitation of the maximum texture array size being only **2048** layers, which is insufficient for certain use cases. A new world currently has 831 layers, so just a few addons could hit this limit. The maintainers and users discuss various potential solutions including using a texture atlas (which has too many problems, such as needing GL_REPEAT), multiple texture arrays (but that seems like it could only delay the inevitable and also would make sampling more annoying), bindless textures (not sure how well supported, but could be part of the planned Vulkan survey #2959), and software emulation (NO! Not again!). They explore the feasibility of sparse textures but find that they do not increase the layer limit significantly (`MAX_SPARSE_ARRAY_TEXTURE_LAYERS_ARB` also has a limit of 2048 layers). The discussion highlights the need to find a solution that supports larger textures without introducing significant complexity or performance overhead.

## Related Questions
- What is the current maximum number of layers for a texture array in Cubyz?
- How does bindless textures compare to other solutions for increasing texture array size?
- Can sparse textures be used to increase the layer limit beyond 2048?
- What are the potential performance implications of using multiple texture arrays?
- Why is software emulation not considered a viable solution for this issue?
- How does the use of bindless textures align with the planned Vulkan survey?

*Source: unknown | chunk_id: github_issue_3026_discussion*
