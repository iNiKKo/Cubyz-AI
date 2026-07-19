# [src/blueprint.zig] - PR #1141 review diff

**Type:** review
**Keywords:** blueprint.zig, Compression, ZonElement, Vec3i, Block, NeverFailingAllocator, User, BlueprintCompression, FileHeader, BinaryWriter, BinaryReader, explicit serialization, automatic serialization, file size reduction, deflate
**Symbols:** blueprint.zig, Compression, ZonElement, Vec3i, Block, NeverFailingAllocator, User, BlueprintCompression, FileHeader, BinaryWriter, BinaryReader
**Concepts:** thread safety, backwards compatibility, memory leak, serialization, compression

## Summary
The addition of a new file `blueprint.zig` introduces a blueprint system with compression support for Cubyz. The reviewer discusses the potential benefits and drawbacks of using explicit serialization versus automatic serialization, emphasizing the importance of clarity and maintainability in code.

## Explanation
The addition of a new file `blueprint.zig` introduces a blueprint system with compression support for Cubyz. The reviewer discusses the potential benefits and drawbacks of using explicit serialization versus automatic serialization, emphasizing the importance of clarity and maintainability in code.

The `FileHeader` struct is defined as follows:

```zig
pub const FileHeader = packed struct {
    version: u16 = 0,
    compression: BlueprintCompression = .deflate,
    paletteSizeBytes: u32 = 0,
    paletteBlockCount: u16 = 0,
    blockArraySizeX: u16 = 0,
    blockArraySizeY: u16 = 0,
    blockArraySizeZ: u16 = 0,
};
```

The reviewer points out that while automatic serialization (referred to as 'magic') can simplify code, it may lead to unforeseen consequences and difficulties in debugging. In contrast, explicit serialization, though more verbose, provides better control and clarity, making it easier to spot mistakes and ensure compatibility with changes over time. The reviewer also mentions the potential for file size reduction through compression but questions its necessity given that the palette and block array are already compressed using deflate.

## Related Questions
- What is the purpose of the `blueprint.zig` file in Cubyz?
- How does the new blueprint system handle compression?
- Why does the reviewer prefer explicit serialization over automatic serialization?
- Can you explain the potential benefits and drawbacks of using deflate for compression?
- What are the implications of changing fields in `ChunkPosition` on old world files?
- How does explicit serialization improve code maintainability compared to automatic serialization?

*Source: unknown | chunk_id: github_pr_1141_comment_1996024540*
