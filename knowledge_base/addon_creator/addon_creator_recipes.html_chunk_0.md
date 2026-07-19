# [easy/addon_creator_recipes.html] - Chunk 0

**Type:** ui
**Keywords:** recipe creator, preset loading, ingredient input, output item, save recipe
**Symbols:** panel, recipePresetSelectorSearch, recipePresetDropdown, dropdown-options, dropdown-option, form-group, col, texture-select-wrapper, input, label, h2, h3, button
**Concepts:** data-binding, form validation, live preview

## Summary
UI component for creating and editing recipes in the Cubyz Addon Creator.

## Explanation
This UI component is responsible for allowing users to create and edit recipes in the Cubyz Addon Creator. It includes a 'Load Preset' dropdown with exactly two presets: 'Oak Planks' (`loadRecipePreset('planks')`) and 'Workbench' (`loadRecipePreset('workbench')`). The preset 'Oak Planks' corresponds to the recipe where 4 oak logs are crafted into 1 oak plank. The preset 'Workbench' corresponds to the recipe where 4 planks are crafted into 1 workbench. Input Ingredients allows up to 4 items (the 2nd-4th are optional, searchable via a filterable dropdown), each with a quantity and texture selection. The output section specifies the result item, amount made, and texture selection. A save button adds the finished recipe to the project.

**Input Validation:** Recipe IDs must be lowercase alphanumeric characters or underscores. Any other characters are automatically removed as the user types.

**Texture Selections:** Users can select textures for input items and the output item from a dropdown menu that provides live filtering based on user input.

**Default Values:** Input fields have default values of 1 for quantities, and the 'Recipe ID' field is initially empty. The 'Load Preset' dropdown defaults to 'None'.

**Dropdown Menus:** Dropdown menus are implemented with a search functionality that filters options as the user types. They provide live previews and allow users to select items or custom blocks.

**Recipe Data Structure:** Recipe data includes the recipe ID, input ingredients (with quantities), output item (with quantity), and texture selections for both inputs and outputs.

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
