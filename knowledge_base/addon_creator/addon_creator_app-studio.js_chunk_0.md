# [hard/addon_creator_app-studio.js] - Chunk 0

**Type:** ui
**Keywords:** UI interactions, dropdowns, checkboxes, dynamic tags, touch settings, interaction logic, visibility toggles, event handlers, form dirty state, UI updates
**Symbols:** handleRotationChange, toggleDropInput, toggleItemIconInput, autoToggleTransparentTag, initDynamicTagSystem, handleSimpleTouchChange, handleSimpleInteractChange
**Concepts:** data-binding, form validation, dynamic UI updates, event handling, conditional rendering

## Summary
The script handles various UI interactions and updates for the addon creation studio, including dropdowns, checkboxes, and dynamic tag systems.

## Explanation
**Explanation**

This JavaScript file contains several functions that manage different aspects of the addon creation interface. The `handleRotationChange` function updates multiple UI elements based on a selected value, such as enabling or disabling certain checkboxes and updating dropdown options. Specifically, when 'cubyz:ore' is selected, it checks an item icon checkbox and disables it; for 'cubyz:decayable', it enables several block-related checkboxes (blockTransparent, blockDegradable, blockViewThrough, blockAlwaysViewThrough, blockHasBackFace) and disables the ore allowance checkbox. When 'cubyz:stairs' is selected, it disables all block-related checkboxes and sets the ore allowance checkbox based on whether the value is 'cubyz:ore'. The `toggleDropInput` function controls the visibility of a custom drop wrapper based on a checkbox state. The `toggleItemIconInput` function toggles the visibility of an item icon wrapper based on a checkbox state. The `initDynamicTagSystem` function initializes a dynamic tagging system where users can add tags to an element, with validation and removal functionality. Tags must be alphanumeric and unique within the container.

The `autoToggleTransparentTag` function is responsible for automatically toggling the transparent tag based on certain conditions (not detailed in the provided script).

Other functions like `handleSimpleTouchChange` manage touch settings, setting the touch type to 'hurt' and updating related dropdowns based on the selected value ('none', 'support', 'decay', 'vine_decay'). The `handleSimpleInteractChange` function manages interaction logic settings, showing or hiding specific UI elements based on the selected interaction type ('open_window').

**Specific Details:**
- **Dropdown Options for Different Block Types:*
  - For 'cubyz:stairs' or 'cubyz:ore' or 'cubyz:direction': Adds options 'none' (Default) and 'support' (Breaks if ground below is gone).
  - For 'cubyz:decayable': Adds options 'decay' (Decays into air if away from logs) and 'none' (Default).
  - For 'cubyz:hanging': Adds options 'vine_decay' (Breaks if ceiling disappears) and 'none' (Default).
  - For 'cubyz:carpet': Adds options 'support' (Breaks if ground below is gone) and 'none' (Default).
  - For other values: Adds options 'none' (Default) and 'support' (Breaks if ground below is gone).

- **Touch Settings Management:**
  - When the value is 'none', sets `rawTouch.value` to 'none' and hides the settings sub-container.
  - When the value is not 'none', sets `rawTouch.value` to 'hurt', updates `rawMode.value` based on the selected value, shows the settings sub-container, and sets the variant dropdown (`variantDropdown`) to 'heal' if the value is 'heal', otherwise to 'heat'.

- **UI Elements Affected by `handleSimpleInteractChange`:*
  - Shows or hides the advanced interaction window wrapper based on whether the selected interaction type is 'open_window'.

**Event Handlers:**
- `window.handleRotationChange`
- `window.toggleDropInput`
- `window.toggleItemIconInput`
- `window.autoToggleTransparentTag`
- `window.initDynamicTagSystem`
- `window.handleSimpleTouchChange`
- `window.handleSimpleInteractChange`

## Related Questions
- What does the `handleRotationChange` function do?
- How does the `toggleDropInput` function affect the UI?
- What is the purpose of the `initDynamicTagSystem` function?
- How are touch settings managed in this script?
- What happens when a user selects 'cubyz:decayable' in the rotation dropdown?
- How does the dynamic tag system handle invalid tags?
- What UI elements are affected by the `handleSimpleInteractChange` function?
- How is the visibility of specific input sections controlled?
- What event handlers are defined for managing touch and interaction settings?
- How does the script ensure that form changes are marked as dirty?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_0*
