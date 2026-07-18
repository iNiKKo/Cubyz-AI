# [issues/issue_1217.md] - Issue #1217 discussion

**Type:** review
**Keywords:** world editing, blocks requiring support, atomic update, preserving connection states, bulk data transfer, mesh updates, light updates
**Concepts:** atomic operations, block updates, connection states, bulk data transfer

## Summary
Discussion on world editing behavior, particularly regarding blocks that require support. Maintainers suggest atomic updates and preserving connection states during paste operations.

## Explanation
The discussion revolves around the issue of world editing breaking when pasting blocks that require support, such as branches needing to connect to leaves. The maintainers propose an atomic update approach where the pasted region's block types and data values are preserved exactly as copied. This includes maintaining invalid rotation modes at the edges. Additionally, there is a suggestion to combine this with bulk data transfer to reduce mesh updates from per-block to per-chunk, which could also optimize light updates.

## Related Questions
- What is the proposed behavior for pasting blocks that require support?
- How does the maintainers' suggestion address the issue of broken world editing?
- Can you explain the concept of atomic operations in this context?
- What are the potential benefits of combining bulk data transfer with block updates?
- How might light updates be optimized alongside mesh updates?
- What changes were made in #2459 to fix the issue?
- Are there any specific examples of blocks that require support mentioned in the discussion?
- How does the maintainers' suggestion impact performance during world editing?
- Is there a plan to implement these suggestions in future releases?
- What are the potential drawbacks of preserving invalid rotation modes at the edges?

*Source: unknown | chunk_id: github_issue_1217_discussion*
