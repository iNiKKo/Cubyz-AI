# [issues/issue_3179.md] - Issue #3179 discussion

**Type:** review
**Keywords:** Entity component data disappears, host, crash, bag, server, components, player entity, assert, storage
**Concepts:** data loss, assertion, component storage

## Summary
A user reports that their player entity's components disappear after a crash, and suggests adding an assertion to detect future occurrences.

## Explanation
The issue revolves around data loss for player entities' components in the game. The user experienced this problem twice, once during a play session where their bag was gone after a crash, and another time where they could not interact with their bag at all. The maintainer notes that they still see the bag on the client side. The user proposes adding an assertion to help identify when components are stored without being present, aiming to prevent similar issues in the future.

## Related Questions
- What is the current state of the issue regarding entity component data disappearance?
- Has there been any previous discussion about similar issues in the past?
- Why does the maintainer still see the bag on the client side?
- How would adding an assertion help detect future occurrences of this issue?
- Are there any known causes for this type of data loss in the game?
- What steps can be taken to prevent similar issues from happening again?

*Source: unknown | chunk_id: github_issue_3179_discussion*
