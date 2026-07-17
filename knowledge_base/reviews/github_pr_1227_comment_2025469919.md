# [src/blueprint.zig] - Chunk 2025469919

**Type:** review
**Keywords:** PasteMode, pasteInGeneration, SubstitutionMap, ServerChunk, liesInChunk, blocks, width, depth, height, sbb.isOriginBlock, sbb.isChildBlock, updateBlockInGeneration
**Symbols:** Blueprint, PasteMode, pasteInGeneration, Vec3i, ServerChunk, liesInChunk, blocks, width, depth, height, get, sbb.isOriginBlock, sbb.isChildBlock, SubstitutionMap, updateBlockInGeneration
**Concepts:** performance optimization, iteration over block lists, compile‑time vs runtime dispatch, substitution mapping, chunk generation, memory locality, conditional block writing, architecture scalability

## Summary
The diff introduces a new PasteMode enum and a pasteInGeneration method to Blueprint, allowing pasting blocks into a generation chunk with optional substitution mapping; the reviewer flags iterating over block lists during generation as performance‑critical.

## Explanation
The change adds explicit mode handling (all/noAir/replaceAir) and an optional SubstitutionMap so that pasted structures can be transformed before being written. The original implementation likely iterated a list of blocks or tags to decide what to paste, which is O(N) per generation cell and becomes prohibitive for millions of cells in large worlds. By moving the iteration into a tight nested loop over the Blueprint’s own block dimensions (width/depth/height) and using direct array indexing, we avoid any external list traversal. The reviewer also notes that the runtime switch on mode could be compiled away with comptime if the set of modes is known at compile time, further reducing overhead. This refactor targets both correctness (ensuring only non‑origin/non‑child blocks are written) and performance (minimizing per‑cell work).

## Related Questions
- What are the three values of PasteMode and how does each affect block writing?
- How is SubstitutionMap used inside pasteInGeneration to transform blocks before insertion?
- Why does the code skip origin and child blocks via sbb.isOriginBlock / sbb.isChildBlock?
- What does liesInChunk guard against when iterating over Blueprint.blocks?
- If mode were known at compile time, how could we replace the runtime switch with comptime logic?
- How many nested loops are executed per call to pasteInGeneration and what determines their bounds?
- Is there any risk of double‑writing a block if both substitution and mode=all apply?
- What would be the asymptotic complexity of pasting an N×N×N structure into a generation chunk with this implementation?
- How does this change interact with existing Blueprint methods that also write blocks?
- Could we precompute world coordinates to avoid repeated Vec3i indexing overhead?

*Source: unknown | chunk_id: github_pr_1227_comment_2025469919*
