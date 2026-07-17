# [src/server/server.zig] - PR #1228 review diff

**Type:** review
**Keywords:** undo history, circular buffer, blueprint, position, message, capacity, dequeue, enqueue, full capacity, memory allocation
**Symbols:** WorldEditData, maxWorldEditHistoryCapacity, selectionPosition1, selectionPosition2, clipboard, undoHistory, History, Value, init, deinit, changes, CircularBufferQueue
**Concepts:** Undo/Redo functionality, Circular buffer, Memory management, Data structure design

## Summary
Added undo history functionality to WorldEditData, including a circular buffer queue for storing edit changes.

## Explanation
The change introduces an undo history mechanism within the WorldEditData struct. This includes a CircularBufferQueue to store edit changes up to a maximum capacity of 1024 entries. Each entry in the queue is a Value struct containing a blueprint, position, and message. The reviewer suggests swapping the order of operations in the push method to ensure full capacity utilization.

## Related Questions
- What is the maximum capacity of the undo history?
- How does the Value struct manage memory for its message and blueprint?
- Why is there a suggestion to swap the order of operations in the push method?
- How does the CircularBufferQueue handle full capacity scenarios?
- What are the implications of using globalAllocator for memory management in this context?
- Can you explain the purpose of the clearRetainingCapacity method in the History struct?

*Source: unknown | chunk_id: github_pr_1228_comment_2010870507*
