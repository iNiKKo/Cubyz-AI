# [src/network.zig] - PR #943 review diff

**Type:** review
**Keywords:** player save, disconnection, update thread, concurrent access, deinit function
**Symbols:** Protocols, Connection, receive, main.server.world.savePlayer, user
**Concepts:** thread safety, race conditions, data consistency

## Summary
Moved player save logic from connection receive to user deinitialization to prevent concurrent access issues.

## Explanation
The reviewer identified a critical architectural issue where saving a player's state during a disconnection could lead to race conditions. The update thread might still be accessing the player's inventory while the disconnect is being processed, potentially causing data corruption or inconsistencies. By moving the save operation to the `user.deinit()` function, which is called after all threads have finished using the user object, the code ensures that the player's state is safely saved without concurrent access conflicts.

## Related Questions
- What is the purpose of moving the player save logic to `user.deinit()`?
- How does this change ensure thread safety during disconnection?
- Can you explain why saving the player state in `receive` could lead to race conditions?
- What are the potential consequences if the player save operation fails in `deinit`?
- Is there any impact on performance by moving the save operation to a different function?
- How does this change affect backwards compatibility with existing code?

*Source: unknown | chunk_id: github_pr_943_comment_1920670309*
