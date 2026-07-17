# [hard/addon_creator_app-save.js] - Chunk 0

**Type:** ui
**Keywords:** block-save, item-save, validation, dropdowns, callbacks, material-stats, HSL-conversion, project-data, checkboxes, text-inputs
**Symbols:** function showDropdown, function saveBlockToProject, function saveItemToProject, window.dropdownsGenerated, window.rebuildDropdowns, window.filterDropdown, window.projectData.blocks, window.projectData.items, window.editingId, window.hasUnsavedChanges, window.updateSearchableItems, window.updateSidebarProjectTree
**Concepts:** data-binding, form-validation, state-management, object-construction, color-space-conversion

## Summary
This module defines the core save logic for both blocks and items within the Cubyz Addon Creator. It gathers values from various form inputs, validates them (e.g., requiring a block ID or texture), constructs detailed data objects with properties like rotation mode, health, callbacks, and material stats, then updates the global `window.projectData` state and triggers UI refresh functions.

## Explanation
UI Controls: Multiple text inputs (blockId, topSearch, itemTextureSearch, itemId, matColorBase), checkboxes (dropAuto, hasItemIcon, blockCollide, etc.), select dropdowns (rotationMode, touchType, decayReplacement), and numeric inputs (friction, bounciness). Event Handlers: Functions `saveBlockToProject` and `saveItemToProject` are bound to window-level events; they read DOM values via `document.getElementById`. Validation: Block save requires non-empty blockId and topSearch; ore rotation requires itemIconSearch. Item save requires itemId and texture; base color parsing includes HSL conversion logic. Defaults: Missing numeric fields default to 0 or specific constants (e.g., friction 20, emittedLightColor '#000000'). Templates: None explicitly defined here; data is assembled into objects using spread operators for optional properties like `blockEntity`. Bindings: All inputs are bound directly via DOM queries. Engine Mappings: Data structures align with Cubyz block/item schema (e.g., sides, callbacks, material). Configuration Generation: Produces `window.projectData.blocks` and `window.projectData.items` arrays.

## Related Questions
- What happens if a user saves a block without specifying a Block ID?
- How does the system handle missing textures for procedural world ores?
- Which DOM elements are queried to populate the `sidesData` object in saveBlockToProject?
- What is the default value assigned to `friction` when the input field is empty?
- How does the item save function convert the base color hex string into HSL values?
- Are there any optional properties added conditionally during block or item saving, and what triggers them?
- Which global state flags are reset after a successful save operation?
- What UI refresh functions are called immediately after updating `window.projectData`?
- How does the code ensure that duplicate IDs (e.g., editingId) do not persist in the project data arrays?
- Is there any validation for numeric inputs like `blockHealth` or `matDurability`, and what defaults apply if they are missing?

*Source: unknown | chunk_id: addon_creator_app-save.js_chunk_0*
