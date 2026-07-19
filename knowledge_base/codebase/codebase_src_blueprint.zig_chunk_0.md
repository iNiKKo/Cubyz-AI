# [hard/codebase_src_blueprint.zig] - Chunk 0

**Type:** configuration
**Keywords:** constants, types, enums, structs, compression methods, versioning
**Symbols:** blueprintVersion, voidType, BlueprintCompression
**Concepts:** blueprint management, compression, versioning

## Summary
Defines constants and types for blueprint management, including compression methods and versioning.

## Explanation
This chunk declares various constants and types used in the blueprint system of the Cubyz engine. It imports necessary modules such as `std`, `main`, `Compression`, `ZonElement`, `vec`, `Vec3i`, `Array3D`, `Block`, `NeverFailingAllocator`, `User`, `ServerChunk`, `Degrees`, `Tag`, `BinaryWriter`, `BinaryReader`, `AliasTable`, and `List`. It defines enums, structs, and type aliases related to blueprint storage, compression, and versioning. The `blueprintVersion` constant specifies the current version of blueprints as 1, while the `BlueprintCompression` enum lists supported compression methods like 'deflate'. The `voidType` variable is defined as an optional u16 with a value of null.

## Related Questions
- What is the current version of blueprints?
- Which compression method is supported by the blueprint system?
- How is the `voidType` variable defined in this chunk?
- What types are imported from the `main` module?
- What does the `BlueprintCompression` enum contain?
- Is there a struct or enum defined for storing blueprints?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_0*
