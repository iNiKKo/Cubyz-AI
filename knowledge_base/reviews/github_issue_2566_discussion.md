# [issues/issue_2566.md] - Issue #2566 discussion

**Type:** review
**Keywords:** player whitelist, public key display, first login handling, confusion avoidance, algorithmic issues
**Concepts:** whitelist, public key, first login

## Summary
Discussion about implementing a player whitelist feature in Cubyz, focusing on how to display and handle public keys during the first login.

## Explanation
Discussion about implementing a player whitelist feature in Cubyz, focusing on how to display and handle public keys during the first login. The maintainer suggests displaying only one key as text during the first login to avoid confusion. This approach is deemed acceptable because any incorrect key used during this initial login can be corrected later, minimizing the impact of potential algorithmic issues. Additionally, it requires a window to get the player's public key.

## Related Questions
- How does Cubyz currently handle player authentication?
- What are the potential security implications of displaying multiple public keys during the first login?
- Can the whitelist feature be extended to support more complex key management strategies?
- How will the server determine if a different key should be used after the initial login?
- Are there any plans to implement a user interface for managing the whitelist in future releases?
- What measures are in place to ensure the integrity of public keys during transmission and storage?

*Source: unknown | chunk_id: github_issue_2566_discussion*
