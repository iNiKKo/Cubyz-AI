# [src/tool/modifiers/restrictions/conductedWith.zig] - PR #2646 review diff

**Type:** review
**Keywords:** grid size, crafting grid, offset calculations, array size, code clarity, maintainability
**Symbols:** Encased, Vec2i, NeverFailingAllocator, ModifierRestriction, Tool, ZonElement, getIndexInCheckArray, satisfied
**Concepts:** Grid Alignment, Code Consistency, Maintainability

## Summary
The reviewer suggests modifying the `Encased` struct and its associated functions to use a grid size consistent with the tool's crafting grid, reducing array size and eliminating offset calculations.

## Explanation
The current implementation uses a fixed check range of 5 for the grid, which may not align with the actual tool grid size. The reviewer recommends using `main.items.Tool.craftingGridSideLength` to define the grid size, ensuring consistency and potentially simplifying the logic by removing the need for different offsets. This change aims to improve code clarity and maintainability while avoiding potential discrepancies between the assumed grid size and the actual tool grid dimensions.

## Related Questions
- What is the purpose of the `Encased` struct in the `conductedWith.zig` file?
- How does the current implementation determine the check range for the grid?
- Why is there a suggestion to use `main.items.Tool.craftingGridSideLength` for the grid size?
- What potential issues could arise from using a fixed check range of 5?
- How does the suggested change improve code maintainability?
- Are there any performance implications associated with changing the grid size?

*Source: unknown | chunk_id: github_pr_2646_comment_2971625992*
