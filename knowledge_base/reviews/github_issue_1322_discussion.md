# [issues/issue_1322.md] - Issue #1322 discussion

**Type:** review
**Keywords:** ConnectionResetByPeer, disconnect, delay, Windows 11, network.zig, sleep, reproduce
**Symbols:** Connection, network.zig
**Concepts:** thread safety, networking, error handling

## Summary
A delay was added in the `disconnect` function of `network.zig` to prevent a 'ConnectionResetByPeer' error on Windows 11.

## Explanation
The issue occurred when leaving a local world, causing an operating system cleanup of the network connection before the other side received the disconnect signal. The maintainer introduced a delay of 10 milliseconds in the `disconnect` function to address this problem. After implementing this change, the error was no longer reproducible.

## Related Questions
- What is the purpose of adding a delay in the disconnect function?
- How does the delay affect network connection handling on Windows 11?
- Is there any potential impact on performance due to the added sleep call?
- Can this change introduce new issues or regressions?
- Why was the delay specifically set to 10 milliseconds?
- Are there similar issues reported on other operating systems?

*Source: unknown | chunk_id: github_issue_1322_discussion*
