# [easy/addon_creator_recipes.html] - Chunk 0

**Type:** ui
**Keywords:** recipe creator, preset loading, ingredient input, output item, save recipe
**Symbols:** panel, recipePresetSelectorSearch, recipePresetDropdown, dropdown-options, dropdown-option, form-group, col, texture-select-wrapper, input, label, h2, h3, button
**Concepts:** data-binding, form validation, live preview

## Summary
UI component for creating and editing recipes in the Cubyz Addon Creator.

## Explanation
This UI component is responsible for allowing users to create and edit recipes. It includes a dropdown menu for loading preset recipes, input fields for specifying recipe ID, input ingredients with quantity and texture selection, output item result with amount made and texture selection, and a save button to add the recipe to the project.

## Code Example
```zig
<input type="text" id="recipeFilename" value="" autocomplete="off" oninput="this.value = this.value.toLowerCase().replace(/[^a-z0-9_]/g, '')">
```

## Related Questions
- How does the Recipe Creator handle input validation for recipe IDs?
- What is the purpose of the 'Load Preset' dropdown menu in the Recipe Creator?
- How are texture selections handled in the Recipe Creator?
- Can users add more than four ingredients to a recipe?
- What happens when a user clicks the 'Save Recipe to Project' button?
- How does the Recipe Creator handle default values for input fields?
- What is the purpose of the dropdown options in the Recipe Creator?
- How are the dropdown menus implemented in the Recipe Creator?
- Can users search for items or custom blocks when selecting an output item?
- How are the dropdown menus filtered as the user types in the Recipe Creator?
- What happens if a user enters an invalid recipe ID?
- How is the recipe data structured and stored in the Cubyz Addon Creator?

*Source: unknown | chunk_id: addon_creator_recipes.html_chunk_0*
