# [issues/issue_1517.md] - Issue #1517 discussion

**Type:** review
**Keywords:** dynamic lights, torches, exploration, performance, gameplay impact, invisible light source, grid-aligned block
**Concepts:** gameplay balance, performance optimization, lighting system

## Summary
Discussion about implementing dynamic lighting in Cubyz, with concerns over optimization and gameplay impact.

## Explanation
The discussion revolves around the idea of allowing entities, particles, and dropped items to emit light dynamically. The maintainer expresses concerns about scalability and potential negative impacts on gameplay, suggesting that it might encourage players to avoid placing torches. A user defends dynamic lighting, arguing that it can enhance exploration by providing temporary light sources without permanently altering the environment. The user also proposes a compromise involving an invisible light source tied to the player's position as a grid-aligned block, which could potentially improve performance compared to shader-based solutions.

## Related Questions
- What are the potential optimization issues with implementing dynamic lighting in Cubyz?
- How might dynamic lighting affect player behavior and gameplay balance?
- Can you explain the proposed compromise involving an invisible light source tied to the player's position?
- What are the advantages of using a grid-aligned block for temporary lighting compared to shader-based solutions?
- How could dynamic lighting be integrated without significantly impacting performance?
- Are there any potential drawbacks to allowing entities and particles to emit light dynamically?
- How might dynamic lighting impact the design of future mob behaviors in Cubyz?
- What are the trade-offs between dynamic lighting and traditional torch placement in terms of gameplay experience?
- Can you provide examples of how other games have implemented dynamic lighting systems?
- How could the current lighting system be modified to support temporary light sources without major overhauls?

*Source: unknown | chunk_id: github_issue_1517_discussion*
