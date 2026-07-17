# [easy/codebase_src_gui_gui_component.zig] - Chunk 0

**Type:** implementation
**Keywords:** union, pointer, switch, delegate, method, pointers, rectangle, boolean
**Symbols:** GuiComponent, BagSlot, Button, CheckBox, HorizontalList, Icon, ItemSlot, Label, MutexComponent, ScrollBar, ContinuousSlider, DiscreteSlider, TextInput, VerticalList, GuiComponent.deinit, GuiComponent.mutPos, GuiComponent.mutSize, GuiComponent.pos, GuiComponent.size, GuiComponent.updateSelected, GuiComponent.updateHovered, GuiComponent.render, GuiComponent.mainButtonPressed, GuiComponent.mainButtonReleased, GuiComponent.contains
**Concepts:** GUI components, deinitialization, position and size manipulation, event handling, rendering

## Summary
Defines a union of different GUI component types with methods for deinitialization, position and size manipulation, updating selection and hover state, rendering, and handling mouse button events.

## Explanation
The `GuiComponent` union in the Cubyz engine's GUI system represents various UI components such as buttons, labels, and sliders. Each variant of the union corresponds to a specific type of component, storing a pointer to an instance of that component. The union provides methods for common operations like deinitialization (`deinit`), updating selection (`updateSelected`), handling mouse hover events (`updateHovered`), rendering (`render`), and responding to mouse button presses (`mainButtonPressed` and `mainButtonReleased`). These methods delegate to the appropriate implementation based on the variant of the union. Additionally, there's a static method `contains` that checks if a point is within a given rectangle.

## Code Example
```zig
pub fn deinit(self: GuiComponent) void {
	switch (self) {
		inline else => |impl| {
			if (@hasDecl(@TypeOf(impl.*), "deinit")) {
				impl.deinit();
			}
		},
	}
}
```

## Related Questions
- What is the purpose of the `GuiComponent` union?
- How are different GUI components handled within the `GuiComponent` union?
- What methods are available for updating the state of a GUI component?
- How does the `contains` method determine if a point is within a rectangle?
- Which methods delegate to the appropriate implementation based on the variant of the union?
- What happens when calling `deinit` on a `GuiComponent` that has a custom deinitialization method?

*Source: unknown | chunk_id: codebase_src_gui_gui_component.zig_chunk_0*
