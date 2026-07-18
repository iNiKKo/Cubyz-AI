# [issues/issue_2894.md] - Issue #2894 discussion

**Type:** review
**Keywords:** interface, cubyz servers, applications, mods, chat messages, serverReceive, patching
**Symbols:** Protocol, serverReceive
**Concepts:** modding, server-client interaction, patching

## Summary
Discussion about allowing applications to interface with Cubyz servers directly, focusing on potential implementation via server-side mods or patching.

## Explanation
The discussion revolves around enabling applications to interact with Cubyz servers without requiring a player to be online. The maintainer initially suggests using server-side mods but acknowledges that the official modding system cannot currently achieve this functionality. The user proposes catching chat messages just before they enter the Protocol serverReceive function as an alternative approach.

## Related Questions
- What is the current capability of server-side mods in Cubyz?
- How can applications currently interact with Cubyz servers?
- What are the potential benefits and drawbacks of implementing a direct interface for applications?
- Can patching into the serverReceive function be a viable solution?
- Are there any security concerns associated with allowing application interfaces to Cubyz servers?
- How would this feature impact backwards compatibility with existing mods?

*Source: unknown | chunk_id: github_issue_2894_discussion*
