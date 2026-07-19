# [issues/issue_1821.md] - Issue #1821 discussion

**Type:** review
**Keywords:** block data, 48 bits, ores, moss, stacking issues, atomic operations, lock-free access, overlay mode, performance
**Concepts:** block data extension, atomic operations, lock-free access, performance

## Summary
Discussion on extending block data to support multiple ores and decorative elements like moss on walls. Maintainers express concerns about stacking issues and performance implications.

## Explanation
The discussion revolves around extending block data from 16 bits to 48 bits to support multiple ores and decorative elements like moss on walls. Specifically, block data needs to be extended to allow for 3 ores on a full block, or 2 ores on a block with data of its own, or one ore with 16 bits of custom data (potentially for fluids). The primary concern is stacking issues where different materials could interfere with each other's placement or structural integrity, such as the coal + pebbles combo causing leftover damage and risking block breakage. Maintainers also highlight performance considerations, noting that atomic operations are crucial for fast lock-free access and that increasing the bit limit to 64 bits allows for this functionality without architectural changes. There is a suggestion to introduce an 'overlay' rotation mode for moss to avoid stacking conflicts with ores like diamond or pebbles. The overall goal is to enhance block customization while maintaining performance and avoiding architectural changes.

## Related Questions
- What are the potential performance implications of extending block data to 48 bits?
- How does increasing block data size affect atomic operations and lock-free access?
- What is the proposed solution for placing moss on ore blocks without stacking conflicts?
- Why is there a preference for maintaining limits in block data size despite its limitations?
- Can you explain the concept of an 'overlay' rotation mode for decorative elements like moss?
- How does the current block storage system handle atomic operations, and why is this important?
- What are the specific concerns regarding griefing in the context of stacking different materials?

*Source: unknown | chunk_id: github_issue_1821_discussion*
