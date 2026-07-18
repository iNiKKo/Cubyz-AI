# [issues/issue_2424.md] - Issue #2424 discussion

**Type:** review
**Keywords:** disconnection, operations, mutex, queue, reconnection, player removal, race condition prevention
**Symbols:** userMutex, disconnect, removePlayer, userDeinitList
**Concepts:** thread safety, race condition, asynchronous operations

## Summary
The issue involves operations not being stored before a player disconnects due to the player being removed prematurely.

## Explanation
The discussion revolves around handling player disconnections in a way that ensures all pending operations are completed before the player is fully removed. The initial suggestion was to remove `userMutex` and use a single mutex for both sync operations and disconnections, but this approach was found to cause asynchronous disconnection issues. Another proposal was to push user indices into a queue at the end of the update function to handle removals safely, preventing race conditions. However, this method also encountered problems, specifically preventing reconnection after disconnection.

## Related Questions
- What is the purpose of `userMutex` in the network handling code?
- How does the current disconnection process handle asynchronous operations?
- Why was removing `userMutex` not a viable solution for preventing race conditions?
- What specific issues arose when trying to push user indices into a queue for removal?
- How can reconnection be ensured after a player disconnects without causing further issues?
- Is there a way to synchronize disconnection with the completion of all pending operations?

*Source: unknown | chunk_id: github_issue_2424_discussion*
