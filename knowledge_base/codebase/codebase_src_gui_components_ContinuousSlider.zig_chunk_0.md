# [medium/codebase_src_gui_components_ContinuousSlider.zig] - Chunk 0

**Type:** implementation
**Keywords:** slider, continuous slider, mouse interaction, drag anchor, formatter callback, texture binding, custom rendering, label update, value clamp, scissor clipping
**Symbols:** ContinuousSlider, border, fontSize, texture, pos, size, minValue, maxValue, callback, formatter, currentValue, currentText, label, button, mouseAnchor, globalInit, globalDeinit, init, deinit, toComponent, setButtonPosFromValue, updateLabel, updateValueFromButtonPos, updateHovered, getBarPos, getBarSize, mainButtonPressed, mainButtonReleased, render
**Concepts:** GUI component lifecycle, mouse interaction handling, drag anchor tracking, value formatting callbacks, texture binding, custom rendering pipeline, label update on value change, scissor clipping

## Summary
Implements the ContinuousSlider GUI component with initialization, deinitialization, mouse interaction handling (hover detection, drag anchor tracking), label formatting via callbacks, and rendering using a texture.

## Explanation
The chunk defines the ContinuousSlider struct with fields for position, size, min/max values, callback, formatter, current value/text, label, button, and mouseAnchor. It declares globalInit() to load a slider texture from assets/cubyz/ui/slider.png and globalDeinit() to free it. The init() function allocates a ContinuousSlider on the global allocator, constructs internal Label and Button components (using provided width, minValue, maxValue, initialValue, callback, formatter), sets button size/position relative to label, computes overall component size, calls setButtonPosFromValue(), and returns self. deinit() frees currentText, destroys label/button, and deallocates the struct itself. toComponent() wraps self into a GuiComponent union variant .continuousSlider. setButtonPosFromValue() clamps currentValue to [minValue,maxValue], computes the draggable range (size[0] - 3*border - button.size[0]), maps value linearly to button.x position, and updates label via updateLabel(). updateLabel() frees old currentText, calls formatter(main.globalAllocator, newValue) to produce new text, creates a centered Label with width-3*border, deinit()-s the old label, assigns the new one. updateValueFromButtonPos() mirrors setButtonPosFromValue() but reads button.x position, computes value from mouseAnchor offset (button.pos[0] - 1.5*border)/range*len + minValue, updates currentValue if changed, calls updateLabel(), then invokes callback(value). updateHovered() checks if mousePosition is inside the button rect or bar rect; if inside button and button.updateHovered returns .handled it propagates .handled, otherwise returns .ignored. getBarPos() returns center of the slider track (1.5*border + button.size[0]/2, button.y + button.size[1]/2 - border). getBarSize() returns {range, 2*border} where range is size[0] - 3*border - button.size[0]. mainButtonPressed() computes mousePositionRelativeToSelf; if inside button and button.mainButtonPressed returns .handled it sets mouseAnchor to mouse.x - button.pos.x and returns .handled. Else if inside bar rect it sets mouseAnchor to self.pos.x + button.size.x/2, adjusts button.pos.x by subtracting mouseAnchor (drag start), then calls button.mainButtonPressed() which will handle the drag update. mainButtonReleased() simply calls button.mainButtonReleased(undefined). render() binds texture to slot 0, binds Button.pipeline scissor, draws customShadedRect with Button.buttonUniforms at self.pos/self.size; it begins a color block (sets oldColor = draw.setColor(0x80000000) and defers restore), but the snippet cuts off before completing the render logic.

## Related Questions
- What is the purpose of globalInit() in ContinuousSlider?
- How does init() construct the internal Label and Button components?
- What happens when deinit() is called on a ContinuousSlider instance?
- Describe how setButtonPosFromValue() maps a numeric value to button position.
- How does updateLabel() ensure thread-safe memory management for currentText?
- Explain the logic in mainButtonPressed() that distinguishes between button press and bar drag start.
- What is returned by updateHovered() when the mouse is over the slider track but not the button?
- How does getBarPos() compute the center point of the draggable region?
- In what order are label, button, and texture resources freed in deinit()?
- Does ContinuousSlider store its own allocator or rely on main.globalAllocator?
- What is the effect of calling toComponent() on a ContinuousSlider instance?
- How does render() prepare for drawing the slider background color?

*Source: unknown | chunk_id: codebase_src_gui_components_ContinuousSlider.zig_chunk_0*
