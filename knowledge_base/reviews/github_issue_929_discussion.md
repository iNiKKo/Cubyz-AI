# [issues/issue_929.md] - Issue #929 discussion

**Type:** review
**Keywords:** grass seeds, soil blocks, dry grass, block data, connectivity
**Concepts:** block transformation, ore rotation mode

## Summary
Discussion on implementing grass seeds functionality without modifying existing code.

## Explanation
Discussion on implementing grass seed functionality without modifying existing code. The maintainer suggests that the current ore rotation mode allows for transforming soil blocks into their grassy variants by using grass seeds, but this approach may not be sufficient if more block data is needed for features like grass connectivity. Specifically, the use of grass seeds involves placing them on any soil block (dirt, soil, mud) to turn it into its grassy variant. The maintainer also notes that ore rotation mode requires all 32 bits of block data and may need additional data for proper grass connectivity.

## Related Questions
- How does the use of grass seeds transform soil blocks?
- What are the specific requirements for block data in ore rotation mode?
- Are there any limitations to using ore rotation mode for grass seed functionality?

*Source: unknown | chunk_id: github_issue_929_discussion*
