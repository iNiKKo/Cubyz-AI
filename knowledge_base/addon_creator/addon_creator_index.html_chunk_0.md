# [easy/addon_creator_index.html] - Chunk 0

**Type:** ui
**Keywords:** toolbar, sidebar, import, export, navigation, panels, blocks, items, recipes, biomes, entities, particles
**Symbols:** addonName, importAddonFile, exportFullAddon(), toggleMetricsPanel(), folderStatus, sidebarBlocksTree, sidebarItemsTree, sidebarRecipesTree, sidebarBiomesTree, sidebarEntitiesTree, sidebarParticlesTree, loadStudioPanel()
**Concepts:** data-binding, form-validation, live-preview, tree-navigation, addon-import-export

## Summary
The Cubyz Addon Creator index page provides the main navigation hub, displaying a toolbar with addon name input and import/export buttons, alongside a project explorer sidebar listing blocks, items, recipes, biomes, entities, and particles.

## Explanation
UI Controls: The page includes an editable text input for 'addonName' that auto-sanitizes to lowercase alphanumeric characters via oninput event. Two toolbar buttons are present: an import button wrapping a hidden file input (id='importAddonFile') triggered by onchange, and an export button invoking exportFullAddon(). A metrics panel with id='folderStatus' is clickable via onclick handler window.toggleMetricsPanel() showing a status pill labeled 'Connecting...'. The sidebar contains six collapsible tree sections: sidebarBlocksTree, sidebarItemsTree, sidebarRecipesTree, sidebarBiomesTree, sidebarEntitiesTree, and sidebarParticlesTree, each initially displaying placeholder text. Navigation buttons in the nav-bar (loadStudioPanel) switch between categories.

## Related Questions
- What happens when the user types into the addonName field?
- How does the import button trigger file selection without a visible input element?
- Which function is called when the metrics panel is clicked?
- Are there any validation rules applied to the addon name besides lowercasing?
- How are unsaved changes communicated to the user before switching panels?
- What placeholder text appears in each sidebar tree section initially?
- Is there a way to programmatically load a specific studio panel from this index page?
- Does the export button perform any pre-export validation or confirmation?
- How does the nav-bar buttons interact with the dynamicWorkspace div?
- Are any external scripts loaded that handle addon creation logic?

*Source: unknown | chunk_id: addon_creator_index.html_chunk_0*
