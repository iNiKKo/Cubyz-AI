# [issues/issue_1821.md] - Issue #1821 discussion

**Type:** review
**Keywords:** block data, 48 bits, ores, moss, stacking issues, atomic operations, lock-free access, overlay mode, performance
**Concepts:** block data extension, atomic operations, lock-free access, performance

## Summary
Discussion on extending block data to support multiple ores and decorative elements like moss on walls. Maintainers express concerns about stacking issues and performance implications.

## Explanation
The discussion revolves around the proposal to extend block data from 16 bits to 48 bits to accommodate more complex block configurations, such as placing multiple ores or decorative elements like moss on walls. The primary concern is the potential for stacking issues, where different materials could interfere with each other's placement or structural integrity. Maintainers also highlight performance considerations, noting that atomic operations are crucial for fast lock-free access and that increasing the bit limit to 64 bits allows for this functionality. There is a suggestion to introduce an 'overlay' rotation mode for moss to avoid stacking conflicts. The overall goal is to enhance block customization while maintaining performance and avoiding architectural changes.

## Related Questions
- What are the potential performance implications of extending block data to 48 bits?
- How does increasing block data size affect atomic operations and lock-free access?
- What is the proposed solution for placing moss on ore blocks without stacking conflicts?
- Why is there a preference for maintaining limits in block data size despite its limitations?
- Can you explain the concept of an 'overlay' rotation mode for decorative elements like moss?
- How does the current block storage system handle atomic operations, and why is this important?
- What are the potential architectural changes required to support arbitrary stacking of rotation modes?
- How might the introduction of a fluid layer interact with the proposed block data extension?
- What are the specific concerns regarding griefing in the context of stacking different materials?
- How does the current system handle the breaking of blocks when multiple materials are present?

*Source: unknown | chunk_id: github_issue_1821_discussion*
