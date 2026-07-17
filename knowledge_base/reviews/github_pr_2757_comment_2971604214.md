# [src/gui/windows/authentication/unlock.zig] - PR #2757 review diff

**Type:** review
**Keywords:** authentication failure, onClose, invalid memory access, global label, component cleanup
**Symbols:** textComponent, incorrectPassword, apply, failureText, accountCode
**Concepts:** data corruption, thread safety, memory management

## Summary
The code now handles authentication failure by setting a flag and calling `onClose`, which leads to potential data corruption due to premature cleanup of components.

## Explanation
The reviewer points out that setting `incorrectPassword` to true and immediately calling `onClose` results in the cleanup of components while they are still being iterated, leading to invalid memory access. The reviewer suggests storing the label text globally and updating it instead, which would prevent premature cleanup and potential data corruption.

## Related Questions
- What is the purpose of the `incorrectPassword` flag?
- Why should `onClose` not be called immediately after setting `incorrectPassword`?
- How does storing the label text globally prevent data corruption?
- What are the potential consequences of premature component cleanup?
- How can we ensure that components are not accessed after they are cleaned up?
- What is the role of `main.stackAllocator` in this code snippet?

*Source: unknown | chunk_id: github_pr_2757_comment_2971604214*
