# [src/settings.zig] - PR #1719 review diff

**Type:** review
**Keywords:** double free, deinit, zonObject, join, error handling, memory leak
**Symbols:** save, zonObject, keyboard, main.files.cubyzDir().readToZon, settingsFile, oldZonObject
**Concepts:** thread safety, memory management

## Summary
The change introduces a potential double-free issue by deinitializing both `oldZonObject` and `zonObject`.

## Explanation
The reviewer points out that the code now deinits both `oldZonObject` and `zonObject`, which could lead to a double free if `oldZonObject` is an object. This architectural oversight needs to be addressed to prevent memory corruption and ensure thread safety.

## Related Questions
- What is the purpose of `zonObject.join(zonObject)` in this code?
- How does the error handling work in the `readToZon` function call?
- Why is there a need to check if `oldZonObject` is an object before joining?
- What are the potential consequences of not properly managing memory in this function?
- How can we ensure that both objects are not deinitialized twice?
- Is there any other part of the codebase where similar issues might occur?

*Source: unknown | chunk_id: github_pr_1719_comment_2230237026*
