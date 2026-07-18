# [easy/codebase_src_gui_windows_authentication_stay_logged_in.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, button actions, window lifecycle, account code handling, memory cleanup
**Symbols:** window, padding, accountCode, setAccountCode, stayLoggedIn, dontStayLoggedIn, onOpen, onClose
**Concepts:** GUI window management, user authentication, settings persistence

## Summary
Handles the GUI window for staying logged in, managing user choices and updating settings.

## Explanation
This chunk defines a GUI window that prompts the user to decide whether they want to stay logged in. It includes functions to set the account code, handle button actions for staying or not staying logged in, initialize the window components on open, and clean up resources on close. The window uses vertical and horizontal lists to layout labels and buttons.

## Code Example
```zig
pub fn setAccountCode(accountCode_: main.network.authentication.AccountCode) void {
	accountCode = accountCode_;
}
```

## Related Questions
- How does the `setAccountCode` function work?
- What happens when the user chooses to stay logged in?
- What components are added to the window on open?
- How is memory cleaned up when the window closes?
- What is the purpose of the `padding` constant?
- Which functions handle button actions in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_stay_logged_in.zig_chunk_0*
