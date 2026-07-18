# [issues/issue_3346.md] - Issue #3346 discussion

**Type:** review
**Keywords:** simple_vegetation, ceiling placement, block generation, height configuration, bug report
**Symbols:** .id, .block, .generationMode, .chance, .height, .height_variation
**Concepts:** Block Placement, Configuration Parameters, Height Calculation

## Summary
The issue involves the placement of simple vegetation blocks on ceilings, where setting `.height = 0` places them one block below the ceiling, and setting `.height = 1` results in an excessively long placement.

## Explanation
The problem stems from the configuration of the `simple_vegetation` generation mode. The user reports that when `.height = 0`, the blocks are placed incorrectly at one block below the ceiling. Adjusting `.height = 1` does not resolve the issue and instead results in an overlong placement, indicating a potential bug in the height calculation logic for ceiling placements. The maintainer suggests experimenting with different height values to identify the correct behavior.

## Related Questions
- What is the expected behavior of `.height = 0` for ceiling placements?
- How does changing `.height` affect the placement length of simple vegetation blocks?
- Is there a known bug in the height calculation logic for ceiling placements?
- What other configuration parameters might influence block placement on ceilings?
- Are there any regression tests covering this issue to prevent future bugs?
- Can adjusting `.height_variation` help achieve the correct ceiling placement?

*Source: unknown | chunk_id: github_issue_3346_discussion*
