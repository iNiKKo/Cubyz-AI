# [issues/issue_2810.md] - Issue #2810 discussion

**Type:** review
**Keywords:** ornate blocks, crafting, textures, colors, procedural, chiseling, palette swapping, design patterns, inventory bloat, unique textures
**Symbols:** cubyz:ornate, cubyz:ore, ornate_colors, ornate workbench
**Concepts:** palette swapping, procedural generation, block crafting, inventory management

## Summary
The discussion revolves around implementing ornate blocks in Cubyz, focusing on how to handle unique textures and colors of source blocks. The proposal includes a static color table for each block type and suggests procedural generation as an extension.

## Explanation
The issue proposes adding ornate blocks that can be crafted using a dedicated workbench with predefined patterns. Each full block used in crafting has a static color table, similar to ore blocks. The discussion highlights the limitation of this approach due to unique textures of different stone types and potential inventory bloat from procedural variants. Maintainers suggest chiseling options or palette-swapping base textures as alternatives. Users propose design patterns that can be applied to any block, suggesting a simpler implementation with fixed patterns rather than full procedural generation.

## Related Questions
- How does the ornate block system handle unique textures of different stone types?
- What are the potential performance impacts of implementing procedural generation for ornate blocks?
- How can inventory bloat be mitigated when using procedural ornate blocks?
- What is the proposed method for palette swapping base textures in ornate blocks?
- Can you explain how chiseling options could be integrated into the ornate block system?
- What are the advantages and disadvantages of using fixed patterns instead of full procedural generation for ornate blocks?

*Source: unknown | chunk_id: github_issue_2810_discussion*
