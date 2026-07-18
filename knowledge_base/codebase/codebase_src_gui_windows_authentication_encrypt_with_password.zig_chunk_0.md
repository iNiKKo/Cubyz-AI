# [easy/codebase_src_gui_windows_authentication_encrypt_with_password.zig] - Chunk 0

**Type:** implementation
**Keywords:** GUI window, account code encryption, password input, checkbox, button
**Symbols:** settings, Vec2f, gui, GuiComponent, GuiWindow, Button, CheckBox, Label, HorizontalList, TextInput, VerticalList, window, innerList, encryptWithPasswordCheckbox, passwordTextField, passwordRow, confirmButton, encryptAccountCode, padding, accountCode, setAccountCode, confirm, encryptAccountCodeCallback, refreshInner, back, onOpen, update, onClose
**Concepts:** GUI, authentication, encryption, password

## Summary
GUI window for encrypting account code with password

## Explanation
This chunk defines a GUI window for encrypting an account code using a password. It includes components like checkboxes, text inputs, and buttons to allow the user to choose encryption method and enter a password. The window updates based on user input and handles actions such as confirming encryption and returning to previous screens.

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
- What actions does the `onClose` function perform?
- Where is the password row stored in memory?
- What happens if the user chooses not to encrypt with a password?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_encrypt_with_password.zig_chunk_0*
