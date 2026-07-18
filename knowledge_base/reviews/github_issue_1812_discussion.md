# [issues/issue_1812.md] - Issue #1812 discussion

**Type:** review
**Keywords:** account name, in-game name, player name change, inventory preservation, private key, UUID, GUID
**Concepts:** account management, user experience, security

## Summary
Discussion on decoupling account names from in-game names to allow for player name changes without losing inventory.

## Explanation
The discussion revolves around the idea of separating the account name used for authentication and identification from the in-game display name. This separation would enable players to change their in-game names freely without affecting their game progress or inventory. The user also raises a question about whether the account name should be a string or if it could be represented by more secure identifiers like private keys, UUIDs, or GUIDs.

## Related Questions
- What are the potential security implications of using private keys or UUIDs for account names?
- How can we ensure that decoupling account and in-game names does not introduce new bugs or vulnerabilities?
- What steps should be taken to maintain backwards compatibility with existing player accounts?
- How will the change impact user experience, particularly for players who are accustomed to using their account name as their in-game identity?
- What is the expected performance impact of implementing this feature on the server and client sides?
- How can we prevent regressions related to account management after making changes to the name handling system?

*Source: unknown | chunk_id: github_issue_1812_discussion*
