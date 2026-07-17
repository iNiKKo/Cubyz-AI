# [hard/addon_creator_app-save.js] - Chunk 4

**Type:** ui
**Keywords:** biomes, recipes, entities, particles, Zig.ZON, ZIP export, data formatting, optional fields, default values, file structure
**Symbols:** bio, bioZon, rZon, ent, pZon, packs, folders, writeTex, exportFullAddon
**Concepts:** data serialization, file generation, ZIP file creation, conditional data inclusion

## Summary
Handles the saving of addon data, including biomes, recipes, entities, and particles into a ZIP file.

## Explanation
This JavaScript code snippet is responsible for exporting an entire Cubyz addon project. It processes various types of data such as biomes, recipes, entities, and particles, formatting them into specific Zig.ZON files. The script ensures that each element's properties are correctly serialized, including handling optional fields and default values. For example, it formats chance values to two decimal places and checks if certain conditions (like `isCave`) are met before adding additional properties. It also manages the creation of subfolders based on the data's structure and writes files accordingly. The final step is to generate a ZIP file containing all these formatted files and prompt the user to download it.

## Related Questions
- How does the script handle optional properties when generating Zig.ZON files?
- What is the purpose of the `writeTex` function in this code snippet?
- How are biomes with structures handled differently compared to those without?
- Can you explain how the script ensures that each entity's model and texture paths are correctly formatted?
- What steps does the script take to generate a ZIP file containing all the addon data?
- How does the script manage the creation of subfolders for different types of data (e.g., biomes, recipes)?
- What is the role of the `exportFullAddon` function in this context?
- How are default values applied when serializing properties to Zig.ZON files?
- Can you describe how the script handles different types of structures within biomes?
- What mechanisms does the script use to ensure that all necessary textures are included in the final ZIP file?

*Source: unknown | chunk_id: addon_creator_app-save.js_chunk_4*
