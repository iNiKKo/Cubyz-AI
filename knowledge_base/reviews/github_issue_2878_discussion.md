# [issues/issue_2878.md] - Issue #2878 discussion

**Type:** review
**Keywords:** player.id, playerIndex, entityId, health, sync code, entityComponent protocol, refactoring, synchronization, client-side prediction
**Symbols:** player.id, playerIndex, entityId, health, sync code, entityComponent protocol
**Concepts:** refactoring, synchronization, client-side prediction

## Summary
Discussion on splitting player.id into playerIndex and entityId, and reworking health transmission using entityComponent protocol.

## Explanation
Discussion on splitting player.id into playerIndex and entityId, and reworking health transmission using entityComponent protocol. The maintainer suggests moving attributes like health to their own components but emphasizes the necessity of proper synchronization (sync code) and client-side prediction for these components. Specifically, components need to be properly synced and client-side predicted, so they will likely need to be put through the sync system in some way, at least for the player's own components.

## Related Questions
- How does the separation of player index and entity ID impact existing gameplay mechanics?
- What are the potential performance implications of moving health to its own component?
- How will the sync system be modified to accommodate new components like health?
- Are there any backward compatibility concerns with this change?
- What is the expected behavior for client-side prediction when using the entityComponent protocol?
- How will this refactoring affect multiplayer interactions and latency?
- Is there a risk of introducing bugs due to changes in how health is transmitted?
- What are the architectural considerations for ensuring thread safety during these changes?
- How will unit tests be updated to reflect the new component-based architecture?
- Are there any memory management concerns with the introduction of new components?

*Source: unknown | chunk_id: github_issue_2878_discussion*
