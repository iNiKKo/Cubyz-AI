# [hard/addon_creator_app-save.js] - Chunk 0

**Type:** ui
**Keywords:** saveBlockToProject, block data, input validation, project update, rotation mode, interaction type
**Symbols:** showDropdown, saveBlockToProject, blockId, tSearch, rotationMode, itemIconSearch, sidesData, interactMode, blockData, window.projectData.blocks, window.editingId, window.currentPanelName
**Concepts:** data-binding, form validation, project state management

## Summary
The `saveBlockToProject` function handles saving block data to the project, validating inputs, and updating project state.

## Explanation
This JavaScript code snippet defines a function `saveBlockToProject` that is responsible for saving block data into a project. It collects various input values from HTML elements, validates them, constructs a block data object, and updates the project's internal state. The function ensures that all required fields are filled out correctly before proceeding with the save operation. It also handles optional fields and specific conditions based on the selected rotation mode and interaction type.

## Related Questions
- What is the purpose of the `showDropdown` function?
- How does the `saveBlockToProject` function validate input fields?
- What happens if the required block ID or base texture is not provided?
- How are optional fields handled in the `saveBlockToProject` function?
- What specific conditions are checked for the 'cubyz:ore' rotation mode?
- How does the function update the project's internal state after saving a block?
- What is the role of the `window.projectData.blocks` array in this code?
- How are interaction types like 'open_chest' handled in the block data object?
- What validation is performed on numeric fields such as friction and bounciness?
- How does the function ensure that no duplicate block IDs exist in the project?

*Source: unknown | chunk_id: addon_creator_app-save.js_chunk_0*
