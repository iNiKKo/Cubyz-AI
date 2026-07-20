# [hard/addon_creator_app-save.js] - Chunk 2

**Type:** ui
**Keywords:** biome, entity, project data, input validation, color conversion, structural layers, UI update
**Symbols:** saveBiomeToProject, saveEntityToProject, getHexColorAsRGBVector, autoNamespaceBlock
**Concepts:** data-binding, form validation, live preview

## Summary
The chunk implements functions to save biome and entity configurations to the project data, handling input validation and updating the UI.

## Explanation
**Explanation**

This JavaScript code defines two primary functions: `saveBiomeToProject` and `saveEntityToProject`. These functions are responsible for saving biome and entity configurations into the project's data structure, respectively. Both functions include input validation to ensure that all necessary fields are correctly filled out before proceeding.

### saveBiomeToProject Function
- **Input Validation**: The function first checks if a Biome ID is specified. If not, it alerts the user to specify one and exits.
- **Color Conversion**: It uses the `getHexColorAsRGBVector` function to convert hexadecimal color values for sky and fog into RGB vectors. For example, if no value is provided, it defaults to `#75b2ff` for sky and `#e2f2ff` for fog.
- **Block Namespace Handling**: The `autoNamespaceBlock` function ensures that block IDs are correctly namespaced. If a block ID is not already in the correct format, it adds the appropriate namespace based on whether the block exists in the project or defaults to 'cubyz'.
- **Structural Layers**: The function processes structural layers by iterating over each row in the structure table. Depending on the type of structural layer (e.g., simple_tree, simple_vegetation), it extracts and validates specific properties such as log types, leaf types, block types, sizes, heights, variations, etc.
  - **simple_tree**: Extracts `log`, `leaves`, `height`, `height_variation`, `leafRadius`. Defaults to 'cubyz:oak_log' for `log` and calculates other properties based on these defaults.
  - **simple_vegetation**: Extracts `blockType`, `size`, `variation`. Uses default values if not provided.
- **Biome Properties**: The function collects various biome properties like temperature, humidity, zone, growth, and height properties from the form inputs. These are represented by radio buttons or dropdowns in the UI.
- **Updating Project Data**: It updates the project data by removing any existing biomes with the same ID and adding the new biome configuration. It also ensures that certain flags are reset (e.g., `hasUnsavedChanges`) and the sidebar project tree is updated to reflect changes.

### saveEntityToProject Function
- **Input Validation**: Similar to `saveBiomeToProject`, it checks if an Entity ID is specified. If not, it alerts the user and exits.
- **Entity Configuration**: It collects entity properties such as height, coordinate system, model, default texture, and tags from the form inputs.
- **Updating Project Data**: It updates the project data by removing any existing entities with the same ID and adding the new entity configuration. It also ensures that certain flags are reset (e.g., `hasUnsavedChanges`) and the sidebar project tree is updated to reflect changes.

### Supporting Functions
- **getHexColorAsRGBVector**: Converts a hexadecimal color string into an RGB vector format. For example, `#75b2ff` becomes `[0.4588, 0.6902, 1]`.
- **autoNamespaceBlock**: Ensures block IDs are correctly namespaced based on their existence in the project or defaults to 'cubyz'.

### UI Updates
After saving a biome or entity configuration, the code updates the UI by resetting flags like `hasUnsavedChanges` and updating the sidebar project tree to reflect the changes.

### Default Values
The code handles default values for various properties when saving a biome. For example, if no log type is specified for a simple_tree, it defaults to 'cubyz:oak_log'. Similarly, other fields have default values that are used if they are not explicitly provided by the user.

## Related Questions
- What is the purpose of the `getHexColorAsRGBVector` function?
- How does the code handle invalid biome or entity IDs?
- What data structures are used to store structural layers in a biome configuration?
- How does the code ensure that only valid block IDs are used in the project data?
- What happens if a user tries to save a biome without specifying a Biome ID?
- How is the `autoNamespaceBlock` function used in the code?
- What UI elements are updated after saving a biome or entity configuration?
- How does the code handle default values for various properties when saving a biome?
- What types of structural layers can be configured for a biome, and how are they represented?
- How is the project data structure modified when a new biome or entity is saved?

*Source: unknown | chunk_id: addon_creator_app-save.js_chunk_2*
