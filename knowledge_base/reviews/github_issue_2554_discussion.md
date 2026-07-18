# [issues/issue_2554.md] - Issue #2554 discussion

**Type:** review
**Keywords:** seed phrase, logout, unlock window, input seed phrase, authentication PR
**Concepts:** user interface, authentication, logout

## Summary
The issue discusses a bug where logging out before restarting the game results in an input seed phrase window instead of an unlock window. The maintainer clarified that this behavior is intentional.

## Explanation
The user reported a discrepancy between their expectation and the actual behavior of the logout functionality. After discussing with the maintainer, it was determined that logging out should log the user out of the account rather than lock it, which aligns with the intended design. The maintainer's comment clarified that this is working as expected.

## Related Questions
- What is the intended behavior of logging out in the game?
- Why does logging out result in an input seed phrase window instead of an unlock window?
- How does the authentication process affect the logout functionality?
- Is there a way to lock the account after logging out?
- What changes were made in the authentication PR that might have caused this issue?
- How can we ensure that the user interface behaves as expected during logout?

*Source: unknown | chunk_id: github_issue_2554_discussion*
