# [src/blueprint.zig] - PR #1141 review diff

**Type:** review
**Keywords:** blueprintVersion, GameIdToBlueprintIdMapType, BlockIdSizeType, BlockStorageType, BinaryWriter, BinaryReader, BlueprintCompression, FileHeader, backwards compatibility, network performance, data compression, memory optimization, serialization
**Symbols:** blueprintVersion, GameIdToBlueprintIdMapType, BlockIdSizeType, BlockStorageType, BinaryWriter, BinaryReader, BlueprintCompression, FileHeader
**Concepts:** backwards compatibility, network performance, data compression, memory optimization, serialization

## Summary
The review discusses architectural considerations for modifying code that affects saved files, network performance, and data compression. It also explores potential optimizations like using varints for block IDs and the benefits of automated serialization functions.

## Explanation
The reviewer emphasizes the importance of considering backwards compatibility when changing code that interacts with saved files, suggesting that developers should be cautious about modifications to ensure older save files remain functional. The discussion on network performance highlights the need to optimize data transmission, particularly in scenarios where multiple users are connected simultaneously. The review also touches on the use of varints for block IDs as a potential memory-saving technique, although it questions the effectiveness given that the palette and block array are already compressed using deflate. Additionally, there is a suggestion to implement universal serialization functions for structs, vectors, and arrays to reduce code duplication.

The `FileHeader` structure is defined with specific fields: `version`, `compression`, `paletteSizeBytes`, `paletteBlockCount`, `blockArraySizeX`, `blockArraySizeY`, and `blockArraySizeZ`. The reviewer suggests that changes to the blueprint version should be made cautiously to maintain compatibility with older save files. They also discuss the network performance implications of hosting a server with multiple users, noting that each user's effective upload speed is significantly reduced when many users are connected. The review questions whether using varints for block IDs would provide significant memory savings, given that the data is already compressed using deflate. Finally, there is a suggestion to implement universal serialization functions for structs, vectors, and arrays to reduce code duplication.

## Related Questions
- How does the modification of blueprintVersion affect older save files?
- What are the potential impacts on network performance if block IDs are changed to varints?
- Can you provide examples of where varints have been successfully used in similar contexts?
- How can we implement universal serialization functions for structs, vectors, and arrays?
- What are the trade-offs between using varints and existing compression algorithms like deflate?
- How does the current implementation ensure backwards compatibility with older save files?

*Source: unknown | chunk_id: github_pr_1141_comment_1992216207*
