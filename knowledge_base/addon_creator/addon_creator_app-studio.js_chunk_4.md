# [hard/addon_creator_app-studio.js] - Chunk 4

**Type:** ui
**Keywords:** recipe preset, biome preset, texture preview, custom entity model, custom texture upload, form dirty flag, serverTextures registry, file input handler, addon identifier, thumbnail generation
**Symbols:** loadRecipePreset, loadBiomePreset, updateBlockFacePreviews, handleCustomEntityModel, handleCustomEntityTexture, handleCustomBlockTexture
**Concepts:** preset loading, texture preview generation, custom asset upload handling, form state management, data binding to UI inputs, addon identifier construction

## Summary
This module defines the core UI event handlers for the Addon Studio blueprint editor, including functions to populate form fields from preset data (item presets, recipe presets, biome presets), update texture previews based on user input, and handle custom entity/block textures uploaded via file inputs.

## Explanation
The chunk exports several window-level functions that bind UI controls to data models. loadRecipePreset populates the crafting recipe form fields with predefined values for 'planks' or 'workbench', clearing other input slots. loadBiomePreset clears the biome structures container and sets biome ID, height ranges, surface/sub/stone blocks, and adds structure rows based on the key ('mountain' or 'cave'). updateBlockFacePreviews reads text inputs (topSearch, frontSearch, etc.), maps them to texture data URLs from window.serverTextures or fallbacks, and updates preview images accordingly; it also handles thumbnail generation for various texture search fields. handleCustomEntityModel processes a file upload for custom entity models: it extracts the addon name and filename, constructs an identifier like 'my_addon:name', stores the file in window.customEntityModels, and sets the corresponding search input value. handleCustomEntityTexture performs similar logic for textures: it reads the uploaded file as a data URL, prepends a texture object to window.serverTextures with metadata (isCustom:true, isEntityType:true), updates the search input, and triggers updateBlockFacePreviews. handleCustomBlockTexture begins analogous handling for block textures.

## Related Questions
- What happens when loadRecipePreset is called with the key 'planks'?
- How does updateBlockFacePreviews determine which texture to display for a given face?
- Where are custom entity model files stored after upload via handleCustomEntityModel?
- Does loadBiomePreset clear existing biome structures before adding new ones?
- What metadata is attached to textures added by handleCustomEntityTexture?
- How does the code construct an addon identifier from a filename and addon name?
- Which UI elements are affected when updateBlockFacePreviews runs?
- Is there any validation on texture filenames before they are registered?
- What fallback is used if no matching texture is found in serverTextures?
- How does the form get marked as dirty after preset loading or custom uploads?

*Source: unknown | chunk_id: addon_creator_app-studio.js_chunk_4*
