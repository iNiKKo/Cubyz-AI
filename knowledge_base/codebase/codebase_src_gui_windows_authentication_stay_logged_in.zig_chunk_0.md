# [easy/codebase_src_gui_windows_authentication_stay_logged_in.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, HorizontalList, Button, AccountCode, deinit, windowlist, onAction
**Symbols:** setAccountCode, stayLoggedIn, dontStayLoggedIn, onOpen, onClose
**Concepts:** authentication flow, GUI window management, account code persistence, user choice handling

## Summary
This chunk defines a GUI window for the authentication flow, presenting a choice to stay logged in or not. It initializes a vertical list with labels and buttons that invoke corresponding functions to manage account code persistence and window navigation.

## Explanation
The chunk declares imports from main (settings, Vec2f) and gui (GuiWindow, GuiComponent types). It defines a global var window of type GuiWindow with contentSize set to {128, 256} and closeIfMouseIsGrabbed true. A pub fn setAccountCode takes an AccountCode and assigns it to the global accountCode variable. The stayLoggedIn function calls gui.windowlist.@

## Code Example
```zig
pub fn setAccountCode(accountCode_: main.network.authentication.AccountCode) void {
	accountCode = accountCode_;
}
```

## Related Questions
- What is the default content size of the authentication window?
- How does the chunk ensure no trace of the account code remains in memory on close?
- Which function is called when the user selects 'Yes' to stay logged in?
- What happens to the global accountCode variable after stayLoggedIn executes?
- Does the window automatically close if the mouse is grabbed, and how is that configured?
- How are the button actions wired to their respective functions?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_stay_logged_in.zig_chunk_0*
