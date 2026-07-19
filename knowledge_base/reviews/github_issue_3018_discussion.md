# [issues/issue_3018.md] - Issue #3018 discussion

**Type:** review
**Keywords:** inventory, workbench, player, leaving world, rejoining, ECS, persistent storage, synchronization, memory usage, UI clarity
**Symbols:** onLastCloseCallback, userlist, userdeinitList, ECS
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
The issue involves inventory items disappearing when a user leaves and rejoins the world due to the `onLastCloseCallback` being called after the user is moved to `userdeinitList`. The discussion explores potential solutions using the Entity Component System (ECS) or persistent storage, with considerations for synchronization, memory usage, and UI clarity.

## Explanation
The issue involves inventory items disappearing when a user leaves and rejoins the world due to the `onLastCloseCallback` being called after the user is moved to `userdeinitList`. The problem arises because, upon leaving the server, the user gets removed from the `userlist` and added to the `userdeinitList`, causing their inventory to close. When `onLastCloseCallback` is triggered for a workbench, it searches for the user in the `userlist` but fails to find them since they are now in `userdeinitList`. As a result, no action is taken and items disappear from the workbench when the player rejoins.

The discussion explores potential solutions using the Entity Component System (ECS) or persistent storage. The ECS approach involves storing workbench inventories as components with players, ensuring that upon rejoining, items are reloaded without loss. This method avoids item loss when a player leaves due to insufficient inventory space. An alternative route is making workbenches entities with permanent storage for their items, which would unload the entity if necessary but introduces synchronization challenges and less optimal memory usage.

The team also considers adding a 'dumpster slot' using the bag mechanic where all items are dumped if the player lacks inventory space when swapping item templates. Another idea is to modify the UI so that disabled slots only allow taking out items, preventing sudden item relocation during template swaps. However, this approach may make the interface less clear and require manual cleanup.

The ECS solution aims for consistent UI behavior by saving currently open templates and making workbench UI feel less fragile and temporary.

## Related Questions
- What are the exact steps to reproduce the issue of inventory items disappearing when a user leaves and rejoins?
- How does `onLastCloseCallback` behave in this scenario, specifically regarding its search for the user in `userlist`?
- What synchronization challenges arise with making workbenches entities with persistent storage?
- Why was the 'dumpster slot' or UI modification considered as solutions to handle item transitions more gracefully?

*Source: unknown | chunk_id: github_issue_3018_discussion*
