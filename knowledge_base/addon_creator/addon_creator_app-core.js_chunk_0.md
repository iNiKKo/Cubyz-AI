# [medium/addon_creator_app-core.js] - Chunk 0

**Type:** ui
**Keywords:** server assets, async loading, texture categorization, UI metrics, status updates, global variables, fetch API, Promise.all, error handling, UI rendering
**Symbols:** serverBlocks, serverItems, serverTextures, serverMusicList, serverEntityModels, serverParticles, blockTexturesOnly, itemTexturesOnly, particleTexturesOnly, allSearchableItems, dropdownsGenerated, VERSION_PATH, hasUnsavedChanges, currentPanelName, editingId, projectData, metricsExpandedState, metricCounts, loadServerAssets, renderMetricsUI
**Concepts:** data-binding, asynchronous data loading, UI updates based on data, error handling in UI

## Summary
The script initializes server asset data and UI components for the Cubyz Addon Creator, handling asynchronous loading of assets and updating UI elements based on loaded data.

## Explanation
This JavaScript file is part of the Cubyz Addon Creator application. It defines several global variables to store server asset data such as blocks, items, textures, recipes, music, entities, and particles. The `loadServerAssets` function asynchronously fetches these assets from a specified version path and updates the corresponding global arrays. It also processes texture paths to categorize them into block, item, entity, or particle textures, updating metrics accordingly. The `renderMetricsUI` function updates the UI with status information and metrics based on the loaded data. Additionally, there are placeholders for other functions like `updateSearchableItems`, `rebuildDropdowns`, and `updateSidebarProjectTree` which are assumed to be defined elsewhere in the application.

## Related Questions
- What is the purpose of the `loadServerAssets` function?
- How does the script handle errors when loading server assets?
- What data structures are used to store server asset information?
- How are textures categorized in this script?
- What UI elements are updated based on the loaded metrics?
- What is the role of the `renderMetricsUI` function?
- How does the script manage unsaved changes?
- What global variables are defined for project data management?
- How are dropdowns generated and managed in this script?
- What is the structure of the `projectData` object?

*Source: unknown | chunk_id: addon_creator_app-core.js_chunk_0*
