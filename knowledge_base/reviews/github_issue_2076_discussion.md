# [issues/issue_2076.md] - Issue #2076 discussion

**Type:** review
**Keywords:** disconnection, invalid packets, network data processing, debugging info, version 0.0.1
**Concepts:** network communication, packet validation, error handling

## Summary
A player disconnects from the server due to an 'Invalid' error while processing network data during mining activities. The maintainer suggests adding more debugging information in version 0.0.1 to help identify and resolve the problem.

## Explanation
The issue arises when the game encounters invalid packets during network communication, leading to a disconnection. The player was mining at the time of the error. Here are some key details from the log file:

```
[info]: Resizing internal mesh buffer from 256 MiB to 512 MiB
...
[warning]: The server is lagging behind by 38.7 ms
[error]: Got error while processing received network data: Invalid
[info]: Chat: cuppercom§#ffff00 left
[info]: Disconnected
```
The maintainer suggests adding more debugging information in version 0.0.1 to help identify and resolve the problem. The additional debugging information should include details about the invalid packets, such as their content or origin, to better understand why they are being received.

The player was mining during this session, which may be a contributing factor. Mining activities could generate a high volume of network traffic, potentially leading to packet processing issues if not handled properly.

## Related Questions
- What is the cause of the 'Invalid' error during network data processing?
- How can we improve packet validation to prevent disconnections?
- What additional debugging information should be added in version 0.0.1?
- Are there any known issues with network communication in Cubyz?
- How does the game handle invalid packets currently?
- Can the server logs provide more insights into the issue?
- Is there a way to reproduce the disconnection consistently?
- What are the potential consequences of invalid packets on gameplay?
- How can we ensure better error handling for network issues?
- Are there any performance implications related to network data processing?

*Source: unknown | chunk_id: github_issue_2076_discussion*
