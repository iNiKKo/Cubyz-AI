# [medium/addon_creator_app-core.js] - Chunk 0

**Type:** ui
**Keywords:** server assets, fetching data, UI components, status badge, dropdowns, metrics UI, error handling
**Symbols:** window.serverBlocks, window.serverItems, window.serverTextures, window.serverMusicList, window.serverEntityModels, window.serverParticles, window.blockTexturesOnly, window.itemTexturesOnly, window.particleTexturesOnly, window.allSearchableItems, window.dropdownsGenerated, window.VERSION_PATH, window.hasUnsavedChanges, window.currentPanelName, window.editingId, window.projectData, window.metricsExpandedState, window.metricCounts, loadServerAssets
**Concepts:** data-binding, async operations, UI updates, error handling

## Summary
This chunk handles the loading of server assets and updating UI components based on the loaded data.

## Explanation
This chunk handles the loading of server assets and updating UI components based on the loaded data. It defines several global variables to store server asset data such as blocks, items, textures, recipes, music, entities, and particles. The function `loadServerAssets` fetches JSON data from the server for these assets using specific paths defined by `window.VERSION_PATH`. For example, it fetches blocks.json, items.json, textures.json, recipes.json, music.json, entity_models.json, and particles.json. If any of these files are missing on the server during the fetch operation, an error is thrown with a message indicating that one or more manifests are missing.

The function updates various UI components like status badges, dropdowns, and metrics UI based on the loaded data. It categorizes textures into different types (block textures, item textures, entity textures, particle textures) by checking if their paths include specific keywords such as 'blocks/', 'items/', 'entityModels/', or 'particles/'. Each texture is represented by a `textureObject` containing properties like name, dataUrl, and type flags indicating whether it's a block, item, entity, or particle texture.

The function also updates the global variable `window.metricCounts`, which stores counts of various assets such as blocks, items, textures, music tracks, entities, and particles. The structure of `window.metricCounts` is defined as follows:
```json
{
    "blocks": window.serverBlocks.length,
    "items": window.serverItems.length,
    "blockTex": window.blockTexturesOnly.length,
    "itemTex": window.itemTexturesOnly.length,
    "music": window.serverMusicList.length,
    "entities": window.serverEntityModels.length,
    "particles": window.serverParticles.length
}
```
Dropdowns are rebuilt after loading server assets using the `rebuildDropdowns` function if it is defined. If an error occurs during data fetching, it logs the error to the console and updates the status badge with a specific error message.

## Related Questions
- What is the purpose of the `loadServerAssets` function?
- How does the chunk handle errors when fetching server data?
- Which global variables store the loaded server assets?
- What UI components are updated after loading the server assets?
- How does the chunk categorize textures into different types?
- What is the role of the `window.metricCounts` object?
- How does the chunk update the status badge in case of an error?
- What is the structure of the `textureObject` created for each texture?
- How are dropdowns rebuilt after loading server assets?
- What happens if some JSON files are missing on the server during the fetch operation?

*Source: unknown | chunk_id: addon_creator_app-core.js_chunk_0*
