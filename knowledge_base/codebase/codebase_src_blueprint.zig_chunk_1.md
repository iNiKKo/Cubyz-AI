# [hard/codebase_src_blueprint.zig] - Chunk 1

**Type:** serialization
**Keywords:** binary serialization, paste mode, block updating, palette handling, version checking
**Symbols:** Blueprint, Blueprint.PasteMode, Blueprint.pasteInGeneration, _pasteInGeneration, Blueprint.PasteFlags, Blueprint.paste, load, store, makeBlueprintIdToGameIdMap
**Concepts:** blueprint loading, blueprint storing, block pasting

## Summary
The chunk implements Blueprint loading, storing, and pasting functionality.

## Explanation
This chunk defines the Blueprint struct with methods for loading from a buffer, storing to a buffer, and pasting into the world. It includes handling for different paste modes and flags. The load method deserializes blueprint data, while the store method serializes it. The pasteInGeneration method updates blocks in a ServerChunk based on the blueprint's content.

## Code Example
```zig
pub const PasteMode = enum { all, degradable };
```

## Related Questions
- What are the different paste modes available in Blueprint?
- How does the Blueprint struct handle block pasting into the world?
- What is the process for loading a blueprint from a buffer?
- How does the Blueprint store its data to a buffer?
- What version checking is performed during blueprint loading?
- What methods are used to update blocks in a ServerChunk?

*Source: unknown | chunk_id: codebase_src_blueprint.zig_chunk_1*
