# [easy/codebase_src_gui_windows_social.zig] - Chunk 0

**Type:** api
**Keywords:** GuiWindow, VerticalList, CheckBox, Button, streamerMode, showPlayerIndexWithName, KeyCollection, getPublicKey, deinit, closeIfMouseIsGrabbed
**Symbols:** GuiWindow, toggleStreamerMode, toggleNamesWithIndex, logout, copy, onOpen, onClose, update
**Concepts:** social GUI window, account settings, streamer mode toggle, name change, logout flow, clipboard copy, window lifecycle callbacks, multiplayer window closing

## Summary
This chunk defines the social GUI window (account settings, streamer mode toggles, name change, logout) and its lifecycle callbacks.

## Explanation
The chunk imports main settings, Vec2f, and several GUI components (GuiWindow, Button, CheckBox, Label, VerticalList). It declares a global GuiWindow instance with content size 128x256 and closeIfMouseIsGrabbed enabled. Two internal vars track logoutButton pointer and inGameDisabled flag. The chunk defines four helper functions: toggleStreamerMode writes to main.settings.streamerMode and saves; toggleNamesWithIndex writes to main.settings.showPlayerIndexWithName and saves; logout deinitializes the stored account, resets authentication.KeyCollection.initialized, closes any open windows whose id contains 'multiplayer' (or matches a specific save_selection window), sets logoutButton.disabled = true; copy retrieves the public key via KeyCollection.getPublicKey using settings.launchConfig.preferredAuthenticationAlgorithm, frees it on defer, and sets clipboard. The main UI is built in onOpen: a VerticalList is initialized with padding 8 and height 400; two CheckBoxes are added for Streamer Mode (tied to main.settings.streamerMode) and Display players index after their name (tied to main.settings.showPlayerIndexWithName); a Button 'Copy public key' is added, disabled if KeyCollection.initialized is false; inGameDisabled is set based on whether main.game.world is non-null; a Button 'Change Name' is added, disabled when inGameDisabled; logoutButton is created as a Button with text 'Logout', disabled when inGameDisabled or !KeyCollection.initialized; the list is finished centered and assigned to window.rootComponent, then contentSize is recomputed from rootComponent position/size plus padding, and gui.updateWindowPositions() is called. onClose deinitializes the rootComponent if present. update re-evaluates logoutButton.disabled based on inGameDisabled and KeyCollection.initialized.

## Related Questions
- What happens when the user clicks the 'Copy public key' button in this social window?
- How does the logout function handle closing multiplayer windows versus other windows?
- Under what conditions is the 'Change Name' button disabled in onOpen?
- Which settings fields are modified by toggleStreamerMode and toggleNamesWithIndex, and how are they persisted?
- What is the purpose of checking main.game.world != null when building the UI list?
- How does the chunk ensure that logoutButton remains enabled only when not in-game and authentication keys exist?
- What steps are taken to deinitialize the stored account during logout, and why is KeyCollection.initialized reset?
- Why is gui.updateWindowPositions() called after setting window.rootComponent in onOpen?
- How does the chunk compute the final contentSize of the social window based on its root component?
- What would happen if a user tries to copy the public key before authentication.KeyCollection.initialized becomes true?

*Source: unknown | chunk_id: codebase_src_gui_windows_social.zig_chunk_0*
