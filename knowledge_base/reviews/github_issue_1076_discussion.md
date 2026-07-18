# [issues/issue_1076.md] - Issue #1076 discussion

**Type:** review
**Keywords:** Iron Ore, allowOres, break blocks, hand interaction, replacement issue
**Concepts:** game mechanics, block configuration, player interaction

## Summary
Discussion about an issue where iron ore cannot be placed back into blocks that naturally occur it, affecting any block with '.allowOres = true'. The root cause is identified as the inability to break these blocks with a hand.

## Explanation
Discussion around an issue where players are unable to replace iron ore in blocks that originally contained it, affecting any block configured with '.allowOres = true'. The core problem is identified as the inability to break these blocks using a player's hand. This condition affects all blocks with the attribute '.allowOres = true', not just regular stone. The maintainer comments confirm that breaking such blocks with hands is restricted.

## Related Questions
- What is the exact configuration (.allowOres) that determines which blocks allow ore replacement?
- How does the game mechanics prevent block breaking with a player's hand for these specific blocks?

*Source: unknown | chunk_id: github_issue_1076_discussion*
