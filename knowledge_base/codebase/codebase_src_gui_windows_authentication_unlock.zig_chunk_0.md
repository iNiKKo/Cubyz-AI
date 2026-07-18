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
- The window contains labels with specific text and dimensions, a text input field with an obfuscated password entry and show/hide checkbox, buttons for logout and decryption, and secure memory zeroing when the window closes.

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
