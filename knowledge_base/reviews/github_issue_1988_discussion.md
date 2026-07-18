# [issues/issue_1988.md] - Issue #1988 discussion

**Type:** review
**Keywords:** client disconnection, headless server, peer-to-peer, unreachable address, error propagation, thread safety, logging
**Symbols:** ConnectionManager, run
**Concepts:** error handling, thread safety, logging

## Summary
Discussion about whether client disconnections should be logged as errors, especially in headless server environments.

## Explanation
The issue revolves around whether client disconnections should be logged as errors, particularly in headless server environments. The current implementation logs these events and attempts to display an error window, which is problematic for headless servers where such windows cannot be launched. Specifically, the log message 'Got error.ConnectionResetByPeer on receive' indicates that a previous message did not find a valid destination, leading to issues like 'Could not find window with id error_prompt'. The maintainer argues that this behavior is necessary in peer-to-peer systems to handle unreachable addresses, as entering an incorrect address could lead to errors. However, the user suggests differentiating between unreachable addresses and clean client disconnections by propagating errors out of `ConnectionManager.run` so that either the server or client can handle them appropriately. The discussion highlights concerns about thread safety, error handling, and the need for more nuanced logging based on context.

## Related Questions
- What is the exact log message when a client disconnects due to an unreachable address?
- How does the current implementation affect headless server environments specifically?
- Why does the maintainer consider unreachable addresses as errors in peer-to-peer systems?

*Source: unknown | chunk_id: github_issue_1988_discussion*
