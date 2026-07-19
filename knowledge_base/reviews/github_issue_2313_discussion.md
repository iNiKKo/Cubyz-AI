# [issues/issue_2313.md] - Issue #2313 discussion

**Type:** review
**Keywords:** block updates, player reach, vertex distance, ray casting, server-side physics
**Concepts:** client-server architecture, reach validation

## Summary
The issue discusses rejecting block updates that are too far away from the player, with a focus on defining the distance threshold.

## Explanation
The issue discusses rejecting block updates that are too far away from the player to prevent clients from modifying blocks outside their expected reach. The user suggests considering the closest vertex of the block rather than just its center, while the maintainer proposes setting a simpler threshold at `hand_reach + 1` and ignoring further distances unless full ray casting is implemented on the server side. This approach ensures that clients cannot modify blocks beyond this distance without additional validation.

## Related Questions
- What is the current implementation of block update validation?
- How does the client determine the reach of a player?
- Can the server-side ray casting be implemented in the near future?
- What are the potential security implications of allowing clients to modify distant blocks?
- How will this change affect multiplayer gameplay experience?
- Is there a plan to implement full server-side physics validation?

*Source: unknown | chunk_id: github_issue_2313_discussion*
