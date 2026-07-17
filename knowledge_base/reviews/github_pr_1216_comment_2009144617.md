# [src/rotation.zig] - Chunk 2009144617

**Type:** review
**Keywords:** TexturePile, rotatedModels, blockToStateCountMap, u16, virtual functions, function signatures, memory usage, compile time, deduplication, generic class, ModelIndex
**Symbols:** RotationModes, TexturePile, rotatedModels, blockToStateCountMap, ModelIndex
**Concepts:** virtual functions, function signature complexity, memory optimization, code deduplication, compile time bloat, generic instantiation, state pointer passing, architectural flexibility

## Summary
The diff introduces a new TexturePile struct with rotatedModels and blockToStateCountMap fields, but reviewers reject it due to excessive function signature complexity, lack of meaningful memory savings (u16 is already indexable), and Zig's poor code deduplication leading to compile-time bloat.

## Explanation
The architectural review highlights that passing a pointer to state in virtual functions would make signatures unwieldy. The proposed TexturePile uses u16 for blockToStateCountMap, which reviewers argue is unnecessary since u16 can already serve as an index into local lists without restrictions. Memory optimization claims are dismissed because adding this parameter to every block only saves 128 kiB, deemed not worth the cost. Additionally, making TexturePile generic would instantiate 15 copies in Zig due to its inability to deduplicate code, worsening compile times which are already problematic.

## Related Questions
- What is the purpose of TexturePile in rotation.zig?
- Why does the reviewer oppose passing a pointer to state in virtual functions?
- How much memory would be saved by adding TexturePile parameters to every block?
- What limitation of Zig causes generic classes to compile multiple instances?
- Is u16 sufficient for indexing without restrictions in this context?
- What alternative approach is suggested instead of TexturePile?
- Why is 128 kiB considered not worth optimizing here?
- How does the current RotationModes struct handle state management?
- What would happen if TexturePile were made generic with different maxStateCount values?
- Are there any existing patterns in rotation.zig that avoid pointer-heavy virtual functions?

*Source: unknown | chunk_id: github_pr_1216_comment_2009144617*
