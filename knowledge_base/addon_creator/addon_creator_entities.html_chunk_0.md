# [easy/addon_creator_entities.html] - Chunk 0

**Type:** ui
**Keywords:** entity creator, blueprint creation, model selection, texture upload, tag management
**Symbols:** panel, form-group, col, input, label, h2, span, dropdown-options, dropdown-option, file-input-label, img
**Concepts:** data-binding, form validation, live preview

## Summary
UI component for creating and configuring entity blueprints in the Cubyz Addon Creator.

## Explanation
UI component for creating and configuring entity blueprints in the Cubyz Addon Creator.

The UI component allows users to input details about an entity, including:
- **Entity ID**: A text input with a placeholder of 'snale', which must be lowercase, alphanumeric, and can include underscores. The input field automatically converts any invalid characters to lowercase and removes non-alphanumeric characters except underscores.
- **Height**: A number input defaulting to `2.0` blocks, with `step="0.1"` and `min="0.1"`. This specifies the entity's height in blocks.
- **Coordinate System**: A dropdown menu with two options: 'Right-Handed Z-Up (CUBERT)' (default) and 'Left-Handed Y-Up (SNALE)'. Users can select one of these coordinate systems for their entity.
- **Model**: A searchable dropdown that filters against the `entity_models` list as users type. It also includes a custom-upload option that accepts `.glb` files, allowing users to upload custom models in this format.
- **Texture**: A searchable dropdown with a preview thumbnail image (displayed when a texture is selected) and a custom-upload option that accepts `.png` files, enabling users to upload custom textures in this format.
- **Tags**: Entered freely via a text input, plus three 'Quick Add' buttons that pre-fill common tags: `playerModel`, `living`, and `ambient`. Users can add multiple tags by separating them with spaces or pressing Enter.

A save button creates the entity blueprint from these inputs. The coordinate system can be selected using a dropdown with two options: 'Right-Handed Z-Up (CUBERT)' and 'Left-Handed Y-Up (SNALE)'. Users can upload custom models in `.glb` format and textures in `.png` format through the respective file input fields. The hint text provides additional information about certain fields, such as the Entity ID field which must be lowercase and alphanumeric with underscores allowed.

The explanation also mentions that there is no live preview feature for entity creation.

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
