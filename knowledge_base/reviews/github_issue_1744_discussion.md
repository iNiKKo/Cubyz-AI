# [issues/issue_1744.md] - Issue #1744 discussion

**Type:** review
**Keywords:** inventory mutex, single thread, parallelization, checkerboard pattern, out of order execution, deadlocks, synchronization
**Symbols:** inventory mutex, update thread
**Concepts:** thread safety, deadlock prevention, parallelization

## Summary
The review discusses issues with the omnipresence of the inventory mutex and proposes moving all inventory operations to a single thread for simplicity and potential future parallelization.

## Explanation
The review discusses issues with the omnipresence of the inventory mutex and proposes moving all inventory operations to a single thread for simplicity and potential future parallelization. The primary concern with the current inventory mutex implementation is that it leaks into the update block function, posing a significant risk of causing severe deadlocks in the future. The maintainer suggests executing all inventory-related code on a single thread (the update thread) to avoid excessive locking and potential deadlocks. This approach simplifies synchronization but could complicate future parallelization efforts. Inventory operations can be executed out of order if they don't involve moving items, such as taking durability or removing items, as long as we don't care about which operations fail in case of resource shortage. For example, imagine mining 2 blocks behind each other, but (through some other event that the client couldn't know about) the pickaxe only has 1 durability left. This restriction would mean that the game is allowed to break only the further away block. Most player actions happen on a large time-scale. A non-cheating player will not insta-switch while mining blocks at sub-tick speeds. When block updates only ever read their direct neighbors (and never write), then we can parallelize block updates on a checkerboard pattern, first updating all chunks with even (x + y + z), then updating all chunks with odd (x + y + z). Writing could be achieved through events executed in future frames. So overall, we can run inventory operations in parallel, as long as we separate moving operations from non-moving operations, and execute moving operations sequentially. For now though, the first step in either case is to push things onto the update thread. It's nice to see that parallelization is possible in principle, though I still doubt we need to even go that far.

## Related Questions
- What is the primary concern with the current inventory mutex implementation?
- How does the maintainer propose to address the issue of excessive locking?
- What are the potential benefits and drawbacks of executing all inventory operations on a single thread?
- How can block updates be parallelized according to the maintainer's observations?
- Under what conditions can inventory operations be executed out of order?

*Source: unknown | chunk_id: github_issue_1744_discussion*
