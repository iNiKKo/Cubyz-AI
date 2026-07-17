# [easy/codebase_src_gui_windows_authentication_login.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, TextInput, Button, CheckBox, account code, secureZero, clipboard deletion, window lifecycle, callback-driven UI, obfuscated text
**Symbols:** GuiWindow, GuiComponent.Button, GuiComponent.CheckBox, GuiComponent.Label, GuiComponent.HorizontalList, GuiComponent.TextInput, GuiComponent.VerticalList, textComponent, loginButton, window, padding, login, updateText, showTextCallback, none, openCreateAccountWindow, onOpen, onClose
**Concepts:** authentication GUI window, account code input validation, secure memory clearing, clipboard deletion, window lifecycle management, callback-driven UI updates, obfuscated text field toggle

## Summary
This chunk defines the GUI window for authentication, handling login via account code input and creation of new accounts.

## Explanation
The chunk declares a public GuiWindow instance with size (128,256) and closeIfMouseIsGrabbed enabled. It imports several GuiComponent types: Button, CheckBox, Label, HorizontalList, TextInput, VerticalList. It defines two top-level variables: textComponent of type *TextInput and loginButton of type *Button, both initialized to undefined. A public var window is declared with contentSize Vec2f{128, 256} and closeIfMouseIsGrabbed true. The chunk contains four functions: login(), updateText(), showTextCallback(), none(), openCreateAccountWindow(), onOpen(), onClose(). The login() function validates the account code via main.network.authentication.AccountCode.initFromUserInput, raises notifications for empty or failed verification, optionally sets a flag loginAnyways to allow proceeding despite errors, and calls main.network.authentication.KeyCollection.init(accountCode) before closing the current window and opening authentication/stay_logged_in. updateText() resets loginAnyways, updates the login button label, and disables it if textComponent.currentString.items.len == 0. showTextCallback() toggles obfuscated on TextInput by setting textComponent.obfuscated = !showText. none() is an empty stub function. openCreateAccountWindow() closes the current window and opens authentication/create_account_general_info. onOpen() constructs a VerticalList with padding, adds labels prompting for account code, creates a TextInput with callbacks (onNewline -> none(), onUpdate -> updateText), adds a CheckBox labeled Show that toggles obfuscated via showTextCallback, adds a warning label about sharing the account code, builds a HorizontalList for createAccountRow containing a Button labeled Create Account with onAction = openCreateAccountWindow, and finally creates loginButton as a Button labeled Login with onAction = login and initially disabled. It sets window.rootComponent to list.toComponent(), adjusts contentSize based on component position/size plus padding, and calls gui.updateWindowPositions(). onClose() securely zeroes textComponent.textBuffer.glyphs and textComponent.currentString.items using std.crypto.secureZero, clears clipboard via main.Window.setClipboardString, opens clipboard_deleted window, and deinitializes the rootComponent if present.

## Related Questions
- What happens when the user enters an empty account code?
- How does the login function handle verification errors that occur in future versions?
- Which window is opened after a successful login or when proceeding despite errors?
- What security measures are taken to clear sensitive data on window close?
- How is the TextInput configured for obfuscation and newline handling?
- What label text appears next to the create account button?
- Does the login button remain disabled until a valid account code is entered?
- Which function is called when the user clicks Create Account?
- How does showTextCallback affect the TextInput's visual state?
- Is there any mechanism to prevent multiple simultaneous logins?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_login.zig_chunk_0*
