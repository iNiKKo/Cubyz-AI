# [hard/addon_creator_app-studio.js] - Chunk 6

**Type:** ui
**Keywords:** dropdown, filtering, form-generation, Cubyz-blocks, texture-select, clear-button, mark-dirty, project-data, server-textures, input-handling
**Symbols:** createInputHTML, createNormalInputHTML, showRecipeDropdown, filterDropdown, initDropdownClearButtons, updateClearButtonVisibility, markFormAsDirty, updateBlockFacePreviews
**Concepts:** dynamic form generation, dropdown filtering, clear-button visibility toggle, data binding to Cubyz block IDs, event-driven UI updates

## Summary
This module handles the dynamic generation of UI forms for various Cubyz addon types (e.g., vegetation, boulders) and provides reusable dropdown logic with filtering and clear-button management.

## Explanation
UI Controls: createInputHTML / createNormalInputHTML generate form fields bound to data properties; showRecipeDropdown populates a select from projectData.blocks/items or serverTextures; filterDropdown filters options by text. Event Handlers: input listeners call markFormAsDirty (guarded by isInitializingPanel); mouseup triggers updateBlockFacePreviews and initDropdownClearButtons; mousedown outside texture-select-wrapper hides open dropdowns. Validation/Defaults: defaults are passed as third arguments to create*HTML functions (e.g., '6' for height). Templates: none explicitly defined here, but HTML strings are injected via innerHTML. Bindings: data?.log → field-log with default 'cubyz:oak_log'; data?.block → field-block; etc. Engine Mappings: Cubyz block IDs (cubyz:oak_log, cubyz:fern) map to UI inputs. Configuration Generation: showRecipeDropdown builds a pool of selectable items and renders them as clickable divs inside the dropdown container.

## Related Questions
- What happens when a user types into a texture-select input field?
- How are custom project blocks added to the dropdown options?
- Which Cubyz block IDs are used as defaults for vegetation addons?
- Why is markFormAsDirty guarded by window.isInitializingPanel?
- What triggers updateBlockFacePreviews and when does it run?
- How does filterDropdown handle case-insensitive search queries?
- Where are the clear-input-btn elements inserted in the DOM?
- Can a user select a vanilla texture from serverTextures via this dropdown?
- What prevents multiple dropdowns from staying open simultaneously?
- Are any validation rules enforced on numeric inputs like height or width?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_6*
