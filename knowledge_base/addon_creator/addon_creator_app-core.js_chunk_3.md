# [medium/addon_creator_app-core.js] - Chunk 3

**Type:** ui
**Keywords:** dropdown, search input, event handling, dynamic filtering, server assets, DOM manipulation, input events, change events, UI components, addon creation
**Symbols:** input, dropdown, opt, filterDropdown, renderDropOptions, showRecipeDropdown
**Concepts:** data-binding, form validation, live preview

## Summary
The chunk manages UI components for dropdowns and search inputs in the addon creator app, including dynamic filtering and event handling.

## Explanation
This JavaScript code snippet is part of the Cubyz Addon Creator workspace. It defines functions to handle dropdown menus and search inputs within the application. The `window.showRecipeDropdown` function populates a dropdown with options based on a given type (e.g., blocks, music) and dispatches input and change events when an option is selected. The `window.filterDropdown` function filters dropdown options based on user input in the corresponding search field. The `window.renderDropOptions` function initializes these components by attaching event listeners to search inputs and creating dropdown elements if they don't exist. The code also includes a `DOMContentLoaded` event listener to load server assets when the document is ready.

## Related Questions
- How does the `showRecipeDropdown` function populate the dropdown options?
- What is the purpose of the `filterDropdown` function in this code?
- How are event listeners attached to search inputs in the `renderDropOptions` function?
- What happens when a user selects an option from the dropdown menu?
- How does the code ensure that the dropdown is displayed only when there are visible options?
- What role do the `DOMContentLoaded` and `input.onfocus` events play in this UI component?
- How is the visibility of dropdown options dynamically controlled based on user input?
- What types of assets are loaded when the document content is fully loaded?
- How does the code handle cases where the search input or dropdown elements do not exist?
- What is the relationship between the `showRecipeDropdown` and `filterDropdown` functions in managing the dropdown UI?

*Source: unknown | chunk_id: addon_creator_app-core.js_chunk_3*
