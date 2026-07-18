# [issues/issue_1773.md] - Issue #1773 discussion

**Type:** review
**Keywords:** items storage, ore-locked chests, block entities, independent from block types, padlock, key item, diamond encrusted lids
**Concepts:** block entity, ore block, independence

## Summary
Discussion on allowing items to be stored inside ore-locked chests, highlighting technical challenges and alternative ideas.

## Explanation
The discussion revolves around the feasibility of storing items in chests that are locked by ores. The maintainer points out that the current implementation does not support associating block entities with ore blocks, which is necessary for this feature. They suggest making block entities independent from block types as a potential solution, but also mention alternative ideas such as using padlocks and keys or encrusted lids on chests.

## Related Questions
- What is the current limitation preventing items from being stored in ore-locked chests?
- How would making block entities independent from block types address the issue?
- Can you provide examples of alternative solutions to storing items in ore-locked chests?
- What are the potential benefits and drawbacks of allowing items to be stored in ore-locked chests?
- How could the current implementation be modified to support this feature?
- Are there any security concerns associated with allowing items to be stored in ore-locked chests?

*Source: unknown | chunk_id: github_issue_1773_discussion*
