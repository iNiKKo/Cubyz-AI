# [issues/issue_1408.md] - Issue #1408 discussion

**Type:** review
**Keywords:** snap, SBB, blueprint, terrain alignment, generator SBBs, block restrictions, surface overwrites, performance implications, thread safety, backwards compatibility
**Symbols:** cubyz:rare/mushroom_pole, snap, Blueprint, SBB metadata, void, child, origin, generators, birch_forest_generator.zig.zon
**Concepts:** thread safety, backwards compatibility, memory leak, performance optimization, data structure design

## Summary
The discussion revolves around implementing a 'snap' feature for SBBs (Structure Blueprint Blocks) to align them with terrain. The maintainers propose separating normal SBBs from generator SBBs, which would have restrictions on block types and allow additional features like snapping.

## Explanation
The discussion revolves around implementing a 'snap' feature for SBBs (Structure Blueprint Blocks) to align them with terrain. The maintainers propose creating two categories of SBBs: normal and generator. Generator SBBs would have limitations on block types, allowing only `cubyz:void`, child blocks, and origin blocks. This separation aims to clarify behavior during snapping operations, particularly when dealing with surface overwrites. For example, if a blueprint contains gray (stone) pixels that overwrite the terrain surface, the child block will snap to the old surface pre-blueprint-pasting (Option A). The proposal also considers performance implications: accessing the ceiling or floor is O(1), while finding a wall is O(n). This separation prevents unintended block replacements and ensures consistent behavior across different structures. Additionally, the maintainers aim to restrict snapping operations to up and down directions due to higher computational costs for other orientations.

## Related Questions
- What are the specific block types allowed in generator SBBs?
- How does the performance differ between accessing ceiling/floor vs. finding a wall?

*Source: unknown | chunk_id: github_issue_1408_discussion*
