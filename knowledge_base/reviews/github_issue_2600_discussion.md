# [issues/issue_2600.md] - Issue #2600 discussion

**Type:** review
**Keywords:** velocity-based chunk priority, falling down, lower-end computers, terminal velocity, hyperspeed flying, chunk prioritization
**Concepts:** chunk loading, player velocity, performance optimization, multiplayer

## Summary
The issue discusses improving chunk loading priority based on player velocity to enhance performance during long falls in multiplayer sessions, particularly on lower-end computers.

## Explanation
The issue discusses improving chunk loading priority based on player velocity to enhance performance during long falls in multiplayer sessions, particularly on lower-end computers. The maintainers suggest adding the player's velocity to the chunk loading priority calculation even if it isn't terminal velocity. This would help prevent unnecessary loading of distant chunks that will never be visible and focus rendering only on necessary paths. Additionally, this optimization is intended to enhance gameplay when flying at high speeds without being too specific for falling down scenarios.

## Related Questions
- How does the current chunk loading mechanism handle player velocity?
- What changes were made to the chunk loading priority calculation?
- How does the new implementation affect performance during falls?
- Are there any potential side effects of adding velocity to chunk prioritization?
- How will this change impact multiplayer gameplay?
- Can this optimization be extended to other high-speed movements in the game?

*Source: unknown | chunk_id: github_issue_2600_discussion*
