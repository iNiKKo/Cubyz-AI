# [issues/issue_2870.md] - Issue #2870 discussion

**Type:** review
**Keywords:** multiplayer, crash, internet, ping, server, timeout, connection, offline
**Concepts:** networking, offline mode, timeout handling

## Summary
The multiplayer feature crashes the game when used without an internet connection due to excessive server ping attempts.

## Explanation
The issue arises because the network module attempts to determine the player's IP address by pinging multiple servers, each with a generous timeout. When offline, this leads to prolonged freezing and timeouts as the game waits for responses that will never come. The proposed solution is to close the connection immediately upon realizing the lack of internet connectivity, thus preventing further server ping attempts and avoiding the crash.

## Related Questions
- What is the current behavior of the network module when trying to determine the player's IP address without an internet connection?
- How does the proposed solution aim to resolve the issue of excessive server ping attempts in offline mode?
- Are there any potential side effects or regressions introduced by immediately closing the connection upon detecting no internet connectivity?
- What is the impact on performance when the network module recognizes the lack of internet and closes the connection promptly?
- How does this change affect the user experience during multiplayer sessions without an active internet connection?
- Is there a risk of data loss or corruption if the connection is closed prematurely while attempting to determine the IP address?

*Source: unknown | chunk_id: github_issue_2870_discussion*
