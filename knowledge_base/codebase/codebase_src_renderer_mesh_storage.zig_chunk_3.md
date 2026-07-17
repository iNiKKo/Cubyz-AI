# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 3

**Type:** implementation
**Keywords:** mesh creation, render distance calculation, coordinate iteration, LOD handling, memory management
**Symbols:** createNewMeshes, reduceRenderDistance
**Concepts:** mesh storage, LOD management, chunk rendering

## Summary
Handles mesh storage and creation for rendering, managing LODs and chunk positions.

## Explanation
This chunk contains logic for managing mesh storage and creation in the renderer. It includes functions to create new meshes based on player position changes and to handle old map deinitialization. The code calculates render distances, iterates over x, y, and z coordinates, and manages mesh requests and light map fragment positions. It uses bitwise operations and assertions for bounds checking and coordinate calculations.

## Related Questions
- What is the purpose of the `createNewMeshes` function?
- How does the code calculate render distances for different LODs?
- What operations are performed on x, y, and z coordinates in this chunk?
- How does the code handle old map deinitialization?
- What is the role of the `reduceRenderDistance` function in this chunk?
- How does the code manage mesh requests and light map fragment positions?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_3*
