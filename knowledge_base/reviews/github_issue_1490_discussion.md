# [issues/issue_1490.md] - Issue #1490 discussion

**Type:** review
**Keywords:** block entities, leaked, crashes, support blocks, cmpxchgBlock, fix, #2459, event system
**Symbols:** cmpxchgBlock
**Concepts:** memory leak, block update event

## Summary
The issue of block entities being leaked and causing crashes when their support blocks break has been addressed by moving the action to a block update event in commit #2459.

## Explanation
The original problem occurred because only the main block was checked during the `cmpxchgBlock` operation, leading to block entities not being properly cleaned up and causing crashes when attempting to unload them. The fix involves modifying the code to handle block updates through an event system, ensuring that all related block entities are correctly managed and preventing memory leaks.

## Related Questions
- What was the original issue with block entities and support blocks?
- How did commit #2459 address the problem of block entity leaks and crashes?
- What changes were made to the `cmpxchgBlock` function in commit #2459?
- Why is an event system used for handling block updates?
- Can you explain how the fix prevents memory leaks in Cubyz?
- How does the block update event ensure that all related block entities are managed correctly?

*Source: unknown | chunk_id: github_issue_1490_discussion*
