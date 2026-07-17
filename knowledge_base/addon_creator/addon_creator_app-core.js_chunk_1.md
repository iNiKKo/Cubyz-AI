# [medium/addon_creator_app-core.js] - Chunk 1

**Type:** ui
**Keywords:** metrics display, dropdown options, form changes, sidebar project tree, server database metrics, searchable items, texture options, unsaved changes, UI components, event handlers
**Symbols:** loadServerAssets, renderMetricsUI, toggleMetricsPanel, updateSearchableItems, markFormAsDirty, renderDropdownOptions, rebuildDropdowns, deletedAddonElements, updateSidebarProjectTree
**Concepts:** data-binding, form validation, live preview, UI rendering, event handling

## Summary
The chunk implements UI rendering and interaction for displaying server metrics, updating dropdown options, marking form changes as dirty, and rebuilding sidebar project trees.

## Explanation
This JavaScript code snippet is part of the Cubyz Addon Creator workspace. It defines several functions and event handlers related to UI components such as metrics display, dropdowns, and form validation. The `renderMetricsUI` function updates the status container with server database metrics based on the expanded state. The `toggleMetricsPanel` function toggles the visibility of the metrics panel. The `updateSearchableItems` function generates a list of searchable items based on project data. The `markFormAsDirty` function marks the form as having unsaved changes. The `renderDropdownOptions` function populates dropdowns with texture options, and `rebuildDropdowns` rebuilds all relevant dropdowns. The `updateSidebarProjectTree` function updates the sidebar tree view for different project elements like blocks, items, biomes, entities, and particles.

## Related Questions
- What function is responsible for updating the server metrics UI?
- How does the `toggleMetricsPanel` function affect the UI?
- What items are included in the searchable items list?
- When is the form marked as dirty?
- How are dropdown options populated and filtered?
- What elements are updated in the sidebar project tree?
- How does the code handle errors when loading server assets?
- What CSS classes are used to style the status container?
- How are custom block and item IDs generated?
- What is the purpose of the `deletedAddonElements` object?

*Source: unknown | chunk_id: addon_creator_app-core.js_chunk_1*
