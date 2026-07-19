# [medium/codebase_src_gui_components_DiscreteSlider.zig] - Chunk 0

**Type:** implementation
**Keywords:** slider UI, discrete values, button drag, memory allocation, deinitialization
**Symbols:** DiscreteSlider, DiscreteSlider.border, DiscreteSlider.fontSize, DiscreteSlider.texture, DiscreteSlider.pos, DiscreteSlider.size, DiscreteSlider.callback, DiscreteSlider.currentSelection, DiscreteSlider.text, DiscreteSlider.currentText, DiscreteSlider.values, DiscreteSlider.label, DiscreteSlider.button, DiscreteSlider.mouseAnchor, DiscreteSlider.globalInit, DiscreteSlider.globalDeinit, DiscreteSlider.init, DiscreteSlider.deinit, DiscreteSlider.toComponent, DiscreteSlider.setButtonPosFromValue, DiscreteSlider.updateLabel, DiscreteSlider.updateValueFromButtonPos, DiscreteSlider.updateHovered, DiscreteSlider.getBarPos, DiscreteSlider.getBarSize, DiscreteSlider.mainButtonPressed
**Concepts:** GUI component, discrete value selection, user interaction, memory management

## Summary
The DiscreteSlider component manages a slider UI element with discrete values. It includes methods for initializing and deinitializing the slider, updating its state based on user interactions, and rendering it. The slider consists of a button that can be dragged along a bar to select different values from a predefined list. The component also handles memory allocation and deallocation for internal data structures such as text buffers and value lists.

## Explanation
This chunk defines the DiscreteSlider struct, which represents a GUI component for selecting discrete values. It includes methods for initializing and deinitializing the slider, updating its state based on user interactions, and rendering it. The slider consists of a button that can be dragged along a bar to select different values from a predefined list. The component also manages memory allocation and deallocation for internal data structures such as text buffers and value lists.

The DiscreteSlider struct has several fields including `border` (3), `fontSize` (16), `texture`, `pos`, `size`, `callback`, `currentSelection`, `text`, `currentText`, `values`, `label`, `button`, and `mouseAnchor`. The `globalInit()` method initializes the texture from a file, while `globalDeinit()` deinitializes it. The `init()` method sets up the slider with given parameters such as position, width, text, format string for values, initial value, and callback function. It also allocates memory for internal data structures like labels and buttons.

The `deinit()` method frees allocated memory and destroys the DiscreteSlider instance. The `toComponent()` method converts the slider to a GUI component. Methods such as `setButtonPosFromValue()`, `updateLabel()`, `updateValueFromButtonPos()`, `updateHovered()`, `getBarPos()`, `getBarSize()`, and `mainButtonPressed()` handle updating the button position, label text based on selection, value updates from button positions, hover detection, bar positioning, bar sizing, and main button press events respectively.

The specific numerical constants used in DiscreteSlider are `border` (3) and `fontSize` (16). The `init()` method sets up the slider by allocating memory for internal data structures like labels and buttons. It also formats the values based on the provided format string and initializes the label with the initial text and value.

The exact process for updating the label text based on current selection involves freeing the previous currentText, creating a new one that combines the static text with the selected value, and then initializing a new Label instance with this combined text. The callback function gets triggered in DiscreteSlider when the user selects a different value by dragging the button or clicking on the bar.

## Code Example
```zig
pub fn globalInit() void {
	texture = Texture.initFromFile("assets/cubyz/ui/slider.png");
}
```

## Related Questions
- What are the specific numerical constants used in DiscreteSlider (e.g., border width, font size)?
- How does the `init()` method set up the slider with given parameters?
- What is the exact process for updating the label text based on current selection?
- How does memory management work for internal data structures like labels and buttons?
- Under what conditions does the callback function get triggered in DiscreteSlider?

*Source: unknown | chunk_id: codebase_src_gui_components_DiscreteSlider.zig_chunk_0*
