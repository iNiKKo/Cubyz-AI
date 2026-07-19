# [medium/addon_creator_app-core.js] - Chunk 1

**Type:** ui
**Keywords:** metrics UI, toggle panel, searchable items, mark form dirty, dropdown options, rebuild dropdowns, texture filtering, event listeners, UI updates, form changes
**Symbols:** window.renderMetricsUI, window.toggleMetricsPanel, updateSearchableItems, window.markFormAsDirty, window.renderDropdownOptions, window.rebuildDropdowns
**Concepts:** data-binding, form validation, live preview

## Summary
The `addon_creator_app-core.js` file contains functions for rendering UI components related to metrics, handling form changes, and managing dropdown options in the Cubyz Addon Creator workspace.

## Explanation
The `addon_creator_app-core.js` file contains several functions that manage various aspects of the UI in the Cubyz Addon Creator. The `renderMetricsUI` function updates the status panel with metrics information based on the current state. When the metrics panel is expanded (`window.metricsExpandedState` is true), it displays specific counts for blocks, items, block textures, item textures, music, entities, and particles. For example, if `window.metricCounts.blocks` is 100, it will display 'Blocks: 100'. The `toggleMetricsPanel` function toggles the visibility of the metrics panel by expanding or collapsing it and updating the UI accordingly. The `updateSearchableItems` function generates a list of searchable items based on project data and server lists, including custom blocks and items derived from an addon name. For instance, if the addon name is 'my_addon' and there are two blocks with IDs 'block1' and 'block2', it will include 'my_addon:block1' and 'my_addon:block2' in the list. The `markFormAsDirty` function marks the form as having unsaved changes, triggering updates in the sidebar project tree if necessary. The `renderDropdownOptions` function populates dropdown menus with texture options, handling custom textures and filtering based on dropdown type (block, item, or particle). For example, if the dropdown ID starts with 'item', it will filter textures to include only items. The `rebuildDropdowns` function rebuilds all dropdowns, setting up event listeners for focus and input events to filter and display options dynamically. When a user selects an option from a dropdown menu, the selected texture name is set in the corresponding search input, and the dropdown is hidden. Texture filtering works by updating the displayed options based on the user's input in the search field.

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
