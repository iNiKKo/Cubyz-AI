# [src/server/storage.zig] - PR #2350 review diff

**Type:** review
**Keywords:** BlockIndex, BlockPos, BlockLoc, u16, fromIndex, toIndex, global block position, data reading, architectural review
**Symbols:** ChunkCompression, reader, compressionAlgo, ch, index, pos, dataLength, blockEntityData, block, chunk.BlockIndex
**Concepts:** type safety, code clarity, variable naming

## Summary
The code changes the type of `index` from `u16` to a custom `chunk.BlockIndex` struct, which includes a conversion method `.fromIndex()`. The reviewer suggests renaming `BlockIndex` to better reflect its role as a position or location.

## Explanation
**Explanation**
The code changes involve modifying the data reading process in the `ChunkCompression` struct. Previously, `index` was directly read as a `u16`, but now it is converted using `.fromIndex()` method of the `chunk.BlockIndex` struct. The reviewer points out that the term `BlockIndex` might be misleading because it does not clearly indicate its role as a position or location in the block data structure. This could lead to confusion about the nature of the variable and its usage within the codebase.

**Specific Changes:**
- **Type Change:** The type of `index` is changed from `u16` to `chunk.BlockIndex`, which includes a conversion method `.fromIndex()`.
- **Conversion Method:** When reading the index, it is now read as a `u15` and then converted to `chunk.BlockIndex` using `.fromIndex(try reader.readInt(u15))`.
- **Data Retrieval:** The block data is retrieved using `ch.data.getValue(index.toIndex())`, where `index` is of type `chunk.BlockIndex`.

**Architectural Review:**
The reviewer suggests renaming `BlockIndex` to better reflect its role as a position or location, such as `BlockPos(ition)` or `BlockLoc(ation)`. This change aims to improve code clarity and reduce confusion about the variable's purpose within the block data structure.

**Potential Implications:**
- **Code Clarity:** Renaming `BlockIndex` could enhance code readability and maintainability by making it clear that the variable represents a position or location.
- **Type Safety:** Using a custom struct for block indices instead of primitive types can provide additional type safety and prevent misuse of the index values.
- **Backward Compatibility:** The change might introduce backward compatibility issues if other parts of the codebase rely on `index` being of type `u16`. Careful consideration should be given to ensure that all related code is updated accordingly.

## Related Questions
- What is the purpose of the `fromIndex()` method in the `chunk.BlockIndex` struct?
- How does changing `index` to `chunk.BlockIndex` affect the performance of data reading?
- Why did the reviewer suggest renaming `BlockIndex` to `BlockPos` or `BlockLoc`?
- What are the potential implications of using a custom struct for block indices instead of primitive types?
- Does this change introduce any backward compatibility issues with existing code?
- How does this modification impact thread safety in the data reading process?

*Source: unknown | chunk_id: github_pr_2350_comment_2563450825*
