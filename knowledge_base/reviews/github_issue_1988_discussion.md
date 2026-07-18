# [issues/issue_1988.md] - Issue #1988 discussion

**Type:** review
**Keywords:** client disconnection, headless server, peer-to-peer, unreachable address, error propagation, thread safety, logging
**Symbols:** ConnectionManager, run
**Concepts:** error handling, thread safety, logging

## Summary
Discussion about whether client disconnections should be logged as errors, especially in headless server environments.

## Explanation
The issue revolves around the logging of client disconnections as errors. The current implementation logs these events and attempts to display an error window, which is problematic for headless servers where such windows cannot be launched. The maintainer argues that this behavior is necessary for peer-to-peer systems to handle unreachable addresses. However, the user suggests differentiating between unreachable addresses and clean client disconnections, proposing to propagate errors out of `ConnectionManager.run` so that either the server or client can handle them appropriately. The discussion highlights concerns about thread safety, error handling, and the need for more nuanced logging based on context.

## Related Questions
- What is the current behavior of logging client disconnections in Cubyz?
- Why does the maintainer consider client disconnections as errors in peer-to-peer systems?
- How can the error handling be improved to differentiate between unreachable addresses and clean client disconnections?
- What are the implications of propagating errors out of `ConnectionManager.run`?
- How does the current implementation affect headless server environments?
- Are there any potential thread safety issues with the current logging mechanism?

*Source: unknown | chunk_id: github_issue_1988_discussion*
