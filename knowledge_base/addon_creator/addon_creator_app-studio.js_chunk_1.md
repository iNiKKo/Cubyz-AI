# [hard/addon_creator_app-studio.js] - Chunk 1

**Type:** ui
**Keywords:** environment change, dynamic tags, custom confirmation, UI interactions, tag management, modal dialog, form elements, event handling
**Symbols:** handleSimpleEnvChange, addDynamicTagPill, removeDynamicTagPill, updateTagSuggestionVisibility, showCustomConfirm
**Concepts:** data-binding, form validation, dynamic UI components, user interaction handling

## Summary
This chunk defines several functions for handling UI interactions in the Cubyz Addon Creator, including environment change handling, dynamic tag management, and custom confirmation dialogs.

## Explanation
**Explanation**

This chunk defines several functions for handling UI interactions in the Cubyz Addon Creator, including environment change handling, dynamic tag management, and custom confirmation dialogs.

- **handleSimpleEnvChange**: This function manages changes to environment settings. If `val` is 'none' or 'support', it sets `rawUpdate.value` to 'none' or 'checkSupportBlocks' respectively and hides the decay sub-settings (`decaySub`). For other values, it sets `rawUpdate.value` to `val` and shows/hides the decay sub-settings based on whether `val` is 'decay'. If `val` is 'decay', it sets `decayReplacement` to 'cubyz:air' and `decayPrevention` to '.log, .branch'. It also marks the form as dirty if not initializing.

- **addDynamicTagPill**: This function adds a dynamic tag pill to a container. It trims, lowercases, and cleans the tag input, checks for duplicates, creates a styled pill element with a remove button, and appends it to the container. The pill's removal event handler removes the pill, updates tag suggestion visibility, and marks the form as dirty.

- **removeDynamicTagPill**: This function removes a dynamic tag pill from a container based on the cleaned tag input.

- **updateTagSuggestionVisibility**: This function controls the display of buttons in a form group. It checks if active tags include certain values and hides or shows corresponding buttons accordingly.

- **showCustomConfirm**: This function provides a custom modal dialog for user confirmation. It sets the title and message, displays the modal, and resolves a promise based on user action (OK or Cancel).

## Related Questions
-  What does the `handleSimpleEnvChange` function do when `val` is 'decay'?
-  How are dynamic tags cleaned before being added to the UI?
-  What specific values are set for `decayReplacement` and `decayPrevention` when `val` is 'decay'?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_1*
