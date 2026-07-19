# [issues/issue_2142.md] - Issue #2142 discussion

**Type:** review
**Keywords:** oxygen bar, drowning penalties, health drain, player frustration, game balance
**Concepts:** game design, player control, drowning mechanics

## Summary
The proposal introduces an alternative drowning system for Cubyz where the player's oxygen bar depletes and triggers various penalties as it reaches zero. The maintainer suggests a different approach involving health drain instead of debuffs, emphasizing game fairness and player control.

## Explanation
The issue proposes modifying the existing drowning mechanics in Cubyz by introducing an oxygen bar that depletes over time when underwater. When the oxygen bar hits zero, it transitions into a 'drowning' state with increasing penalties as the drowning progresses. The specific penalties are as follows:

- **25% Drowning:** Swimming speed is halved; attack speed and damage are halved; block placement distance is halved; mining speed is reduced to 1/4; a blinding or vision reduction effect is applied.

- **50% Drowning:** Swimming speed is reduced to 1/4; the player cannot place or mine blocks; the blinding effect is buffed; weakness is applied.

- **75% Drowning:** The player sinks and cannot swim up anymore; the player cannot attack; weakness is buffed.

- **100% Drowning:** The player drowns and dies instantly.

The maintainer raises concerns about player frustration and control issues associated with debuffing players during drowning. Instead, the maintainer suggests draining health gradually while drowning, which would prevent players from regenerating health faster than they can take damage. This approach aims to maintain game balance and fairness by ensuring that players cannot exploit the system. The maintainer also mentions that Don't Starve's health drain approach could be a good reference for this mechanic.

## Related Questions
- What are the proposed penalties for different levels of drowning in Cubyz?
- Why does the maintainer suggest draining health instead of debuffing players during drowning?
- How does the current drowning system in Cubyz differ from the proposed alternative?
- What concerns does the maintainer have about player control and frustration in the proposed drowning mechanics?
- How would the new health-draining approach prevent players from exploiting the system?
- What is the reasoning behind maintaining game balance and fairness in the proposed drowning mechanics?

*Source: unknown | chunk_id: github_issue_2142_discussion*
