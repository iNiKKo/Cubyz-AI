# [src/entityModel.zig] - PR #2762 review diff

**Type:** review
**Keywords:** GLB, OBJ, EntityModel, stackAllocator, globalAllocator, readAsset, loadRawModelDataFromObj, memory leak, thread safety, backwards compatibility
**Symbols:** EntityModel, stackAllocator, globalAllocator, readAsset, loadRawModelDataFromObj
**Concepts:** memory management, allocator usage, file formats

## Summary
The code was updated to read entity models in GLB format instead of OBJ and corrected the use of allocators.

## Explanation
The change involved modifying the `EntityModel` struct to load model data from a GLB file instead of an OBJ file. The reviewer emphasized the importance of using the stack allocator for local allocations, which was previously not adhered to. This update ensures better memory management and aligns with architectural guidelines.

Specifically, the code now reads entity models in GLB format using `main.assets.readAsset(main.globalAllocator, "entityModels/models", self.modelId.?, ".glb");`. The reviewer suggested changing this to use `main.stackAllocator` instead for better memory management practices.

The purpose of changing the file format from OBJ to GLB is to improve performance and reduce file size, as GLB is a binary format that supports more complex models with animations and materials. Using the stack allocator instead of the global allocator helps prevent memory leaks and improves thread safety by ensuring that allocations are scoped to the current function call.

This change affects memory management in Cubyz by ensuring that local allocations are properly managed, reducing the risk of memory leaks and improving overall performance. There is a potential for regression if existing models are not compatible with the new GLB format, but this should be mitigated by thorough testing.

The benefits of using the stack allocator over the global allocator include better control over memory usage, reduced fragmentation, and improved performance due to faster allocation and deallocation times. This change impacts backwards compatibility with existing models, as they may need to be converted to the new GLB format.

## Related Questions
- What is the purpose of changing the file format from OBJ to GLB?
- Why was the stack allocator emphasized in this review?
- How does this change affect memory management in Cubyz?
- Is there any potential for regression due to this update?
- What are the benefits of using the stack allocator over the global allocator?
- How does this change impact backwards compatibility with existing models?

*Source: unknown | chunk_id: github_pr_2762_comment_3068173654*
