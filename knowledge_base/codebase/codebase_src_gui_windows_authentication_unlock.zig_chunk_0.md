# [easy/codebase_src_gui_windows_authentication_unlock.zig] - Chunk 0

**Type:** api
**Keywords:** GUI components, password input, authentication, decryption, secure memory zeroing
**Symbols:** window, padding, textComponent, logoutButton, incorrectPasswordLabel, apply, showTextCallback, logout, onTextUpdate, onOpen, onClose
**Concepts:** GUI window management, user authentication, password decryption, error handling, memory security

## Summary
Handles the GUI logic for the authentication unlock window in Cubyz, including password input, error handling, and account decryption.

## Explanation
This chunk defines the behavior of the authentication unlock window in Cubyz. It includes functions for applying the entered password to decrypt the account, showing/hiding the password text, logging out, updating text components, opening the window, and closing it securely. The window contains a vertical list with labels, a text input field for the password, a checkbox to show/hide the password, buttons for logout and decryption, and error handling for incorrect passwords or corrupted data.

Specifically:
- `window.contentSize` is set to `{128, 256}`.
- Padding value is defined as `const padding: f32 = 8;`.
- The text input field (`textComponent`) has an obfuscated password entry and updates the `logoutButton.disabled` state based on its length. If the password input field is empty, the logout button becomes enabled; otherwise, it remains disabled.
- Error handling includes displaying messages like "#ff0000Incorrect password." for authentication failure or a formatted error message for other errors, such as "#ff0000Authentication data is corrupted: {error_name}".

When the window opens, the following components are added to the vertical list:
- A label with text "Please enter your local password to decrypt your Multiplayer Account." and width 420.
- A label with text "If you lost your password you can also log out and reenter your Account Code." and width 420.
- An `incorrectPasswordLabel` initialized with empty text and left alignment, with a width of 420.
- A horizontal list (`passwordRow`) containing:
  - A `TextInput` field for password input with dimensions `{0, 0}`, width 340 (420 - 80), height 22, and an obfuscated entry. The text buffer is selected by default.
  - A `CheckBox` with position `{10, 0}`, width 70, label "Show", initial state false, and a callback function `showTextCallback` to toggle the password visibility.
- A horizontal list (`buttonRow`) containing:
  - A `Button` for logout with dimensions `{0, 0}`, width 200, text "Logout", and an action that calls the `logout` function. The button is initially enabled.
  - A `Button` for decryption with dimensions `{8, 0}`, width 200, text "Decrypt", and an action that calls the `apply` function.

Secure memory zeroing is performed when the window closes by using `std.crypto.secureZero` to clear the password buffer and current string items. The clipboard is also cleared, and any remaining components are deinitialized.

## Code Example
```zig
fn logout() void {
	main.settings.storedAccount.deinit(main.globalAllocator);
	main.settings.storedAccount = .empty;
	main.settings.save();
	gui.closeWindowFromRef(&window);
	gui.openWindow("authentication/login");
}
```

## Related Questions
- What is the purpose of the `apply` function in this chunk?
- How does the chunk handle incorrect passwords or corrupted authentication data?
- What components are added to the vertical list when the window opens?
- How is memory secured when the window closes?
- What happens if the password input field is empty?
- How does the `logout` function work in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_unlock.zig_chunk_0*
