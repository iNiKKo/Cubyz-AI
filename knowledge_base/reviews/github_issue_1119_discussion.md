# [issues/issue_1119.md] - Issue #1119 discussion

**Type:** review
**Keywords:** modifiers, tool creation, diminishing returns, rune idea, socketing system, procedural crafting
**Concepts:** gameplay mechanics, modifier system, crafting optimization

## Summary
The discussion revolves around how to handle multiple modifiers of the same type on tools in Cubyz. The maintainers suggest a diminishing returns system based on the location of the modifier within the tool's crafting grid.

## Explanation
The discussion revolves around how to handle multiple modifiers of the same type on tools in Cubyz. The maintainers suggest a diminishing returns system based on the location of the modifier within the tool's crafting grid, where subsequent instances of the same material will increase the modifier by a tiny amount. This encourages strategic placement of modifiers rather than stacking duplicates. For example, the 'good at' modifier can be 100% effective in the tip spot, while the 'long' modifier is most effective on the handle and less so elsewhere. The maintainers also considered an idea similar to runes from Wither 3, where specific effects could be crafted using different materials (e.g., tier 1 good at rune: stone + copper = 5% boost; tier 2: deep stone or alike + gold = 10% boost; tier 3: obsidian + diamond = 15% boost). However, this idea was ultimately dismissed in favor of maintaining the procedural crafting system's depth and simplicity. The diminishing returns approach is preferred to ensure that modifiers are small but stackable for significant effects.

## Related Questions
- What are the potential implications of allowing duplicate modifiers to stack?
- How does the diminishing returns system encourage strategic tool creation?
- Why was the rune idea ultimately dismissed in favor of other approaches?
- Can you explain how the proposed modifier location-based effectiveness works in practice?
- What are the benefits and drawbacks of using a socketing system like Diablo II's?
- How might the procedural crafting system be enhanced beyond simple modifier stacking?

*Source: unknown | chunk_id: github_issue_1119_discussion*
