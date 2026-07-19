# [hard/addon_creator_app-save.js] - Chunk 0

**Type:** ui
**Keywords:** saveBlockToProject, block data, input validation, project update, rotation mode, interaction type
**Symbols:** showDropdown, saveBlockToProject, blockId, tSearch, rotationMode, itemIconSearch, sidesData, interactMode, blockData, window.projectData.blocks, window.editingId, window.currentPanelName
**Concepts:** data-binding, form validation, project state management

## Summary
The `saveBlockToProject` function handles saving block data to the project, validating inputs, and updating project state.

## Explanation
**Explanation**

The `saveBlockToProject` function handles saving block data to the project by collecting input values from HTML elements, validating them, constructing a block data object, and updating the project's internal state. It ensures that all required fields are filled out correctly before proceeding with the save operation.

- **Input Collection**: The function collects various input values such as `blockId`, `tSearch` (base texture), `rotationMode`, `itemIconSearch`, and side textures (`front`, `left`, `right`, `up`, `bottom`, `back`). It also handles optional fields like `interactMode`.

- **Validation**: The function validates input fields to ensure that the block ID and base texture are provided. For the 'cubyz:ore' rotation mode, it checks if an item icon search is specified. Numeric fields such as friction, bounciness, density, terminal velocity, mobility, emitted light, and absorbed light are validated and converted to appropriate types.

- **Block Data Construction**: The function constructs a `blockData` object with various properties including `id`, `subFolder`, `health`, `resistance`, `rotation`, collision settings (`collide`, `transparent`, `replaceable`, `degradable`, `viewThrough`, `alwaysViewThrough`, `hasBackFace`, `allowOres`), physical properties (`friction`, `bounciness`, `density`, `terminalVelocity`, `mobility`), light properties (`emittedLightColor`, `absorbedLightColor`, `emittedLight`, `absorbedLight`), tags, drop settings (`dropAuto`, `dropSearch`), item icon settings (`hasItemIcon`, `itemIconSearch`), base texture (`baseTexture`), and callbacks for interaction types like 'open_chest'.

- **Project State Update**: The function updates the project's internal state by filtering out existing blocks with the same ID, adding the new block data to `window.projectData.blocks`, and resetting relevant window properties (`hasUnsavedChanges`, `editingId`, `currentPanelName`). It also calls functions to update searchable items and the sidebar project tree.

- **Rotation Modes**: The function supports various rotation modes such as 'cubyz:stairs' and 'cubyz:ore', each with specific requirements (e.g., item icon for 'cubyz:ore').

- **Interaction Types**: Interaction types like 'open_chest' are handled by adding a `blockEntity` property to the block data object.

- **Numeric Fields Validation**: Numeric fields such as friction, bounciness, density, terminal velocity, and mobility are validated and converted to floating-point numbers. The emitted light and absorbed light values are converted from hexadecimal color codes to integers.

- **Duplicate Block IDs**: The function ensures that no duplicate block IDs exist in the project by filtering out existing blocks with the same ID before adding the new block data.

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
