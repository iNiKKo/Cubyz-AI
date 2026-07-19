# [issues/issue_2810.md] - Issue #2810 discussion

**Type:** review
**Keywords:** ornate blocks, crafting, textures, colors, procedural, chiseling, palette swapping, design patterns, inventory bloat, unique textures
**Symbols:** cubyz:ornate, cubyz:ore, ornate_colors, ornate workbench
**Concepts:** palette swapping, procedural generation, block crafting, inventory management

## Summary
The discussion revolves around implementing ornate blocks in Cubyz, focusing on how to handle unique textures and colors of source blocks. The proposal includes a static color table for each block type and suggests procedural generation as an extension.

## Explanation
Ornate blocks would be crafted using a dedicated ornate workbench that contains N predefined block patterns player can select from. Each full block used in crafting has an associated static color table (`ornate_colors`) for coloring the resulting ornate block. The resulting ornate block has a fixed orientation and uses a rotation mode similar to `cubyz:ore`. Players can craft ornate blocks using one input slot filled with any full block, and colors of the resulting ornate block depend on the materials used.

Unique textures of different stone types could be handled through palette swapping or chiseling options. The discussion highlights limitations due to unique textures of different stone types and potential inventory bloat from procedural variants. Maintainers suggest chiseling options or palette-swapping base textures as alternatives. Users propose design patterns that can be applied to any block but support a simpler implementation with fixed patterns rather than full procedural generation, which would involve crafting ornate blocks out of 8 arbitrary blocks and generating the texture on the fly based on the source blocks' `ornate_colors` table.

The number of predefined block patterns (N) in the ornate workbench is not specified. Palette swapping base textures involves creating a single 'smooth' variant for each stone type that represents its base texture after being 'worked,' and then having designs as overlays on that texture that only contain highlight/shadow lines, which would be palette swapped depending on the block. Chiseling options could involve a menu or in-world interaction to chisel different variants of blocks.

Additionally, ornate blocks would require a dedicated item type that remembers the type of source block used since normal items do not have data information fields. The procedural extension would have a significant performance impact due to the large amount of data stored and would require ornate blocks to be block entities instead of using 16 data bits.

## Related Questions
- How many predefined block patterns are available in the ornate workbench?

*Source: unknown | chunk_id: github_issue_2810_discussion*
