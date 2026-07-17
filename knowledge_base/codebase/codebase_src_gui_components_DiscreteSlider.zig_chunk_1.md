# [medium/codebase_src_gui_components_DiscreteSlider.zig] - Chunk 1

**Type:** implementation
**Keywords:** discrete slider, mouse hover detection, button press handler, bar region computation, anchor offset tracking, position clamping, defer restore color, label render positioning, track rectangle draw, value update function call, custom shaded rect pipeline, scissor binding
**Symbols:** DiscreteSlider, getBarPos, getBarSize, mainButtonPressed, mainButtonReleased, render, updateValueFromButtonPos
**Concepts:** UI component input handling, mouse drag anchor tracking, geometry clamping, deferred resource restoration, label positioning, track rendering with scissor, value update from button position

## Summary
DiscreteSlider component handles mouse input for a slider UI element, including button press detection, dragging the handle along the bar, and rendering the label and track.

## Explanation
The chunk defines several inline functions and public methods for the DiscreteSlider struct. The getBarPos function calculates the center of the draggable bar region by combining border spacing and half the button size. The getBarSize function computes the available range along the X axis by subtracting borders and the button width from the total slider size, returning a Vec2f with that range and a fixed height (2*border). The mainButtonPressed method first checks if the mouse is over the main button; if so it delegates to the button's handler and records an anchor offset for dragging. If not over the button but over the bar region (computed via getBarPos/getBarSize), it sets an anchor at the left edge of the button, moves the button into that position relative to the mouse, and then calls the button's mainButtonPressed. The mainButtonReleased method simply forwards to the button's released handler with undefined arguments. The render method binds textures and scissor, draws a custom shaded rectangle for the track using Button.pipeline, sets a temporary color (0x80000000) via draw.setColor and restores it later with defer, draws the bar rect at self.pos + getBarPos() sized by getBarSize(), positions and renders the label, and if the button is pressed updates its X position to follow the mouse while clamped between 1.5*border and 1.5*border + getBarSize()[0] - 0.001, then calls updateValueFromButtonPos (declared elsewhere) to reflect the new value; it also temporarily sets translation via draw.setTranslation and restores with defer before rendering the button itself.

## Related Questions
- How does DiscreteSlider compute the draggable bar region for mouse hit testing?
- What is the purpose of getBarPos and how are borders incorporated into its calculation?
- Why does mainButtonPressed check both the button and the bar region separately instead of a single unified test?
- How does the code ensure that dragging the handle stays within valid bounds when updating button position?
- Where is updateValueFromButtonPos invoked in this chunk and what state change does it represent?
- What happens to draw.setColor and draw.restoreColor around the track rendering block?
- Why is translation temporarily set via draw.setTranslation before rendering the button itself?
- How does mainButtonReleased differ from a typical event handler that might perform additional logic?
- Does getBarSize return a fixed height or compute it, and what constant defines that height?
- What effect does the -0.001 offset have in the clamping expression for button position?
- Is texture.bindTo(0) specific to this component or part of a global draw state?
- How are mouse coordinates adjusted relative to self.pos before being passed to button handlers?

*Source: unknown | chunk_id: codebase_src_gui_components_DiscreteSlider.zig_chunk_1*
