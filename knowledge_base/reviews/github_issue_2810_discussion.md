# [issues/issue_2810.md] - Issue #2810 discussion

**Type:** review
**Keywords:** ornate blocks, crafting, textures, colors, procedural, chiseling, palette swapping, design patterns, inventory bloat, unique textures
**Symbols:** cubyz:ornate, cubyz:ore, ornate_colors, ornate workbench
**Concepts:** palette swapping, procedural generation, block crafting, inventory management

## Summary
The discussion revolves around implementing ornate blocks in Cubyz, focusing on how to handle unique textures and colors of source blocks. The proposal includes a static color table for each block type and suggests procedural generation as an extension.

## Explanation
The discussion revolves around implementing ornate blocks in Cubyz. The proposal includes a dedicated ornate workbench with predefined block patterns that players can select from, though the exact number of these patterns is not specified. Each full block used in crafting has an associated static color table (`ornate_colors`) for coloring the resulting ornate block. The resulting ornate block has a fixed orientation and uses a rotation mode similar to `cubyz:ore`. Players can craft ornate blocks using one input slot filled with any full block, and colors of the resulting ornate block depend on the materials used. The discussion highlights limitations due to unique textures of different stone types and potential inventory bloat from procedural variants. Maintainers suggest chiseling options or palette-swapping base textures as alternatives. Users propose design patterns that can be applied to any block but support a simpler implementation with fixed patterns rather than full procedural generation, which would involve crafting ornate blocks out of 8 arbitrary blocks and generating the texture on the fly based on the source blocks' `ornate_colors` table.

## Related Questions
- How does the ornate block system handle unique textures of different stone types?
- What are the potential performance impacts of implementing procedural generation for ornate blocks?
- How can inventory bloat be mitigated when using procedural ornate blocks?
- What is the proposed method for palette swapping base textures in ornate blocks?
- Can you explain how chiseling options could be integrated into the ornate block system?
- What are the advantages and disadvantages of using fixed patterns instead of full procedural generation for ornate blocks?

*Source: unknown | chunk_id: github_issue_2810_discussion*
