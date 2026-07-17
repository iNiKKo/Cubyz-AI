# [easy/codebase_src_gui_windows_authentication_encrypt_with_password.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, CheckBox, TextInput, HorizontalList, VerticalList, settings.save, deinit, onOpen, update, onClose
**Symbols:** window, innerList, encryptWithPasswordCheckbox, passwordTextField, passwordRow, confirmButton, encryptAccountCode, padding, accountCode, setAccountCode, confirm, encryptAccountCodeCallback, refreshInner, back, onOpen, update, onClose
**Concepts:** authentication UI, password encryption checkbox, settings persistence, memory cleanup on close, GUI component tree construction, window lifecycle callbacks

## Summary
This chunk implements the authentication window UI for storing and encrypting an account code, handling user input via checkboxes and text fields, persisting settings with optional password encryption, and cleaning up memory on close.

## Explanation
The chunk defines a GuiWindow named 'window' with fixed content size (128x256) that is non-closeable but closes when mouse is grabbed. It declares several uninitialized pointers: innerList (*VerticalList), encryptWithPasswordCheckbox (*CheckBox), passwordTextField (*TextInput), passwordRow (*HorizontalList), and confirmButton (*Button). A boolean 'encryptAccountCode' defaults to true, and a padding constant of 8f32 is used for layout spacing. The accountCode variable holds the current authentication code (type from main.network.authentication.AccountCode) and is initialized via setAccountCode(). The onOpen() function constructs the UI: it creates a VerticalList with padding, adds a Label explaining storage options, initializes innerList as an empty VerticalList, then adds a CheckBox labeled 'Encrypt it with a password...' bound to encryptWithPasswordCheckbox and wired to encryptAccountCodeCallback. If encryption is enabled, passwordRow (a HorizontalList) is added containing a Label 'Local Password:' and a TextInput for the password; otherwise passwordRow is omitted. A second VerticalList named list wraps innerList and button rows. The button row contains a 'Back' Button invoking back() and a 'Confirm' Button invoking confirm(). After building the component tree, window.rootComponent is set to list.toComponent(), contentSize is recomputed based on rootComponent position/size plus padding, and gui.updateWindowPositions() is called. The update() function disables confirmButton when encryption is enabled but the password field is empty (len == 0). back() closes this window, calls gui.windowlist.@

## Code Example
```zig
pub fn setAccountCode(accountCode_: main.network.authentication.AccountCode) void {
	accountCode = accountCode_;
}
```

## Related Questions
- What is the default value of encryptAccountCode when the window opens?
- How does confirm() handle the case where encryption is disabled versus enabled?
- Which GUI component is used to capture the user-entered password string?
- What happens to accountCode in onClose() regardless of encryption setting?
- Does back() modify the stored account code before navigating away?
- How is window.rootComponent assigned after building the UI tree?
- Under what condition does confirmButton become disabled during update()?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_encrypt_with_password.zig_chunk_0*
