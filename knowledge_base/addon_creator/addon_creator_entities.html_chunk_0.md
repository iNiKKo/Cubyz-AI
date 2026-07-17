# [easy/addon_creator_entities.html] - Chunk 0

**Type:** ui
**Keywords:** entity creator, blueprint creation, model selection, texture upload, tag management
**Symbols:** panel, form-group, col, label, input, hidden, text, number, span, dropdown-options, dropdown-option, file-input-label, recipe-dropdown, filter-dropdown, handleCustomEntityModel, handleCustomEntityTexture, addDynamicTagPill
**Concepts:** data-binding, form validation, live preview

## Summary
UI component for creating and configuring entity blueprints in the Cubyz Addon Creator workspace.

## Explanation
This UI component is responsible for allowing users to create and configure entity blueprints in the Cubyz Addon Creator. It includes fields for specifying the entity's ID, height, coordinate system, model, texture, and tags. The component also provides dropdowns for selecting models and textures, as well as buttons for adding custom GLB and PNG files. Additionally, it includes a save button to upload the entity blueprint to the project.

## Code Example
```zig
<input type="text" id="entityId" placeholder="snale" autocomplete="off" oninput="this.value = this.value.toLowerCase().replace(/[^a-z0-9_]/g, '')">
```

## Related Questions
- What is the purpose of the 'Entity ID' field?
- How does the 'Height' input control work?
- Can you explain how the coordinate system dropdown works?
- What are the options available in the model dropdown?
- How can I add a custom GLB file for the entity?
- What is the purpose of the texture upload feature?
- How do I add a custom PNG file for the entity?
- Can you explain how the tag management section works?
- What are some quick tags available to add?
- How does the save button work in this UI component?
- What is the role of the hint text and field explanation elements?
- How can I customize the appearance or behavior of the entity creator UI?

*Source: unknown | chunk_id: addon_creator_entities.html_chunk_0*
