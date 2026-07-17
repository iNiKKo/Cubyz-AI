# [easy/codebase_src_gui_windows_authentication_create_account_storage_method.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, Button, StorageMethod, onOpen, onClose, initText, initWithInt, closeIfMouseIsGrabbed
**Symbols:** settings, Vec2f, gui, GuiComponent, GuiWindow, Button, CheckBox, HorizontalList, Label, TextInput, VerticalList, StorageMethod, window, padding, next, onOpen, onClose
**Concepts:** account code storage method selection UI, vertical list component construction, button action callbacks with enum conversion, window lifecycle management (open/close), storage method enumeration

## Summary
This chunk defines the UI window for selecting an account code storage method, exposing a public `onOpen` handler that builds a vertical list of buttons (Password Manager, Save as file, Write it down yourself) and a private `next` helper that closes the current window, sets the chosen StorageMethod via the windowlist API, and reopens the same window.

## Explanation
The chunk imports std and main, then pulls GuiComponent, GuiWindow, Button, CheckBox, HorizontalList, Label, TextInput, VerticalList from gui.GuiComponent. It also imports the enum StorageMethod from gui.windowlist.@

## Related Questions
- What is the default content size of the authentication create account window?
- Which storage methods are presented to the user in the UI list?
- How does the next function update the global windowlist state after a selection?
- Does the onOpen handler perform any cleanup before building its component tree?
- What happens to the rootComponent when onClose is invoked?
- Is the closeable flag of the window set to true or false by default in this chunk?

*Source: unknown | chunk_id: codebase_src_gui_windows_authentication_create_account_storage_method.zig_chunk_0*
