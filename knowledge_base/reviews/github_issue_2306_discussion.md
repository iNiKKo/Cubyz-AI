# [issues/issue_2306.md] - Issue #2306 discussion

**Type:** review
**Keywords:** leaf quality, chunk borders, inconsistency, performance, transparency
**Concepts:** chunk boundaries, leaf quality calculation, performance optimization

## Summary
The issue discusses inconsistent leaf quality calculations, particularly around chunk borders.

## Explanation
The discussion revolves around an inconsistency in how leaf quality is calculated, especially when leaves are placed at the boundary of chunks. The maintainer notes that leaf quality does not activate across chunk borders due to performance concerns related to accessing data from neighboring chunks. This leads to issues where leaves should be opaque on a certain quality level but appear transparent instead. Specifically, the inconsistency arises when leaves are placed at height 0, which is right above a chunk border. The maintainer notes that this placement causes leaf quality to not activate correctly, resulting in an opaque appearance despite being on the wrong side of the chunk border.

## Related Questions
- Why does leaf quality not activate across chunk borders?
- What is the performance impact of considering data from surrounding chunks?
- How can the inconsistency in leaf quality calculations be resolved?
- Is there a way to optimize the calculation without sacrificing accuracy?
- Can the current implementation handle leaves placed at height 0 correctly?
- Are there any plans to improve the handling of leaf quality across chunk borders?

*Source: unknown | chunk_id: github_issue_2306_discussion*
