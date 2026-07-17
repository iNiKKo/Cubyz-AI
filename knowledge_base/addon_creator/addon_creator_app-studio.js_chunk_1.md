# [hard/addon_creator_app-studio.js] - Chunk 1

**Type:** ui
**Keywords:** studio panel, nav buttons, fetch template, tag pill system, dirty flag, custom confirm modal, dropdown rebuild, input change handler, decay settings toggle, populate form values
**Symbols:** loadStudioPanel, showCustomConfirm, handleSimpleInteractChange, handleSimpleEnvChange, addDynamicTagPill, removeDynamicTagPill, updateTagSuggestionVisibility, initDynamicTagSystem
**Concepts:** panel navigation, template loading, dynamic tag pills, form dirty tracking, modal confirmation, dropdown rebuilding, event delegation on inputs

## Summary
This chunk defines the core panel-loading logic for the Cubyz Addon Studio, handling navigation between blocks/items/recipes/etc., fetching HTML templates, rebuilding dropdowns, and initializing dynamic tag systems.

## Explanation
UI Controls: nav-btn buttons (active state), customConfirmModal dialog with OK/Cancel, dynamicWorkspace container for injected HTML. Event Handlers: loadStudioPanel triggers fetch of panelName.html, rebuildDropdowns on blocks/items/entities/particles panels, markFormAsDirty on any input/change except ID fields, initDynamicTagSystem calls for blockTagsContainer/itemTagsContainer/entityTagsContainer. Validation: showCustomConfirm returns Promise resolving true/false; handleSimpleInteractChange/handleSimpleEnvChange map user-select values to raw inputs and toggle visibility of advanced sub-forms (advInteractWindowWrapper/simpleDecaySettings). Defaults: decayReplacement defaults to 'cubyz:air' when updateType is 'decay'; decayPrevention defaults to '.log, .branch'. Templates: dynamicWorkspace.innerHTML replaced by fetched HTML; dropdowns regenerated via rebuildDropdowns. Bindings: Object.assign sets hasUnsavedChanges=false, currentPanelName=panelName, editingId=targetIdToEdit; funcMap maps panelName to populate*FormValues functions. Engine Mappings: none explicit here—pure DOM manipulation and fetch. Configuration Generation: none in this chunk.

## Related Questions
- What happens when a user clicks a nav-btn for the 'blocks' panel while unsaved changes exist?
- How does loadStudioPanel prevent duplicate dropdown generation after fetching a new panel template?
- Which DOM elements are excluded from triggering markFormAsDirty on input/change events, and why?
- In handleSimpleEnvChange, what rawUpdate value is assigned when the user selects 'support' for decay type?
- How does addDynamicTagPill ensure that duplicate tag pills are not added to a container?
- What is the purpose of updateTagSuggestionVisibility after removing or adding a dynamic tag pill?
- When loadStudioPanel receives a targetIdToEdit, how are existing form values populated into the newly loaded template?
- Which panels trigger rebuildDropdowns automatically after their HTML is injected into dynamicWorkspace?
- What default replacement string is set for decayReplacement when updateType equals 'decay'?
- How does showCustomConfirm handle the case where its modal element (#customConfirmModal) is missing from the DOM?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_1*
