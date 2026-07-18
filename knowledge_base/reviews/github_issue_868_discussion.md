# [issues/issue_868.md] - Issue #868 discussion

**Type:** review
**Keywords:** item drop velocity, random direction flight, floaty movement, phasing through blocks, network latency, server tick, item appearance, center of the block, game release polishing, gliding without friction
**Concepts:** item physics, latency, network performance

## Summary
The issue discusses improving item physics in Cubyz, addressing issues like random direction flight, floaty movement, phasing through blocks, and latency between block break and item drop. The maintainer reduced latency by ~50 ms and suggests further improvements for release polishing.

## Explanation
The discussion revolves around enhancing the physics of items that drop from blocks in Cubyz. The main issues identified include random direction flight, floaty movement, occasional phasing through blocks, and a noticeable delay between block breakage and item appearance. The maintainer addressed latency by reducing it by approximately 50 ms, attributing much of the remaining delay to network latency. Concerns about items not always appearing from the center of the block were also raised. The maintainer notes that while the current implementation is functional, further polishing is needed for game release. Additionally, there are ongoing issues with item gliding without friction and other priorities that block further improvements.

## Related Questions
- What was the average reduction in latency achieved?
- How much of the remaining latency is attributed to network issues?
- Why did items sometimes phase through blocks?
- What specific changes were made to reduce latency?
- Is there a plan to address the issue where items don't always appear from the center of the block?
- What other priorities are blocking further improvements to item physics?

*Source: unknown | chunk_id: github_issue_868_discussion*
