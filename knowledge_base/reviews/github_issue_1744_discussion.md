# [issues/issue_1744.md] - Issue #1744 discussion

**Type:** review
**Keywords:** inventory mutex, single thread, parallelization, checkerboard pattern, out of order execution, deadlocks, synchronization
**Symbols:** inventory mutex, update thread
**Concepts:** thread safety, deadlock prevention, parallelization

## Summary
The review discusses issues with the omnipresence of the inventory mutex and proposes moving all inventory operations to a single thread for simplicity and potential future parallelization.

## Explanation
The issue highlights that locking the inventory mutex during every block update is problematic, leading to potential deadlocks. The maintainer suggests executing all inventory-related code on a single thread (the update thread) to avoid excessive locking. This approach simplifies synchronization but could complicate future parallelization efforts. The maintainer also notes that inventory operations can be executed out of order if they don't involve moving items, and block updates can be parallelized using a checkerboard pattern for read-only operations. For now, the focus is on centralizing inventory operations on the update thread.

## Related Questions
- What is the primary concern with the current inventory mutex implementation?
- How does the maintainer propose to address the issue of excessive locking?
- What are the potential benefits and drawbacks of executing all inventory operations on a single thread?
- How can block updates be parallelized according to the maintainer's observations?
- Under what conditions can inventory operations be executed out of order?
- What is the proposed method for handling write operations in future frames?

*Source: unknown | chunk_id: github_issue_1744_discussion*
