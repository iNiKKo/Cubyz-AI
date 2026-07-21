# [hard/addon_creator_app-save.js] - Chunk 4

**Type:** implementation
**Keywords:** exportFullAddon, Cubyz, JSZip, Zig, ZIP, blocks, items, biomes, recipes, entities, particles, textures, models
**Symbols:** exportFullAddon, window.projectData, JSZip, folders, packs, zip, writeTex
**Concepts:** Cubyz game engine, addon export, Zig format, ZIP archive, blocks, items, biomes, recipes, entities, particles, textures, custom models

## Summary
This script exports an addon for the Cubyz game engine. It generates various files and folders containing information about blocks, items, biomes, recipes, entities, particles, and textures. The data is structured in Zig format and saved as a ZIP file. The script handles different types of elements like boulders, ground patches, fallen trees, structure blocks, recipes, entity models, and particle effects. It also manages custom textures and models, ensuring they are included in the export.

## Explanation
Clicking "Export Full Addon" calls the **`exportFullAddon()`** function, which handles the entire export process. It walks every object in **`window.projectData`** (the in-memory store of everything entered into the Addon Creator's forms) and writes each one out as a `.zig.zon` file, packed into a ZIP archive built with the JSZip library. The script then iterates through various elements defined in the project data, such as blocks, items, biomes, recipes, entities, and particles, and writes their information to corresponding files in the ZIP archive. Each element's data is formatted according to Zig syntax rules. For textures, the script checks if they are custom or need to be fetched from URLs, then adds them to the appropriate folders within the ZIP. The script also handles custom entity models by writing them directly to the models folder. Finally, it generates a blob of the ZIP file and triggers a download for the user. This comprehensive approach ensures that all necessary components of an addon are correctly exported and organized.

## Related Questions
- What does clicking "Export Full Addon" do in the Cubyz Addon Creator?
- What function handles exporting a full addon in the Cubyz Addon Creator, and what does it iterate over?
- How does the script handle custom textures and models?
- What is the purpose of the `writeTex` function in the script?
- Can you explain how the script formats data for Zig syntax?
- How are recipes and entity models exported in this script?
- What types of elements are included in the addon export process?
- How does the script ensure that all necessary components are correctly organized within the ZIP archive?

*Source: unknown | chunk_id: addon_creator_app-save.js_chunk_4*
