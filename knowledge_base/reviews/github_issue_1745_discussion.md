# [issues/issue_1745.md] - Issue #1745 discussion

**Type:** review
**Keywords:** chained block updates, long update chains, cycles, scheduled tasks, lag spikes, intermediate states, chunk boundaries
**Symbols:** vines, leaves, block updates, scheduled tasks
**Concepts:** thread safety, performance optimization, dependency management

## Summary
Discussion on implementing chained block updates to handle dependencies between blocks like vines and leaves. Maintainers highlight concerns about long update chains, cycles, and performance implications.

## Explanation
The discussion centers on implementing chained block updates to handle dependencies between blocks like vines and leaves, which currently do not break completely if their supporting blocks are removed. The maintainer highlights several potential issues: long update chains (e.g., a vine chain can easily have up to 100 blocks), cycles, and performance implications due to the need for multiple chunk updates. For example, updating one block could trigger updates in its neighbors, leading to informing another ~402 blocks if no optimizations are applied. The maintainer suggests using scheduled tasks as an approach but notes that intermediate states may not be valid (e.g., a fence or branch doesn't have a side face when extended). Additionally, the system currently discards block updates outside of loaded chunks. Despite these challenges, the maintainer believes that scheduled tasks offer a more viable solution to prevent large lag spikes compared to immediate updates. The issue is tracked in #2486.

## Related Questions
- What are the potential performance impacts of implementing chained block updates?
- How can long update chains be managed to prevent lag spikes?
- What are the benefits and drawbacks of using scheduled tasks for block updates?
- How does the current system handle updates that span across multiple chunks?
- What measures can be taken to ensure intermediate states during updates are valid?
- How might intentional player actions affect the performance of chained block updates?

*Source: unknown | chunk_id: github_issue_1745_discussion*
