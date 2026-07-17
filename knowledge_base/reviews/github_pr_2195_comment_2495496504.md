# [src/server/terrain/structure_building_blocks.zig] - Chunk 2495496504

**Type:** review
**Keywords:** structureList, resize, stage1Count, postResolutionChecks, ZonHashMap, childrenToResolve, refactor, capacity, memory, allocation
**Symbols:** StructureBuildingBlock, registerSBB, structureList, Assets.ZonHashMap, childrenToResolve, stage1Count
**Concepts:** staged memory allocation, capacity management, refactor motivation, architectural clarity, debug naming conventions

## Summary
Refactor of StructureBuildingBlock.registerSBB to introduce a staged resizing approach for structureList and add stage1Count tracking, with reviewer noting the original name was misleading due to experimental multi-stage sizing.

## Explanation
The change replaces an immediate full resize of structureList with a two-phase strategy: first allocate enough space (stage1) then later filter via postResolutionChecks. The reviewer identified that the initial stage allocation was the root cause of memory inefficiency, and the filtering step turned out unnecessary for fixing it. Consequently, the code now tracks stage1Count to make the staged behavior explicit, allowing future renaming to reflect the true intent rather than the experimental placeholder name.

## Related Questions
- What is the purpose of stage1Count in registerSBB?
- How does the staged resize differ from a single large allocation?
- Why was postResolutionChecks considered unnecessary for this fix?
- What memory inefficiency did the initial stage cause?
- Is structureList now guaranteed to be fully sized after registration?
- Could childrenToResolve affect the staging logic?
- How does ensuring total capacity interact with the staged approach?
- What would happen if main.worldArena runs out during stage1?
- Does this change impact any other parts of the terrain module?
- Is there a risk of double-counting structures with the new stages?

*Source: unknown | chunk_id: github_pr_2195_comment_2495496504*
