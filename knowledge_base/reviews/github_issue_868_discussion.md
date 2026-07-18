# [issues/issue_868.md] - Issue #868 discussion

**Type:** review
**Keywords:** item drop velocity, random direction flight, floaty movement, phasing through blocks, network latency, server tick, item appearance, center of the block, game release polishing, gliding without friction
**Concepts:** item physics, latency, network performance

## Summary
The issue discusses improving item physics in Cubyz, addressing issues like random direction flight, floaty movement, phasing through blocks, and latency between block break and item drop. The maintainer reduced latency by ~50 ms and suggests further improvements for release polishing.

## Explanation
The issue discusses improving item physics in Cubyz, addressing issues like random direction flight, floaty movement, phasing through blocks, and latency between block breakage and item appearance. The maintainer identified that items drop with a random velocity vector and can sometimes phase through blocks entirely due to high velocities. They also noted a significant delay of around 50 ms before the item appears after breaking a block, attributing this largely to network latency (2/3) and server tick updates once every tick. The maintainer reduced the overall latency by approximately 50 ms on average, noting that further improvements are needed for game release polishing. Additionally, there are ongoing issues with items gliding without friction (#83), which is blocked by another priority issue (#816).

## Related Questions
- What was the exact reduction in latency achieved?
- How much of the remaining latency is attributed to network issues?
- Why did items sometimes phase through blocks entirely?
- What specific changes were made to reduce latency?
- Is there a plan to address the issue where items don't always appear from the center of the block?
- What other priorities are blocking further improvements to item physics?

*Source: unknown | chunk_id: github_issue_868_discussion*
