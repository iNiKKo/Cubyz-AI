# [issues/issue_1745.md] - Issue #1745 discussion

**Type:** review
**Keywords:** chained block updates, long update chains, cycles, scheduled tasks, lag spikes, intermediate states, chunk boundaries
**Symbols:** vines, leaves, block updates, scheduled tasks
**Concepts:** thread safety, performance optimization, dependency management

## Summary
Discussion on implementing chained block updates to handle dependencies between blocks like vines and leaves. Maintainers highlight concerns about long update chains, cycles, and performance implications.

## Explanation
The issue revolves around the lack of chained block updates, which would allow for more realistic behavior in scenarios such as vine breaking or leaf decay. The maintainer points out potential problems with long update chains and cycles, where updating a block could trigger updates to its neighbors recursively. This could lead to significant performance issues, especially if the chain involves many blocks or spans across multiple chunks. The maintainer also discusses the possibility of using scheduled tasks for updates but raises concerns about intermediate states being invalid and the complexity of managing these tasks across chunk boundaries. Despite these challenges, the maintainer believes that scheduled tasks are a more viable approach to prevent large lag spikes compared to immediate updates.

## Related Questions
- What are the potential performance impacts of implementing chained block updates?
- How can long update chains be managed to prevent lag spikes?
- What are the benefits and drawbacks of using scheduled tasks for block updates?
- How does the current system handle updates that span across multiple chunks?
- What measures can be taken to ensure intermediate states during updates are valid?
- How might intentional player actions affect the performance of chained block updates?

*Source: unknown | chunk_id: github_issue_1745_discussion*
