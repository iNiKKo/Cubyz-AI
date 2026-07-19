# [issues/issue_1486.md] - Issue #1486 discussion

**Type:** review
**Keywords:** redirect stdout/stderr, dummy process, log files, stack traces, contributor friendly, viable solution
**Concepts:** stdout, stderr, stack traces, logging

## Summary
Discussion about redirecting stdout/stderr or using a dummy process to store stack traces in log files.

## Explanation
Discussion about capturing stack traces in log files by redirecting stdout/stderr or using a dummy process. The maintainers suggest that while redirecting stdout/stderr could work as an interim solution (referencing #227), it may not be contributor-friendly. They emphasize finding a viable solution now rather than waiting for another large topic.

## Related Questions
- How can we redirect stdout/stderr to store stack traces in log files?
- What are the potential drawbacks of using a dummy process for this purpose?
- Are there any existing solutions or tools that can help with capturing stack traces?
- How does redirecting stdout/stderr impact performance and resource usage?
- What are the implications of not being contributor friendly when implementing this solution?
- Can we find an alternative approach to capture stack traces without modifying stdout/stderr?

*Source: unknown | chunk_id: github_issue_1486_discussion*
