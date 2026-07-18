# [issues/issue_1708.md] - Issue #1708 discussion

**Type:** review
**Keywords:** No sync point, world loading, timer, sync point, thread synchronization, error logging, debug mode, release mode
**Symbols:** syncPoint, entryFn
**Concepts:** thread synchronization, error handling, logging

## Summary
The issue involves a 'No sync point' error during world loading, indicating that a sync point was not executed within the expected time frame.

## Explanation
The error message suggests that a sync point, which is crucial for thread synchronization, did not occur in the specified time (18387 ms). The maintainer and user discuss potential solutions such as increasing the timer or changing the logging behavior. The maintainer considers increasing the timer to 20 seconds as a possible compromise.

## Related Questions
- What is the purpose of the 'syncPoint' function in Cubyz?
- How does increasing the timer affect the detection of missing sync points?
- Why is logging behavior different between debug and release modes?
- Can you explain the impact of thread synchronization on performance in Cubyz?
- What are the potential consequences of forgetting to add a sync point in the main loop?
- How can we ensure that all threads have proper sync points without increasing the timer indefinitely?

*Source: unknown | chunk_id: github_issue_1708_discussion*
