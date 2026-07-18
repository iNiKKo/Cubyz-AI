# [medium/addon_creator_app-core.js] - Chunk 0

**Type:** ui
**Keywords:** server assets, fetching data, UI components, status badge, dropdowns, metrics UI, error handling
**Symbols:** window.serverBlocks, window.serverItems, window.serverTextures, window.serverMusicList, window.serverEntityModels, window.serverParticles, window.blockTexturesOnly, window.itemTexturesOnly, window.particleTexturesOnly, window.allSearchableItems, window.dropdownsGenerated, window.VERSION_PATH, window.hasUnsavedChanges, window.currentPanelName, window.editingId, window.projectData, window.metricsExpandedState, window.metricCounts, loadServerAssets
**Concepts:** data-binding, async operations, UI updates, error handling

## Summary
This chunk handles the loading of server assets and updating UI components based on the loaded data.

## Explanation
The chunk defines several global variables to store server asset data, such as blocks, items, textures, recipes, music, entities, and particles. It includes an asynchronous function `loadServerAssets` that fetches JSON data from the server for these assets. The function updates various UI components like status badges, dropdowns, and metrics UI based on the loaded data. It also handles errors by logging them to the console and updating the status badge with an error message.

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
