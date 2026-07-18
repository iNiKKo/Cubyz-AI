# [issues/issue_803.md] - Issue #803 discussion

**Type:** review
**Keywords:** block breaking, damage per hit, mesh updates, random tick regeneration, player health, server sync, Terraria
**Concepts:** block breaking mechanics, durability tracking, server synchronization

## Summary
The discussion revolves around improving block breaking mechanics, focusing on durability tracking per hit and potential server synchronization.

## Explanation
The discussion revolves around improving block breaking mechanics by focusing on durability tracking per hit rather than per block. This change aims to discourage excessive tool usage and potentially sync with the server for collaborative block mining. The maintainer initially expressed concerns about increased mesh updates due to random tick regeneration but later suggested storing health data per player, which could be synced with the server. Block breaking is accomplished via auto-swing rather than block progress, allowing tracking of durability per hit instead of per-block broken. This method prevents resetting block health when switching tools and discourages hitting blocks that are too hard for the tool. The discussion also references Terraria's approach of tracking the last few blocks mined by each player. Block damage depends on several factors including the block's health, hardness, the tool's power, and type.

## Related Questions
- How does the current block-breaking system track damage?
- What are the potential benefits of tracking durability per hit?
- What concerns were raised about server synchronization in this discussion?
- How might storing health data per player improve the game experience?
- What factors determine the amount of damage dealt to a block?
- How could random tick regeneration affect mesh updates on the client?

*Source: unknown | chunk_id: github_issue_803_discussion*
