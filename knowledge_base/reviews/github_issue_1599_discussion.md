# [issues/issue_1599.md] - Issue #1599 discussion

**Type:** review
**Keywords:** bloom filter, search time, tags, dataset size, code complexity, SIMD, performance improvement
**Concepts:** bloom filter, SIMD operations

## Summary
The maintainer decided against using a bloom filter for searching tags due to the small dataset size and potential increase in code complexity.

## Explanation
The maintainer evaluated the use of a bloom filter for improving search time when checking if a block or item has a specific tag. They concluded that it is not worth implementing because the current dataset of tags is small (only 1 or 2 integers). The maintainer also noted that using SIMD operations could achieve similar performance improvements with less complexity by properly aligning and over-allocating the buffer.

## Related Questions
- What is the current size of the tag dataset in Cubyz?
- How does the maintainer suggest improving search performance for tags?
- Why did the maintainer decide against using a bloom filter?
- Can SIMD operations be used to improve tag search performance in Cubyz?
- What are the potential benefits and drawbacks of using a bloom filter in this context?
- How would over-allocating the buffer help with SIMD operations?

*Source: unknown | chunk_id: github_issue_1599_discussion*
