# [medium/addon_creator_app-core.js] - Chunk 2

**Type:** ui
**Keywords:** projectData, deleteItemFromProject, updateSidebarProjectTree, filterDropdown, showRecipeDropdown, loadStudioPanel, unsavedChanges, sidebarTree, dropdown-options, asset management
**Symbols:** window.deletedAddonElements, window.updateSidebarProjectTree, window.deleteItemFromProject, window.showRecipeDropdown, window.filterDropdown
**Concepts:** sidebar tree rendering, asset deletion with confirmation, dropdown filtering and search, unsaved changes indicator, dynamic DOM manipulation

## Summary
This module defines the core UI logic for managing project assets (blocks, items, recipes, etc.) in the sidebar tree view and provides dropdown filtering/searching functionality.

## Explanation
UI Controls: The code exposes several global functions that manipulate the DOM. window.updateSidebarProjectTree() dynamically renders lists of saved assets into specific sidebar containers identified by IDs like 'sidebarBlocksTree', 'sidebarItemsTree', etc., handling both empty states and populated lists with delete buttons. It also conditionally appends an unsaved changes indicator if the current panel matches the asset type.

Event Handlers: The updateSidebarProjectTree function attaches onclick handlers to individual list items that call window.loadStudioPanel() to load a specific asset into the editor, and calls window.deleteItemFromProject() for removal. Delete buttons also have onmouseover/onmouseout events to toggle their color state.

Validation/Defaults: The delete operation uses window.showCustomConfirm() (an external dependency) to validate user intent before modifying window.projectData arrays or objects. It tracks deleted IDs in window.deletedAddonElements and clears the editingId if a deletion occurs while an item is being edited, setting hasUnsavedChanges to false.

Templates: No explicit HTML templates are defined; instead, innerHTML is used with string interpolation for dynamic content generation (e.g., adding subfolder indicators).

Engine Mappings: The code maps asset categories ('blocks', 'items', 'recipes', etc.) to specific DOM containers and data structures in window.projectData.

Configuration Generation: This chunk does not generate configuration files; it manipulates the runtime state of the application.

## Related Questions
- What happens to the editingId when an asset is deleted while it is currently being edited?
- How does the updateSidebarProjectTree function handle empty project data lists versus populated ones?
- Which DOM element IDs are targeted by the updateSidebarProjectTree function for rendering different asset categories?
- Does the deleteItemFromProject function modify window.projectData directly, and how does it track deleted items?
- What is the purpose of the showCustomConfirm call within the deleteItemFromProject function?
- How does the filterDropdown function determine which dropdown options to display based on user input?
- In what way does the code handle unsaved changes when an asset is deleted from the project data?
- Are there any specific event handlers attached to the delete buttons in the sidebar tree rows, and how do they behave on hover?
- What logic is used to construct the validationItems array inside showRecipeDropdown for different filter types like blocks or textures?
- How does the code ensure that deleting an asset stops propagation of events when clicking a delete button?

*Source: unknown | chunk_id: addon_creator_app-core.js_chunk_2*
