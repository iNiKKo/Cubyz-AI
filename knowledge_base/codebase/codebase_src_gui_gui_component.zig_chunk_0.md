# [easy/codebase_src_gui_gui_component.zig] - Chunk 0

**Type:** api
**Keywords:** union, method delegation, component-based architecture, switch statement, inline else, position and size handling, mouse interaction, rendering
**Symbols:** GuiComponent, GuiComponent.BagSlot, GuiComponent.Button, GuiComponent.CheckBox, GuiComponent.HorizontalList, GuiComponent.Icon, GuiComponent.ItemSlot, GuiComponent.Label, GuiComponent.MutexComponent, GuiComponent.ScrollBar, GuiComponent.ContinuousSlider, GuiComponent.DiscreteSlider, GuiComponent.TextInput, GuiComponent.VerticalList, GuiComponent.bagSlot, GuiComponent.button, GuiComponent.checkBox, GuiComponent.horizontalList, GuiComponent.icon, GuiComponent.itemSlot, GuiComponent.label, GuiComponent.mutexComponent, GuiComponent.scrollBar, GuiComponent.continuousSlider, GuiComponent.discreteSlider, GuiComponent.textInput, GuiComponent.verticalList, GuiComponent.deinit, GuiComponent.mutPos, GuiComponent.mutSize, GuiComponent.pos, GuiComponent.size, GuiComponent.updateSelected, GuiComponent.updateHovered, GuiComponent.render, GuiComponent.mainButtonPressed, GuiComponent.mainButtonReleased, GuiComponent.contains, BagSlot, Button, CheckBox, HorizontalList, Icon, ItemSlot, Label, MutexComponent, ScrollBar, ContinuousSlider, DiscreteSlider, TextInput, VerticalList
**Concepts:** GUI component management, polymorphic behavior through union, method delegation based on component type

## Summary
Defines a union of GUI components with common methods for initialization, position, size, rendering, and interaction handling.

## Explanation
The `GuiComponent` union in this chunk encapsulates 13 component types: `BagSlot`, `Button`, `CheckBox`, `HorizontalList`, `Icon`, `ItemSlot`, `Label`, `MutexComponent`, `ScrollBar`, `ContinuousSlider`, `DiscreteSlider`, `TextInput`, and `VerticalList`. Each component type is imported from its respective file within the 'components' directory. The union provides a common interface for these components through methods like deinitialization (`deinit`), getting or setting position and size (`mutPos`, `mutSize`, `pos`, `size`), updating selection state (`updateSelected`), handling mouse hover events (`updateHovered`), rendering (`render`), and responding to button presses (`mainButtonPressed`, `mainButtonReleased`). The methods use a switch statement with an inline else clause to delegate calls to the appropriate component's method if it exists. Additionally, a static method `contains` is provided to check if a point lies within a given rectangle defined by position and size.

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
- What are the different types of GUI components defined in this chunk?
- How does the `GuiComponent` union handle method calls for each component type?
- What is the purpose of the `deinit` method in the `GuiComponent` union?
- How does the `contains` static method work in this chunk?
- Which methods in the `GuiComponent` union are responsible for handling mouse interactions?
- What is the role of the `switch` statement with an inline else clause in the methods of the `GuiComponent` union?

*Source: unknown | chunk_id: codebase_src_gui_gui_component.zig_chunk_0*
