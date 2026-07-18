# [issues/issue_354.md] - Issue #354 discussion

**Type:** review
**Keywords:** fence state, save loading, orientation calculation, server-client communication, chunk reloading
**Concepts:** synchronization, client-server architecture

## Summary
The issue involves fences losing their state when loaded from a save due to improper synchronization between the client and server.

## Explanation
The problem stems from the fact that the fence's orientation is not being sent to the server when it is placed. This results in the server not having the complete information about the fence, leading to incorrect state restoration when the chunk is reloaded. The maintainer suggests that the actual issue is on the server side where the fence state should be calculated and stored properly.

## Related Questions
- What is the current mechanism for sending fence placement information from the client to the server?
- How does the server currently handle the state of fences when a chunk is saved and then reloaded?
- Is there any existing code that attempts to calculate or store the orientation of fences on the server side?
- What changes are needed to ensure that the server receives all necessary information about a fence when it is placed?
- How can we verify that the fix for this issue does not introduce new synchronization problems between the client and server?
- Are there any other objects or entities in Cubyz that might suffer from similar state loss issues due to improper synchronization?

*Source: unknown | chunk_id: github_issue_354_discussion*
