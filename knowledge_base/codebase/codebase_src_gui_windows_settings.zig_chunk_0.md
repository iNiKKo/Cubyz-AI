# [easy/codebase_src_gui_windows_settings.zig] - Chunk 0

**Type:** implementation
**Keywords:** GuiWindow, VerticalList, openWindowCallback, initText, deinit, padding, rootComponent, updateWindowPositions, contentSize, center
**Symbols:** Vec2f, GuiComponent, GuiWindow, window, padding, onOpen, onClose
**Concepts:** GUI window management, vertical list layout, button callbacks, content size computation, component lifecycle

## Summary
This chunk defines the Settings window UI component, including its initialization logic that populates a vertical list of buttons for Graphics, Sound, Controls, Advanced Controls, and Social categories.

## Explanation
The chunk declares a global `window` variable of type `GuiWindow`, initialized with a content size of Vec2f{128, 256} and the closeIfMouseIsGrabbed flag set to true. It imports the main module for Vec2f, the gui module for GuiComponent/GuiWindow and openWindowCallback, and Button/VerticalList components from ../components/. A constant padding value of 8 is defined. The onOpen function creates a VerticalList with the specified padding and height (300), then adds five buttons: Graphics, Sound, Controls, Advanced Controls, and Social. Each button uses initText with position {0,0}, width 128, and an onAction callback that invokes gui.openWindowCallback with the corresponding category string. After adding all buttons, list.finish(.center) is called to center-align them, then list.toComponent() converts the list into a GuiComponent which becomes window.rootComponent. The window's contentSize is recomputed by taking the root component's position and size (via ?.pos() and ?.size()) and adding padding on both sides using @splat(padding). Finally, gui.updateWindowPositions() is called to refresh layout positions. The onClose function checks if window.rootComponent exists and calls comp.deinit() on it.

## Related Questions
- What is the default content size of the Settings window?
- Which categories are available in the Settings window buttons?
- How does onOpen compute the final window contentSize after adding the list?
- What happens to the rootComponent when onClose is called?
- Does the Settings window close automatically when mouse is grabbed?
- Where are the Button and VerticalList components imported from?

*Source: unknown | chunk_id: codebase_src_gui_windows_settings.zig_chunk_0*
