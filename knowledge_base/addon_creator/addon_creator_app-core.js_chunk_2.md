# [medium/addon_creator_app-core.js] - Chunk 2

**Type:** ui
**Keywords:** sidebar, project tree, item deletion, recipe management, dropdown, filtering, unsaved changes, dynamic UI update
**Symbols:** deletedAddonElements, updateSidebarProjectTree, loadStudioPanel, deleteItemFromProject, showCustomConfirm, showRecipeDropdown, filterDropdown
**Concepts:** data-binding, form validation, live preview, event handling

## Summary
The script manages the sidebar project tree UI, handling item deletion and recipe management.

## Explanation
This JavaScript file contains functions to manage the sidebar project tree UI in an addon creation application. The `updateSidebarProjectTree` function dynamically updates the sidebar with project data for blocks, items, biomes, entities, particles, and recipes. If no saved elements exist, it displays a placeholder message indicating 'None saved yet'. For each category, it maps over the project data to create clickable rows in the sidebar tree, displaying element IDs and providing options to delete them. The function also marks unsaved changes by highlighting the current item being edited with a special border color and text.

The `deleteItemFromProject` function handles the deletion of items from the project after confirming with the user via a custom confirmation dialog. It removes the specified item from the relevant project data object (e.g., blocks, items, recipes) and tracks deleted elements in the `deletedAddonElements` object for undo functionality or logging purposes.

The `showRecipeDropdown` function manages dropdown menus specifically for recipe elements, filtering options based on user input to provide a dynamic selection experience. It filters validation items based on the type of element (blocks, music, models, textures) and populates the dropdown with relevant options. The `filterDropdown` function then filters these options based on user input in real-time.

The script ensures that deleted items are tracked by updating the `deletedAddonElements` object whenever an item is deleted from the project data. If a user confirms the deletion of an asset, the UI updates to reflect the removal and highlights the current item being edited with a special border color and text if applicable.

## Related Questions
- What are the exact steps taken by `updateSidebarProjectTree` when updating the sidebar with project data?
- How does `deleteItemFromProject` handle tracking deleted items in the `deletedAddonElements` object?
- Can you explain how `showRecipeDropdown` filters dropdown options based on different types of elements (blocks, music, models, textures)?
- What happens to the UI when an item is marked as having unsaved changes?

*Source: unknown | chunk_id: addon_creator_app-core.js_chunk_2*
