# [issues/issue_2267.md] - Issue #2267 discussion

**Type:** review
**Keywords:** foliage, replaceable, building, mining, sickle, toggle, tool interaction
**Concepts:** gameplay improvement, user experience, toggle functionality

## Summary
Discussion on making foliage replaceable by blocks the player builds, with suggestions for toggles and specific tools to ignore foliage.

## Explanation
Discussion on making foliage replaceable by blocks the player builds, with suggestions for toggles and specific tools to ignore foliage. The maintainers propose that foliage should be completely ignored when building and mining, similar to Terraria's approach. They suggest a toggle when sneaking or using specific tools like a sickle to clear foliage. Additionally, the use of a shovel is proposed to ignore foliage entirely when placing blocks behind it. This would enhance player efficiency and provide more flexibility in world-building. The block assets should be updated with `.replaceable = true` for these changes to take effect. To implement this, players can modify the block assets by adding the `.replaceable = true` command. The performance impact of the new foliage interaction is currently unknown and may require further testing.

## Related Questions
- How can we implement a toggle to ignore foliage when sneaking?
- What specific tools should be designated to clear foliage in the game?
- Can you provide an example of how to modify block assets to make them replaceable with `.replaceable = true`?
- How will the new foliage interaction affect performance in the game?
- Are there any potential regressions with the proposed changes to foliage handling?
- How can we ensure that the new toggle functionality is intuitive for players?

*Source: unknown | chunk_id: github_issue_2267_discussion*
