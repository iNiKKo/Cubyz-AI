# [issues/issue_794.md] - Issue #794 discussion

**Type:** review
**Keywords:** game time, biome discrepancies, time commands, synchronization issues, server-client communication
**Concepts:** network synchronization, time management, client-server communication

## Summary
Players report discrepancies in game time and biomes being sent to clients incorrectly.

## Explanation
The issue involves players experiencing different times of day within the same game session. Additionally, time commands are not functioning as expected, suggesting a potential problem with how time updates are being handled or propagated across the network. The maintainer notes that this is an odd behavior, indicating that it might be a bug introduced in recent changes or could be related to underlying synchronization issues between server and clients.

## Related Questions
- What changes were made to the time handling code recently?
- Are there any known issues with network synchronization in Cubyz?
- How are time updates currently being sent from the server to clients?
- Is there a specific version of Cubyz where this issue started occurring?
- Have there been any recent changes to the client-side rendering of time and biomes?
- What is the expected behavior for time commands in Cubyz?

*Source: unknown | chunk_id: github_issue_794_discussion*
