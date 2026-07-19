# [hard/addon_creator_app-studio.js] - Chunk 4

**Type:** ui
**Keywords:** recipe presets, biome settings, block face previews, custom entity models, texture uploads, DOM manipulation, event handling
**Symbols:** loadRecipePreset, loadBiomePreset, updateBlockFacePreviews, handleCustomEntityModel, handleCustomEntityTexture
**Concepts:** data-binding, form validation, live preview

## Summary
The script provides functions to load recipe and biome presets, update block face previews, handle custom entity models and textures, and mark forms as dirty.

## Explanation
This JavaScript file contains several functions that manage different aspects of the Cubyz Addon Creator UI. The `loadRecipePreset` function sets default values for recipe inputs based on a selected preset ('planks' or 'workbench'). For the 'planks' preset, it assigns the filename 'oak_planks_crafting', sets the input search to 'cubyz:oak_log', and sets the output search to 'cubyz:planks/oak' with an output count of 4. For the 'workbench' preset, it assigns the filename 'workbench_production', sets the input search to 'cubyz:planks/oak' with a count of 4, and sets the output search to 'cubyz:workbench'. Similarly, `loadBiomePreset` configures biome settings for predefined biomes ('mountain' or 'cave'). For the 'mountain' preset, it assigns the biome ID 'misty_peaks', sets the minimum height to 100, maximum height to 150, surface block to 'cubyz:cold_grass', sub-block to 'cubyz:permafrost', stone block to 'cubyz:glacite/smooth', and adds structures like 'cubyz:sbb', 'cubyz:sbb', 'cubyz:ground_patch', 'cubyz:flower_patch', and 'cubyz:boulder' with a chance of 0.01 each. For the 'cave' preset, it assigns the biome ID 'deep_abyss_caves', sets the minimum height to -600, maximum height to -512, surface block to 'cubyz:slate/rough', and marks it as a cave. The `updateBlockFacePreviews` function updates texture previews for block faces based on user input. It maps each face (up, front, left, right, bottom, back) to the corresponding search value or base value if not specified. It then finds the appropriate texture from `window.serverTextures` and updates the image source accordingly. Functions like `handleCustomEntityModel` and `handleCustomEntityTexture` manage file uploads for custom entity models and textures, updating the UI accordingly. Each of these functions interacts with the DOM to set values, update images, and mark forms as dirty to indicate changes.

## Related Questions
- What does the `loadRecipePreset` function do?
- How are block face previews updated in the UI?
- What is the purpose of the `handleCustomEntityTexture` function?
- How does the script handle file uploads for custom entity models?
- What happens when a user selects a recipe preset?
- How are biome settings configured using presets?
- What role do event handlers play in this script?
- How does the script ensure that forms are marked as dirty after changes?
- Can you explain how texture previews are generated for block faces?
- What is the process for uploading and handling custom entity textures?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_4*
