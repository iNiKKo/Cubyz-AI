# [src/blueprint.zig] - PR #1141 review diff

**Type:** review
**Keywords:** blueprint.zig, FileHeader, BlueprintCompression, version, compression, paletteSizeBytes, paletteBlockCount, blockArraySizeX, blockArraySizeY, blockArraySizeZ, varints, network optimization, memory usage, backwards compatibility
**Symbols:** blueprint.zig, FileHeader, BlueprintCompression, version, compression, paletteSizeBytes, paletteBlockCount, blockArraySizeX, blockArraySizeY, blockArraySizeZ
**Concepts:** serialization, deserialization, backwards compatibility, network optimization, memory usage

## Summary
The review discusses the addition of a new file `blueprint.zig` with a struct `FileHeader` and an enum `BlueprintCompression`. The reviewer emphasizes the importance of considering changes to serialized data structures carefully to maintain compatibility with older save files. They also suggest using variable-length integers (varints) for efficient network communication and propose adding serialization functions for common types like vectors.

## Explanation
The review focuses on the architectural implications of adding a new file `blueprint.zig` that includes a struct `FileHeader` and an enum `BlueprintCompression`. The `FileHeader` struct contains several fields: `version`, `compression`, `paletteSizeBytes`, `paletteBlockCount`, `blockArraySizeX`, `blockArraySizeY`, and `blockArraySizeZ`, all of which are initialized to specific values. The reviewer highlights the need to be cautious when modifying serialized data structures, as changes can affect compatibility with older save files. They also discuss the importance of optimizing network communication by using varints for encoding packet lengths and other small integers, which can significantly reduce memory usage and improve performance in scenarios with limited bandwidth. Additionally, the reviewer suggests creating universal serialization functions for common types like vectors to avoid code duplication and improve maintainability.

The reviewer mentions that drives read at Gb/s speeds, but networks have much lower throughput, such as an upload speed of 20 Mbit/s, which can be further reduced when multiple users are connected. They also note that the current usage of varints is limited to encoding packet lengths in the network system and suggest using it more often for other small integers, like block IDs, to save memory in small structures.

## Related Questions
- How does changing the `FileHeader` struct affect serialization and deserialization?
- What are the potential impacts of modifying serialized data structures on older save files?
- How can varints be effectively used to optimize network communication in Cubyz?
- Why is it important to consider network bandwidth when designing serialization formats?
- What are the benefits of adding universal serialization functions for common types like vectors?
- How does the use of varints impact memory usage in small structures?

*Source: unknown | chunk_id: github_pr_1141_comment_1992122237*
