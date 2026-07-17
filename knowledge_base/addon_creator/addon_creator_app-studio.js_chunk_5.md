# [hard/addon_creator_app-studio.js] - Chunk 5

**Type:** ui
**Keywords:** structure row, feature type selector, spawn chance, dropdown focus trigger, sub-field injection, filter on input, mark form dirty, readonly search field, hidden value binding, clear button wrapper
**Symbols:** window.addStructureRow, window.toggleStructSubFields, window.initDropdownClearButtons, displayLabels, createInputHTML, createNormalInputHTML
**Concepts:** dynamic form generation, type-specific sub-fields, searchable dropdowns with focus trigger, live filtering on input, form dirty state tracking, hidden value binding to visible search, UI event delegation via inline handlers

## Summary
This chunk defines the core UI logic for adding and configuring biome structure rows, including dynamic sub-field toggling based on selected feature type.

## Explanation
The code implements window.addStructureRow to create a new row in #biomeStructuresContainer with a hidden value input, a searchable dropdown (triggered on focus), spawn chance number field, and a remove button. It populates displayLabels for types like cubyz:simple_tree, cubyz:simple_vegetation, etc., and renders them as clickable options inside an absolute-positioned dropdown div. When a user selects an option via mousedown, it updates the hidden value input, the search text input, calls window.toggleStructSubFields with the rowId and selected type, and hides the dropdown. The toggleStructSubFields function clears any existing sub-fields in .struct-subfields-wrapper and conditionally injects HTML for each supported type: simple_tree adds Log Block (dropdown), Leaves Block (dropdown), Base Trunk Height, Height Variance, Crown Size; simple_vegetation adds Foliage Sprite Block (dropdown) and Sprite Max Height; flower_patch adds Foliage/Flower Block (dropdown), Patch Width Scale, Patch Variance, Patch Density; boulder adds Stone Block Variant (dropdown), Base Radius Size, Size Variance Step; ground_patch adds Replacement Block (dropdown), Patch Width, Patch Depth layers, Edge Smoothness; fallen_tree adds Log Block Type (dropdown), Log Length size, Length Variance; sbb adds SBB Asset path ID and Place Mode flag. Each dropdown input has onfocus="window.showRecipeDropdown(...)" to open a recipe list and oninput="window.filterDropdown(...)" to filter as the user types. Normal inputs have placeholder text and are bound via createNormalInputHTML. After injecting HTML, it attaches an 'input' event listener to all newly created inputs that calls window.markFormAsDirty() unless window.isInitializingPanel is true. The chunk also includes partial implementation of initDropdownClearButtons which iterates over .texture-select-wrapper elements, finds the text input, and if not readonly creates a clear button wrapper (code truncated).

## Related Questions
- What happens when a user focuses the structure type search input?
- How does toggleStructSubFields determine which inputs to render for a given feature type?
- Which event listeners are attached to newly created sub-field inputs and why?
- Is there any validation on spawn chance values before they are stored?
- What is the purpose of window.markFormAsDirty in this context?
- How does the code handle saving existing data when adding a row with savedData parameter?
- Are dropdown options generated dynamically or hardcoded, and how are they populated?
- What role does initDropdownClearButtons play for texture-select-wrapper elements?
- Does the UI support undoing changes to structure rows before finalizing the addon?
- How are placeholder values chosen when a row is created without savedData?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_5*
