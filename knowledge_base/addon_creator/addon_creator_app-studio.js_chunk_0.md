# [hard/addon_creator_app-studio.js] - Chunk 0

**Type:** ui
**Keywords:** UI interactions, dropdowns, checkboxes, dynamic tags, touch settings, interaction logic, visibility toggles, event handlers, form dirty state, UI updates
**Symbols:** handleRotationChange, toggleDropInput, toggleItemIconInput, autoToggleTransparentTag, initDynamicTagSystem, handleSimpleTouchChange, handleSimpleInteractChange
**Concepts:** data-binding, form validation, dynamic UI updates, event handling, conditional rendering

## Summary
The script handles various UI interactions and updates for the addon creation studio, including dropdowns, checkboxes, and dynamic tag systems.

## Explanation
This JavaScript file contains several functions that manage different aspects of the addon creation interface. The `handleRotationChange` function updates multiple UI elements based on a selected value, such as enabling or disabling certain checkboxes and updating dropdown options. Specifically, when 'cubyz:ore' is selected, it checks an item icon checkbox and disables it; for 'cubyz:decayable', it enables several block-related checkboxes and disables the ore allowance checkbox. The `toggleDropInput` function controls the visibility of a custom drop wrapper based on a checkbox state. The `toggleItemIconInput` function toggles the visibility of an item icon wrapper based on a checkbox state. The `initDynamicTagSystem` function initializes a dynamic tagging system where users can add tags to an element, with validation and removal functionality. Tags must be alphanumeric and unique within the container. Other functions like `handleSimpleTouchChange` manage touch settings, setting the touch type to 'hurt' and updating related dropdowns based on the selected value. The `handleSimpleInteractChange` function manages interaction logic settings, showing or hiding specific UI elements based on the selected interaction type.

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
