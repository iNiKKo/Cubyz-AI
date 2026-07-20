# [src/gui/windows/authentication/unlock.zig] - PR #2757 review diff

**Type:** review
**Keywords:** data corruption, invalid memory access, global label, architectural review, error handling, decryption failure, window closure
**Symbols:** textComponent, incorrectPassword, apply, failureText, accountCode, main.settings.storedAccount.decryptFromPassword, std.log.err, error.AuthenticationFailed, onClose
**Concepts:** data corruption, thread safety, memory management

## Summary
The review addresses a critical data corruption issue in the `unlock.zig` file by modifying the error handling mechanism to prevent accessing invalid memory.

## Explanation
The review addresses a critical data corruption issue in the `unlock.zig` file by modifying the error handling mechanism to prevent accessing invalid memory. The reviewer identifies a significant architectural flaw where calling `onClose()` immediately after setting `incorrectPassword` to true leads to data corruption. This is because `onClose()` cleans up components that are still being iterated over, resulting in invalid memory access. The proposed solution involves storing the label text globally and updating it instead of directly closing the window, which prevents accessing invalid memory.

Specifically, the error handling mechanism now checks if the error is `error.AuthenticationFailed` and sets `incorrectPassword` to true before calling `onClose()`. Additionally, the reviewer suggests storing the label in a global variable and changing only the label text to prevent invalid memory access. The code changes include adding a new variable `incorrectPassword` and modifying the `apply()` function to handle the error as follows:

```zig
var incorrectPassword = false;

fn apply() void {
    var failureText: main.List(u8) = .init(main.stackAllocator);
    defer failureText.deinit();
    const accountCode = main.settings.storedAccount.decryptFromPassword(textComponent.currentString.items, &failureText) catch |err| {
        if (err == error.AuthenticationFailed) {
            incorrectPassword = true;
            onClose();
        }
    }
}
```

By setting `incorrectPassword` to true and then calling `onClose()`, the code ensures that the window is closed only after the password decryption fails, preventing invalid memory access. Storing the label text globally and updating it instead of directly closing the window further helps prevent this issue.

## Related Questions
- What is the purpose of the `incorrectPassword` variable in the `unlock.zig` file?
- How does the current error handling mechanism lead to data corruption?
- Why is it critical to prevent accessing invalid memory in this context?
- What is the proposed solution to fix the data corruption issue?
- How does storing the label text globally help prevent invalid memory access?
- What are the potential implications of not addressing this architectural flaw?

*Source: unknown | chunk_id: github_pr_2757_comment_2971604214*
