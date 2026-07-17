# [src/network.zig] - PR #943 review diff

**Type:** review
**Keywords:** player save, disconnection, race condition, update thread, inventory access, deinitialization
**Symbols:** Protocols, Connection, user, main.server.world.savePlayer
**Concepts:** thread safety, data consistency

## Summary
Moved player save logic from connection receive to user deinitialization.

## Explanation
The reviewer identified a critical architectural issue where saving a player during disconnection could lead to race conditions. The update thread might still be accessing the player's inventory while the disconnect is being processed, potentially causing data corruption or inconsistencies. By moving the save logic to the user's deinitialization function, the system ensures that all updates are completed before the player data is saved, thus preventing potential concurrency issues and ensuring data integrity.

## Related Questions
- What is the purpose of moving player save logic to user deinitialization?
- How does this change prevent race conditions between the update thread and disconnection?
- Can you explain the potential consequences if the player save logic remains in the connection receive function?
- What other architectural considerations should be taken into account when handling player data during disconnection?
- How does this change impact the overall performance of the network module?
- Are there any backward compatibility concerns with this refactoring?

*Source: unknown | chunk_id: github_pr_943_comment_1920670309*
