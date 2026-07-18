# [issues/issue_2793.md] - Issue #2793 discussion

**Type:** review
**Keywords:** ZON notation, block data, readability, verbosity, hash map, order of keys, comma-separated values
**Symbols:** cubyz:oak_fence, isConnectedNegX, isConnectedNegY, cubyz:branch/birch
**Concepts:** human-readable notation, block data representation, key stability

## Summary
Proposes adding a ZON notation for human-readable block data representation, with discussion on verbosity and key stability.

## Explanation
The proposal introduces a ZON-based notation to represent block data in a more readable format. The main concern raised is the verbosity of this notation compared to existing binary or numeric representations. For instance, the example given for a branch block using ZON notation is significantly longer than its current representation. Additionally, there are concerns about key stability and ensuring that different orders of keys resolve consistently into the same block data. The maintainer suggests considering alternative notations like comma-separated short values to address these issues.

## Related Questions
- What are the potential performance implications of using ZON notation for block data?
- How can we ensure that different orders of keys in ZON notation resolve to the same block data?
- Can you provide examples of how the proposed alternative notations (e.g., comma-separated values) would be parsed?
- What are the benefits and drawbacks of allowing arbitrary whitespace in block data definitions?
- How does the addition of ZON notation impact backwards compatibility with existing block data representations?
- What is the expected impact on parsing tasks when using ZON notation?

*Source: unknown | chunk_id: github_issue_2793_discussion*
