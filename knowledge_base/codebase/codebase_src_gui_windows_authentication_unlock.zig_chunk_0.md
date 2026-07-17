# [easy/codebase_src_gui_windows_authentication_unlock.zig] - Chunk 0

**Type:** implementation
**Keywords:** decryptFromPassword, authentication failed, secureZero, clipboard cleared, KeyCollection init, GuiComponent Button, GuiComponent TextInput, GuiComponent CheckBox, GuiComponent Label, main.settings.storedAccount
**Symbols:** window, padding, textComponent, logoutButton, incorrectPasswordLabel, apply, showTextCallback, logout, onTextUpdate, onOpen, onClose
**Concepts:** authentication unlock window UI, password entry and decryption, error display for incorrect passwords, corrupted auth data handling, logout with secure memory clearing, GuiWindow lifecycle management, VerticalList and HorizontalList composition

## Summary
This chunk implements the authentication unlock window UI, handling password entry, decryption of stored account data, error display for incorrect passwords or corrupted auth data, and logout with secure memory clearing.

## Explanation
The chunk defines a GuiWindow (window) with content size 128x256, closeIfMouseIsGrabbed enabled, and closeable disabled. It declares padding as f32 = 8. It holds pointers to TextInput (textComponent), Button (logoutButton), and Label (incorrectPasswordLabel). The apply() function decrypts the account from the password entered in textComponent using main.settings.storedAccount.decryptFromPassword; on error.AuthenticationFailed it updates incorrectPasswordLabel with '#ff0000Incorrect password.', otherwise it allocates a formatted error string via std.fmt.allocPrint, logs a warning if failureText.items is non-empty, initializes main.network.authentication.KeyCollection with the decrypted accountCode, closes this window and opens 'multiplayer'. showTextCallback toggles textComponent.obfuscated. logout() deinitializes storedAccount using main.globalAllocator, resets storedAccount to .empty, saves settings, closes this window and opens 'authentication/login'. onTextUpdate enables/disables logoutButton based on whether textComponent.currentString.items is empty. onOpen builds a VerticalList with padding rows, adds labels explaining password entry and account code reentry, creates the incorrectPasswordLabel, builds a HorizontalList for the password row containing TextInput (with .onNewline = apply and .onUpdate = onTextUpdate) and a CheckBox labeled 'Show' wired to showTextCallback, then a button row with Logout (action = logout) and Decrypt (action = apply), finishes the list, assigns it as window.rootComponent, adjusts contentSize based on rootComponent position/size plus padding, and calls gui.updateWindowPositions. onClose securely zeros textComponent.textBuffer.glyphs[0] via std.crypto.secureZero, zeros currentString.items, clears clipboard with main.Window.setClipboardString, opens 'clipboard_deleted', and deinitializes window.rootComponent if present.

## Related Questions
- What happens when the user enters an incorrect password in the authentication unlock window?
- How does the chunk handle corrupted authentication data during decryption?
- Which GUI component is used to display the 'Show' checkbox for toggling password visibility?
- What action is bound to the Decrypt button onOpen function?
- How does the logoutButton enable/disable state depend on textComponent.currentString.items length?
- Where are the decrypted account credentials stored after successful decryption in apply()?
- Which window is opened immediately after decrypting and initializing KeyCollection?
- What memory clearing steps occur in onClose to ensure no password trace remains?
- How does onOpen compute the final contentSize of the authentication unlock window?
- What label text is shown when incorrectPasswordLabel is updated with an error message?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_unlock.zig_chunk_0*
