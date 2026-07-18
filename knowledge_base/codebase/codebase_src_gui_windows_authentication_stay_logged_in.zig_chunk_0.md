# [easy/codebase_src_gui_windows_authentication_stay_logged_in.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, button actions, window lifecycle, account code handling, memory cleanup
**Symbols:** window, padding, accountCode, setAccountCode, stayLoggedIn, dontStayLoggedIn, onOpen, onClose
**Concepts:** GUI window management, user authentication, settings persistence

## Summary
Handles the GUI window for staying logged in, managing user choices and updating settings.

## Explanation
This chunk defines a GUI window (`padding = 8`, used to size the layout) that prompts the user with "Would you like to stay logged in? This will store your Account Code locally in your settings file." and two buttons, "No" and "Yes". Clicking "Yes" (`stayLoggedIn`) hands the account code to the `"authentication/encrypt_with_password"` window, clears the local `accountCode` variable, closes this window, and opens that one. Clicking "No" (`dontStayLoggedIn`) just closes this window and opens `"multiplayer"` directly (the code is never persisted). `onClose` explicitly calls `accountCode.deinit()` first, with a comment noting this ensures no trace of the account code or password remains in memory.

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
