# [src/blueprint.zig] - PR #1141 review diff

**Type:** review
**Keywords:** blueprint.zig, FileHeader, BlueprintCompression, BinaryWriter, BinaryReader, getBlockArraySize, getDecompressedDataSizeBytes, init, deinit, clear, capture, paste, mesh_storage, updateBlock
**Symbols:** blueprintVersion, GameIdToBlueprintIdMapType, BlockIdSizeType, BlockStorageType, BinaryWriter, BinaryReader, BlueprintCompression, FileHeader, Blueprint, main.List(Block), Vec3i, NeverFailingAllocator, User, mesh_storage, Block, ZonElement
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The `paste` function attempts to update block data on the server side by directly accessing a client-side structure (`mesh_storage`), which is architecturally incorrect.

## Explanation
The reviewer points out that the `paste` function in the `Blueprint` struct accesses and modifies `mesh_storage`, which is a client-side data structure. This direct access from server-side code is fundamentally flawed because it violates the separation of concerns between client and server. Additionally, this approach could lead to duplicate updates: once through the network interface and again directly on the server side. The reviewer emphasizes that such practices are never allowed and can cause significant architectural issues.

To address these issues, the `paste` function should be modified to ensure that block data is only updated through the network interface, avoiding direct access to client-side structures. This can be achieved by sending update requests to the server, which will then handle the updates appropriately without duplicating them. The architecture should also be adjusted to enforce strict separation between client and server data handling, ensuring that server-side code does not inadvertently access client-side structures.

For example, when a block is pasted, the `paste` function should send a network request to the server with the necessary block update information. The server will then process this request and update the block data accordingly, ensuring that the updates are handled correctly without duplication.

## Related Questions
- Why is direct access to client-side structures from server-side code problematic?
- How can the `paste` function be modified to avoid updating data twice?
- What are the potential consequences of not separating client and server data handling?
- How should the architecture be adjusted to prevent such violations in the future?
- Can you provide an example of how to correctly handle block updates between the client and server?
- What measures can be taken to ensure that server-side code does not inadvertently access client-side structures?

*Source: unknown | chunk_id: github_pr_1141_comment_1986329261*
