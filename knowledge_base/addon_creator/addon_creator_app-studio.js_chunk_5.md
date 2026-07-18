# [hard/addon_creator_app-studio.js] - Chunk 5

**Type:** ui
**Keywords:** structure rows, biome structures, custom textures, dropdowns, input fields, subfields, event listeners, data URL, file reader, UI generation
**Symbols:** handleCustomBlockTexture, addStructureRow, toggleStructSubFields
**Concepts:** data-binding, form validation, dynamic UI generation, event handling, user input management

## Summary
The chunk implements a UI component for adding and managing structure rows in the addon creator app. Each row allows users to define different types of biome structures with specific parameters.

## Explanation
This JavaScript code snippet defines two primary functions: `handleCustomBlockTexture` and `addStructureRow`. The `handleCustomBlockTexture` function handles file input for custom block textures, reading the file, processing it into a data URL, and updating relevant UI elements. The `addStructureRow` function dynamically adds new structure rows to the UI, each containing dropdowns for selecting structure types, inputs for spawn chances, and additional subfields based on the selected structure type. These subfields allow users to specify detailed parameters for each structure type, such as log blocks, foliage sprites, or SBB asset paths.

## Related Questions
- What is the purpose of the `handleCustomBlockTexture` function?
- How does the `addStructureRow` function dynamically add new structure rows to the UI?
- What types of parameters can users specify for each structure type in the subfields?
- How are event listeners used in this chunk to manage user input?
- What is the role of the `toggleStructSubFields` function in the UI component?
- How does the code handle custom block textures and update the UI accordingly?
- What is the purpose of the `displayLabels` object in the `addStructureRow` function?
- How are dropdown options dynamically generated for each structure type?
- What happens when a user selects a different structure type from the dropdown?
- How does the code ensure that the form remains marked as dirty after user input?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_5*
