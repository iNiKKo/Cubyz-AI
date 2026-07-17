# [src/blueprint.zig] - Chunk 2051500218

**Type:** review
**Keywords:** PasteMode, pasteInGeneration, chunk generation, palette compression, memory footprint, substitutions, origin block, child block, ServerChunk, Vec3i
**Symbols:** Blueprint, PasteMode, pasteInGeneration, Vec3i, ServerChunk, blocks, width, depth, height, get, sbb.isOriginBlock, sbb.isChildBlock, SubstitutionMap, map.get
**Concepts:** chunk generation pipeline, palette compression, memory footprint, hot path optimization, block substitution, origin/child block exclusion, world coordinate mapping, mask-based replacement

## Summary
The change introduces a new `PasteMode` enum and a `pasteInGeneration` method to Blueprint, enabling block pasting during chunk generation while respecting origin/child blocks and optional substitution maps.

## Explanation
Architecturally, this addition shifts paste logic from runtime command execution into the chunk-generation pipeline. The reviewer notes that palette compression is already critical for chunks; adding a full copy of blueprint data with substitutions would inflate memory usage, potentially necessitating more aggressive palette compression anyway. By integrating pasting directly into generation, we avoid extra allocations and keep the hot path (chunk gen) fast—since it accounts for ~50% of total chunk+load time. The method iterates over the blueprint’s bounding box, maps local coordinates to world space, checks containment via `chunk.liesInChunk`, skips origin/child blocks using `sbb.isOriginBlock`/`isChildBlock`, and applies substitutions if provided. This design also opens the door for future mask-based replacements (via palette modification) without bloating the core generation loop.

## Related Questions
- What are the defined values of PasteMode and when should each be used?
- How does pasteInGeneration handle blocks that lie outside the target chunk?
- Why are origin and child blocks skipped during pasting in generation?
- Where is SubstitutionMap declared and how is it populated for blueprint data?
- Does pasteInGeneration modify the original Blueprint or create a new copy?
- How does this change interact with existing /set command pattern matching?
- What performance impact would applying substitutions at instantiation time have on memory usage?
- Is there any concurrency consideration when pasting into ServerChunk during generation?
- Could pasteInGeneration be called from other parts of the codebase besides chunk generation?
- How does this affect undo/redo semantics for world edit commands?

*Source: unknown | chunk_id: github_pr_1227_comment_2051500218*
