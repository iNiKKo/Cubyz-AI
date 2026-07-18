# [issues/issue_3018.md] - Issue #3018 discussion

**Type:** review
**Keywords:** inventory, workbench, player, leaving world, rejoining, ECS, persistent storage, synchronization, memory usage, UI clarity
**Symbols:** onLastCloseCallback, userlist, userdeinitList, ECS
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The issue involves inventory items disappearing when a user leaves and rejoins the world due to the `onLastCloseCallback` being called after the user is moved to `userdeinitList`. The discussion explores potential solutions using the Entity Component System (ECS) or persistent storage, with considerations for synchronization, memory usage, and UI clarity.

## Explanation
The problem arises because when a user leaves the world, their inventory is closed, triggering `onLastCloseCallback`, which attempts to find the user in the `userlist`. Since the user is moved to `userdeinitList`, the callback fails to locate the user and does nothing. The discussion suggests using ECS to manage workbench inventories as components stored with players, ensuring items are reloaded upon rejoining without loss. Alternatively, making workbenches entities with persistent storage could solve the issue but introduces challenges like synchronization and memory efficiency. The team also considers adding a 'dumpster slot' or modifying the UI to handle item transitions more gracefully.

## Related Questions
- What is the current behavior of `onLastCloseCallback` when a user leaves and rejoins?
- How does the ECS approach solve the issue of inventory item loss?
- What are the potential drawbacks of making workbenches entities with persistent storage?
- Why was the 'dumpster slot' or UI modification considered as solutions?
- How does the proposed ECS solution handle synchronization between different tool types?
- What is the impact on memory usage when using persistent storage for workbenches?

*Source: unknown | chunk_id: github_issue_3018_discussion*
