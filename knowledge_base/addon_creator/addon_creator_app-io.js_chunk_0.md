# [medium/addon_creator_app-io.js] - Chunk 0

**Type:** ui
**Keywords:** ZIP file import, project data update, texture parsing, block properties, item properties, global project data
**Symbols:** importExistingAddon, parseIntegerToHexColor, extractVal, extractMinMax
**Concepts:** data-binding, file handling, resource extraction, project data update

## Summary
Handles the import of existing addons by parsing a ZIP file and updating project data accordingly.

## Explanation
Handles the import of existing addons by parsing a ZIP file and updating project data accordingly. The function `importExistingAddon` processes the file to extract various types of resources such as textures, blocks, items, recipes, biomes, entities, and particles. It updates global project data structures like `window.projectData` and `window.serverTextures`. Specifically, it determines the namespace name from the ZIP file's filename, extracts texture files, parses block properties including health (default '1'), resistance (default '0'), rotation (default 'cubyz:stairs'), collision detection (default true), transparency (default false), replaceability (default false), degradability (default false), view-through properties (default false), back face visibility (default false), ore allowance (default false), friction (default '20'), bounciness (default '0.0'), density (default '1.2'), terminal velocity (default '90'), mobility (default '1.0'), light emission and absorption colors (default '#000000' for emitted, '#ffffff' for absorbed), drop auto-generation (default true), item icon search (default empty string), base textures (default 'stone'), callbacks for touch type (default 'none'), damage mode (default 'damage'), DPS (default '0.6'), variant (default 'heat'), update type (default 'none'), tick type (default 'none'), break type (default 'none'), interact type (default 'none'), and window name (default 'crafting_table'). It also includes helper functions `parseIntegerToHexColor`, `extractVal`, and `extractMinMax` to handle specific value extractions. The function ensures that duplicate texture files are not added to `serverTextures`. If a file with an unsupported extension is encountered during the import process, it is skipped.

For items, the function parses properties such as tags, base texture, and other relevant attributes from the `.zig.zon` files within the 'items' directory. These properties are then stored in the `window.projectData.items` array.

## Related Questions
- What is the purpose of the `parseIntegerToHexColor` function?
- How does the function determine the namespace name from the ZIP file's filename?
- What types of resources are extracted from the ZIP file and how are they processed?
- How are block properties parsed and stored in the project data, including specific attributes like health, resistance, rotation, collision detection, transparency, replaceability, degradability, view-through properties, back face visibility, ore allowance, friction, bounciness, density, terminal velocity, mobility, light emission and absorption colors, drop auto-generation, item icon search, base textures, callbacks for touch type, damage mode, DPS, variant, update type, tick type, break type, interact type, and window name?
- What happens if a file with an unsupported extension is encountered during the import process?
- How does the function ensure that duplicate texture files are not added to `serverTextures`?

*Source: unknown | chunk_id: addon_creator_app-io.js_chunk_0*
