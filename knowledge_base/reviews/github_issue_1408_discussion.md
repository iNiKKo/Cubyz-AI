# [issues/issue_1408.md] - Issue #1408 discussion

**Type:** review
**Keywords:** snap, SBB, blueprint, terrain alignment, generator SBBs, block restrictions, surface overwrites, performance implications, thread safety, backwards compatibility
**Symbols:** cubyz:rare/mushroom_pole, snap, Blueprint, SBB metadata, void, child, origin, generators, birch_forest_generator.zig.zon
**Concepts:** thread safety, backwards compatibility, memory leak, performance optimization, data structure design

## Summary
The discussion revolves around implementing a 'snap' feature for SBBs (Structure Blueprint Blocks) to align them with terrain. The maintainers propose separating normal SBBs from generator SBBs, which would have restrictions on block types and allow additional features like snapping.

## Explanation
The issue discusses the implementation of a 'snap' feature for SBBs to ensure they align correctly with the terrain. The maintainers suggest creating two categories of SBBs: normal and generator. Generator SBBs would have limitations on block types, allowing only `cubyz:void`, child blocks, and origin blocks. This separation aims to clarify behavior during snapping operations, particularly when dealing with surface overwrites. The proposal also considers performance implications, noting that accessing the ceiling or floor is O(1) while finding a wall is O(n). The maintainers aim to prevent unintended block replacements and ensure consistent behavior across different structures.

## Related Questions
- What is the proposed implementation for the 'snap' feature in SBBs?
- How does the separation of normal and generator SBBs affect performance?
- What are the restrictions on block types for generator SBBs?
- How does the snapping operation handle surface overwrites?
- What are the potential issues with allowing arbitrary blocks in blueprints?
- How does the proposal address the complexity of using multiple SBBs?
- What is the performance difference between accessing ceiling/floor and finding a wall?
- How does the 'snap' feature impact existing blueprint designs?
- What are the implications of limiting snapping to up and down directions?
- How does the separation of SBB categories improve consistency in structure generation?

*Source: unknown | chunk_id: github_issue_1408_discussion*
