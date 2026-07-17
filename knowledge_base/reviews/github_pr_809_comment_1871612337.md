# [src/gui/gui.zig] - Chunk 1871612337

**Type:** review
**Keywords:** openWindow, onClose, notification, memory leak, hardcode, reopenWindow, lifecycle, defer, windowList, deinit
**Symbols:** openWindow, onClose, onOpenFn, windowList, notification
**Concepts:** memory leak, lifecycle management, architectural coupling, deferred cleanup, function separation

## Summary
The change adds a hardcoded check for the 'notification' window ID inside openWindow, invoking onOpenFn without calling onClose, which introduces memory leaks and violates architectural principles by embedding specific logic in a generic function.

## Explanation
The reviewer identifies two critical issues: (1) Hardcoding special-case behavior inside openWindow breaks modularity and makes the codebase harder to maintain; any future window with similar needs would require another ad-hoc block. (2) Because onClose is never called before onOpenFn, resources allocated by the previous notification window are not freed, leading to memory leaks observable in debug builds. The architectural remedy proposed is to decouple reopening from opening: introduce a new reopenWindow function that first calls onClose on the existing instance (if any), then proceeds with allocation and onOpenFn. This preserves the invariant that openWindow only creates fresh windows, while reopenWindow handles lifecycle transitions safely.

## Related Questions
- What is the exact signature of openWindow and how does it interact with windowList?
- Where are onClose callbacks defined for windows, and what resources do they release?
- Is there any existing pattern in gui.zig for handling window reopening safely?
- How does the defer updateWindowPositions() relate to resource cleanup order?
- What happens if openWindow is called twice with the same id without onClose being invoked?
- Are there other windows besides 'notification' that require special onOpenFn logic?
- Could a generic reopen function be implemented using existing window metadata structures?
- Does the current implementation assume any global state that would leak if not cleaned up?
- What is the expected behavior of onOpenFn for the notification window versus other windows?
- Is there a test case in the repository that verifies memory correctness after reopening windows?

*Source: unknown | chunk_id: github_pr_809_comment_1871612337*
