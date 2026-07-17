# [hard/codebase_src_graphics_Window.zig] - Chunk 4

**Type:** api
**Keywords:** callconv, Vec2f, splat, bitCast, intCast, floatCast, round, modulo arithmetic, address-of reference, enum switch
**Symbols:** GLFWCallbacks, errorCallback, keyCallback, charCallback, framebufferSize, cursorPosition, applyCursorPositionChanges, mouseButton, scroll
**Concepts:** window callbacks, mouse delta averaging, circular buffer, GLFW integration

## Summary
This chunk defines GLFW callback functions for window events including framebuffer resize, cursor position tracking with averaging over a circular buffer, mouse button handling, scroll offset accumulation, and GL debug output categorization.

## Explanation
The chunk declares GLFWCallbacks as a struct containing several callconv(.c) void functions. errorCallback logs GLFW errors to std.log.err. keyCallback processes glfw_key events: it casts _mods to Key.Modifiers via @bitCast, determines textKeyPressedInTextField by checking main.gui.selectedTextInput and c.glfwGetKeyName, sets grabbed from the outer scope, handles press/release actions by iterating over main.KeyBoard.keys array with a for loop using &main.KeyBoard.keys as an address-of reference, calls key.setPressed or key.action depending on action type, and specifically routes GLFW_REPEAT events to key.action. charCallback checks !grabbed before delegating to main.gui.textCallbacks.char. framebufferSize logs new dimensions via std.log.info, casts newWidth/newHeight to c_int with @intCast, updates width/height fields, calls main.renderer.updateViewport, main.gui.updateGuiScale, and main.gui.updateWindowPositions. A circular buffer for mouse deltas is defined: const deltasLen: u2 = 3; var deltas: [deltasLen]Vec2f initialized via @splat(.{0, 0}); var deltaBufferPosition: u2 = 0; var currentPos: Vec2f = Vec2f{0, 0}; var ignoreDataAfterRecentGrab: bool = true. cursorPosition casts x/y to f64 with @floatCast, constructs newPos as Vec2f{...}, checks grabbed and !ignoreDataAfterRecentGrab before computing newDelta by subtracting currentPos from newPos and scaling via @as(Vec2f, @splat(main.settings.mouseSensitivity)), applies settings.invertMouseY by multiplying deltas[1] by -1 if true, accumulates into deltas[deltaBufferPosition], sets ignoreDataAfterRecentGrab = false, updates currentPos = newPos, and sets lastUsedMouse = true. applyCursorPositionChanges sums all deltas in a for loop over deltas, divides averagedDelta by @splat(deltasLen), calls main.game.camera.moveRotation with scaled components (averagedDelta[0]*0.0089, averagedDelta[1]*0.0089), rotates deltaBufferPosition via modulo arithmetic (deltaBufferPosition = (deltaBufferPosition + 1)%deltasLen), and resets deltas[deltaBufferPosition] to Vec2f{0, 0}. mouseButton casts _mods similarly, checks action for press/release, delegates nextKeypressListener if present by calling listener(c.GLFW_KEY_UNKNOWN, button, 0) then setting nextKeypressListener = null, otherwise iterates main.KeyBoard.keys looking for matching key.mouseButton and calls key.setPressed with false for textKeyPressedInTextField. scroll ignores xOffset via _ = xOffset, accumulates yOffset into scrollOffsetFraction using @floatCast, rounds to integer part via @round(scrollOffsetFraction) adding to scrollOffsetInteger, then subtracts the rounded value from scrollOffsetFraction. glDebugOutput maps source enum values to string literals with a switch expression returning 

## Related Questions
- How does the cursorPosition callback handle mouse grabbing state?
- What is the purpose of ignoreDataAfterRecentGrab in cursorPosition?
- How are mouse deltas averaged across frames using a circular buffer?
- Which GLFW actions trigger key.setPressed versus key.action calls?
- How does framebufferSize update renderer viewport and GUI scale?
- What happens to scrollOffsetFraction after rounding the integer part?
- How is textKeyPressedInTextField determined in keyCallback?
- Why does mouseButton pass false for textKeyPressedInTextField?
- What string literals are returned by glDebugOutput source switch?
- How does applyCursorPositionChanges reset delta buffer position?

*Source: unknown | chunk_id: codebase_src_graphics_Window.zig_chunk_4*
