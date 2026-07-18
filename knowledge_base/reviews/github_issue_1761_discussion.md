# [issues/issue_1761.md] - Issue #1761 discussion

**Type:** review
**Keywords:** crash, STUN server, Windows, network.zig, send function, assertion failure, unreachable code, data.len, result, logging, sporadic failure
**Symbols:** send, sendRequest, requestAddress, makeOnline, init, discoverIpAddress, discoverIpAddressFromNewThread
**Concepts:** assertion failure, panic, logging, sporadic failure

## Summary
The game crashes when attempting to find the IP address from a STUN server on Windows. The crash occurs due to an assertion failure in the `send` function within the `network.zig` file.

## Explanation
The issue is triggered by an assertion that checks if the result of sending data matches the length of the data being sent. If this condition fails, it leads to a panic and crash. The maintainer suggests adding logging to print the actual values of `result` and `data.len` to help diagnose the problem. Additionally, they recommend attempting the operation multiple times to determine if it is a sporadic failure.

## Related Questions
- What is the expected behavior of the `send` function in `network.zig`?
- How can we modify the code to handle cases where `result` does not match `data.len`?
- Is there a known issue with STUN server communication on Windows?
- Can you provide more details on how to implement the suggested logging?
- What steps should be taken to verify if this is indeed a sporadic failure?
- How can we improve error handling in the network module to prevent similar crashes?

*Source: unknown | chunk_id: github_issue_1761_discussion*
