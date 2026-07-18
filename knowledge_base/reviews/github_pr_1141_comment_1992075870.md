# [src/blueprint.zig] - PR #1141 review diff

**Type:** review
**Keywords:** packed struct, serialization, deserialization, field order, compile-time checking, wastefulness, varints, manual serialization, automated code, performance penalty
**Symbols:** blueprintVersion, GameIdToBlueprintIdMapType, BlockIdSizeType, BlockStorageType, BinaryWriter, BinaryReader, BlueprintCompression, FileHeader
**Concepts:** serialization, deserialization, packed structs, compile-time checking, performance trade-offs, maintainability

## Summary
The review discusses the use of packed structs for serialization and deserialization in Zig, focusing on potential performance trade-offs and maintainability.

## Explanation
The reviewer argues that using packed structs for serialization and deserialization can lead to more robust code with compile-time checking and a single source of truth for field order. However, the original author counters that this approach may encourage wastefulness by storing unnecessary fields and increases complexity in applying simple compression methods like varints. The review highlights examples where manual serialization could be simplified using functions for struct, vector, and array serialization.

## Related Questions
- What are the potential performance implications of using packed structs for serialization?
- How does using packed structs affect maintainability in comparison to manual serialization?
- Can varints be efficiently applied with packed structs, and if not, why?
- What are the benefits of having universal functions for struct, vector, and array serialization?
- How can the current serialization code be refactored to improve maintainability without sacrificing performance?
- Are there any specific cases where manual serialization is more efficient than using packed structs?

*Source: unknown | chunk_id: github_pr_1141_comment_1992075870*
