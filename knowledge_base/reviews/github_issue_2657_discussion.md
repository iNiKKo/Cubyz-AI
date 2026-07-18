# [issues/issue_2657.md] - Issue #2657 discussion

**Type:** review
**Keywords:** ore distribution, granular, depths, vein size, density, world generation, block properties, code clarity, minHeight, height
**Symbols:** .oreDepths, .veins, .size, .height, .minHeight, .density
**Concepts:** Ore Generation, Block Properties, World Generation, Code Clarity

## Summary
Proposes allowing multiple ore entries per block with varying depths, sizes, densities, and vein counts. Discusses renaming height-related fields for clarity.

## Explanation
The proposal aims to enhance the granularity of ore distribution by allowing each block to have multiple `.ore` entries, each specifying different parameters like density, size, number of veins, and depth ranges. This would enable more complex and realistic ore generation patterns. The discussion also touches on renaming the `.height` and `.minHeight` fields to `.minZ` and `.maxZ` to clarify their purpose, as they currently refer to vertical positions in the world.

## Related Questions
- How does the proposed ore distribution affect performance in world generation?
- What are the potential implications of allowing multiple ore entries per block on existing game mechanics?
- Can you provide a detailed explanation of how the `.oreDepths` array is processed during world generation?
- Why was it decided to rename `.height` and `.minHeight` to `.minZ` and `.maxZ`? What are the benefits?
- How does this change impact backwards compatibility with existing `.zon` files?
- What additional considerations should be taken into account when implementing this feature?

*Source: unknown | chunk_id: github_issue_2657_discussion*
