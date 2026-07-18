# [issues/issue_1076.md] - Issue #1076 discussion

**Type:** review
**Keywords:** Iron Ore, allowOres, break blocks, hand interaction, replacement issue
**Concepts:** game mechanics, block configuration, player interaction

## Summary
Discussion about an issue where iron ore cannot be placed back into blocks that naturally occur it, affecting any block with '.allowOres = true'. The root cause is identified as the inability to break these blocks with a hand.

## Explanation
The discussion revolves around an issue where players are unable to replace iron ore in blocks that originally contained it. This problem affects any block configured with the attribute '.allowOres = true', indicating a broader scope than initially thought. The core issue is determined to be related to the game mechanics preventing the breaking of these blocks using a player's hand, which is essential for replacing the ore.

## Related Questions
- What is the condition that determines which blocks allow ore replacement?
- How does the game handle block breaking with a player's hand?
- Are there any specific configurations that prevent ore replacement?
- Is there a way to modify the game mechanics to allow ore replacement in these blocks?
- Can you provide examples of other blocks affected by this issue?
- What is the intended behavior for blocks with '.allowOres = true'?
- How does the current implementation affect player experience?
- Are there any plans to address this issue in future updates?
- Is there a workaround available for players to replace ore in these blocks?
- Can you explain the logic behind preventing block breaking with a hand?

*Source: unknown | chunk_id: github_issue_1076_discussion*
