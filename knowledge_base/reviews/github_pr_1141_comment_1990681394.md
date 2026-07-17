# [src/blueprint.zig] - PR #1141 review diff

**Type:** review
**Keywords:** serialization, deserialization, field order, packed struct, extern struct, robustness, efficiency, data integrity, wastefulness, compression methods, varints
**Symbols:** FileHeader, BlueprintCompression, BinaryWriter, BinaryReader, BlockStorageType, BlockIdSizeType, GameIdToBlueprintIdMapType, blueprintVersion, Vec3i, User, NeverFailingAllocator, Block, ZonElement, Compression
**Concepts:** Serialization, Deserialization, Field Order, Struct Packing, Robustness, Efficiency, Data Integrity

## Summary
The review discusses adding a new field to the `FileHeader` struct in `blueprint.zig`, emphasizing the importance of proper serialization and deserialization code. It also highlights concerns about field order, robustness, and potential wastefulness.

## Explanation
The reviewer points out that adding a new field to the `FileHeader` struct requires corresponding serialization and deserialization code to ensure data integrity. They stress the critical nature of this step, noting that such mistakes can be easily caught during testing. The review also addresses the potential issue of field order not being guaranteed if the struct is not marked as packed or extern. While using structs for organization can simplify code, the reviewer argues that it may lead to wastefulness and complicate simple compression methods like varints. They suggest a balance between robustness and efficiency in handling data serialization.

## Related Questions
- What is the purpose of marking the `FileHeader` struct as packed or extern?
- How can field order issues be avoided in Zig when adding new fields to a struct?
- Why does the reviewer suggest using local variables instead of structs for serialization?
- What are the potential drawbacks of using structs for data storage in this context?
- How can simple compression methods like varints be applied with manual serialization?
- What is the recommended approach for ensuring robustness and efficiency in data handling?

*Source: unknown | chunk_id: github_pr_1141_comment_1990681394*
