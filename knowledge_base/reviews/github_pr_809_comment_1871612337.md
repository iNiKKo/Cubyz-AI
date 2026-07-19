# [src/gui/gui.zig] - PR #809 review diff

**Type:** review
**Keywords:** hardcoded logic, memory leaks, architectural principles, reopenWindow, deinit, components
**Symbols:** openWindow, windowList, items, id, onOpenFn, onClose
**Concepts:** thread safety, backwards compatibility, memory leak

## Summary
Added specific logic for 'notification' window without handling cleanup, causing memory leaks.

## Explanation
The change introduces hardcoded logic to call `onOpenFn()` for a 'notification' window within the `openWindow` function. This approach is criticized as it violates architectural principles by hardcoding behavior for specific windows. Additionally, it leads to memory leaks because the previous window components are not properly deinitialized using the `onClose` method. The reviewer suggests creating a new function `reopenWindow` that first closes the existing window before reopening it, which would address both the architectural issue and prevent memory leaks.

The code change specifically adds:
```zig
if (std.mem.eql(u8, id, "notification")) {
    window.onOpenFn();
}
```
This hardcoded logic is placed within the `openWindow` function. The reviewer points out that this is not the right place for such specific window handling and suggests a better approach to manage window lifecycle more effectively.

## Related Questions
- What is the impact of not calling `onClose` on window components?
- How can memory leaks be prevented in the `openWindow` function?
- Why is it recommended to introduce a new `reopenWindow` function?
- What are the architectural implications of hardcoding logic for specific windows?
- How does the current implementation affect backwards compatibility?
- Can you provide an example of how to properly deinitialize window components?

*Source: unknown | chunk_id: github_pr_809_comment_1871612337*
