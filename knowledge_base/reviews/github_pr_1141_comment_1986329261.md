# [src/blueprint.zig] - PR #1141 review diff

**Type:** review
**Keywords:** server-side, client-side, data structures, architectural review, double updates, network interface, strict separation, data integrity
**Symbols:** blueprintVersion, GameIdToBlueprintIdMapType, BlockIdSizeType, BlockStorageType, BinaryWriter, BinaryReader, BlueprintCompression, FileHeader, Blueprint, main.List(Block), Vec3i, NeverFailingAllocator, User, mesh_storage, Block
**Concepts:** thread safety, backwards compatibility, memory leak, architectural design, data integrity

## Summary
The review highlights a critical architectural issue where server-side code attempts to directly update client-side data structures, which is prohibited.

## Explanation
The reviewer points out that accessing client-side data structures from the server side is fundamentally flawed. This practice can lead to unintended behavior such as double updates of the same data, once through the network interface and again within the server code. The review emphasizes the importance of maintaining strict separation between client and server logic to prevent such issues.

## Related Questions
- How can the server-side code be modified to avoid direct access to client-side data structures?
- What are the potential consequences of double updating the same data in Cubyz?
- How can strict separation between client and server logic be enforced in Cubyz?
- Can you provide examples of other architectural issues similar to this one in Cubyz?
- What measures should be taken to prevent memory leaks in Cubyz's blueprint system?
- How does the current implementation ensure thread safety when accessing shared data structures?

*Source: unknown | chunk_id: github_pr_1141_comment_1986329261*
