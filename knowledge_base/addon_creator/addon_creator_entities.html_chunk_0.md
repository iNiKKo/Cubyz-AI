# [easy/addon_creator_entities.html] - Chunk 0

**Type:** ui
**Keywords:** entity creator, blueprint creation, model selection, texture upload, tag management
**Symbols:** panel, form-group, col, input, label, h2, span, dropdown-options, dropdown-option, file-input-label, img
**Concepts:** data-binding, form validation, live preview

## Summary
UI component for creating and configuring entity blueprints in the Cubyz Addon Creator.

## Explanation
The UI component is responsible for allowing users to input details about an entity: ID, height, coordinate system, model, texture, and tags. The Height field is a number input defaulting to `2.0` (blocks), with `step="0.1"` and `min="0.1"`. The Model field is a searchable dropdown (filtered against the `entity_models` list as the user types) with a separate custom-upload option accepting `.glb` files. Tags are entered freely via a text input, plus three "Quick Add" buttons that pre-fill common tags: `playerModel`, `living`, and `ambient`. A save button creates the entity blueprint from these inputs.

## Code Example
```zig
<input type="text" id="entityId" placeholder="snale" autocomplete="off" oninput="this.value = this.value.toLowerCase().replace(/[^a-z0-9_]/g, '')">
```

## Related Questions
- What is the purpose of the 'Entity ID' input field?
- How does the 'Model' dropdown work and what models can be selected?
- What are the quick add buttons for tags used for?
- What happens when the 'Save Entity to Project' button is clicked?
- How is the coordinate system selected using the dropdown?
- Can users upload custom models or textures, and if so, how?
- What is the purpose of the hint text in the UI component?
- How does the live preview feature work for entity creation?
- What are the default values for the 'Height' input field?
- How can users add tags to their entity blueprint?
- What happens when a user selects a model or texture from the dropdowns?
- Can users edit the height of the entity after it has been created?

*Source: unknown | chunk_id: addon_creator_entities.html_chunk_0*
