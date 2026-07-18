# [easy/addon_creator_index.html] - Chunk 0

**Type:** ui
**Keywords:** Cubyz Addon Creator, web interface, project explorer, dynamic workspace, addon creation, UI components, event handlers, validation, templates, bindings, engine mappings, configuration generation
**Symbols:** addon_creator_index.html, style.css, app-core.js, app-studio.js, app-save.js, app-io.js
**Concepts:** data-binding, form validation, live preview

## Summary
A web-based interface for creating and managing Cubyz addons, including a toolbar with addon name input, import/export buttons, project explorer sidebar, and dynamic workspace.

## Explanation
The HTML file contains the main structure of the Cubyz Addon Creator application. It includes a header with the app title and version indicator, a toolbar for adding and importing addons, and a project explorer sidebar on the left. The right side displays a navigation bar with buttons to switch between different categories (blocks, items, recipes, biomes, entities, particles) and a dynamic workspace area where content is loaded based on the selected category. The file also includes scripts for app core, studio, save, and IO functionalities.

## Code Example
```zig
<input type="text" id="addonName" value="" autocomplete="off" oninput="this.value = this.value.toLowerCase().replace(/[^a-z0-9_]/g, '')">
```

## Related Questions
- What is the purpose of the 'Project Explorer' sidebar?
- How does the application handle unsaved changes before switching panels?
- What are the default values for the addon name input field?
- Explain how the import/export buttons work in the toolbar.
- Describe the structure of the project explorer sidebar.
- What is the purpose of the 'dynamicWorkspace' div?
- How does the application handle user input validation for the addon name field?
- What are the categories available in the navigation bar?
- Explain how the application handles file uploads using the importAddonFile input element.
- Describe the purpose of the customConfirmModal and its components.
- What is the role of the 'status-pill' class in the toolbar?
- How does the application handle database metrics display?

*Source: unknown | chunk_id: addon_creator_index.html_chunk_0*
