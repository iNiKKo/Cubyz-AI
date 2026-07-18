# [issues/issue_1030.md] - Issue #1030 discussion

**Type:** review
**Keywords:** vine rotation mode, horizontal placement, separate textures, last block model, support block destruction
**Concepts:** block placement, chained block updates

## Summary
The issue discusses the placement and behavior of vines in Cubyz, focusing on their ability to be placed horizontally and the need for different textures/models at the end of a vine chain.

## Explanation
The issue discusses the placement and behavior of vines in Cubyz. The primary concern is that vines can only be placed on the underside of blocks and can only be placed downwards. Ideally, trying to place vines horizontally should result in placing them downwards, similar to dropping a spool of rope. Additionally, there's a suggestion for separate textures/models for the last block in a vine chain. The maintainer notes that making the entire vine break when the support block is destroyed is not feasible without implementing chained block updates, which could be complex.

## Related Questions
- What are the specific placement requirements for vines?
- How can the vine mechanics be modified to allow horizontal placement while adhering to current restrictions?

*Source: unknown | chunk_id: github_issue_1030_discussion*
