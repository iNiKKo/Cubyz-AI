# [hard/codebase_src_renderer_mesh_storage.zig] - Chunk 4

**Type:** api
**Keywords:** mesh requests, networking, thread safety, memory allocation, bfs search, player position
**Symbols:** updateAndGetRenderChunks, meshList, playerPosInt, meshRequests, mapRequests, olderPx, olderPy, olderPz, olderRD, mutex, lastPx, lastPy, lastPz, lastRD, freeOldMeshes, createNewMeshes, searchList, firstPos, lod, node, hasMesh, nodeList, relPos, chunkSizeVector
**Concepts:** render chunk management, network request handling, breadth-first search, player position tracking

## Summary
Handles updating and retrieving render chunks based on player position and frustum.

## Explanation
This chunk contains the `updateAndGetRenderChunks` function, which updates the renderer's internal state with new player position and render distance. It calculates new and old positions and distances, creates mesh requests, sends network requests for light maps and chunk meshes, and performs a breadth-first search to find visible chunks. The function manages memory allocation for lists of mesh and map requests, uses mutexes for thread safety, and interacts with other modules like networking and chunk meshing.

## Related Questions
- What is the purpose of the `updateAndGetRenderChunks` function?
- How does the function handle memory allocation for mesh and map requests?
- What mechanism ensures thread safety in this chunk?
- How are network requests for light maps and chunk meshes sent?
- Describe the breadth-first search algorithm used to find visible chunks.
- What is the role of the `mutex` in this code?
- How does the function calculate new and old positions and distances?
- What steps are taken to manage old mesh data?
- How are new mesh requests created and processed?
- What is the significance of the `playerPosInt` variable?

*Source: unknown | chunk_id: codebase_src_renderer_mesh_storage.zig_chunk_4*
