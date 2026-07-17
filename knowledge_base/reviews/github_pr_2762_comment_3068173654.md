# [src/entityModel.zig] - PR #2762 review diff

**Type:** review
**Keywords:** entityModel.zig, .obj, .glb, stackAllocator, globalAllocator, local allocations, model loading, 3D models, Vertex, u32, defer, alloc
**Symbols:** EntityModel, main.assets.readAsset, main.stackAllocator, main.globalAllocator, quadInfos, vertices, indices
**Concepts:** memory management, thread safety, performance optimization

## Summary
The code was updated to read entity models from a '.glb' file instead of '.obj'. The reviewer emphasized the importance of using `stackAllocator` for local allocations.

## Explanation
The change involves modifying the file extension from '.obj' to '.glb', which is likely a more efficient binary format for 3D models. The reviewer's comment highlights a critical architectural decision regarding memory management, specifically the use of `stackAllocator` for local allocations to ensure better performance and avoid potential memory leaks. This update also implies a shift in the model loading process, potentially affecting how models are parsed and stored in memory.

## Related Questions
- Why was the file extension changed from '.obj' to '.glb'?
- What are the benefits of using 'stackAllocator' for local allocations in this context?
- How does changing the model format affect the parsing and storage of models?
- Is there a performance impact associated with switching from '.obj' to '.glb'?
- Are there any potential memory leak risks if 'globalAllocator' is used instead of 'stackAllocator'?
- What other architectural considerations should be taken into account when modifying model loading processes?

*Source: unknown | chunk_id: github_pr_2762_comment_3068173654*
