# [easy/codebase_src_gui_windows_authentication_encrypt_with_password.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, account code encryption, password input, checkbox, button
**Symbols:** settings, Vec2f, gui, GuiComponent, GuiWindow, Button, CheckBox, Label, HorizontalList, TextInput, VerticalList, window, innerList, encryptWithPasswordCheckbox, passwordTextField, passwordRow, confirmButton, encryptAccountCode, padding, accountCode, setAccountCode, confirm, encryptAccountCodeCallback, refreshInner, back, onOpen, update, onClose
**Concepts:** GUI, authentication, encryption, password

## Summary
GUI window for encrypting an account code using a password, including checkboxes, text inputs, and buttons to handle user input and actions such as confirming encryption or returning to previous screens.

## Explanation
This chunk defines a GUI window for encrypting an account code using a password. It includes components like checkboxes, text inputs, and buttons to allow the user to choose encryption method and enter a password. The `encryptAccountCode` variable determines whether the account code is encrypted with a password or stored unencoded. When the confirm button is clicked, the function checks if `encryptAccountCode` is true and initializes the settings accordingly using either `initFromPassword` or `initUnencoded`. If encryption is chosen, the user must enter a password in the text input field. The window updates based on user input and handles actions such as confirming encryption and returning to previous screens. The inner list dynamically adds components like checkboxes and horizontal lists with labels and text inputs when encrypting with a password. The back button returns the user to the 'authentication/stay_logged_in' screen, while the confirm button saves settings and opens the multiplayer window. The `refreshInner` function updates the content of the vertical list based on the value of `encryptAccountCode`. The confirm button becomes disabled if encryption is chosen but no password has been entered. Upon closing the window, any traces of the account code or password are removed from memory.

## Code Example
```zig
fn confirm() void {
    if (encryptAccountCode) {
        settings.storedAccount.deinit(main.globalAllocator);
        settings.storedAccount = .initFromPassword(main.globalAllocator, accountCode, passwordTextField.currentString.items);
    } else {
        settings.storedAccount.deinit(main.globalAllocator);
        settings.storedAccount = .initUnencoded(main.globalAllocator, accountCode);
    }
    settings.save();
    gui.closeWindowFromRef(&window);
    gui.openWindow("multiplayer");
}
```

## Related Questions
- What is the purpose of the `encryptAccountCode` variable?
- How does the `confirm` function handle encryption and password input?
- What components are added to the inner list when encrypting with a password?
- What action does the back button perform?
- Where is the account code stored in memory after encryption?
- What happens if the user chooses not to encrypt the account code?
- How is the window content size updated after changes?
- What is the purpose of the `refreshInner` function?
- What are the conditions under which the confirm button becomes disabled?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_encrypt_with_password.zig_chunk_0*
