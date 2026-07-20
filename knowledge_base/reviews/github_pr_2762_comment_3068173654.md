# [src/entityModel.zig] - PR #2762 review diff

**Type:** review
**Keywords:** GLB, OBJ, EntityModel, stackAllocator, globalAllocator, readAsset, loadRawModelDataFromObj, memory leak, thread safety, backwards compatibility
**Symbols:** EntityModel, stackAllocator, globalAllocator, readAsset, loadRawModelDataFromObj
**Concepts:** memory management, allocator usage, file formats

## Summary
The code was updated to read entity models in GLB format instead of OBJ and corrected the use of allocators.

## Explanation
The code was updated to read entity models in GLB format instead of OBJ and corrected the use of allocators. Specifically, the change involved modifying the `EntityModel` struct to load model data from a GLB file using `main.assets.readAsset(main.stackAllocator, "entityModels/models", self.modelId.?, ".glb");`. This update ensures better memory management by using the stack allocator for local allocations, which was previously not adhered to. The reviewer emphasized the importance of using the stack allocator for local allocations, which helps prevent memory leaks and improves thread safety by ensuring that allocations are scoped to the current function call.

## Related Questions
- What is the purpose of changing the file format from OBJ to GLB?
- Why was the stack allocator emphasized in this review?
- How does this change affect memory management in Cubyz?
- Is there any potential for regression due to this update?
- What are the benefits of using the stack allocator over the global allocator?
- How does this change impact backwards compatibility with existing models?

*Source: unknown | chunk_id: github_pr_2762_comment_3068173654*
