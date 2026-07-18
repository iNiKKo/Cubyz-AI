# [medium/addon_creator_app-core.js] - Chunk 1

**Type:** ui
**Keywords:** metrics UI, toggle panel, searchable items, mark form dirty, dropdown options, rebuild dropdowns, texture filtering, event listeners, UI updates, form changes
**Symbols:** window.renderMetricsUI, window.toggleMetricsPanel, updateSearchableItems, window.markFormAsDirty, window.renderDropdownOptions, window.rebuildDropdowns
**Concepts:** data-binding, form validation, live preview

## Summary
The `addon_creator_app-core.js` file contains functions for rendering UI components related to metrics, handling form changes, and managing dropdown options in the Cubyz Addon Creator workspace.

## Explanation
This JavaScript file defines several functions that manage various aspects of the user interface within the Cubyz Addon Creator. The `renderMetricsUI` function updates the status panel with metrics information based on the current state. The `toggleMetricsPanel` function toggles the visibility of the metrics panel and updates the UI accordingly. The `updateSearchableItems` function generates a list of searchable items based on project data and server lists. The `markFormAsDirty` function marks the form as having unsaved changes, triggering updates in the sidebar project tree if necessary. The `renderDropdownOptions` function populates dropdown menus with texture options, handling custom textures and filtering based on dropdown type. The `rebuildDropdowns` function rebuilds all dropdowns, setting up event listeners for focus and input events to filter and display options dynamically.

## Related Questions
- What is the purpose of the `renderMetricsUI` function?
- How does the `toggleMetricsPanel` function affect the UI?
- What data is used to populate the searchable items list?
- When is the form marked as dirty, and what happens next?
- How are dropdown options rendered in the UI?
- What events trigger the rebuilding of dropdowns?
- How does texture filtering work in the dropdown menus?
- What is the role of `markFormAsDirty` in the addon creation process?
- How is the metrics panel expanded or collapsed?
- What happens when a user selects an option from a dropdown menu?

*Source: unknown | chunk_id: addon_creator_app-core.js_chunk_1*
