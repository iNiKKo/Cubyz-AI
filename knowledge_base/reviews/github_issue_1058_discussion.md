# [issues/issue_1058.md] - Issue #1058 discussion

**Type:** review
**Keywords:** Droptype=side, spawn location, surface triangles, un-stucking, random direction
**Concepts:** item drop behavior, block interaction, stuck detection

## Summary
Discussion about the behavior of dropped ores spawning inside blocks and potential solutions.

## Explanation
The discussion revolves around the issue where dropped ores are spawning inside the block instead of outside. The maintainers suggest adding an option to control the drop location, such as 'Droptype=side' to spawn items on the side mined. They also mention that the current implementation does not correctly detect when the item is stuck because it only checks surface triangles. There's a concern about the randomness of direction if the item automatically pops out and whether this behavior should be relied upon for block drops.

## Related Questions
- How does the current implementation detect if an item is stuck inside a block?
- What are the potential issues with relying on automatic un-stucking for block drops?
- Can you explain how the 'Droptype=side' option would work in practice?
- Why is it important to correctly figure out when an item is stuck inside a block?
- How does the current implementation handle the direction of dropped items if they are unstuck?
- What changes need to be made to ensure that dropped ores spawn outside the block?

*Source: unknown | chunk_id: github_issue_1058_discussion*
