# [issues/issue_803.md] - Issue #803 discussion

**Type:** review
**Keywords:** block breaking, damage per hit, mesh updates, random tick regeneration, player health, server sync, Terraria
**Concepts:** block breaking mechanics, durability tracking, server synchronization

## Summary
The discussion revolves around improving block breaking mechanics, focusing on durability tracking per hit and potential server synchronization.

## Explanation
The issue discusses enhancing the block-breaking system to track damage per hit rather than per block. This change aims to improve player behavior by discouraging excessive tool usage and potentially syncing with the server for collaborative block mining. The maintainer initially expressed concerns about increased mesh updates due to random tick regeneration but later suggested storing health data per player, which could be synced with the server. The discussion also references Terraria's approach of tracking the last few blocks mined.

## Related Questions
- How does the current block-breaking system track damage?
- What are the potential benefits of tracking durability per hit?
- What concerns were raised about server synchronization in this discussion?
- How might storing health data per player improve the game experience?
- What is the relationship between block hardness and tool power in the breaking mechanics?
- How could random tick regeneration affect mesh updates on the client?

*Source: unknown | chunk_id: github_issue_803_discussion*
