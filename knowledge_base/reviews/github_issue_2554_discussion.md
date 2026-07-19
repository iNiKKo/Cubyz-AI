# [issues/issue_2554.md] - Issue #2554 discussion

**Type:** review
**Keywords:** seed phrase, logout, unlock window, input seed phrase, authentication PR
**Concepts:** user interface, authentication, logout

## Summary
The issue discusses a bug where logging out before restarting the game results in an input seed phrase window instead of an unlock window. The maintainer clarified that this behavior is intentional.

## Explanation
The issue discusses a bug where logging out before restarting the game results in an input seed phrase window instead of an unlock window. The user expected to be presented with an unlock window upon logging out, but instead, they were prompted for their seed phrase. This discrepancy was clarified by the maintainer, who stated that this behavior is intentional and aligns with the intended design of the logout functionality. Logging out should result in the user being logged out of their account rather than locked into it.

## Related Questions
- What is the intended behavior of logging out in the game?
- Why does logging out result in an input seed phrase window instead of an unlock window?
- How does the authentication process affect the logout functionality?
- Is there a way to lock the account after logging out?
- What changes were made in the authentication PR that might have caused this issue?
- How can we ensure that the user interface behaves as expected during logout?

*Source: unknown | chunk_id: github_issue_2554_discussion*
