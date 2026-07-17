# [src/blueprint.zig] - PR #1141 review diff

**Type:** review
**Keywords:** blueprint.zig, BlueprintCompression, FileHeader, BinaryWriter, BinaryReader, BlockStorageType, allocator, externalAllocator, stackAllocator, capture, paste, store
**Symbols:** blueprintVersion, GameIdToBlueprintIdMapType, BlockIdSizeType, BlockStorageType, BinaryWriter, BinaryReader, BlueprintCompression, FileHeader, Blueprint, NeverFailingAllocator, User, Vec3i, ZonElement
**Concepts:** Data Serialization, Memory Management, Resource Capture and Restoration, Thread Safety, Backwards Compatibility

## Summary
The new `blueprint.zig` file introduces a blueprint system for capturing and pasting game blocks. It includes structures for handling file headers, block storage, and compression.

## Explanation
This code defines a blueprint system that allows users to capture a section of the game world and store it as a blueprint. The `Blueprint` struct captures blocks within a specified region and stores them in a list. The `FileHeader` struct manages metadata about the blueprint, including version, compression type, and dimensions. The review highlights naming consistency issues with allocators and suggests avoiding local aliasing of global allocators to prevent confusion.

## Related Questions
- What is the purpose of the `blueprintVersion` constant?
- How does the `FileHeader` struct handle different data types during storage and loading?
- Why is there a concern about naming consistency with allocators in this code?
- What is the role of the `NeverFailingAllocator` in the blueprint system?
- How does the `Blueprint` struct manage block storage and retrieval?
- What is the significance of the `getBlockArraySizeBytes` method in the `FileHeader` struct?
- How does the `capture` method determine the bounds of the captured region?
- What steps are taken to ensure thread safety when pasting blocks?
- How does the blueprint system handle compression and decompression of data?
- What is the impact of using `stackAllocator` locally in this context?

*Source: unknown | chunk_id: github_pr_1141_comment_1986306043*
